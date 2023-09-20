# Use the official Python image as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Copy the model file from your local machine into the container
COPY acne_classification_model.h5 /app/acne_classification_model.h5


# Define the command to run your application
CMD ["python", "app.py"]
