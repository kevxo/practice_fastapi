import json

def test_create_job(client):
  data = {
    "title": "SDE super",
    "company": "doogle",
    "company_url": "www.doogle.com",
    "location": "USA, NY",
    "description": "python",
    "data_posted": "2022-03-20"
  }

  response = client.post("/jobs/create-job/", json.dumps(data))

  assert response.status_code == 200
  assert response.json()["company"] == "doogle"
  assert response.json()["description"] == "python"


def test_get_a_job(client):
  data = {
    "title": "SDE super",
    "company": "doogle",
    "company_url": "www.doogle.com",
    "location": "USA, NY",
    "description": "python",
    "data_posted": "2022-03-20"
  }

  response = client.post("/jobs/create-job/", json.dumps(data))

  response = client.get("/jobs/get/1")
  assert response.status_code == 200
  assert response.json()["title"] == "SDE super"


def test_cant_get_job(client):
  response = client.get("/jobs/get/1")
  assert response.status_code == 404
  assert response.json()["detail"] == "Job with thus id 1 doesn't exist"

def test_it_can_read_all_jobs(client):
  data = {
    "title": "SDE super",
    "company": "doogle",
    "company_url": "www.doogle.com",
    "location": "USA, NY",
    "description": "python",
    "data_posted": "2022-03-20"
  }

  client.post("/jobs/create-job/", json.dumps(data))
  client.post("/jobs/create-job/", json.dumps(data))

  response = client.get("/jobs/all")
  assert response.status_code == 200
  assert response.json()[0]
  assert response.json()[1]