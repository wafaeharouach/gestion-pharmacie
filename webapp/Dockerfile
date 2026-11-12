FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY init_db.py .

EXPOSE 8501

CMD ["sh", "-c", "python init_db.py && streamlit run app.py --server.address=0.0.0.0 --server.port=8501"]