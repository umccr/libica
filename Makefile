help:
	@echo 'make doc'

.PHONY: doc
doc:
	@pdoc --force --html libiap -o docs/
	@py.test --cov-config=.coveragerc --cov-report html:docs/coverage --cov=libiap
	@(cd openapi && mkdocs build --clean -d ../docs/openapi)

.PHONY: local
local:
	@pdoc --force --html libiap -o local/
	@py.test --cov-config=.coveragerc --cov-report html:local/coverage --cov=libiap
	@(cd openapi && mkdocs build --clean -d ../local/openapi)

up:
	@docker-compose up -d

down:
	@docker-compose down

test_iap_mock:
	@curl -s -H "Authorization: Bearer Test" -X GET http://localhost/v1/workflows/runs/wfr.anything_work | jq

install:
	@pip install -e '.[test,dev]' .

unit:
	@py.test --no-cov tests/unit

autounit:
	@py.test --no-cov libiap/openapi

it:
	@py.test --no-cov tests/integration/

test:
	@py.test

pilot:
	@python3 pilot.py

.PHONY: dist
dist:
	@python setup.py sdist bdist_wheel

# Usage: make testpypi version=0.2.0
testpypi: dist/libiap-$(version).tar.gz
	@twine upload --repository testpypi --sign dist/libiap-$(version)*

pypi: dist/libiap-$(version).tar.gz
	@twine upload --sign dist/libiap-$(version)*

.PHONY: getapi genapi mvapidoc rmapi
getapi:
	@. syncapi.sh; getapi

genapi:
	@. syncapi.sh; genapi; mvapidoc

mvapidoc:
	@. syncapi.sh; mvapidoc
