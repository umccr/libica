help:
	@echo 'make doc'

.PHONY: doc
doc:
	@(cd sphinx && make github)
	@pdoc --force --html libiap -o docs/
	@py.test --cov-config=.coveragerc --cov-report html:docs/coverage --cov=libiap
	@(cd openapi && mkdocs build --clean -d ../docs/openapi)

.PHONY: local
local:
	@(cd sphinx && make local)
	@pdoc --force --html libiap -o local/
	@py.test --cov-config=.coveragerc --cov-report html:local/coverage --cov=libiap
	@(cd openapi && mkdocs build --clean -d ../local/openapi)

test:
	@py.test

pilot:
	@python3 pilot.py

.PHONY: dist
dist:
	@python setup.py sdist bdist_wheel

.PHONY: getapi genapi mvapidoc rmapi
getapi:
	@. syncapi.sh; getapi

genapi:
	@. syncapi.sh; genapi; mvapidoc

mvapidoc:
	@. syncapi.sh; mvapidoc
