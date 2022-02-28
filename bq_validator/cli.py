#  Licensed to the Apache Software Foundation (ASF) under one or more
#  contributor license agreements.  See the NOTICE file distributed with
#  this work for additional information regarding copyright ownership.
#  The ASF licenses this file to You under the Apache License, Version 2.0
#  (the "License"); you may not use this file except in compliance with
#  the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import sys
from typing import Optional

import click
import click_completion

import bq_validator
from bq_validator.bigquery import create_bigquery_client, validate_query
from bq_validator.utils import read_file, get_sql_files

# Initialize click-completion
click_completion.init()


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option("--client_project",
              type=str,
              required=False,
              help="BigQuery client project ID")
@click.option("--client_location",
              type=str,
              required=False,
              help="BigQuery client location")
@click.option("--impersonate_service_account",
              type=str,
              required=False,
              help="Impersonate service account email")
@click.version_option(version=bq_validator.__version__)
def main(path: str, client_project: Optional[str],
         client_location: Optional[str],
         impersonate_service_account: Optional[str]):
    """Validate BigQuery queries

    PATH is either of a SQL file path or a directory.
    When it is a directory, the command recursively validates all SQL files in the directory.
    """
    # Create a BigQuery client
    client = create_bigquery_client(
        client_project_id=client_project,
        location=client_location,
        impersonate_service_account=impersonate_service_account)
    # Validate queries
    sql_files = get_sql_files(path=path)
    errors = {}
    for query_file in sql_files:
        query = read_file(path=query_file)
        is_valid, error_message = validate_query(client=client, query=query)
        if is_valid is False:
            errors[query_file] = error_message
    # Show errors
    if len(errors) > 0:
        for file, error_message in errors.items():
            click.echo(f"{file}: {error_message}")
        sys.exit(1)
