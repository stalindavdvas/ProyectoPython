# USe a image with python
FROM python:3.10-slim

# put the directory on container
WORKDIR /app

# Copy the file of requirements to image
COPY requirements.txt .

# Install the dependences
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source of aplication to workspace
COPY . .

# Expose the port that will Flask Use
EXPOSE 5000

# Define the variable to env for flask
ENV FLASK_APP=app.py

# Command to execute the aplication
CMD ["flask", "run", "--host=0.0.0.0"]
