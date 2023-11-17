FROM python:3.9.18-slim-bookworm

WORKDIR .

COPY . .

RUN apt-get update && apt-get -y upgrade && pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["app/Main.py"]