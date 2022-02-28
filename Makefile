# Set up an environment
.PHONEY: setup
setup:
	bash ./dev/setup.sh

# Check all the coding style.
.PHONY: lint
lint: lint-shell lint-python

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
	bash ./dev/run_python_tests.sh

# Build the package
build: clean lint test
	python -m build

clean:
	bash ./dev/clean.sh
