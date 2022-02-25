#!/bin/bash
set -e

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"

pylint -v "${MODULE_DIR}"/bq_validator "${MODULE_DIR}"/tests
