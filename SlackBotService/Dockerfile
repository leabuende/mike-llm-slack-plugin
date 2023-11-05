# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Define environment variable
ENV NAME slackbot-service
ENV SLACK_SIGNING_SECRET e34090427cbed1a75be83519f2aa0aaa
ENV SLACK_BOT_TOKEN xoxb-6099716673159-6150592408225-eHWSWhCCAxNoBl5S56SPOdkl
ENV VERIFICATION_TOKEN SdfSycTLt3nDOwPoKnt3Uj6Z

# Run app.py when the container launches
CMD ["python", "main.py"]