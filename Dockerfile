FROM python:3.10
WORKDIR /payment_system
COPY . /payment_system
RUN pip install -r requirements.txt
CMD ["uvicorn", "main", "--host=0.0.0.0", "--port=8080"]