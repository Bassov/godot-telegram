define BACKEND_HELP
Availiable backend <target>:
	backend/prepare_env    - Initialize the environment for local development

	Migrations:
	backend/gen_auto_migration - Generate auto migration based on SQLModel definitions
	backend/gen_migration      - Generate empty migration
	backend/migrate            - Run migrations
	backend/rollback           - Rollback last migration

	Tests:
	backend/test               - Run tests

	Other:
	backend/bash               - Run bash

endef
export BACKEND_HELP

backend/help:
	@echo "$$BACKEND_HELP"

# env
backend/prepare_env:
	test -f apps/backend/.env.secret || cp apps/backend/.env.secret.example apps/backend/.env.secret && \
	test -f apps/backend/.venv || mkdir apps/backend/.venv

# DB migrations
backend/gen_auto_migration:
	docker compose run --rm backend alembic revision --autogenerate -m "$(name)"
backend/gen_migration:
	docker compose run --rm backend alembic revision -m "$(name)"
backend/migrate:
	docker compose run --rm backend alembic upgrade head
backend/rollback:
	docker compose run --rm backend alembic downgrade -1

# tests
backend/test:
	docker compose run --rm backend pytest

backend/bash:
	docker compose run --rm backend bash
backend/image-bash:
	docker run --rm -it godot-telegram-backend:latest /bin/bash