SHELL := /bin/bash

.PHONY: bootstrap up stop logs import backup smoke language-selector-check validate homepage-refresh homepage-build homepage-check homepage-reference homepage-compare homepage-audit-reference homepage-audit

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

language-selector-check:
	./scripts/check-language-selector.sh

validate:
	./scripts/validate-source.sh

homepage-refresh:
	python3 scripts/refresh-wikipedia-homepage.py --write

homepage-build:
	python3 scripts/build-wikipedia-homepage.py

homepage-check:
	python3 scripts/build-wikipedia-homepage.py --check

homepage-reference:
	./scripts/run-backstop.sh reference contract

homepage-compare:
	./scripts/run-backstop.sh test contract

homepage-audit-reference:
	./scripts/run-backstop.sh reference audit

homepage-audit:
	./scripts/run-backstop.sh test audit
