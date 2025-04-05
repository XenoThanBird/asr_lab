# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Default to Streamlit dashboard on container start
CMD ["streamlit", "run", "asr_config_tester_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
