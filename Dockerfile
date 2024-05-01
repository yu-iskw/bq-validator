FROM python:3.11-slim

HEALTHCHECK NONE

# Create a non-root user and switch to it
RUN mkdir /home/app && \
    groupadd -g 10001 app && \
    useradd -u 10000 -g app app && \
    chown -R app:app /home/app
USER app:app
WORKDIR /home/app

# Install bq-validator
ENV BQ_VALIDATOR_VERSION=0.6.0
RUN python -m pip install --no-cache-dir -U pip==23.3.0 && \
    python -m pip install --no-cache-dir bq-validator==${BQ_VALIDATOR_VERSION}

ENTRYPOINT [ "bq-validator" ]
