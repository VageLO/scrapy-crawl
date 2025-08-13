#FROM python:3.13-slim
FROM ubuntu:24.04
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN apt-get update
WORKDIR /app
COPY . .
WORKDIR /app/tutorial
RUN uv sync --frozen --no-cache
RUN uv run playwright install chromium --with-deps --only-shell
#RUN uv run playwright install-deps
#CMD ["uv", "run", "scrapy", "crawl", "awesome"]
