# Scrapy settings for work01 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'work01'

SPIDER_MODULES = ['work01.spiders']
NEWSPIDER_MODULE = 'work01.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'work01 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#     'scrpay.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
#     'work01.middlewares.RandomProxyMiddleware': 543
#
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrpay.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    'work01.middlewares.RandomProxyMiddleware': 500
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'work01.pipelines.MySQLPipeline': 100,
}

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
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

DOWNLOAD_DELAY = 4
RANDOMIZE_DOWNLOAD_DELAY = True
CONCURRENT_REQUESTS = 1
LOG_LEVEL = "INFO"
DOWNLOAD_TIMEOUT = 30
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408]
HTTPERROR_ALLOWED_CODES = [500]

try:
    with open("proxies.txt", "r") as f:
        HTTP_PROXY_LIST = list(filter(lambda x: x.strip(), f.readlines()))
    if not HTTP_PROXY_LIST:
        raise ValueError()
except (OSError, ValueError) as e:
    print(e)
    HTTP_PROXY_LIST = [
        "http://49.48.64.221:8080",
        "https://46.229.187.169:53281",
        "https://201.91.82.155:3128"
    ]

# MySQL CONFIG

DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = ""
DB_USER = ""
DB_PWD = ""