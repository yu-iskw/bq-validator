# Set up an environment
.PHONEY: setup
setup: setup-python setup-pre-commit

.PHONEY: setup-python
setup-python:
	bash ./dev/setup.sh

.PHONEY: setup-pre-commit
setup-pre-commit:
	pre-commit install

.PHONEY: update-pre-commit
update-pre-commit:
	pre-commit autoupdate

# Check all the coding style.
.PHONY: lint
lint: lint-shell lint-python lint-pre-commit

.PHONE: lint-pre-commit
lint-pre-commit:
	pre-commit run --all-files

# Check the coding style for the shell scripts.
.PHONY: lint-shell
lint-shell:
	shellcheck ./dev/*.sh

# Check the coding style for the python files.
.PHONY: lint-python
lint-python:
	bash ./dev/lint_python.sh

# Format source codes
format: format-python

# Format python codes
format-python:
	bash ./dev/format_python.sh

# Run the unit tests.
.PHONEY: test
test:
	bash ./dev/test_python.sh

# Build the package
build: clean format test
	flit build

clean:
	bash ./dev/clean.sh

# Publish to pypi
publish:
	bash ./dev/publish.sh "pypi"

# Publish to testpypi
test-publish:
	bash ./dev/publish.sh "testpypi"
