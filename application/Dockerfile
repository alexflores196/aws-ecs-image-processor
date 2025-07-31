# Use an official Python runtime as a parent image
FROM public.ecr.aws/docker/library/python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable for the S3 bucket (will be passed in by ECS Task Definition)
ENV S3_BUCKET_NAME=""

# Run app.py when the container launches
CMD ["python", "app.py"]