FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir "psycopg[binary]>=3.2,<4"
COPY server.py import_export.py validate.py sync_names.py /app/
EXPOSE 8080
CMD ["python", "-u", "server.py"]
