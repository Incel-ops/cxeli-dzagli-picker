FROM python:3.10-slim

WORKDIR /app

# ვაკოპირებთ requirements.txt და ვაინსტალირებთ ბიბლიოთეკებს
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY episodes.json .

CMD ["python", "-u", "main.py"]
