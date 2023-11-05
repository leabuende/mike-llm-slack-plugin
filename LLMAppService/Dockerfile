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
ENV TRELLO_KEY ''
ENV TRELLO_TOKEN ''
ENV TRELLO_BOARD_ID ''

ENV OPENAI_API_TOKEN ''
ENV EMBEDDINGS_MODEL ''
ENV MAX_TOKENS 2000
ENV EMBEDDING_DIMENSION 1536

# Run your Python script when the container launches
CMD ["python", "main.py"]