FROM python:3.10-slim
WORKDIR /app
COPY . /app
# Install the current directory as a package
RUN pip install --no-cache-dir .
RUN useradd -m myuser
USER myuser
EXPOSE 7860
# Run the script defined in pyproject.toml
CMD ["server"]
