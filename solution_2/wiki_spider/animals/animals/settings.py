# Scrapy settings for animals project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "animals"

SPIDER_MODULES = ["animals.spiders"]

NEWSPIDER_MODULE = "animals.spiders"

ALLOWED_DOMAINS = ["ru.wikipedia.org"]

START_URLS = [
    "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
]

ROBOTSTXT_OBEY = False

COOKIES_ENABLED = True

CONCURRENT_REQUESTS = 32

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

FEED_EXPORT_ENCODING = "utf-8"
