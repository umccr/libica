help:
	@echo 'make doc'

.PHONY: doc
doc:
	@pdoc --force --html libica -o docs/
	@py.test --cov-config=.coveragerc --cov-report html:docs/coverage --cov=libica
	@(cd openapi && mkdocs build --clean -d ../docs/openapi)

.PHONY: local
local:
	@pdoc --force --html libica -o local/
	@py.test --cov-config=.coveragerc --cov-report html:local/coverage --cov=libica
	@(cd openapi && mkdocs build --clean -d ../local/openapi)

up:
	@docker compose up -d

down:
	@docker compose down

ps:
	@docker compose ps

test_ica_mock:
	@curl -s -H "Authorization: Bearer Test" -X GET http://localhost/v1/workflows/runs/wfr.anything_work | jq

test_icav2_mock:
	@curl -s -H "Authorization: Bearer Test" -X GET http://localhost/api/projects/1 | jq

install:
	@pip install '.[test,dev]'
	@yarn install

unit:
	@py.test --no-cov tests/

autounit:
	@py.test --no-cov libica/openapi

test:
	@py.test

tox:
	@tox -vv

nose:
	@nose2 -vv

clean:
	@rm -rf build/
	@rm -rf libica.egg-info/

.PHONY: dist
dist: clean
	@python setup.py sdist bdist_wheel

# Usage: make testpypi version=0.2.0
testpypi: dist/libica-$(version).tar.gz
	@twine upload --repository testpypi --sign dist/libica-$(version)*

pypi: dist/libica-$(version).tar.gz
	@twine upload --sign dist/libica-$(version)*

.PHONY: getapi genapi mvapidoc rmapi
getapi:
	@. syncapi.sh; getapi

genapi:
	@. syncapi.sh; genapi; mvapidoc

mvapidoc:
	@. syncapi.sh; mvapidoc

check: chkepver validate

# check endpoint version
chkepver:
	@. syncapi.sh; chkepver

# validate swagger openapi definitions
validate:
	@. syncapi.sh; validateapi

########
# ICA v2

.PHONY: getapi2 genapi2 mvapidoc2 rmapi2 sweepapi2
getapi2:
	@. syncapi2.sh; getapi

sweepapi2:
	@python sweep.py

genapi2:
	@. syncapi2.sh; genapi; mvapidoc

mvapidoc2:
	@. syncapi2.sh; mvapidoc

check2: chkepver2 validate2

# check endpoint version
chkepver2:
	@. syncapi2.sh; chkepver

# validate swagger openapi definitions
validate2:
	@. syncapi2.sh; validateapi
