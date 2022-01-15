FROM python:3.8.10-slim

RUN pip install pytest && pip install pytest-cov \
    && mkdir -p /home/app

WORKDIR /home/app

COPY . .

CMD [ "python", "main.py"]