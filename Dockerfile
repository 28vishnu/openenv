FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir fastapi uvicorn openai python-multipart openenv-core
RUN useradd -m myuser
USER myuser
EXPOSE 7860
# Direct path to the app within the server folder
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]
