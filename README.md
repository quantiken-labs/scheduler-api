# Scheduler API (Podman) — Test Version

⚠️ IMPORTANT NOTICE  
This software is a **test / evaluation version of a paid subscription service**.

It is provided **strictly for testing, development, and evaluation purposes only**.

❌ Production use is not permitted  
❌ Commercial use is not permitted  
❌ SLA, reliability, or uptime guarantees are not provided  

---

## Overview

This project is a **test scheduling API** that allows users to:

- Schedule interval-based background jobs
- List scheduled jobs
- Remove scheduled jobs

The scheduler runs **in-memory only** and is reset on container restart.  
This is intentional and part of the test-only design.

---

## Project Structure

scheduler-api/
├── app/
│   ├── main.py
│   └── scheduler.py
├── Containerfile
├── requirements.txt
├── .env
└── README.md

---

## Intended Use (Test Only)

Allowed:
- Local testing
- Development environments
- Proof-of-concept usage
- Feature validation

Not allowed:
- Production workloads
- Customer-facing deployments
- Persistent job scheduling
- Financial, medical, or safety-critical systems
- Commercial resale or redistribution

---

## Requirements

- Podman
- Network access for API testing

---

## Build the Test Container

podman build -t scheduler-api-test .

---

## Run the Test API

podman run -d -p 8000:8000 --env-file .env scheduler-api-test

The API will be available at:

http://localhost:8000

Swagger UI (test only):

http://localhost:8000/docs

---

## API Endpoints (Test)

POST /schedule  
Create an interval job

Example body:
{
  "seconds": 10,
  "message": "test job"
}

GET /jobs  
List all scheduled jobs

DELETE /jobs/{job_id}  
Delete a scheduled job

---

## Limitations (By Design)

- Jobs are not persisted
- No authentication
- No rate limiting
- No retries
- No HA or redundancy

---

## Production Disclaimer

This software is **NOT production-ready**.

A paid subscription version would include:
- Persistent job storage
- Authentication and authorization
- Distributed execution
- Monitoring and alerting
- Failure handling and retries

---

## License

Test License Only

Use is limited to testing and evaluation purposes.  
All other rights are reserved.
