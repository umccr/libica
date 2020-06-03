help:
	@echo 'make doc'

.PHONY: doc
doc:
	@(cd sphinx && make github)
	@pdoc --force --html libiap -o docs/
	@py.test --cov-report html:docs/coverage --cov=libiap tests/

test:
	@pytest
	@python pilot.py

.PHONY: dist
dist:
	@python setup.py sdist bdist_wheel
