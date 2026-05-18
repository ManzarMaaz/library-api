# Stage 1: Base builder stage
FROM python:3.12-slim AS builder
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Stage 2: Development & Testing
FROM builder AS development
COPY . /code
# Development retains testing capabilities (pytest, coverage)
CMD ["fastapi", "run", "app/main.py", "--port", "80"]

# Stage 3: Lean Production
FROM python:3.12-slim AS production
WORKDIR /code
# Copy only installed python packages from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
# Copy only core application files (No tests folder allowed!)
COPY ./app /code/app
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
