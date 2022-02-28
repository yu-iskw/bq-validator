# bq-validator
This is a yet another BigQuery query validator.

The `bq query --dry_run` command enables us to validate queries.
However, the `bq` command doesn't support OIDC and impersonate service account.
When we take advantage of OIDC and impersonate service account, the `bq-validator` command would be useful.

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
