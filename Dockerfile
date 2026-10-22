FROM python:3.12-slim

WORKDIR /app

COPY optical_status.py .
COPY optical_data.json .

CMD ["python", "optical_status.py"]
