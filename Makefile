help:
	@echo 'make doc'

scan:
	@trufflehog --debug --only-verified git file://./ --since-commit main --branch HEAD --fail

deep: scan
	@ggshield secret scan repo .

pre-commit:
	@pre-commit run --all-files

baseline:
	@detect-secrets scan --exclude-files '^(package-lock.json|.local/|docs/|openapi/|swagger/)' > .secrets.baseline

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

test_icav2_mock:
	@curl -s -H "Authorization: Bearer Test" -X GET http://localhost/api/projects/1 | jq

install:
	@pip install '.[test,dev]'
	@npm install
	@pre-commit install

single:
	@python -m unittest libica.openapi.v3.test.test_workflow_v3.TestWorkflowV3
	@python -m unittest libica.openapi.v3.test.test_workflow_v4.TestWorkflowV4

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
	@python3 -m build

# Usage: make testpypi version=0.2.0
testpypi: dist/libica-$(version).tar.gz
	@python3 -m twine upload --repository testpypi dist/libica-$(version).tar.gz
	@python3 -m twine upload --repository testpypi dist/libica-$(version)-*.whl

pypi: dist/libica-$(version).tar.gz
	@python3 -m twine upload dist/libica-$(version).tar.gz
	@python3 -m twine upload dist/libica-$(version)-*.whl

########
# Generate v2 SDK package

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

########
# Generate v3 SDK package

.PHONY: getapi3 genapi3 mvapidoc3 rmapi3 sweepapi3
# THIS WILL BE THE SAME AS v2 PACKAGE SINCE USING THE SAME API DOC. COMMENTING OUT FOR NOT TO CONFUSE.
#getapi3:
#	@. syncapi3.sh; getapi
#
#sweepapi3:
#	@python sweep.py

genapi3:
	@. syncapi3.sh; genapi; mvapidoc

mvapidoc3:
	@. syncapi3.sh; mvapidoc

check3: chkepver3 validate3

# check endpoint version
chkepver3:
	@. syncapi3.sh; chkepver

# validate swagger openapi definitions
validate3:
	@. syncapi3.sh; validateapi
