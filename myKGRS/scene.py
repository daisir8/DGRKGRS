#!/usr/bin/env python
# coding: utf-8
'''
景点爬虫，从某个具体的地点开始
'''


from selenium import webdriver
import pandas as pd
import time

def getDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    #options.add_argument("--no-sandbox") # linux only
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browserClientA"}})
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        """
    })
    return driver

driver = getDriver()

def to_one_place_detali(place):  # 进入一个地区的详情页
    url = 'http://www.mafengwo.cn/search/q.php?q='+place
    driver.get(url)
    elements = driver.find_elements_by_class_name('head-link')
    url = ''
    for i in elements:
        if '热门景点' in i.text:
            url = i.find_element_by_tag_name('a').get_attribute('href')
            break
    print(url)
    driver.get(url)

def to_every_jd_detail():  # 收集每个景点详情页的网站
    url_data = []
    while True:
        time.sleep(1)
        elements = driver.find_element_by_class_name('scenic-list.clearfix').find_elements_by_tag_name('li')
        for i in elements:
            url = i.find_element_by_tag_name('a').get_attribute('href')
            url_data.append(url)
            # print(url)
        try:
            driver.find_element_by_class_name('pg-next').click()
        except:
            return url_data

def get_one_jd_detail(place):  # 获取一个景点的详细信息
    part_data=[]
    url_data=to_every_jd_detail()
    print(url_data)
    for i in url_data:
        time.sleep(1)
        driver.get(i)
        time.sleep(3)
        try:
            j=driver.find_element_by_class_name('mod.mod-detail')
        except:
            j=''
        try:
            summary=j.find_element_by_class_name('summary').text
        except:
            summary=''
        try:
            tel=j.find_element_by_class_name('baseinfo').find_element_by_class_name('tel').find_element_by_class_name('content').text
        except:
            tel=''
        try:
            item_time = j.find_element_by_class_name('baseinfo').find_element_by_class_name(
                'item-time').find_element_by_class_name('content').text
        except:
            item_time = ''
        one_data=dict(zip(['summary','tel','item_time'],[summary,tel,item_time]))
        part_data.append(one_data)
    to_one_place_detali(place)
    return part_data



def get_one_place_all_jd(place):  # 获取一个地方所有景点信息
    all_data = []
    while True:
        time.sleep(1)
        elements = driver.find_element_by_class_name('scenic-list.clearfix').find_elements_by_tag_name('li')
        for i in elements:
            url = i.find_element_by_tag_name('a').get_attribute('href')
            title = i.find_element_by_tag_name('a').get_attribute('title')
            img = i.find_element_by_tag_name('img').get_attribute('src')
            one_data = dict(zip(['url','title','img','location'],[url,title,img,place]))
            all_data.append(one_data)
            print(one_data)
        try:
            driver.find_element_by_class_name('pg-next').click()
        except:
            return all_data


if __name__ == '__main__':
    place_list = ['武汉']
    data=[]
    all_data = []
    for i in place_list:
        to_one_place_detali(i)
        data1=get_one_jd_detail(i)
        data2 = get_one_place_all_jd(i)
        for j in range(len(data1)):
            d={**data1[j],**data2[j]}
            data.append(d)
        all_data+=data
    df = pd.DataFrame(all_data)
    df.to_excel('武汉景点信息.xls',index=False)





