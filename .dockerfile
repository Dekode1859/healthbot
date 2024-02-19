# This is the dockerfile for the streamlit app
# use the official image as a parent image

FROM python:3.9

# Set the working directory to /app

WORKDIR /app

# Copy the current directory contents into the container at /app

COPY . /app

# Install any needed packages specified in requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# expose the port inside the container

EXPOSE 8501

# Run app.py when the container launches with port mapping

CMD ["streamlit", "run", "app.py" "--server.port=8501", "--server.address=0.0.0.0"]