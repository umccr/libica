help:
	@echo 'make doc'

doc:
	@(cd sphinx && make github)
	@pdoc --force --html libiap -o docs/
	@py.test --cov-report html:docs/coverage --cov=libiap tests/

test:
	@pytest
	@python pilot.py

dist:
	@python setup.py sdist bdist_wheel
