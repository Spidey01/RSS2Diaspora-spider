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
# from feeddiasp import FeedDiasp, FBParser, RSSParser

from rss2diaspora_spider import rss
from rss2diaspora_spider.diaspora import Diaspora
from rss2diaspora_spider.post import Post
from rss2diaspora_spider.settings import Settings
from rss2diaspora_spider.db import Database

import sys

def parse_args():
    """Return an argparse."""
    parser = argparse.ArgumentParser(prog=sys.argv[0])

    parser.add_argument('-v, --verbose',  dest='verbose', action='store_true', default=False)

    parser.add_argument("-s, --settings", dest='settings', metavar='FILE', type=argparse.FileType('rt'), help="Load settings form FILE.")

    parser.add_argument("--only-database", dest='only_database', action='store_true', default=False, help="Parse feed into database but do not post.")

    return parser.parse_args()

def main():

    args = parse_args()

    me = Settings(args.settings, args.verbose, args.only_database)

    if args.verbose:
        print("Me: '{0}' on '{1}' using feed '{2}'".format(me.username, me.pod, me.feed))

    db = Database(me.database, me.verbose)
    parser = rss.Parser(me.feed, me.verbose)
    bot = Diaspora(me.pod, me.username, me.password, args.verbose)

    bot.login()

    for post in parser.get():
        if args.verbose:
            print("Post: RSS id: '{0}' title: {1} link: {2} content: ... tags: {3}".format(post.id, post.link, post.title, post.tags))

        if db.has(post):
            if me.verbose:
                print("Post: id: '{0}' already in database. Skipping")
            dummy = db.load(post.id)
            continue

        if not me.only_database:
            bot.publish(post)

        # store after publish: so if there's failure there will be retries!
        db.store(post)
