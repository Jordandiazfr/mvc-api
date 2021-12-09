FROM python:3.8.12

WORKDIR /app
 
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


EXPOSE 80

COPY api /app/api

COPY test_mvc.py .

RUN pytest ./test_mvc.py



CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "80"]
