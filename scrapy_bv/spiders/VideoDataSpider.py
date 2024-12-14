"""
自动请求、返回请求页面的内容-----可以提取html元素
    使用response.css 或者  response.xpath 可以获取其中信息
"""
import datetime
import json
from time import sleep
from typing import Iterable

import scrapy
from scrapy import Request
from scrapy.http import Response

from scrapy_bv import settings
from scrapy_bv.items import ScrapyBvItem


class VideoDataSpider(scrapy.Spider):
    name = 'video_data'  # 运行爬虫命令为：scrapy crawl xxx
    prefix = "https://api.bilibili.com/x/web-interface/view?bvid="
    start_urls = []
    bv_names = []
    for key, value in settings.BV_MAP.items():
        start_urls.append(prefix + value)
        bv_names.append(key)
    interval = settings.INTERVAL

    def start_requests(self) -> Iterable[Request]:
        for i in range(len(self.start_urls)):
            args = {"game": self.bv_names[i]}
            yield scrapy.Request(self.start_urls[i], dont_filter=True, callback=self.parse, cb_kwargs=args)

    # 初始化init时 会自动执行 父类中的 start_requests方法，就会去请求start_urls中的url
    def parse(self, response: Response, **kwargs):
        # 获取百度热搜 的10个标题
        data = json.loads(response.text)
        # 输出获取到的文本内容
        try:
            videoStat = data['data']['stat']
            stat = ScrapyBvItem()
            stat['date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            stat['game'] = kwargs['game']
            stat['view'] = videoStat['view']
            stat['danmaku'] = videoStat['danmaku']
            stat['reply'] = videoStat['reply']
            stat['favorite'] = videoStat['favorite']
            stat['coin'] = videoStat['coin']
            stat['share'] = videoStat['share']
            stat['like'] = videoStat['like']
            yield stat
            sleep(self.interval)
            for i in range(len(self.start_urls)):
                args = {"game": self.bv_names[i]}
                yield scrapy.Request(self.start_urls[i], dont_filter=True, callback=self.parse, cb_kwargs=args)
        except Exception as e:
            print(e)
            sleep(self.interval)
            for i in range(len(self.start_urls)):
                args = {"game": self.bv_names[i]}
                yield scrapy.Request(self.start_urls[i], dont_filter=True, callback=self.parse, cb_kwargs=args)
