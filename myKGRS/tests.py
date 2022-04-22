# import pandas as pd
# a=set()
# data1=pd.read_excel(io='./templates/景点信息-分类后.xls')
# data2=pd.read_excel(io='./templates/关系——景点景点之间的关系.xls')
# data3=pd.read_excel(io='./templates/武汉景点信息.xls')
# work_data = data1.values.tolist()
# work_data2=data2.values.tolist()
# work_data3=data3.values.tolist()
# print(work_data)
# print(work_data2)
# print(work_data3)
# for i in work_data:
#     if i[4]=="武汉":
#         a.add(i[2])
# print(list(a))

#
#
# data = []
# links = []
# for i in range(len(work_data)):  # len(work_data)
#     dic1 = {'name': '{}'.format(work_data[i][2]), 'des': '{}'.format(work_data[i][2]), 'symbolSize': 70,
#             'category': 0, 'symbol':'{}'.format(work_data[i][3])}
#     data.append(dic1)
#
#
# for i in range(len(work_data2)):
#     dic2 = {'target': '{}'.format(work_data2[i][1]), 'source': '{}'.format(work_data2[i][3]),
#             'name': '{}'.format(work_data2[i][2]), 'des': '景点-景点'}
#     links.append(dic2)
#
#
# print(data)
# print(links)


