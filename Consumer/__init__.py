from kafka import KafkaConsumer
import psycopg2

topicName = "userMockData"

consumer = KafkaConsumer(
    topicName,
    bootstrap_servers='kafkaservice:9093',
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    auto_commit_interval_ms=1000,
    group_id="my-group-1",
)


class postgresDB:
    @staticmethod
    def getconnection():
        try:
            connection = psycopg2.connect(
                user="farhan",
                password="1234",
                host="pgcontainer",
                port="5432",
                database="service_db"
            )
            return connection
        except psycopg2.DatabaseError:
            print("Error connecting to database")
            raise psycopg2.DatabaseError
