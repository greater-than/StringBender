VENV_NAME?=.venv
PYTHON=${VENV_NAME}/bin/python
PYTHON_VERSION=3.12.5
SRC_DIR=src

# By default, set up the virtual environment and install dependencies
all: venv setup

venv:
	# Create virtual environment
	test -d $(VENV_NAME) || python -m venv $(VENV_NAME)
	. $(VENV_NAME)/bin/activate
	touch venv

poetry:
	pipx install poetry
	poetry env use 3.12.5

install-dependencies: venv poetry
	poetry install

install-build-dependencies: venv poetry
	poetry install --without dev,test

setup: install-dependencies
	$(VENV_NAME)/bin/pre-commit install

format: install-dependencies
	$(VENV_NAME)/bin/isort .

code-check: install-dependencies
	$(VENV_NAME)/bin/pre-commit run --all-files

lint: install-dependencies
	$(VENV_NAME)/bin/flake8 .
	$(VENV_NAME)/bin/isort --check-only $(SRC_DIR)

typecheck: install-dependencies
	$(VENV_NAME)/bin/mypy -m src

test: install-dependencies
	$(VENV_NAME)/bin/pytest

build: clean code-check test
	poetry install --without dev,test --sync
	poetry build

publish: build
	poetry install --with publish
	# poetry publish
	# twine upload --repository $1 dist/*

release:
	git commit --allow-empty -m "Release" $(RELEASE)
	git tag -a $(RELEASE) -m "Version" $(RELEASE)
	git push upstream --tags

clean:
	# Clean up generated folders and files
	rm -rf $(VENV_NAME)
	-find . -name "*.pyc" -exec rm {} \;
	-find . -name "__pycache__" -exec rm -r {} \;
	-find . -name ".mypy_cache" -exec rm -r {} \;
	-find . -name ".pytest_cache" -exec rm -r {} \;
	-find . -name ".test_results" -exec rm -r {} \;
	-find . -name "build" -exec rm -r {} \;
	-find . -name "dist" -exec rm -r {} \;
	touch venv

.PHONY: all venv setup format code-check lint typecheck test build publish release clean
