from scrapy import cmdline

if __name__ == "__main__":
    cmdline.execute(f'scrapy crawl chrome'.split())