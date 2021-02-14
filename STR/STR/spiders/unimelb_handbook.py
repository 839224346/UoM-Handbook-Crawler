import scrapy
from STR.items import StrItem
import logging

logger = logging.getLogger(__name__)


class UnimelbHandbookSpider(scrapy.Spider):
    name = 'handbook'
    allowed_domains = ['handbook.unimelb.edu.au']
    start_urls = ['https://handbook.unimelb.edu.au/2021/subjects/comp' + str(x) for x in range(10001, 10100)] + \
                 ['https://handbook.unimelb.edu.au/2021/subjects/comp' + str(x) for x in range(20001, 20100)] + \
                 ['https://handbook.unimelb.edu.au/2021/subjects/comp' + str(x) for x in range(30001, 30100)] + \
                 ['https://handbook.unimelb.edu.au/2021/subjects/comp' + str(x) for x in range(40001, 40100)] + \
                 ['https://handbook.unimelb.edu.au/2021/subjects/comp' + str(x) for x in range(90001, 90100)] + \
                 ['https://handbook.unimelb.edu.au/2021/subjects/swen' + str(x) for x in range(10001, 10100)] + \
                 ['https://handbook.unimelb.edu.au/2021/subjects/swen' + str(x) for x in range(20001, 20100)] + \
                 ['https://handbook.unimelb.edu.au/2021/subjects/swen' + str(x) for x in range(30001, 30100)] + \
                 ['https://handbook.unimelb.edu.au/2021/subjects/swen' + str(x) for x in range(40001, 40100)] + \
                 ['https://handbook.unimelb.edu.au/2021/subjects/swen' + str(x) for x in range(90001, 90100)]
    # start_urls = ['https://handbook.unimelb.edu.au/2021/subjects/comp10001']
    total_subjects = 0
    count = 0
    items = []

    def parse(self, response):
        item = StrItem()
        self.count += 1
        subject = response.xpath("//span[@class='header--course-and-subject__main']/text()").extract_first()
        description_list = response.xpath("//div[@class='course__overview-wrapper clearfix']")

        item['description'] = description_list.xpath('./p[2]/text()').extract_first()
        item['name'] = subject[:-12]
        item['subject_code'] = subject[subject.find("(") + 1:subject.find(")")]

        yield item
