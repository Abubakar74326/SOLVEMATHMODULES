# Inherit from the Python Docker image
FROM python:3.9-slim
# Install the Flask package via pip
RUN pip install flask

COPY main.py /
COPY api.py /
COPY modulefunction.py /
COPY requirements.txt /
EXPOSE 5004
# Set the command as the script name
CMD ["python", "main.py"]