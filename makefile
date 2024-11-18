VENV_NAME?=.venv
PYTHON=${VENV_NAME}/bin/python
PYTHON_VERSION=3.13.0
SRC_DIR=src
RELEASE=0.4.0

# By default, set up the virtual environment and install dependencies
all: setup

.venv/bin/activate: pyproject.toml
	pipx install poetry
	poetry self add poetry-plugin-sort
	poetry env use ${PYTHON_VERSION}

install-dependencies: .venv/bin/activate
	poetry install

install-build-dependencies:
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

build: clean code-check test install-build-dependencies
	poetry build

publish: build
	poetry install --with publish
	# poetry publish
	# twine upload --repository $1 dist/*

release:
	git commit --allow-empty -m "Release v$(RELEASE)"
	git tag -a v$(RELEASE) -m "Version $(RELEASE)"
	git push origin --tags

clean:
	pipx uninstall poetry
	# Clean up generated folders and files
	rm -rf $(VENV_NAME)
	-find . -name "*.pyc" -exec rm {} \;
	-find . -name "__pycache__" -exec rm -r {} \;
	-find . -name ".mypy_cache" -exec rm -r {} \;
	-find . -name ".pytest_cache" -exec rm -r {} \;
	-find . -name ".test_results" -exec rm -r {} \;
	-find . -name "build" -exec rm -r {} \;
	-find . -name "dist" -exec rm -r {} \;
	touch pyproject.toml

.PHONY: all venv setup format code-check lint typecheck test build publish release clean
