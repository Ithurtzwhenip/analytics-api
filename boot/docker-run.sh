#!/bin/bash

source /opt/venv/bin/activate

cd /code
RUN_PORT=${PORT:-8000}
RUN_HOST=${HOST:-0.0.0.0}

exec gunicorn -k uvicorn.workers.UvicornWorker \
    -b $RUN_HOST:$RUN_PORT \
    --log-level info \
    --access-logfile - \
    --error-logfile - \
    main:app
