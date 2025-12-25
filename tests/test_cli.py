import os
import tempfile
import unittest

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

    def test_cli_stats_option(self):
        runner = CliRunner()
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a few files
            file1 = os.path.join(tmpdir, "test1.sql")
            with open(file1, "w", encoding="utf-8") as f:
                f.write("")  # empty

            # Running bq-validator on this directory
            # We use --warn-on-empty to avoid exit 1, and --stats to see summary
            # Note: We don't actually need a real BQ client for empty files
            result = runner.invoke(main, [tmpdir, "--warn-on-empty", "--stats"])

            self.assertEqual(result.exit_code, 0)
            self.assertIn('"summary":', result.output)
            self.assertIn('"total": 1', result.output)
            self.assertIn('"success": 0', result.output)
            self.assertIn('"errors": 0', result.output)
            self.assertIn('"warnings": 1', result.output)


if __name__ == "__main__":
    unittest.main()
