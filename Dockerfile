FROM ghcr.io/torana-fixpr-test/base:latest
WORKDIR /srv
COPY app ./app
CMD ["python", "-m", "app.main"]