# from selenium import webdriver
# import time
# def getDriver():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--disable-extensions")
#     options.add_argument("--disable-gpu")
#     #options.add_argument("--no-sandbox") # linux only
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option("useAutomationExtension", False)
#     driver = webdriver.Chrome(options=options)
#     driver.execute_cdp_cmd("Network.enable", {})
#     driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browserClientA"}})
#     driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#         "source": """
#             Object.defineProperty(navigator, 'webdriver', {
#                 get: () => undefined
#             })
#         """
#     })
#     return driver
#
# driver = getDriver()
#
# li=['https://www.mafengwo.cn/poi/5811.html', 'https://www.mafengwo.cn/poi/5812.html', 'https://www.mafengwo.cn/poi/5426285.html', 'https://www.mafengwo.cn/poi/5774.html', 'https://www.mafengwo.cn/poi/6221.html', 'https://www.mafengwo.cn/poi/5798.html', 'https://www.mafengwo.cn/poi/5434197.html', 'https://www.mafengwo.cn/poi/5803.html', 'https://www.mafengwo.cn/poi/6218.html', 'https://www.mafengwo.cn/poi/35616.html', 'https://www.mafengwo.cn/poi/5433190.html', 'https://www.mafengwo.cn/poi/6153.html', 'https://www.mafengwo.cn/poi/5427484.html', 'https://www.mafengwo.cn/poi/6725646.html', 'https://www.mafengwo.cn/poi/18680089.html', 'https://www.mafengwo.cn/poi/6767.html', 'https://www.mafengwo.cn/poi/5434165.html', 'https://www.mafengwo.cn/poi/5504185.html', 'https://www.mafengwo.cn/poi/5685088.html', 'https://www.mafengwo.cn/poi/35619.html', 'https://www.mafengwo.cn/poi/31630.html', 'https://www.mafengwo.cn/poi/5428428.html', 'https://www.mafengwo.cn/poi/73487068.html', 'https://www.mafengwo.cn/poi/5686674.html', 'https://www.mafengwo.cn/poi/35814.html', 'https://www.mafengwo.cn/poi/5778.html', 'https://www.mafengwo.cn/poi/17691538.html', 'https://www.mafengwo.cn/poi/6163.html', 'https://www.mafengwo.cn/poi/5687909.html', 'https://www.mafengwo.cn/poi/7047484.html', 'https://www.mafengwo.cn/poi/5614889.html', 'https://www.mafengwo.cn/poi/26146598.html', 'https://www.mafengwo.cn/poi/5426933.html', 'https://www.mafengwo.cn/poi/71490000.html', 'https://www.mafengwo.cn/poi/9008233.html', 'https://www.mafengwo.cn/poi/7392647.html', 'https://www.mafengwo.cn/poi/33584316.html', 'https://www.mafengwo.cn/poi/33584492.html', 'https://www.mafengwo.cn/poi/73150632.html', 'https://www.mafengwo.cn/poi/74603616.html', 'https://www.mafengwo.cn/poi/33343292.html', 'https://www.mafengwo.cn/poi/33583796.html', 'https://www.mafengwo.cn/poi/3456613.html', 'https://www.mafengwo.cn/poi/26894039.html', 'https://www.mafengwo.cn/poi/3322209.html', 'https://www.mafengwo.cn/poi/6207.html', 'https://www.mafengwo.cn/poi/6046862.html', 'https://www.mafengwo.cn/poi/33583360.html', 'https://www.mafengwo.cn/poi/33584472.html', 'https://www.mafengwo.cn/poi/33584256.html', 'https://www.mafengwo.cn/poi/5432184.html', 'https://www.mafengwo.cn/poi/59256076.html', 'https://www.mafengwo.cn/poi/71644112.html', 'https://www.mafengwo.cn/poi/114054704.html', 'https://www.mafengwo.cn/poi/5766.html', 'https://www.mafengwo.cn/poi/26146601.html', 'https://www.mafengwo.cn/poi/5434154.html', 'https://www.mafengwo.cn/poi/33584072.html', 'https://www.mafengwo.cn/poi/17310391.html', 'https://www.mafengwo.cn/poi/17691454.html', 'https://www.mafengwo.cn/poi/34160844.html', 'https://www.mafengwo.cn/poi/73590084.html', 'https://www.mafengwo.cn/poi/91238320.html', 'https://www.mafengwo.cn/poi/5688581.html', 'https://www.mafengwo.cn/poi/5807.html', 'https://www.mafengwo.cn/poi/35815.html', 'https://www.mafengwo.cn/poi/33583976.html', 'https://www.mafengwo.cn/poi/17641435.html', 'https://www.mafengwo.cn/poi/116842840.html', 'https://www.mafengwo.cn/poi/35620.html', 'https://www.mafengwo.cn/poi/5432655.html', 'https://www.mafengwo.cn/poi/6630975.html', 'https://www.mafengwo.cn/poi/33583448.html', 'https://www.mafengwo.cn/poi/5805.html', 'https://www.mafengwo.cn/poi/91990580.html', 'https://www.mafengwo.cn/poi/5429419.html', 'https://www.mafengwo.cn/poi/59346132.html', 'https://www.mafengwo.cn/poi/6630969.html', 'https://www.mafengwo.cn/poi/33583620.html', 'https://www.mafengwo.cn/poi/6775.html', 'https://www.mafengwo.cn/poi/91238400.html', 'https://www.mafengwo.cn/poi/3473448.html', 'https://www.mafengwo.cn/poi/92128956.html', 'https://www.mafengwo.cn/poi/91578660.html', 'https://www.mafengwo.cn/poi/73862504.html', 'https://www.mafengwo.cn/poi/71643956.html', 'https://www.mafengwo.cn/poi/3302431.html', 'https://www.mafengwo.cn/poi/95634112.html', 'https://www.mafengwo.cn/poi/6243.html', 'https://www.mafengwo.cn/poi/8087723.html', 'https://www.mafengwo.cn/poi/95634932.html', 'https://www.mafengwo.cn/poi/91340220.html', 'https://www.mafengwo.cn/poi/91340280.html', 'https://www.mafengwo.cn/poi/92132952.html', 'https://www.mafengwo.cn/poi/91338920.html', 'https://www.mafengwo.cn/poi/91339476.html', 'https://www.mafengwo.cn/poi/91338252.html', 'https://www.mafengwo.cn/poi/92132488.html', 'https://www.mafengwo.cn/poi/91589444.html', 'https://www.mafengwo.cn/poi/95635080.html', 'https://www.mafengwo.cn/poi/92636912.html', 'https://www.mafengwo.cn/poi/91339160.html', 'https://www.mafengwo.cn/poi/91338948.html', 'https://www.mafengwo.cn/poi/34861772.html', 'https://www.mafengwo.cn/poi/91590688.html', 'https://www.mafengwo.cn/poi/91584180.html', 'https://www.mafengwo.cn/poi/92129908.html', 'https://www.mafengwo.cn/poi/91573168.html', 'https://www.mafengwo.cn/poi/91578276.html', 'https://www.mafengwo.cn/poi/92631108.html', 'https://www.mafengwo.cn/poi/91583704.html', 'https://www.mafengwo.cn/poi/73862288.html', 'https://www.mafengwo.cn/poi/17691373.html', 'https://www.mafengwo.cn/poi/91583060.html', 'https://www.mafengwo.cn/poi/91575564.html', 'https://www.mafengwo.cn/poi/91338296.html', 'https://www.mafengwo.cn/poi/92621056.html', 'https://www.mafengwo.cn/poi/33584868.html', 'https://www.mafengwo.cn/poi/91338748.html', 'https://www.mafengwo.cn/poi/92130136.html', 'https://www.mafengwo.cn/poi/92131472.html', 'https://www.mafengwo.cn/poi/5427233.html', 'https://www.mafengwo.cn/poi/109623944.html', 'https://www.mafengwo.cn/poi/92134736.html', 'https://www.mafengwo.cn/poi/91143472.html', 'https://www.mafengwo.cn/poi/91143736.html', 'https://www.mafengwo.cn/poi/115996784.html', 'https://www.mafengwo.cn/poi/33584548.html', 'https://www.mafengwo.cn/poi/96828148.html', 'https://www.mafengwo.cn/poi/17691385.html', 'https://www.mafengwo.cn/poi/33549064.html', 'https://www.mafengwo.cn/poi/73863032.html', 'https://www.mafengwo.cn/poi/33584664.html', 'https://www.mafengwo.cn/poi/91338620.html', 'https://www.mafengwo.cn/poi/75132080.html', 'https://www.mafengwo.cn/poi/91338428.html', 'https://www.mafengwo.cn/poi/91589700.html', 'https://www.mafengwo.cn/poi/98174380.html', 'https://www.mafengwo.cn/poi/33585088.html', 'https://www.mafengwo.cn/poi/90505208.html', 'https://www.mafengwo.cn/poi/5694001.html', 'https://www.mafengwo.cn/poi/73359816.html', 'https://www.mafengwo.cn/poi/91702916.html', 'https://www.mafengwo.cn/poi/91340600.html', 'https://www.mafengwo.cn/poi/34861128.html', 'https://www.mafengwo.cn/poi/32807570.html', 'https://www.mafengwo.cn/poi/34889264.html', 'https://www.mafengwo.cn/poi/5426656.html', 'https://www.mafengwo.cn/poi/91586736.html', 'https://www.mafengwo.cn/poi/33584040.html', 'https://www.mafengwo.cn/poi/5434170.html', 'https://www.mafengwo.cn/poi/91142828.html', 'https://www.mafengwo.cn/poi/3359887.html', 'https://www.mafengwo.cn/poi/91238444.html', 'https://www.mafengwo.cn/poi/34888976.html', 'https://www.mafengwo.cn/poi/34861312.html', 'https://www.mafengwo.cn/poi/34861372.html', 'https://www.mafengwo.cn/poi/91582264.html', 'https://www.mafengwo.cn/poi/91238476.html', 'https://www.mafengwo.cn/poi/34862068.html', 'https://www.mafengwo.cn/poi/91339340.html', 'https://www.mafengwo.cn/poi/34889888.html', 'https://www.mafengwo.cn/poi/102889904.html', 'https://www.mafengwo.cn/poi/91586492.html', 'https://www.mafengwo.cn/poi/91144360.html', 'https://www.mafengwo.cn/poi/76140084.html', 'https://www.mafengwo.cn/poi/92128472.html', 'https://www.mafengwo.cn/poi/33584992.html', 'https://www.mafengwo.cn/poi/91338844.html', 'https://www.mafengwo.cn/poi/5773.html', 'https://www.mafengwo.cn/poi/17691376.html', 'https://www.mafengwo.cn/poi/73994588.html', 'https://www.mafengwo.cn/poi/71739420.html', 'https://www.mafengwo.cn/poi/91575712.html', 'https://www.mafengwo.cn/poi/33584200.html', 'https://www.mafengwo.cn/poi/91340756.html', 'https://www.mafengwo.cn/poi/91918272.html', 'https://www.mafengwo.cn/poi/91588500.html', 'https://www.mafengwo.cn/poi/101372856.html', 'https://www.mafengwo.cn/poi/95633764.html', 'https://www.mafengwo.cn/poi/91578948.html', 'https://www.mafengwo.cn/poi/91585156.html', 'https://www.mafengwo.cn/poi/91928456.html', 'https://www.mafengwo.cn/poi/109029196.html', 'https://www.mafengwo.cn/poi/92132692.html', 'https://www.mafengwo.cn/poi/92135768.html', 'https://www.mafengwo.cn/poi/91143776.html', 'https://www.mafengwo.cn/poi/91301780.html', 'https://www.mafengwo.cn/poi/91584300.html', 'https://www.mafengwo.cn/poi/92129492.html', 'https://www.mafengwo.cn/poi/91339752.html', 'https://www.mafengwo.cn/poi/91380508.html', 'https://www.mafengwo.cn/poi/92620456.html', 'https://www.mafengwo.cn/poi/95636256.html', 'https://www.mafengwo.cn/poi/95633536.html', 'https://www.mafengwo.cn/poi/91589860.html', 'https://www.mafengwo.cn/poi/91582928.html', 'https://www.mafengwo.cn/poi/91574888.html', 'https://www.mafengwo.cn/poi/91579064.html', 'https://www.mafengwo.cn/poi/91587772.html', 'https://www.mafengwo.cn/poi/92128720.html', 'https://www.mafengwo.cn/poi/75509508.html', 'https://www.mafengwo.cn/poi/64703420.html', 'https://www.mafengwo.cn/poi/91578828.html', 'https://www.mafengwo.cn/poi/103748136.html', 'https://www.mafengwo.cn/poi/71739736.html', 'https://www.mafengwo.cn/poi/95634916.html', 'https://www.mafengwo.cn/poi/91586688.html', 'https://www.mafengwo.cn/poi/91589684.html', 'https://www.mafengwo.cn/poi/91588024.html', 'https://www.mafengwo.cn/poi/91590868.html', 'https://www.mafengwo.cn/poi/92031608.html', 'https://www.mafengwo.cn/poi/91586688.html', 'https://www.mafengwo.cn/poi/112066648.html', 'https://www.mafengwo.cn/poi/95634916.html', 'https://www.mafengwo.cn/poi/91584672.html', 'https://www.mafengwo.cn/poi/92105960.html', 'https://www.mafengwo.cn/poi/91339728.html', 'https://www.mafengwo.cn/poi/71739144.html', 'https://www.mafengwo.cn/poi/91142364.html', 'https://www.mafengwo.cn/poi/91142728.html', 'https://www.mafengwo.cn/poi/56689444.html', 'https://www.mafengwo.cn/poi/95633584.html', 'https://www.mafengwo.cn/poi/104753276.html', 'https://www.mafengwo.cn/poi/92132904.html', 'https://www.mafengwo.cn/poi/91575840.html', 'https://www.mafengwo.cn/poi/92132904.html', 'https://www.mafengwo.cn/poi/71739144.html', 'https://www.mafengwo.cn/poi/71739116.html', 'https://www.mafengwo.cn/poi/73993956.html', 'https://www.mafengwo.cn/poi/34913408.html', 'https://www.mafengwo.cn/poi/71739100.html', 'https://www.mafengwo.cn/poi/33584168.html', 'https://www.mafengwo.cn/poi/77163440.html', 'https://www.mafengwo.cn/poi/34890128.html', 'https://www.mafengwo.cn/poi/91238356.html', 'https://www.mafengwo.cn/poi/91574988.html', 'https://www.mafengwo.cn/poi/91579100.html', 'https://www.mafengwo.cn/poi/91589308.html', 'https://www.mafengwo.cn/poi/91589448.html', 'https://www.mafengwo.cn/poi/91574988.html', 'https://www.mafengwo.cn/poi/91579100.html', 'https://www.mafengwo.cn/poi/104750324.html', 'https://www.mafengwo.cn/poi/92134404.html', 'https://www.mafengwo.cn/poi/116772512.html', 'https://www.mafengwo.cn/poi/95635488.html', 'https://www.mafengwo.cn/poi/31640.html', 'https://www.mafengwo.cn/poi/91581052.html', 'https://www.mafengwo.cn/poi/35703.html', 'https://www.mafengwo.cn/poi/34889452.html', 'https://www.mafengwo.cn/poi/70042460.html', 'https://www.mafengwo.cn/poi/3303451.html', 'https://www.mafengwo.cn/poi/33584336.html', 'https://www.mafengwo.cn/poi/35615.html', 'https://www.mafengwo.cn/poi/92130768.html', 'https://www.mafengwo.cn/poi/70085464.html', 'https://www.mafengwo.cn/poi/73861964.html', 'https://www.mafengwo.cn/poi/7687918.html', 'https://www.mafengwo.cn/poi/59257000.html', 'https://www.mafengwo.cn/poi/35625.html', 'https://www.mafengwo.cn/poi/59011020.html', 'https://www.mafengwo.cn/poi/34861668.html', 'https://www.mafengwo.cn/poi/34889176.html', 'https://www.mafengwo.cn/poi/34888936.html', 'https://www.mafengwo.cn/poi/70042448.html', 'https://www.mafengwo.cn/poi/34889996.html', 'https://www.mafengwo.cn/poi/91338900.html', 'https://www.mafengwo.cn/poi/34861764.html', 'https://www.mafengwo.cn/poi/34861320.html', 'https://www.mafengwo.cn/poi/34861116.html', 'https://www.mafengwo.cn/poi/91338900.html', 'https://www.mafengwo.cn/poi/70055752.html', 'https://www.mafengwo.cn/poi/70041872.html', 'https://www.mafengwo.cn/poi/34889048.html', 'https://www.mafengwo.cn/poi/34861480.html', 'https://www.mafengwo.cn/poi/70041920.html', 'https://www.mafengwo.cn/poi/34889160.html', 'https://www.mafengwo.cn/poi/70052620.html', 'https://www.mafengwo.cn/poi/34862060.html', 'https://www.mafengwo.cn/poi/71739380.html', 'https://www.mafengwo.cn/poi/34889396.html', 'https://www.mafengwo.cn/poi/70042404.html', 'https://www.mafengwo.cn/poi/91238484.html', 'https://www.mafengwo.cn/poi/34861168.html', 'https://www.mafengwo.cn/poi/95637564.html', 'https://www.mafengwo.cn/poi/33584376.html', 'https://www.mafengwo.cn/poi/70042248.html', 'https://www.mafengwo.cn/poi/34861964.html', 'https://www.mafengwo.cn/poi/34890044.html', 'https://www.mafengwo.cn/poi/91340320.html', 'https://www.mafengwo.cn/poi/34889512.html', 'https://www.mafengwo.cn/poi/71854832.html', 'https://www.mafengwo.cn/poi/70042320.html', 'https://www.mafengwo.cn/poi/95637364.html', 'https://www.mafengwo.cn/poi/35630.html', 'https://www.mafengwo.cn/poi/5789.html', 'https://www.mafengwo.cn/poi/33583524.html', 'https://www.mafengwo.cn/poi/91578196.html', 'https://www.mafengwo.cn/poi/5690155.html', 'https://www.mafengwo.cn/poi/16747657.html']
# for i in li:
#     time.sleep(1)
#     driver.get(i)
#     time.sleep(2)
#     try:
#         j = driver.find_element_by_class_name('mod.mod-detail')
#     except:
#         j = ''
#
#     try:
#         summary = j.find_element_by_class_name('summary').text
#     except:
#         summary = ''
#     try:
#         tel = j.find_element_by_class_name('baseinfo').find_element_by_class_name('tel').find_element_by_class_name(
#             'content').text
#     except:
#         tel = ''
#     try:
#         item_time = j.find_element_by_class_name('baseinfo').find_element_by_class_name(
#             'item-time').find_element_by_class_name('content').text
#     except:
#         item_time = ''
#
#     one_data = dict(zip(['summary', 'tel', 'item_time'], [summary, tel, item_time]))
#     print(one_data)

