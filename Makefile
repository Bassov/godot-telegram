include ./backend.Makefile

USER_ID:=$(shell id -u ${USER})
GROUP_ID:=$(shell id -g ${USER})

export USER_ID
export GROUP_ID

define HELP
Usage: make <target>
Example usage:
	make help
	make init
	make run

Availiable <target>:
	init            - Initialize the environment for local development
	run             - Run whole godot-telegram services in 1 command

	build           - Build the application
	up              - Start the application
	down            - Stop the application
	bash            - Run bash in the application container
	logs            - Follow the logs

endef
export HELP

help:
	@echo "$$HELP"
	@echo "$$BACKEND_HELP"

init: backend/prepare_env
run: build up backend/migrate logs
build:
	docker compose build
up:
	docker compose up -d
down:
	docker compose down
bash:
	docker compose run --rm backend bash
logs:
	docker compose logs -f
