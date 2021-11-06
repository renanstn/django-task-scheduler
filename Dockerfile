# =============================================================================
# Base
# =============================================================================
FROM python:3.9 AS base
ENV PYTHONUNBUFFERED 1
ENV DOCKERENV 1
RUN pip install --upgrade pip
RUN pip install pipenv
WORKDIR /app
COPY Pipfile Pipfile.lock /app/

# =============================================================================
# Development
# =============================================================================
FROM base as development
RUN pipenv install --system --deploy --dev
COPY ./task_scheduler /app/
RUN chmod +x /app/*.sh
CMD ["sh", "setup_dev.sh"]

# =============================================================================
# Prod
# =============================================================================
FROM base as production
RUN pipenv install --system --deploy
COPY ./task_scheduler /app/
