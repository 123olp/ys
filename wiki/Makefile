SHELL := /bin/bash

.PHONY: bootstrap up stop logs import backup smoke validate homepage-refresh homepage-build homepage-check homepage-compare

bootstrap:
	./scripts/bootstrap.sh

up:
	docker compose --env-file .env up -d

stop:
	docker compose --env-file .env stop

logs:
	docker compose --env-file .env logs -f portal wiki

import:
	./scripts/import-content.sh

backup:
	./scripts/backup.sh

smoke:
	./scripts/smoke-test.sh

validate:
	./scripts/validate-source.sh

homepage-refresh:
	python3 scripts/refresh-wikipedia-homepage.py --write

homepage-build:
	python3 scripts/build-wikipedia-homepage.py

homepage-check:
	python3 scripts/build-wikipedia-homepage.py --check

homepage-compare:
	python3 scripts/compare-wikipedia-homepage.py
