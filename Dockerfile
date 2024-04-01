FROM python:3.11

COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir -r /src/requirements.txt

COPY ./src /app

WORKDIR /src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
