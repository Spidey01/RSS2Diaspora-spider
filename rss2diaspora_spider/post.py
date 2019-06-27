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

import pypandoc

import json
import sys

from collections import namedtuple

class Post:
    """Object representing a post."""

    def __init__(self, entry, format, verbose):
        """Create the data.

        entry - the feedparser or json entry to parse.
        """
        self.verbose = verbose

        if format == "rss":
            self.parse_rss(entry)
        elif format == "json":
            self.parse_json(entry)
        else:
            print("Post: Unknown format: {0}".format(format))
            sys.exit(0)


    def _to_markdown(self, data):
        """Return data converted to markdown."""
        try:
            # need to disable wraps or bad line breaks from sources like Blogger.
            args = ['--wrap', 'none']
            return pypandoc.convert(data, 'commonmark', format='html-native_divs-native_spans', extra_args=args)
        except OSError as nopandoc:
            print(str(nopandoc))
            sys.exit(127)

    def to_json(self):
        """Returns a JSON representation of self."""
        post = {
            'id': self.id,
            "link": self.link,
            "title": self.title,
            "summary": self.summary,
            "content": self.content,
            "tags": self.tags
        }
        return json.JSONEncoder().encode(post)

    def parse_json(self, entry):
        """Fills out our fields from JSON entry."""

        o = json.loads(entry)

        self.id = o["id"]
        self.link = o["link"]
        self.title = o["title"]
        self.summary = o["summary"]
        self.content = o["content"]
        self.tags = o["tags"]

    def parse_rss(self, entry):
        """Fills out our fields from RSS entry."""

        self.id = entry.id
        self.link = entry.link
        self.title = entry.link

        self.summary = self._to_markdown(entry.summary)

        if 'content' in entry:
            data = []
            for content in entry.content:
                data.append(self._to_markdown(content.value))
            self.content = "\n".join(data)

        self.tags = []
        if 'tags' in entry:
            for tag in entry['tags']:
                # term should convert to '#hashtag' I think; label is human readable and optional...
                # if self.verbose:
                #     print("Found tag: term:{0} scheme:{1} label:{2}".format(tag['term'], tag['scheme'], tag['label']))

                if 'term' in tag:
                    self.tags.append(tag['term'])
