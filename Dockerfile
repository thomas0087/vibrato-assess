FROM python:3.6-alpine
ADD . /app
WORKDIR /app
RUN pip install flask
CMD ["python", "main.py"]
