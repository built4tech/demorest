FROM python:3.11.9-alpine

# Set the working directory
WORKDIR /app

# Copy all files from the current directory to the container
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Command to run the Flask application
CMD ["python", "apirest.py", "8080"]