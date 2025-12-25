import os
import tempfile
import unittest
from unittest.mock import patch

from click.testing import CliRunner

from bq_validator.cli import (
    ValidationResult,
    ValidationStatus,
    main,
    validate_and_collect_errors,
)


class TestCLI(unittest.TestCase):
    """Test the CLI module"""

    def test_validate_and_collect_errors_empty_file_no_warn(self):
        with tempfile.NamedTemporaryFile(suffix=".sql", mode="w", delete=False) as f:
            f.write("  \n  ")
            temp_path = f.name

        try:
            # client is not used if the file is empty
            result = validate_and_collect_errors(None, temp_path, warn_on_empty=False)
            self.assertIsNotNone(result)
            self.assertIsInstance(result, ValidationResult)
            self.assertEqual(result.status, ValidationStatus.ERROR)
            self.assertEqual(result.file_path, temp_path)
            # The implementation returns "error" when warn_on_empty=False
            self.assertEqual(result.details["error"], "Query is empty")
        finally:
            os.remove(temp_path)

    def test_validate_and_collect_errors_empty_file_with_warn(self):
        with tempfile.NamedTemporaryFile(suffix=".sql", mode="w", delete=False) as f:
            f.write("")
            temp_path = f.name

        try:
            result = validate_and_collect_errors(None, temp_path, warn_on_empty=True)
            self.assertIsNotNone(result)
            self.assertIsInstance(result, ValidationResult)
            self.assertEqual(result.status, ValidationStatus.WARNING)
            self.assertEqual(result.file_path, temp_path)
            # The implementation returns "warning" when warn_on_empty=True
            self.assertEqual(result.details["warning"], "Query is empty")
        finally:
            os.remove(temp_path)

    @patch("bq_validator.cli.create_bigquery_client")
    def test_cli_stats_option(self, mock_create_client):
        # Mock the BigQuery client since we don't need it for empty files
        mock_create_client.return_value = None

        runner = CliRunner()
        with tempfile.NamedTemporaryFile(suffix=".sql", mode="w", delete=False) as f:
            f.write("")  # empty file
            temp_file = f.name

        try:
            # Running bq-validator on the empty file
            # We use --warn-on-empty to avoid exit 1, and --stats to see summary
            result = runner.invoke(main, [temp_file, "--warn-on-empty", "--stats"])

            self.assertEqual(result.exit_code, 0)
            self.assertIn('"summary":', result.output)
            self.assertIn('"total": 1', result.output)
            self.assertIn('"success": 0', result.output)
            self.assertIn('"errors": 0', result.output)
            self.assertIn('"warnings": 1', result.output)
        finally:
            os.unlink(temp_file)


if __name__ == "__main__":
    unittest.main()
