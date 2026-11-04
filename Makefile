# Set up an environment
.PHONY: setup
setup: setup-python

.PHONY: setup-python
setup-python:
	bash ./dev/setup.sh --deps "development"

# Check all the coding style.
.PHONY: lint
lint:
	trunk check -a

# Check the coding style for the shell scripts.
.PHONY: lint-shell
lint-shell:
	shellcheck ./dev/*.sh

.PHONY: format
format:
	trunk fmt -a

# Run the unit tests in the current environment.
.PHONY: test
test:
	uv run bash ./dev/test_python.sh

# Run the complete supported-Python suite through the same entrypoint as CI.
.PHONY: test-all
test-all:
	uv run --with "nox[uv]==2026.7.11" bash ./dev/test_all.sh

# Build the package
.PHONY: build
build: clean test
	uv build

.PHONY: clean
clean:
	bash ./dev/clean.sh

# Publish to pypi
.PHONY: publish
publish:
	bash ./dev/publish.sh "pypi"

# Publish to testpypi
.PHONY: test-publish
test-publish:
	bash ./dev/publish.sh "testpypi"
