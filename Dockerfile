FROM python:3.13

WORKDIR /flask-app

# Install uv package manager
RUN pip install uv

# Copy Python requirements and install them using uv
COPY requirements.txt ./
RUN uv pip install --system -r requirements.txt

COPY . .

CMD ["python3", "run.py"]