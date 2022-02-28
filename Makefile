# Set up an environment
.PHONEY: setup
setup:
	bash ./dev/setup.sh

# Check all the conding style.
.PHONY: lint
lint: lint-shell lint-python

# Check the conding style for the shell scripts.
.PHONY: lint-shell
lint-shell:
	shellcheck ./dev/*.sh

# Check the conding style for the python files.
.PHONY: lint-python
lint-python:
	bash ./dev/lint_python.sh

# Run the unit tests.
.PHONEY: test
test:
	bash ./dev/run_python_tests.sh

# Build the package
build: lint test
	python -m build
