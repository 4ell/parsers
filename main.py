from sys import argv
from json import dump


CATALOG_DEPH = 256


if "citcat" in argv:
    if "sevas" in argv:
        from parsers.citysites.catalog import CatalogParser
        domain = "www.8692.ru"

    for i in xrange(1, CATALOG_DEPH + 1):
        parser = CatalogParser(domain, 1)
        links = parser.getlinks()

        path = "data/{}/catalog/page{}.json".format(domain, i)
        with open(path, "wb") as f:
            dump(links, f)

        print "page:", i, "\r",
