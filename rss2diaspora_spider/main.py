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

import sys

# TODO: replace these with my own code.
from feeddiasp import FeedDiasp, FBParser, RSSParser

from rss2diaspora_spider.settings import Settings

import sys

# Set to true if first argv is 'debug'
# Debug = False
Debug = True


def main():

    try:
        if sys.argv[1].lower() == "debug":
            Debug = True
    except:
        pass
    print("Debug: {0}".format(Debug))

    me = Settings("config.txt", Debug)
    print("Me: '{0}' on '{1}' using feed '{2}'".format(me.username, me.pod, me.feed))

    if Debug:
        print("Creating RSS feed parser")
    rss = RSSParser(url=me.feed)

    if Debug:
        print("Creating FeedDiasp bot")
    bot = FeedDiasp(parser=rss, pod=me.pod, username=me.username, password=me.password, db=me.database)

    if Debug:
        print("Publishing new posts to {0}".format(me.pod))
    bot.publish()
