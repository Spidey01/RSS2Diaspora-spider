# Copyright 2019-current Terry M. Poulin.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Settings:
    """Simple structure and parser for application settings."""

    def __init__(self, path, Debug):
        if Debug:
            print("Loading configuration from '{0}'".format(path))

        with open(path) as config:
            for line in config:
                line = line.rstrip()
                if not line:
                    continue
                if line.startswith('#') or line.startswith(';'):
                    continue
                field, value = line.split('=')
                # print("varname: '{0}'\tvalue: '{1}'".format(field, value))

                if field == 'pod':
                    self.pod = value
                elif field == 'username':
                    self.username = value
                elif field == 'password':
                    self.password = value
                elif field == 'feed':
                    self.feed = value
                elif field == 'database':
                    self.database = value
