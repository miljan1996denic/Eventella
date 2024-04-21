#!/bin/sh
# pip install debugpy && python -m debugpy --wait-for-client --listen 0.0.0.0:5678 -m uvicorn ticketing.main:app --reload --host 0.0.0.0 --port 80
uvicorn ticketing.main:app --reload --host 0.0.0.0 --port 80