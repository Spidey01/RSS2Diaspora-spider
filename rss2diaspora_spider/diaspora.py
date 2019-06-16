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

import diaspy

class Diaspora:
    """Interface to Diaspora. """

    def __init__(self, pod, username, password, verbose):
        self.pod = pod
        self.username = username
        self.password = password
        self.verbose = verbose

    def login(self):
        if self.verbose:
            print("Logging into {0} as {1}".format(self.pod, self.username))

        try:
            self._connection = diaspy.connection.Connection(pod=self.pod, username=self.username, password=self.password)
            self._connection.login()
        except Exception as e:
            print("Diaspora.login() failed: {0}".format(e))
            raise Exception(str(e))