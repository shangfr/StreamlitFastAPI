FROM python:3.9-slim

WORKDIR /streamlit_ui

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "ui.py", "--server.port=8501", "--server.address=0.0.0.0"]