# import random
# li=['武汉大学', '黄鹤楼', '意大利风情街', '东湖生态旅游风景区', '汉口圣母无原罪教堂']
# random.shuffle(li)
# ans = "根据您的喜好，为您推荐以下几个景点：<br>{}<br>{}<br>{}<br>{}<br>{}".format(li[0],li[1],li[2],li[3],li[4])
# print(ans)


# l1=['summary','tel','itime','img','wea']
# df=pd.DataFrame(l1)
# df.to_excel('./temp.xls',index=False)
# da = pd.read_excel(io='./temp.xls')
# l= da.values.tolist()
# print(l)


import pandas as pd
import pymysql
import requests
# data3 = pd.read_excel(io='./templates/武汉景点信息.xls')
# work_data3 = data3.values.tolist()
# print(work_data3[2])

#329
# def life(text):
#     db = pymysql.connect(host='127.0.0.1', user='root', password='123', database='yao')
#     # 创建游标
#     cursor = db.cursor()
#     sql2 = 'select * from middlescene where img = %s'
#     cursor.execute(sql2,text)
#     work_data3 = cursor.fetchall()
#     # l = list(work_data3[0])
#     l=work_data3[0]
#     return l
# print(life('黄鹤楼'))

# # 连接数据库
# db = pymysql.connect(host='127.0.0.1', user='root', password='123', database='yao')
# # 创建游标
# cursor = db.cursor()
# # SQL语句
# sql1 = 'insert into middlescene values (%s,%s,%s,%s,%s,%s)'
# # 执行SQL语句
# sql2 = 'delete from middlescene'
# cursor.execute(sql2)#先删干净再插，matlab的思想
# cursor.execute(sql1 , (str(summary),str(tel),str(itime),str(img),str(wea),str(jdname)))
# cursor.connection.commit()
# print('sql语句执行成功')



