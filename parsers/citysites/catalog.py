from ..base import BaseParser


class CatalogParser(BaseParser):

    BASE_URL = "http://{}/catalog/page/{}"
    SEL_LINKS = ".company_box .company_title a"

    def __init__(self, domain, page):
        self.page = page
        self.domain = domain
        url = self.BASE_URL.format(domain, page)
        super(CatalogParser, self).__init__(url)

    def fulllink(self, link):
        if link.startswith("/"):
            return "http://{}{}".format(self.domain, link)
        return link

    def getlinks(self):
        links = self.find(self.SEL_LINKS)
        links = [l.attrib["href"] for l in links]
        return map(self.fulllink, links)
