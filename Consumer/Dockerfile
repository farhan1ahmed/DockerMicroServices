FROM python:3
WORKDIR /usr/src/app/Consumer
COPY . /usr/src/app/Consumer
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONPATH /usr/src/app
CMD ["python", "-u", "./consumer.py"]
