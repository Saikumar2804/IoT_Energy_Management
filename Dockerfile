# Step 1: Use Python base image
FROM python:3.9-slim

# Step 2: Set working directory inside the container
WORKDIR /app

# Step 3: Copy project files into the container
COPY . .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose a port (optional, if running as a web app)
# EXPOSE 5000

# Step 6: Specify the command to run your script
CMD ["python", "main.py"]