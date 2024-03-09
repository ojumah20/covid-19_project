# Use an official Python runtime as a parent image
FROM python:3.11.5-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN conda install --no-cache-dir -r requirements.txt

# Copy the IPython notebook, model, app.py, and dataset into the container
COPY xgboost.pkl .
COPY covid_19_project.ipynb .
COPY app.py .
COPY dataset.xlsx .

# Expose the port where the Streamlit app will run
EXPOSE $PORT

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
