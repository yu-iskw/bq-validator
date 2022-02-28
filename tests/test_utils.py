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
import os
import unittest

from bq_validator.utils import get_project_root, get_sql_files, read_file


class TestUtils(unittest.TestCase):

    def test_get_project_root(self):
        self.assertEqual(
            get_project_root(),
            os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

    def test_get_sql_files(self):
        path = os.path.join(get_project_root(), "tests", "resources", "target")
        sql_files = get_sql_files(path=path)
        self.assertEqual(len(sql_files), 6)
        for sql_file in sql_files:
            file_content = read_file(path=sql_file)
            self.assertTrue(len(file_content) > 0)
