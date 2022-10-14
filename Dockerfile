# FROM python:3.8
# WORKDIR /app
# COPY . .
# RUN pip install -r requirements.txt
# CMD ["streamlit", "run", "app.py"]
# app/Dockerfile

FROM python:3.8-slim

# COPY . /app

EXPOSE 8501

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/10tanmay100/Covid-19-Image-Classifier.git .

COPY . /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]