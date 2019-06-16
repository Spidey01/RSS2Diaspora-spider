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

import argparse
import sys

# TODO: replace these with my own code.
from feeddiasp import FeedDiasp, FBParser, RSSParser

from rss2diaspora_spider.settings import Settings

import sys

def parse_args():
    """Return an argparse."""
    parser = argparse.ArgumentParser(prog=sys.argv[0])

#    parser.add_argument(["verbose", "--verbose", "-v"], help="Enable verbose output.")

    parser.add_argument('-v, --verbose',  dest='verbose', action='store_true', default=False)

    parser.add_argument("-s, --settings", dest='settings', metavar='FILE', type=argparse.FileType('rt'), help="Load settings form FILE.")

    return parser.parse_args()

def main():

    args = parse_args()

    me = Settings(args.settings, args.verbose)

    if args.verbose:
        print("Me: '{0}' on '{1}' using feed '{2}'".format(me.username, me.pod, me.feed))

    if args.verbose:
        print("Creating RSS feed parser")
    rss = RSSParser(url=me.feed)

    if args.verbose:
        print("Creating FeedDiasp bot")
    bot = FeedDiasp(parser=rss, pod=me.pod, username=me.username, password=me.password, db=me.database)

    if args.verbose:
        print("Publishing new posts to {0}".format(me.pod))
    bot.publish()
