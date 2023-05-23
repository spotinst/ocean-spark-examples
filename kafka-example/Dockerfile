# choose a base image
FROM public.ecr.aws/ocean-spark/spark:platform-3.3.1-gen19

USER root

# install any required linux packages
RUN apt-get update && apt-get install -y python3  python3-pip libffi-dev
ENV PYSPARK_MAJOR_PYTHON_VERSION=3

# download the kafka related libraries based on the kafka version that you use
RUN wget https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.11.1/commons-pool2-2.11.1.jar
RUN wget https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.3.1/spark-sql-kafka-0-10_2.12-3.3.1.jar 
RUN wget https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.3.1/kafka-clients-3.3.1.jar
RUN wget https://repo1.maven.org/maven2/org/apache/spark/spark-token-provider-kafka-0-10_2.12/3.3.1/spark-token-provider-kafka-0-10_2.12-3.3.1.jar

# move the downloaded libraries to the jars location within the image
RUN mv commons-pool2-2.11.1.jar spark-sql-kafka-0-10_2.12-3.3.1.jar kafka-clients-3.3.1.jar spark-token-provider-kafka-0-10_2.12-3.3.1.jar  /opt/spark/jars/

# install any other libraries that are needed for your application
RUN pip3 install --upgrade pip
RUN pip3 install pandas
RUN pip install azure-ai-textanalytics
