import os
from sys import argv
from json import dump, load


CATALOG_DEPH = 256


if "citcat" in argv:
    if "sevas" in argv:
        from parsers.citysites.catalog import CatalogParser
        domain = "www.8692.ru"

    for i in xrange(1, CATALOG_DEPH + 1):
        parser = CatalogParser(domain, i)
        links = parser.getlinks()

        path = "data/{}/catalog/page{}.json".format(domain, i)
        with open(path, "wb") as f:
            dump(links, f)

        print "page:", i, "\r",


if "citmore" in argv:
    if "sevas" in argv:
        from parsers.citysites.item import ItemParser

        domain = "www.8692.ru"

    links = []
    path = "data/{}/catalog/".format(domain)

    for f in os.listdir(path):
        links.extend(load(open(path + f)))

    for itemurl in set(links):
        path = "data/{}/companies/{}.json"
        try:
            parser = ItemParser(itemurl)
            data = parser.getall()
            path = path.format(domain, data['id'])

            with open(path, 'wb') as f:
                dump(data, f)

            print "success", data['id'], "\r",
        except:
            print "error"
            print itemurl

