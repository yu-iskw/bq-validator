[![Test python](https://github.com/yu-iskw/bq-validator/actions/workflows/test.yml/badge.svg)](https://github.com/yu-iskw/bq-validator/actions/workflows/test.yml)
<a href="https://pypi.org/project/bq-validator" target="_blank">
    <img src="https://img.shields.io/pypi/v/bq-validator?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/bq-validator" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/bq-validator.svg?color=%2334D058" alt="Supported Python versions">
</a>


# bq-validator
This is a yet another BigQuery query validator.

The `bq query --dry_run` command enables us to validate queries.
However, the `bq` command doesn't support OIDC and impersonate service account.
When we take advantage of OIDC and impersonate service account, the `bq-validator` command would be useful.

## Install
The package is available on [pypi](https://pypi.org/project/bq-validator/)
```bash
pip install -U bq-validator
```

## How to use

```bash
Usage: bq-validator [OPTIONS] PATH

  Validate BigQuery queries

  PATH is either of a SQL file path or a directory. When it is a directory,
  the command recursively validates all SQL files in the directory.

Options:
  --client_project TEXT           BigQuery client project ID
  --client_location TEXT          BigQuery client location
  --impersonate_service_account TEXT
                                  Impersonate service account email
  --version                       Show the version and exit.
  --help                          Show this message and exit.
```
