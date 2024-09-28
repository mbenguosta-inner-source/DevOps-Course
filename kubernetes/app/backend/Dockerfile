# Base image from docker hub
FROM python:3.9

# Create main directory from where we work
WORKDIR /code

# Copy requirements file
COPY ./requirements.txt /code/requirements.txt

# Install requirements from requirement.txt copied in the above step
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy code from local to container
COPY ./app /code/app

EXPOSE 8000

# Execute main file to run the App
CMD ["uvicorn", "app.server.app:app", "--host", "0.0.0.0", "--port", "8000"]
