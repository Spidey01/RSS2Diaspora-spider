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

import dbm
import os.path

from rss2diaspora_spider.post import Post

class Database:
    """Handle storing Posts."""

    def __init__(self, path, verbose):
        self.verbose = verbose
        self.path = path
        if self.verbose:
            print("Database is '{0}'".format(self.path))

    def has(self, post):
        """Returns true if Post instance is stored in the database."""
        with dbm.open(self.path, 'c') as handle:
            return post.id in handle

    def store(self, post):
        """Stores Post instance in the database.

        post.id will be used as the key.
        """
        if self.verbose:
            print("Storing Post: id: {0}".format(post.id))
        with dbm.open(self.path, 'c') as handle:
            handle[post.id] = post.to_json()

    def load(self, id):
        """Returns a Post instance for id."""
        with dbm.open(self.path, 'r') as handle:
            return Post(handle[id], 'json', self.verbose)