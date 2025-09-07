# NVIDIA NGC TensorFlow Image with GPU Support
# Source: https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tensorflow/tags
FROM nvcr.io/nvidia/tensorflow:25.02-tf2-py3

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# No default command - allows flexible usage for development
# For production, specify the command when running:
# docker run ... outside-the-box-ngc python run/train_CIFAR.py

# USAGE INSTRUCTIONS:
# Build: docker build -t outside-the-box-ngc -f Dockerfile.ngc .
# 
# Production Run:
# docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 --rm outside-the-box-ngc
#
# Interactive Development:
# docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 --rm -it -v ${PWD}:/app outside-the-box-ngc bash
#
# Run Specific Script:
# docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 --rm -v ${PWD}:/app outside-the-box-ngc python run/train_CIFAR.py
#
# NVIDIA Recommended Flags Explained:
# --gpus all           : Enable access to all GPUs
# --ipc=host          : Use host IPC for shared memory (faster data loading)
# --ulimit memlock=-1 : Remove memory lock limits (required for GPU memory pinning)
# --ulimit stack=...  : Increase stack size for deep neural networks