FROM python:3
WORKDIR /usr/src/app/producer
COPY . . 
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python","-u", "./producer.py"]