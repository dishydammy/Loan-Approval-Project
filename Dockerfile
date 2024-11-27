FROM python:3.12-slim

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY ["pyproject.toml", "poetry.lock", "./"]

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY ["predict.py", "model.bin", "./"]

RUN pip install gunicorn

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
