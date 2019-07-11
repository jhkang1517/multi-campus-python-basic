# -*- coding: utf-8 -*-
import re
import scrapy
from newscrawl.items import NewscrawlItem
from datetime import timedelta, date
from urllib import parse
import time
import random
from time import sleep

start_date = date(2018, 1, 1)
end_date = date(2019, 6, 20)
cnt_per_page = 10
keyword = "마라탕"

url_format = "https://search.naver.com/search.naver?date_from={0}&date_option=8&date_to={0}&dup_remove=1&nso=so%3Add%2Cp%3Afrom{0}to{0}&post_blogurl=&post_blogurl_without=&query={1}&sm=tab_pge&srchby=all&st=date&where=post&start={2}"

class NaverblogSpider(scrapy.Spider):
    def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)

    name = 'naverblog'
    allowed_domains = ['naver.com'] 
    start_urls = []
    
    for single_date in daterange(start_date, end_date):
        start_urls.append(url_format.format(single_date.strftime("%Y%m%d"), keyword, 1))

    def parse(self, response):
        for href in response.xpath("//ul[@class='type01']/li/dl/dt/a/@href").extract() :
            yield response.follow(href, self.parse_iframe)
        
        total_cnt = int(re.sub('[()전체건,]', '', response.xpath("//div[@class='section_head']/span/text()").get().split('/')[1]))
        query_str = parse.parse_qs(parse.urlsplit(response.url).query)
        currpage = int(query_str['start'][0]) 

        startdate = query_str['date_from'][0]
        print("=================== [" + startdate + '] ' + str(currpage) + '/' + str(total_cnt) + "===================") 
        if currpage  < total_cnt : 
            yield response.follow(url_format.format(startdate, keyword, currpage+10)   , self.parse)

    def parse_iframe(self, response):    
        href = 'https://blog.naver.com' + response.xpath("//iframe/@src").get()
        yield response.follow(href, self.parse_details)

    def parse_details(self, response):    
        item = NewscrawlItem()
        item['url'] = response.url
        query_str = parse.parse_qs(parse.urlsplit(response.url).query)
        item['author'] = query_str['blogId'][0]

        
        titlecontent = ""
        title = ""

        if 'blog.naver.com' in response.url :
            title = str(response.xpath("//div[@class='se-module se-module-text se-title-text']/p/span/text()").get())
            item['date'] = response.xpath("//span[contains(@class, 'se_publishDate')]/text()").get()
            content = str(response.xpath("//div[@class='se-main-container']").get())

            if content == 'None' :
                title = str(response.xpath("//div[contains(@class,'se_title')]//h3").get())
                item['date'] = response.xpath("//span[contains(@class, 'se_publishDate')]/text()").get()
                content = str(response.xpath("//div[contains(@class, 'sect_dsc')]").get())

            if content == 'None' :
                title = str(response.xpath("//div[@class='htitle']/span/text()").get())
                item['date'] = response.xpath("//p[contains(@class,'_postAddDate')]/text()").get()
                content = str(response.xpath("//div[@id='postViewArea']/div").get())

        title = re.sub(' +', ' ', str(re.sub(re.compile('<.*?>'), ' ', title.replace('"','')).replace('\r\n','').replace('\n','').replace('\t','').replace('\u200b','').strip()))
        content = re.sub(' +', ' ', str(re.sub(re.compile('<.*?>'), ' ', content.replace('"','')).replace('\r\n','').replace('\n','').replace('\t','').replace('\u200b','').strip()))
        item['title'] = title 
        item['content'] = content  

        yield item
