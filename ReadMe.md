## 使用方法:
### 目录结构:
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
    | scrapy_bv/
    | | scrapy_bv/
    | | |_spiders/
    | | |  | __init__.py
    | | |  |_VideoDataSpider.py
    | | | __init__.py
    | | | items.py
    | | | middlewares.py
    | | | pipelines.py
    | | |_settings.py
    | | ReadMe.md
    | |_scrapy.cfg
    |
###### 以下操作均在`scrapy.cfg`的同级目录下进行
###### 1. 安装python
###### 2. 安装scrapy: `pip install scrapy`
###### 3. 启动爬虫: `scrapy scrawl video_data -o pv.csv`, 其中`pv.csv`为想要输出的文件名
<br/>

### PS: 若需要自行指定抓取的视频数据, 在settings.py中修改对应名称和BV号即可