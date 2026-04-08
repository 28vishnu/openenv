FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir .
RUN useradd -m myuser
USER myuser
EXPOSE 7860
CMD ["server"]
