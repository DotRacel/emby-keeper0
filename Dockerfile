FROM python:3.11 AS builder

WORKDIR /src
COPY . .

RUN python -m venv /opt/venv \
    && . /opt/venv/bin/activate \
    && pip install --no-cache-dir -U pip setuptools wheel \
    && pip install --no-cache-dir .

FROM python:3.11-slim
COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /src/scripts/docker-entrypoint.sh /entrypoint.sh

ENV TZ="Asia/Shanghai"
ENV EK_IN_DOCKER="1"

LABEL org.opencontainers.image.source="https://github.com/DotRacel/emby-keeper0" \
      org.opencontainers.image.description="Emby 签到保号自动化工具 (去中心化维护版)" \
      org.opencontainers.image.licenses="GPL-3.0"

WORKDIR /app
RUN chmod +x /entrypoint.sh \
    && touch config.toml
ENV PATH="/opt/venv/bin:$PATH"

ENTRYPOINT ["/entrypoint.sh"]
