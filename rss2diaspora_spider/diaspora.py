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

import string

#
# Table for str.translate() to convert words into valid #hashtags.
#
HASH_TAG_TRANSLATION = str.maketrans('', '', string.punctuation + string.whitespace)

class Diaspora:
    """Interface to Diaspora. """

    def __init__(self, pod, username, password, verbose, dry_run):
        self.pod = pod
        self.username = username
        self.password = password
        self.verbose = verbose
        self.dry_run = dry_run
        self.logged_in = False

    def login(self):
        if self.verbose:
            print("Logging into {0} as {1}".format(self.pod, self.username))

        try:
            self._connection = diaspy.connection.Connection(pod=self.pod, username=self.username, password=self.password)
            self._connection.login()
            self._stream = diaspy.streams.Stream(self._connection, fetch=False)
            self.logged_in = True
        except Exception as e:
            print("Diaspora.login() failed: {0}".format(e))
            raise Exception(str(e))

    def publish(self, post):
        """Publish a Post instance to diaspora."""
        assert post is not None, "No post provided"
        assert self.logged_in, "Not logged in."

        shameless_plug = "RSS2Diaspora_spider prototype"

        if self.verbose:
            print("Formatting: Post: id: {0}".format(post.id))

        #markdown = post.content
        markdown = ""
        if not markdown:
            markdown = post.summary

        # Would be nice if an option could control this.
        # --option x 'foo bar' -> '#foobar'
        # --option y 'foo bar' -> '#foo_bar'
        hashtags = ' '.join([ '#{0}'.format(t.translate(HASH_TAG_TRANSLATION)) for t in post.tags ])
        text = """
{3}

***

*Tags*: {4}
Posted from [{0}]({1})

""".format(post.title, post.link, post.title, markdown, hashtags)

        if self.verbose:
            print("Publishing: Post: id: {0}".format(post.id))

        # Would be nice to have a setting for the aspect_ids=str.
        # Default is 'public', and diaspy docs don't say how to format the value.
        # print(text)
        if self.dry_run:
            print("dry run: converted text follows:")
            print(text)
            return
        self._stream.post(text, provider_display_name=shameless_plug)


