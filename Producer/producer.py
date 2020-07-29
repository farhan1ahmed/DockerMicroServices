import json
from time import sleep
from kafka import KafkaProducer

topicName = "userMockData"

produder = KafkaProducer(
    bootstrap_servers='kafkaservice:9093'
)
with open('/usr/src/app/producer/MOCK_DATA.json', encoding='utf-8') as mockFile:
    data = json.load(mockFile)

for item in data:
    data = json.dumps(item).encode('utf-8')
    produder.send(topicName, value=data)
    sleep(2)
