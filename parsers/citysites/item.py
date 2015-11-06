import re
from ..base import BaseParser


class ItemParser(BaseParser):

    SEL_PROPS = ".info .info_box"
    SEL_SCOPES = ".company_info h2"
    SEL_SOCIAL = ".sidebar_seti_list li a"
    SEL_COUNTER = ".statistic li:nth-child(3) .counters .current"
    SEL_SCRIPTS = "script:not([src])"

    def getall(self):
        return {
            "id": self.get_companyid(),
            "visitsmonthly": self.get_counter(),
            "properties": self.get_properties(),
            "tags": self.get_scopenames()
        }

    def get_counter(self):
        counter = self.find(self.SEL_COUNTER)
        monthly = counter[0].text
        return int(monthly)

    def get_companyid(self):
        props = self.find(self.SEL_SCRIPTS)
        props = [p.text for p in props if "firm_id" in p.text]
        company = re.findall(r"(\d+)", props[0])[0]
        return int(company)

    def get_properties(self):
        gettext = lambda prop: [get_text(el) for el in prop[:2]]
        props = self.find(self.SEL_PROPS)
        props = map(gettext, props)
        return props

    def get_scopenames(self):
        scopes = self.find(self.SEL_SCOPES)
        scopes = [get_text(p) for p in scopes]

        return self.parse_scopenames(scopes)

    def parse_scopenames(self, names):
        tags = []
        tagsl2 = []
        for name in names:
            parts = name.lower().split("/")[:2]
            l1, l2 = parts
            tags.extend(tag.strip() for tag in l1.split(','))
            tagsl2.extend(tag.strip() for tag in l2.split(','))

        return unique(tags), unique(tagsl2)


def unique(data):
    return list(set(data))

def get_text(node):
    return node.text_content().strip()

