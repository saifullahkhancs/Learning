#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

echo "Waiting for database to be ready..."
while ! nc -z host.docker.internal 5432; do
  sleep 0.5
done
echo "Database is ready."

# The line below is commented out to prevent migration errors on an existing database.
# If your database schema is out of sync, this will allow the server to start.
# echo "Running Alembic migrations..."
# alembic upgrade head

exec "$@"