# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from NED.items import NedItem


class NedPipeline:
    def process_item(self, item, spider):
        if item['text'] != "":
            try:
                with open(f"Data/{item['title']}.txt", "w", encoding='UTF-8') as f:
                    f.write(item['text'])
            except Exception as e:
                if isinstance(e, OSError):
                    item['title'] = item['title'][:5]
                    with open(f"Data/{item['title']}.txt", "w", encoding='UTF-8') as f:
                        f.write(item['text'])
                else:
                    print(e.args)
        return