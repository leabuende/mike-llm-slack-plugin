# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV NAME llm-service
ENV TRELLO_KEY '1edd7bdf3e1d48a388dbe5918a414eac'
ENV TRELLO_TOKEN 'ATTA5df82beb4cc560fefb5f13b14c4893be82c057879cdedeae7385f72f2c41bdc081E2AD11'
ENV TRELLO_BOARD_ID '653f75b393231589d830ef99'

ENV OPENAI_API_TOKEN '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'
ENV EMBEDDINGS_MODEL 'text-embedding-ada-002'
ENV MAX_TOKENS 2000
ENV EMBEDDING_DIMENSION 1536

# Run your Python script when the container launches
CMD ["python", "main.py"]