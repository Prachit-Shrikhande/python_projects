FROM ubuntu:latest

# Install dependencies for Miniconda and other necessary packages
RUN apt-get update && apt-get install -y \
    wget \
    bzip2 \
    ca-certificates \
    curl \
    libgl1 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Download and install Miniconda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-py310_24.4.0-0-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    chmod +x /tmp/miniconda.sh && \
    /tmp/miniconda.sh -b -p /app/miniconda && \
    rm /tmp/miniconda.sh

# Update PATH environment variable to include Miniconda
ENV PATH=/app/miniconda/bin:$PATH

# Set the working directory
WORKDIR /app

# Copy files from host to container
#COPY requirements.txt .
#COPY vision-ai-0.0.1-SNAPSHOT.jar .
#COPY python_module/ .
COPY . .

# Create and activate virtual environment, then install required packages
RUN /app/miniconda/bin/python -m venv /app/venv && \
    /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install -r /app/requirements.txt

# Expose port to the outside world
EXPOSE 8088

# Change the directory to the desired path before starting the container
WORKDIR /app/

# Specify the command to run on container start
# CMD ["/app/venv/bin/streamlit", "run", "streamlit_app.py", "--server.port=8088", "--server.enableCORS=false"]
CMD ["/app/venv/bin/streamlit", "run", "streamlit_app.py", "--server.port=8088", "server.address=127.0.0.1"]


