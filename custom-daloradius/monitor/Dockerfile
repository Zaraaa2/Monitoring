FROM python:3.10-slim
RUN apt update && apt install -y snmp snmp-mibs-downloader && pip install pymysql
WORKDIR /app
COPY . .
CMD ["python", "app.py"]
