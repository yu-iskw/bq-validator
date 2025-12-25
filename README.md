[![Test python](https://github.com/yu-iskw/bq-validator/actions/workflows/test.yml/badge.svg)](https://github.com/yu-iskw/bq-validator/actions/workflows/test.yml)
<a href="https://pypi.org/project/bq-validator" target="_blank">
<img src="https://img.shields.io/pypi/v/bq-validator?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/bq-validator" target="_blank">
<img src="https://img.shields.io/pypi/pyversions/bq-validator.svg?color=%2334D058" alt="Supported Python versions">
</a>

# bq-validator

This is a yet another python-based BigQuery query validator with advanced features for CI/CD pipelines and development workflows.

The `bq query --dry_run` command enables us to validate queries.
However, the `bq` command doesn't support service account impersonation, even though it supports workload identity federation credentials at Google Cloud SDK 390.0.0.
The `bq-validator` command would be useful, when we take advantage of service account impersonation to validate BigQuery queries.

## Features

- **Parallel validation** of multiple SQL files
- **Service account impersonation** support
- **Statistics output** in JSON format for CI/CD integration
- **Flexible error handling** with warning options for empty files
- **Structured JSON output** for programmatic processing

## Install

The package is available on [pypi](https://pypi.org/project/bq-validator/)

```bash
pip install -U bq-validator
```

## How to use

```bash
$ bq-validator --help
Usage: bq-validator [OPTIONS] PATH

  Validate BigQuery queries

  PATH is either of a SQL file path or a directory. When it is a directory,
  the command recursively validates all SQL files in the directory.

Options:
  --quota_project TEXT            BigQuery client project ID
  --client_project TEXT           BigQuery client project ID
  --client_location TEXT          BigQuery client location
  --impersonate_service_account TEXT
                                  Impersonate service account email
  --num_parallels INTEGER         Number of parallel query validations
  --verbose                       Enable verbose output
  --warn-on-empty                 Show just warning(s) not to raise error(s)
                                  if the given file(s) are empty
  --stats                         Show the summary of the results
  --help                          Show this message and exit.
```

## Examples

### Basic Usage

Validate a single SQL file:

```bash
bq-validator path/to/query.sql
```

Validate all SQL files in a directory:

```bash
bq-validator path/to/sql/directory/
```

### Advanced Options

Show validation statistics in JSON format:

```bash
bq-validator --stats path/to/sql/directory/
```

Treat empty SQL files as warnings instead of errors:

```bash
bq-validator --warn-on-empty path/to/sql/directory/
```

Combine options for detailed validation:

```bash
bq-validator --stats --warn-on-empty --verbose path/to/sql/directory/
```

### Output Examples

With `--stats` option, you'll see a JSON summary:

```json
{
  "summary": {
    "total": 5,
    "success": 3,
    "errors": 1,
    "warnings": 1
  }
}
```

Errors and warnings are shown as JSON objects:

```json
{
  "path/to/invalid.sql": {
    "query": "SELECT invalid_column FROM invalid_table",
    "error": "Table \"invalid_table\" must be qualified with a dataset..."
  },
  "path/to/empty.sql": {
    "query": "",
    "warning": "Query is empty"
  }
}
```
