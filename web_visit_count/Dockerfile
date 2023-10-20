# Use a Python image as the base image
FROM python:3.9-slim

# Install required packages
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install psycopg2-binary

# Copy the Python script into the container
COPY ./web_visit_counter.py /app/web_visit_counter.py

# Set the working directory
WORKDIR /app
CMD ["python","web_visit_counter.py"]