# 连接数据库
# def get_weather(text):
#     url = 'http://wthrcdn.etouch.cn/weather_mini?city='+text
#     res = requests.get(url).json()
#     return res
# db = pymysql.connect(host='127.0.0.1', user='root', password='123', database='yao')
# # 创建游标
# cursor = db.cursor()
# sql2 = 'delete from middlescene'
# cursor.execute(sql2)#先删干净再插，matlab的思想
# for i in work_data3:
#     # SQL语句
#     sql1 = 'insert into middlescene values (%s,%s,%s,%s,%s,%s)'
#     # 执行SQL语句
#     wea1='{}{}(今天)  最高气温：{}，最低气温：{}，风向：{},当前温度：{}，{}'.format(i[6],get_weather(i[6])['data']['forecast'][0]['date'],
#                                                           get_weather(i[6])['data']['forecast'][0]['high'],
#                                                           get_weather(i[6])['data']['forecast'][0]['low'],
#                                                           get_weather(i[6])['data']['forecast'][0]['fengxiang'],
#                                                           get_weather(i[6])['data']['wendu'],
#                                                           get_weather(i[6])['data']['ganmao'])
#     cursor.execute(sql1, (str(i[0]), str(i[1]), str(i[2]), str(i[5]), str(wea1), str(i[4])))
#     cursor.connection.commit()
#     print('sql语句执行成功')


# # 连接数据库
# db = pymysql.connect(host='127.0.0.1', user='root', password='123', database='yao')
# # 创建游标
# cursor = db.cursor()
# sql2 = 'delete from middlescene'
# cursor.execute(sql2)#先删干净再插，matlab的思想
# for i in work_data3:
#     # SQL语句
#     sql1 = 'insert into middlescene values (%s,%s,%s,%s,%s)'
#     # 执行SQL语句
#     cursor.execute(sql1, (str(i[0]), str(i[1]), str(i[2]), str(i[5]), str(i[4])))
#     cursor.connection.commit()
#     print('sql语句执行成功')



# from django.shortcuts import HttpResponse
# #329
# def fjsdi():
#     return HttpResponse('登录失败：用户名或密码有误')
#
# fjsdi()