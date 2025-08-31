FROM python:3.12-slim

WORKDIR /usr/src/app

COPY requirements.txt .

# Install build tools and netcat
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    #build-essential \
    #libssl-dev \
    #libffi-dev \
    #python3-dev \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "until nc -z db 3306;do echo '⏳ waiting for db...';  sleep 2; done && python migrations/run_migration.py; streamlit run app.py --server.port=8501 --server.address=0.0.0.0"]


