# Use official Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code into the container
COPY app/mcp_server.py .

# Expose the port your application will listen on
EXPOSE 8001

# Set the default command to run your server
CMD ["python", "mcp_server.py"]

