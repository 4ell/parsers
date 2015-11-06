from lxml import html
from urllib import urlopen


class BaseParser(object):

    def __init__(self, url):
        self.url = url
        self.req = urlopen(url)
        self.parse()

    def parse(self):
        self.tree = html.parse(self.req)
        self.root = self.tree.getroot()

    def find(self, selector):
        return self.root.cssselect(selector)
