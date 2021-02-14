# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo
import logging

logger = logging.getLogger(__name__)


class StrPipeline:
    # change your mongo uri here
    mongo_uri = ''
    mongo_database = pymongo.MongoClient(host=mongo_uri).get_default_database()
    subjects = mongo_database.subjects

    def process_item(self, item, spider):
        self.subjects.insert_one({'name': item['name'], 'subject_code': item['subject_code'], 'description':
            item['description']})
        self.logger.debug(f'{item["subject_code"]} has been saved')
        return item
