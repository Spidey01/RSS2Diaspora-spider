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

import sys

class Post:
    """Object representing a post."""

    def __init__(self, entry, verbose):
        """Create the data.

        entry - the feedparser entry to parse.
        """

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
                # if verbose:
                #     print("Found tag: term:{0} scheme:{1} label:{2}".format(tag['term'], tag['scheme'], tag['label']))

                if 'term' in tag:
                    self.tags.append(tag['term'])

    def _to_markdown(self, data):
        """Return data converted to markdown."""
        try:
            return pypandoc.convert(data, 'md', format='html')
        except OSError as nopandoc:
            print(str(nopandoc))
            sys.exit(127)
