# DockerMicroServices
This project was a hands-on expereince to get accustomed to the world of microservices, the purpose of message broker systems like Apache Kafka,
and the importance of container orchestration tools like Docker and Docker-Compose.

This project has four independent services running on Docker. Among them are:<br><br>
**Producer Service:** A Python based application which reads from a mock-data file and publishes this data to a topic in Kafka broker. <br>
**Kafka Service:** Kafka service runs the Docker image of Kafka Message broker and serves as a streaming platform that is used to publish and subscribe to streams of records.<br>
**Consumer Service:** A Python based application which is subsrcribed to a Kafka topic and consumes the data published on the topic. <br>
**PostgreSQL Service:** An application which runs a postgresql database on top of a Docker container. The Consumer Service inserts the data to a PostgreSQL table. <br>
