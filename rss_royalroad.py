#!/usr/bin/python3

# MIT License

# Copyright (c) 2018 Daniel Nunes

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# USAGE
# [cat <feed> | echo <url> | echo <fname>] | rss_royalroad
#
# This script expects either the feed contents, a url or a file name that
# contains the feed. This must be a valid feed from royalroad.com
#
# The built feed will be printed to stdout.
#
# There is no code to account for improper usage, you're on your own.

import sys
sys.path.append('C:/Users/mudit/Anaconda3/lib/site-packages')
sys.path.append('C:/Users/mudit/Anaconda3/lib')
sys.path.append('C:/Users/mudit/Anaconda3')
import feedparser
import requests
import xml.etree.ElementTree as etree

from bs4 import BeautifulSoup


def parse_url(parse_url):
    print("Starting the process now")

    #parse_url = sys.stdin.readline()
    #print("URL: " + parse_url)
    feed = feedparser.parse(parse_url)
    print("Successfully parsed the url")


    new_feed = etree.Element('rss', version="2.0")
    channel = etree.SubElement(new_feed, 'channel')
    title = etree.SubElement(channel, 'title')
    title.text = feed.feed.title
    link = etree.SubElement(new_feed, 'link')
    link.text = feed.feed.link
    desc = etree.SubElement(new_feed, 'description')
    desc.text = feed.feed.description

    for entry in feed.entries:
        response = requests.get(entry.link, headers = {'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        soup = BeautifulSoup(response.content, features="html5lib")
        
        c = soup.body("div", "chapter-inner chapter-content")   #Royal Road
        c2 = soup.body("div", "fr-view")                        #WuxiaWorld
        c3 = soup.body("div", "chp_raw")                        #ScribbleHub
        c4 = soup.body("div", "entry-content")                  #WordPress

        if c is not None and len(c) > 0:
            children = c[0].children
        elif c2 is not None and len(c2) > 0:
            children = c2[0].children
        elif c3 is not None and len(c3) > 0:
            children = c3[0].children
        elif c4 is not None and len(c4) > 0:
            children = c4[0].children

        item = etree.SubElement(channel, 'item')

        item_title = etree.SubElement(item, 'title')
        item_title.text = entry.title

        item_link = etree.SubElement(item, 'link')
        item_link.text = entry.link

        item_desc = etree.SubElement(item, 'description')
        desc = "".join(str(child) for child in children if str(child).strip())
        item_desc.text = desc

        guid = etree.SubElement(item, 'guid', isPermaLink='false')
        
        try:
            guid.text = entry.id
        except:
            guid.text = ""

        pubDate = etree.SubElement(item, 'pubDate')
        pubDate.text = entry.published

    return (etree.tostring(new_feed, encoding='utf-8', method="xml"))