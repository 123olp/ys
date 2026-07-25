SHELL := /bin/bash

.PHONY: bootstrap up stop logs import backup smoke validate

bootstrap:
	./scripts/bootstrap.sh

up:
	docker compose --env-file .env up -d

stop:
	docker compose --env-file .env stop

logs:
	docker compose --env-file .env logs -f wiki

import:
	./scripts/import-content.sh

backup:
	./scripts/backup.sh

smoke:
	./scripts/smoke-test.sh

validate:
	./scripts/validate-source.sh
