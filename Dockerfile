FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock ./

RUN pip install uv && uv sync --no-dev

COPY . .

EXPOSE 8000

CMD ["uv", "run", "python", "main.py"]
