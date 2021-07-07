from sqlalchemy.orm import Session

from backend.schemas.jobs import JobCreate
from backend.db.models.jobs import Job

def create_new_job(job: JobCreate, db: Session, owner_id: int):
  job_object = Job(**job.dict(), owner_id=owner_id)
  db.add(job_object)
  db.commit()
  db.refresh(job_object)
  return job_object

def retrieve_job(id: int, db: Session):
  item = db.query(Job).filter(Job.id == id).first()
  return item

def list_jobs(db: Session):
  jobs = db.query(Job).filter(Job.is_active == True).all()
  return jobs

def update_job_by_id(id: int, job: JobCreate, db: Session, owner_id):
  find_job = db.query(Job).filter(Job.id == id)

  if not find_job.first():
    return 0

  job.__dict__.update(owner_id = owner_id)
  find_job.update(job.__dict__)
  db.commit
  return 1