import os
from kafka import KafkaProducer



# use public ip addresses in the format {ip}:{port} such as 44.235.242.0:9092,52.89.214.1:9092,54.185.48.2:9092
KAFKA_BOOTSTRAP_SERVERS = '{public ip addresses with port}'
SECURITY_PROTOCOL = 'SASL_PLAINTEXT'  
SASL_MECHANISM = 'SCRAM-SHA-256'  
SASL_USERNAME = os.environ.get('KAFKA_USERNAME')
SASL_PASSWORD = os.environ.get('KAFKA_PASSWORD')


KAFKA_TOPIC = 'test-ofas-demo-0'


# Function to create a Kafka producer
def create_kafka_producer(bootstrap_servers,security_protocol, sasl_mechanism, sasl_username, sasl_password):
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                             security_protocol=security_protocol,
                             sasl_mechanism=sasl_mechanism,
                             sasl_plain_username=sasl_username,
                             sasl_plain_password=sasl_password,
                             key_serializer=str.encode,
                             value_serializer=str.encode)
    return producer


# Create a Kafka producer
kafka_producer = create_kafka_producer(KAFKA_BOOTSTRAP_SERVERS, SECURITY_PROTOCOL, SASL_MECHANISM, SASL_USERNAME, SASL_PASSWORD)

keywords_to_track = ['ChatGPT', 'Bard', 'Github Copilot']
message = ""


for i in range(1000):
    for keyword in keywords_to_track:    
        if i % 3 == 0:
            message = f"{keyword} is good {i}"
        elif i % 3 == 1:
            message = f"{keyword} is bad {i}"
        else:
            message = f"{keyword} is ok {i}"
        kafka_producer.send(KAFKA_TOPIC, key=keyword, value=message)
        








