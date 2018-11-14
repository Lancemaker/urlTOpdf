import pysitemap
if __name__ == '__main__':
    url = 'http://gineco.bayer.foster.com.br//'  # url from to crawl
    logfile = 'errlog.log'  # path to logfile
    oformat = 'xml'  # output format
    crawl = pysitemap.Crawler(url=url, logfile=logfile, oformat=oformat)
    crawl.crawl()