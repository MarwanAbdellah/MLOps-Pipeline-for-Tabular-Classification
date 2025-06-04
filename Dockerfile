FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn onnx onnxruntime numpy 

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]