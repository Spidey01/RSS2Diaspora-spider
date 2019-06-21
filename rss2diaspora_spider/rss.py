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

import feedparser

from rss2diaspora_spider.post import Post

class Parser:
    """Parse RSS from a URL using feedparser."""

    def __init__(self, url, verbose):
        self.verbose = verbose
        if self.verbose:
            print("Parsing {0}".format(url))
        self.url = url
        self.parser = feedparser.parse(self.url)

    def get(self):
        """Generator function returning posts from the feed.

        Posts are a subset of the dicts s from feedparser.

        See https://pythonhosted.org/feedparser/ for info about the fields.
        """

        for entry in self.parser.entries:
            yield Post(entry, "rss", self.verbose)