# Scrapy settings for scrapy_bv project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrapy_bv"

SPIDER_MODULES = ["scrapy_bv.spiders"]
NEWSPIDER_MODULE = "scrapy_bv.spiders"
# LOG_LEVEL = "INFO"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "scrapy_bv (+http://www.yourdomain.com)"
USER_AGENTS_LIST = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
INTERVAL = 1
# 60~70秒更新一次数据,DOWNLOAD_DELAY已设置为2, 不需要额外再设置INTERVAL
BV_MAP = {
    "尘白禁区": "BV1xkqbYtEt9",
    "幻塔": "BV14VBXYbEkm",
    "少女前线": "BV1SriiY7Eqm",
    "原神": "BV1QkzfYdEq5",
    "碧蓝航线": "BV1TnSKYtE3m",
    "战双帕米什": "BV1T7qUYjEHF",
    "崩坏3": "BV1qFivY4E4c",
    "灵魂潮汐": "BV1MzDmYJEej",
    "鸣潮": "BV1p5qhYsEW6",
    "蔚蓝档案": "BV1oizbYEEik",
    "崩坏星穹铁道": "BV1Dg6AYNEpD",
    "明日方舟": "BV1khiZYeEDn",
    "深空之眼": "BV1zNq1YoEJF",
    "命运-冠位指定": "BV1ofiRYmEAd",
    "重返未来：1999": "BV1F8BRYxEV3",
    "第五人格": "BV1cEqgYwEY5",
    "BanG Dream": "BV1gwqGYDELp",
    "三国：谋定天下": "BV1tbD8YAEgc",
    "蛋仔派对": "BV1jMqpY4EqV",
    "物华弥新": "BV1Wgz3YVEXK",
    "三角洲行动": "BV1hii1YkEWS",
    "以闪亮之名": "BV1siizYEEva",
    "少女前线2：追放": "BV158ioYjE3C",
    "无期迷途": "BV1uFqgY5E9j",
    "交错战线": "BV1m6ieYgEY8",
    "女神异闻录：夜幕魅影": "BV1BDBMYsEMx",
    "奇点时代": "BV1pnqAY2EbM",
    "恋与深空": "BV1EczcYzETu",
    "无限大": "BV1tkimYjEz7",
    "异环": "BV1P3SFYgER6",
    "归龙潮": "BV1my6KYBENp",
    "卡拉彼丘": "BV12tzGYSEHo",
    "白荆回廊": "BV1jaUNYTEK8",
    "无限暖暖": "BV184qmYnEPW",
    "对照组": "BV1TQ4y147sD"
}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://www.bilibili.com',
    'upgrade-insecure-requests': '1',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="129", "Not=A?Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'Cookie': "buvid3=65628C38-620E-EA97-24E8-A031A76AB5A708598infoc; b_nut=1727103408; _uuid=DD518F5D-D93E-101074-F22F-8233101CC7ED608643infoc; buvid4=993D9C84-9483-AA79-4C2F-16B6828ABB9910316-024092314-8DpHxIurtrZUol5EzQ5EoA%3D%3D; header_theme_version=CLOSE; enable_web_push=DISABLE; DedeUserID=32860764; DedeUserID__ckMd5=82c66c6c08c17f3f; buvid_fp_plain=undefined; rpdid=|(u|u)kuk)RY0J'u~k~ulJ)mu; fingerprint=b864170e973466ea22f234954efacecc; CURRENT_QUALITY=80; LIVE_BUVID=AUTO2517305592550269; PVID=1; AMP_MKTG_8f1ede8e9c=JTdCJTdE; AMP_8f1ede8e9c=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI4Nzc3MmU3ZC0yNzdhLTQxMzMtYjkyMy1kODliOWVlYjU5NWMlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjJhMTIyOTA4OS05MTdhLTQwMTAtOTA3MC05MWE2NTRlOWY1NTQlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzMxNDQ2NjUyMTA0JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTczMTQ0NjY1MjIyOCUyQyUyMmxhc3RFdmVudElkJTIyJTNBNTMxJTdE; SESSDATA=f60f9190%2C1747155140%2Ca74ec%2Ab2CjBUuEmCGVLj6kMNt9FT3KIjl3vl5HB-qhOHeZ7WlfbVZ6AqQP4_LG3ysIc8XOaQUt8SVlpKY2U3dF82aDZObkIzeVJCWmFaYWs5Q0swZDRtcy1abHV4alZjbzdTV0FDajdmSW9fYm5ITjhLNXpoSlNxdW5nQWt4Q1p2dXZaRkhTTFBlVDdFM1l3IIEC; bili_jct=32f400c0992293ef51b4b94f0eb5cc47; buvid_fp=a025241101eac26e57cc352a4c5b11ea; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzQwOTU3MDksImlhdCI6MTczMzgzNjQ0OSwicGx0IjotMX0.9ZDOWGyn29Rt0MAmsStRSOhi3i19ahvE6oiKQAsMyTo; bili_ticket_expires=1734095649; home_feed_column=5; b_lsid=76B7DE10F_193BF650E44; browser_resolution=1484-880; bp_t_offset_32860764=1010367408294068224; CURRENT_FNVAL=4048; sid=5dfer78l"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "scrapy_bv.middlewares.ScrapyBvSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "scrapy_bv.middlewares.ScrapyBvDownloaderMiddleware": 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "scrapy_bv.pipelines.ScrapyBvPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
