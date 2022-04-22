from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import  FileResponse
from django.views.decorators.csrf import csrf_exempt
import pymysql
import re
from PIL import Image,ImageDraw,ImageFont
from random import randint,choice
import requests
import jieba
import json
import pandas as pd
import random
import tkinter.messagebox #弹窗库
from tkinter import *



# Create your views here.
def index(request):
    return render(request,'index.html')

def get_weather(text):
    url = 'http://wthrcdn.etouch.cn/weather_mini?city='+text
    res = requests.get(url).json()
    return res




# @csrf_exempt
# def activity(request):
#     ans='nothing'
#     data1 = pd.read_excel(io='myKGRS/templates/景点信息-分类后.xls')
#     data2 = pd.read_excel(io='myKGRS/templates/关系——景点景点之间的关系.xls')
#     work_data = data1.values.tolist()
#     work_data2 = data2.values.tolist()
#     data = []
#     links = []
#     for i in range(300):  # len(work_data)
#         dic1 = {'name': '{}'.format(work_data[i][2]), 'des': '{}'.format(work_data[i][2]), 'symbolSize': 70,
#                 'category': 1, 'symbol': 'image://{}'.format(work_data[i][3])}
#         dic2 = {'target': '{}'.format(work_data2[i][1]), 'source': '{}'.format(work_data2[i][3]),
#                 'name': '{}'.format(work_data2[i][2]), 'des': '景点-景点'}
#         data.append(dic1)
#         links.append(dic2)
#     # li=['武汉大学', '黄鹤楼', '意大利风情街', '东湖生态旅游风景区', '汉口圣母无原罪教堂','华中师范大学']#系统一点
#     # random.shuffle(li)
#     # ans = "根据您的喜好，为您推荐以下几个景点：<br>{}<br>{}<br>{}<br>{}<br>{}".format(li[0],li[1],li[2],li[3],li[4])
#     if request.method == "POST":
#         text = request.POST.get('data')
#
#     # return render(request,'activity.html',{"resdata":json.dumps(ans)})
#
#     return render(request, 'activity.html', {"data": json.dumps(data,ensure_ascii=False),"link":json.dumps(links,ensure_ascii=False),"resdata":json.dumps(ans,ensure_ascii=False)})


def life(text):
    db = pymysql.connect(host='127.0.0.1', user='root', password='123', database='yao')
    # 创建游标
    cursor = db.cursor()
    sql2 = "select * from middlescene where img = %s"
    cursor.execute(sql2, text)
    work_data3 = cursor.fetchall()
    # l = list(work_data3[0])

    return work_data3


@csrf_exempt
def activity(request):
    data1 = pd.read_excel(io='myKGRS/templates/景点信息-分类后.xls')
    data2 = pd.read_excel(io='myKGRS/templates/关系——景点景点之间的关系.xls')
    work_data = data1.values.tolist()
    work_data2 = data2.values.tolist()
    data = []
    links = []
    for i in range(300):  # len(work_data)
        dic1 = {'name': '{}'.format(work_data[i][2]), 'des': '{}'.format(work_data[i][2]), 'symbolSize': 70,
                'category': 1, 'symbol': 'image://{}'.format(work_data[i][3])}
        dic2 = {'target': '{}'.format(work_data2[i][1]), 'source': '{}'.format(work_data2[i][3]),
                'name': '{}'.format(work_data2[i][2]), 'des': '景点-景点'}
        data.append(dic1)
        links.append(dic2)
    li = ['华中农业大学', '鄂军都督府', '黄陂大余湾', '徐源泉公馆', '首义广场', '鹦鹉洲', '汉阳江滩', '武汉九真山风景区', '汉口租界', '世纪钟', '武汉体育中心', '汉古艺术馆',
          '野村谷郊野公园', '嵩阳森林公园', '汉口天主堂', '武汉国际博览中心', '同兴里', '武汉木兰云雾山景区', '武汉动物园', '界立方创意空间', '木兰玫瑰园', '辛亥革命博物馆',
          '武汉长江二桥', '中南财经政法大学', '武汉九峰森林动物园', '东湖小梅岭', '盘龙城遗址', '湖北美术学院', '武汉市基督教武昌堂', '国立武汉大学牌楼(新)', '武汉音乐学院',
          '龙降坪国际滑雪场', '洪山宝塔', '谭鑫培公园', '中山公园', '江汉关博物馆', '九真桃源', '楚河汉街', '小南湖公园', '清河桥', '起义门', '东湖磨山风景区', '武汉天地',
          '武汉理工大学', '5D星空错觉艺术馆', '搁笔亭', '武汉园博园-汉口里', '武汉花博汇', '花楼街', '古琴台', '石门峰纪念公园-辛亥革命纪念园', '碧潭观鱼', '风光村', '禹稷行宫',
          '汉口圣母无原罪堂', '晴川阁', '徐东商业街', '九峰国家森林公园', '常青公园', '朴园', '湖北大学', '东湖景区磨山景区日式亭', '先月亭', '万国公园', '关山荷兰风情园',
          '世界城光谷步行街', '朱碑亭', '南岸嘴', '木兰水镇', '昙华林历史文化陈列馆', '武汉电视塔', '合美术馆', '武大樱花园', '平和打包厂旧址', '武汉杜莎夫人蜡像馆',
          '武汉大学万林艺术博物馆', '花园山牧师楼', '白云阁', '黄陂清凉寨', '昙华林', '武汉大学东湖分校东大门', '武汉大学樱园', '光谷国际网球中心', '东湖楚城', '黄鹤归来铜雕',
          '汉口美国领事馆旧址', '武汉大好河山休闲旅游区', '大别山南武当滑雪场', '洪山广场', '武昌红巷码头', '武汉国民政府旧址', '华中师范大学', '樱花大道', '抗洪纪念碑', '荆州长江大桥',
          '湖北省博物馆', '二七长江大桥', '武汉革命博物馆', '农民运动讲习所旧址', '东湖生态旅游风景区梨园', '梵高星空艺术馆', '武昌起义军政府旧址', '老斋舍', '武汉东湖牡丹园', '东湖鸟语林',
          '中国武钢博物馆', 'K11艺术村', '汉阳造广告产业园', '中国地质大学博物馆', '武汉体育学院', '武汉防汛纪念碑', '户部巷小吃一条街', '石榴红村', '宋庆龄旧居', '六一纪念亭',
          '武汉花世界', '花之都儿童乐园', '归元禅寺', '汉口日清洋行大楼旧址', '武汉美术馆', '大智门火车站', '武汉长江大桥建成纪念碑', '武汉张公山寨', '汉口粤汉码头', '大陆坊旧址',
          '临江大道', '古德寺', '堤角公园', '月湖桥', '西北湖绿化广场', '洞庭街', '湖北省图书馆', '武汉长江大桥', '解放公园', '武昌廉政文化公园', '《崔颢题诗图》浮雕', '湖北省美术馆',
          '中国地质大学', '武汉市东湖磨山植物园', '首义文化公园', '鹅池', '蛇山景区', '花山滑翔伞体验', '武汉科技馆', '武汉东西湖郁金香主题公园', '曾侯乙编钟', '光谷多莫大教堂',
          '武汉大学', '旺山公园', '白云洞军事旅游风景区', '禹碑', '武汉大学樱花节', '东湖梅园', '光谷天地', '武汉琴台大剧院', '后襄河公园', '普愿禅寺', '张之洞与武汉博物馆',
          '楚望台遗址公园', '江汉关大楼旧址', '汉正街', '王家墩公园', '汉口近代建筑群', '石门峰名人文化公园', '汉阳造艺术区', '恒河生态园', '汉阳树', '武汉大学珞珈山', '宝通禅寺',
          '青龙山森林公园', '楚天台', '长江武汉关', '武汉别克.汉秀剧场', '琴台公园', '武汉杂技厅', '东湖听涛景区', '汉绣博物馆', '雁洲索桥', '龙灵山生态公园', '中国科学院武汉植物园',
          '神农架国际滑雪场', '东湖落雁岛', '武汉东湖海洋乐园', '东湖荷园', '农耕年华', '蓝波湾庄园', '珞珈山街', '詹天佑故居', '青山公园', '武汉大学-图书馆', '长春街', '异国风情园',
          '黎黄陂路', '东湖南路水生所', '莲溪寺', '翟雅阁博物馆', '汉阳公园', '宝岛公园', '沙湖公园', '金银湖湿地公园', '中南民族大学', '古卓刀泉寺', '紫阳公园', '巴公房子',
          '木兰古门', '绿野仙踪', '木兰湖旅游度假区', '喷泉公园', '失落之塔', '木兰草原风景区-草原牧场', '武汉海昌极地海洋公园', '中山舰博物馆', '施洋烈士陵园', '木兰山风景区',
          '毛泽东词亭', '北洋桥', '汉口江滩', '长春观', '汉口东正教堂', '墨水湖', '黎黄陂路街头博物馆', '木兰花海乐园景区', '汤湖公园', '大成路夜市', '木兰清凉寨风景区',
          '东湖南路凌波门', '九宫山滑雪场', '木兰草原', '晴川桥', '京汉铁路总工会旧址', '星期8小镇武汉站', '马鞍山森林公园', '蔡甸消泗油菜花', '十八栋', '姚家山风景区', '武昌江滩',
          '马投潭遗址公园', '403国际艺术中心', '武汉胜天生态农庄', '鹦鹉洲长江大桥', '汤逊湖', '崇真堂', '天行洲', '意大利风情街', '凤娃古寨', '农讲所旧址纪念馆',
          '中科院水生生物博物馆', '道观河风景区', '汉口江滩边芦苇丛', '紫薇都市田园', '后官湖', '螃蟹甲', '吴家花园', '长江观景第一台', '石瑛故居', '胜像宝塔', '武汉欢乐谷',
          '华中科技大学', '木兰花乡', '江汉路步行街', '龙王庙公园', '东湖杉美术馆', '极乐汤(金银潭店)', '武汉两江游览(夜游长江)', '武汉博物馆', '罗汉堂', '藏龙岛', '越王勾践剑',
          '中山大道', '武汉大学工学部', '木兰天池', '东湖樱花园', '锦里沟', '龟山公园', '天兴洲', '得胜桥', '阅马场', '铁门关', '毛泽东同志旧居', '汉口水塔', '东湖生态旅游风景区',
          '武汉园博园', '屈原纪念馆', '黄鹤楼', '吉庆街', '月湖风景区', '九女墩', '中共五大会址纪念馆', '八七会议会址', '湖北中医药大学', '醉美西湖观光游乐园', '大禹神话园',
          '后官湖湿地公园', '江夏区大花山', '灵泉寺', '武汉大学信息学部', '武汉SPACE酒吧', '恐龙化石博物馆', '武汉琴台钢琴博物馆', '江滩公园']
    random.shuffle(li)
    ans = "根据您的喜好，为您推荐以下几个景点：<br>{}<br>{}<br>{}<br>{}<br>{}".format(li[0], li[1], li[2], li[3], li[4])
    # ans = "你说啥，俺听不懂，请输入景点名称"
    l = [
        '·前身为清末湖广总督张之洞创立的自强学堂，后更名为“国立武汉大学”；濒临东湖，环抱珞珈山，校园内绿树成荫。\n·樱花名声远扬，校园内有樱花城堡、樱花大道、樱顶、珞珈广场等主要赏樱地点；其中，“老斋舍”前的“樱花大道”，是武大赏樱的好去处。\n·除了樱花，更值得一看的是一幢幢的老建筑；珞珈山腰东南的教工住宅群，建筑风格整体采用了英式乡间别墅风格，每一栋都自有其特点。',
        '027-68755114', '1-3小时', 'https://www.mafengwo.cn/poi/5812.html', '武汉大学',
        'https://p1-q.mafengwo.net/s11/M00/85/21/wKgBEFqs9YuAPw3sACUHrWysEyc08.jpeg?imageMogr2%2Fthumbnail%2F%21192x130r%2Fgravity%2FCenter%2Fcrop%2F%21192x130%2Fquality%2F100',
        '武汉']
    summary=l[0]
    tel=l[1]
    itime=l[2]
    img=l[5]
    jdname=l[4]
    # if request.method == "POST":
    #     text = request.POST.get('data')
    #     if(text!=None):
    #         print('start')
    #         print(text)

    text='武汉大学'

    if request.method == "POST":
        text = request.POST.get('data')
    db = pymysql.connect(host='127.0.0.1', user='root', password='123', database='yao')
    # 创建游标
    cursor = db.cursor()
    sql2 = "select * from middlescene where img = %s "
    cursor.execute(sql2, text)
    work_data3 = cursor.fetchall()
    print(work_data3)
    l=work_data3[0]
    summary = json.dumps(l[0], ensure_ascii=False)
    tel = json.dumps(l[1], ensure_ascii=False)
    itime = json.dumps(l[2], ensure_ascii=False)
    img = json.dumps(l[3], ensure_ascii=False)
    jdname = json.dumps(l[4], ensure_ascii=False)

    data=json.dumps(data,ensure_ascii=False)
    link=json.dumps(links, ensure_ascii=False)
    resdata=json.dumps(ans, ensure_ascii=False)
    # print('{} {} {} {} {} {} {} {}'.format(data,link,resdata,summary,tel,itime,img,jdname))
    return render(request, 'activity.html', locals())
    # return render(request, 'activity.html', {"data": json.dumps(data,ensure_ascii=False),"link":json.dumps(links,ensure_ascii=False),"resdata":json.dumps(ans,ensure_ascii=False)})


# def life(text):
#     db = pymysql.connect(host='127.0.0.1', user='root', password='123', database='yao')
#     # 创建游标
#     cursor = db.cursor()
#     sql2 = 'select * from middlescene'
#     cursor.execute(sql2)
#     work_data3 = cursor.fetchall()
#     l=[]
#     for i in work_data3:
#         print(i)
#         if (text in i):
#             l = list(i)
#             break
#         else:
#             # print('{}暂时不在景点库中'.format(text))
#             pass
#     return l

# @csrf_exempt
# def activity(request):
#     data1 = pd.read_excel(io='myKGRS/templates/景点信息-分类后.xls')
#     data2 = pd.read_excel(io='myKGRS/templates/关系——景点景点之间的关系.xls')
#     work_data = data1.values.tolist()
#     work_data2 = data2.values.tolist()
#     data = []
#     links = []
#     for i in range(300):  # len(work_data)
#         dic1 = {'name': '{}'.format(work_data[i][2]), 'des': '{}'.format(work_data[i][2]), 'symbolSize': 70,
#                 'category': 1, 'symbol': 'image://{}'.format(work_data[i][3])}
#         dic2 = {'target': '{}'.format(work_data2[i][1]), 'source': '{}'.format(work_data2[i][3]),
#                 'name': '{}'.format(work_data2[i][2]), 'des': '景点-景点'}
#         data.append(dic1)
#         links.append(dic2)
#     li = ['华中农业大学', '鄂军都督府', '黄陂大余湾', '徐源泉公馆', '首义广场', '鹦鹉洲', '汉阳江滩', '武汉九真山风景区', '汉口租界', '世纪钟', '武汉体育中心', '汉古艺术馆',
#           '野村谷郊野公园', '嵩阳森林公园', '汉口天主堂', '武汉国际博览中心', '同兴里', '武汉木兰云雾山景区', '武汉动物园', '界立方创意空间', '木兰玫瑰园', '辛亥革命博物馆',
#           '武汉长江二桥', '中南财经政法大学', '武汉九峰森林动物园', '东湖小梅岭', '盘龙城遗址', '湖北美术学院', '武汉市基督教武昌堂', '国立武汉大学牌楼(新)', '武汉音乐学院',
#           '龙降坪国际滑雪场', '洪山宝塔', '谭鑫培公园', '中山公园', '江汉关博物馆', '九真桃源', '楚河汉街', '小南湖公园', '清河桥', '起义门', '东湖磨山风景区', '武汉天地',
#           '武汉理工大学', '5D星空错觉艺术馆', '搁笔亭', '武汉园博园-汉口里', '武汉花博汇', '花楼街', '古琴台', '石门峰纪念公园-辛亥革命纪念园', '碧潭观鱼', '风光村', '禹稷行宫',
#           '汉口圣母无原罪堂', '晴川阁', '徐东商业街', '九峰国家森林公园', '常青公园', '朴园', '湖北大学', '东湖景区磨山景区日式亭', '先月亭', '万国公园', '关山荷兰风情园',
#           '世界城光谷步行街', '朱碑亭', '南岸嘴', '木兰水镇', '昙华林历史文化陈列馆', '武汉电视塔', '合美术馆', '武大樱花园', '平和打包厂旧址', '武汉杜莎夫人蜡像馆',
#           '武汉大学万林艺术博物馆', '花园山牧师楼', '白云阁', '黄陂清凉寨', '昙华林', '武汉大学东湖分校东大门', '武汉大学樱园', '光谷国际网球中心', '东湖楚城', '黄鹤归来铜雕',
#           '汉口美国领事馆旧址', '武汉大好河山休闲旅游区', '大别山南武当滑雪场', '洪山广场', '武昌红巷码头', '武汉国民政府旧址', '华中师范大学', '樱花大道', '抗洪纪念碑', '荆州长江大桥',
#           '湖北省博物馆', '二七长江大桥', '武汉革命博物馆', '农民运动讲习所旧址', '东湖生态旅游风景区梨园', '梵高星空艺术馆', '武昌起义军政府旧址', '老斋舍', '武汉东湖牡丹园', '东湖鸟语林',
#           '中国武钢博物馆', 'K11艺术村', '汉阳造广告产业园', '中国地质大学博物馆', '武汉体育学院', '武汉防汛纪念碑', '户部巷小吃一条街', '石榴红村', '宋庆龄旧居', '六一纪念亭',
#           '武汉花世界', '花之都儿童乐园', '归元禅寺', '汉口日清洋行大楼旧址', '武汉美术馆', '大智门火车站', '武汉长江大桥建成纪念碑', '武汉张公山寨', '汉口粤汉码头', '大陆坊旧址',
#           '临江大道', '古德寺', '堤角公园', '月湖桥', '西北湖绿化广场', '洞庭街', '湖北省图书馆', '武汉长江大桥', '解放公园', '武昌廉政文化公园', '《崔颢题诗图》浮雕', '湖北省美术馆',
#           '中国地质大学', '武汉市东湖磨山植物园', '首义文化公园', '鹅池', '蛇山景区', '花山滑翔伞体验', '武汉科技馆', '武汉东西湖郁金香主题公园', '曾侯乙编钟', '光谷多莫大教堂',
#           '武汉大学', '旺山公园', '白云洞军事旅游风景区', '禹碑', '武汉大学樱花节', '东湖梅园', '光谷天地', '武汉琴台大剧院', '后襄河公园', '普愿禅寺', '张之洞与武汉博物馆',
#           '楚望台遗址公园', '江汉关大楼旧址', '汉正街', '王家墩公园', '汉口近代建筑群', '石门峰名人文化公园', '汉阳造艺术区', '恒河生态园', '汉阳树', '武汉大学珞珈山', '宝通禅寺',
#           '青龙山森林公园', '楚天台', '长江武汉关', '武汉别克.汉秀剧场', '琴台公园', '武汉杂技厅', '东湖听涛景区', '汉绣博物馆', '雁洲索桥', '龙灵山生态公园', '中国科学院武汉植物园',
#           '神农架国际滑雪场', '东湖落雁岛', '武汉东湖海洋乐园', '东湖荷园', '农耕年华', '蓝波湾庄园', '珞珈山街', '詹天佑故居', '青山公园', '武汉大学-图书馆', '长春街', '异国风情园',
#           '黎黄陂路', '东湖南路水生所', '莲溪寺', '翟雅阁博物馆', '汉阳公园', '宝岛公园', '沙湖公园', '金银湖湿地公园', '中南民族大学', '古卓刀泉寺', '紫阳公园', '巴公房子',
#           '木兰古门', '绿野仙踪', '木兰湖旅游度假区', '喷泉公园', '失落之塔', '木兰草原风景区-草原牧场', '武汉海昌极地海洋公园', '中山舰博物馆', '施洋烈士陵园', '木兰山风景区',
#           '毛泽东词亭', '北洋桥', '汉口江滩', '长春观', '汉口东正教堂', '墨水湖', '黎黄陂路街头博物馆', '木兰花海乐园景区', '汤湖公园', '大成路夜市', '木兰清凉寨风景区',
#           '东湖南路凌波门', '九宫山滑雪场', '木兰草原', '晴川桥', '京汉铁路总工会旧址', '星期8小镇武汉站', '马鞍山森林公园', '蔡甸消泗油菜花', '十八栋', '姚家山风景区', '武昌江滩',
#           '马投潭遗址公园', '403国际艺术中心', '武汉胜天生态农庄', '鹦鹉洲长江大桥', '汤逊湖', '崇真堂', '天行洲', '意大利风情街', '凤娃古寨', '农讲所旧址纪念馆',
#           '中科院水生生物博物馆', '道观河风景区', '汉口江滩边芦苇丛', '紫薇都市田园', '后官湖', '螃蟹甲', '吴家花园', '长江观景第一台', '石瑛故居', '胜像宝塔', '武汉欢乐谷',
#           '华中科技大学', '木兰花乡', '江汉路步行街', '龙王庙公园', '东湖杉美术馆', '极乐汤(金银潭店)', '武汉两江游览(夜游长江)', '武汉博物馆', '罗汉堂', '藏龙岛', '越王勾践剑',
#           '中山大道', '武汉大学工学部', '木兰天池', '东湖樱花园', '锦里沟', '龟山公园', '天兴洲', '得胜桥', '阅马场', '铁门关', '毛泽东同志旧居', '汉口水塔', '东湖生态旅游风景区',
#           '武汉园博园', '屈原纪念馆', '黄鹤楼', '吉庆街', '月湖风景区', '九女墩', '中共五大会址纪念馆', '八七会议会址', '湖北中医药大学', '醉美西湖观光游乐园', '大禹神话园',
#           '后官湖湿地公园', '江夏区大花山', '灵泉寺', '武汉大学信息学部', '武汉SPACE酒吧', '恐龙化石博物馆', '武汉琴台钢琴博物馆', '江滩公园']
#     random.shuffle(li)
#     ans = "根据您的喜好，为您推荐以下几个景点：<br>{}<br>{}<br>{}<br>{}<br>{}".format(li[0], li[1], li[2], li[3], li[4])
#     l = [
#         '·前身为清末湖广总督张之洞创立的自强学堂，后更名为“国立武汉大学”；濒临东湖，环抱珞珈山，校园内绿树成荫。\n·樱花名声远扬，校园内有樱花城堡、樱花大道、樱顶、珞珈广场等主要赏樱地点；其中，“老斋舍”前的“樱花大道”，是武大赏樱的好去处。\n·除了樱花，更值得一看的是一幢幢的老建筑；珞珈山腰东南的教工住宅群，建筑风格整体采用了英式乡间别墅风格，每一栋都自有其特点。',
#         '027-68755114', '1-3小时', 'https://www.mafengwo.cn/poi/5812.html', '武汉大学',
#         'https://p1-q.mafengwo.net/s11/M00/85/21/wKgBEFqs9YuAPw3sACUHrWysEyc08.jpeg?imageMogr2%2Fthumbnail%2F%21192x130r%2Fgravity%2FCenter%2Fcrop%2F%21192x130%2Fquality%2F100',
#         '武汉']
#
#     text = request.POST.get('data')
#
#     print('start')
#     print(text)
#
#     l=life(text)
#     summary = l[0]
#     tel=l[1]
#     itime=l[2]
#     img=l[5]
#     jdname=l[4]
#     # for i in work_data3:
#     #     print(i)
#     #     if (text in i):
#     #         l = list(i)
#     #         break
#     #     else:
#     #         # print('{}暂时不在景点库中'.format(text))
#     #         pass
#     # else:
#     #     ans = "不好意思，请重新输入，小呆的景点库中没有你输入的景点哦！"
#
#     summary = json.dumps(l[0], ensure_ascii=False)
#     tel = json.dumps(l[1], ensure_ascii=False)
#     itime = json.dumps(l[2], ensure_ascii=False)
#     img = json.dumps(l[3], ensure_ascii=False)
#     jdname = json.dumps(l[4], ensure_ascii=False)
#
#     data=json.dumps(data,ensure_ascii=False)
#     link=json.dumps(links, ensure_ascii=False)
#     resdata=json.dumps(ans, ensure_ascii=False)
#     print('{} {} {} {} {} {} {} {}'.format(data,link,resdata,summary,tel,itime,img,jdname))
#     return render(request, 'activity.html', locals())
#









# @csrf_exempt
# def activity2(request):
#     ans='nothing'
#     data1 = pd.read_excel(io='myKGRS/templates/景点信息-分类后.xls')
#     data2 = pd.read_excel(io='myKGRS/templates/关系——景点景点之间的关系.xls')
#     # data3 = pd.read_excel(io='myKGRS/templates/武汉景点信息.xls')
#     work_data = data1.values.tolist()
#     work_data2 = data2.values.tolist()
#     # work_data3 = data3.values.tolist()
#     data = []
#     links = []
#     for i in range(300):  # len(work_data)
#         dic1 = {'name': '{}'.format(work_data[i][2]), 'des': '{}'.format(work_data[i][2]), 'symbolSize': 70,
#                 'category': 1, 'symbol': 'image://{}'.format(work_data[i][3])}
#         dic2 = {'target': '{}'.format(work_data2[i][1]), 'source': '{}'.format(work_data2[i][3]),
#                 'name': '{}'.format(work_data2[i][2]), 'des': '景点-景点'}
#         data.append(dic1)
#         links.append(dic2)
#     li=['华中农业大学', '鄂军都督府', '黄陂大余湾', '徐源泉公馆', '首义广场', '鹦鹉洲', '汉阳江滩', '武汉九真山风景区', '汉口租界', '世纪钟', '武汉体育中心', '汉古艺术馆', '野村谷郊野公园', '嵩阳森林公园', '汉口天主堂', '武汉国际博览中心', '同兴里', '武汉木兰云雾山景区', '武汉动物园', '界立方创意空间', '木兰玫瑰园', '辛亥革命博物馆', '武汉长江二桥', '中南财经政法大学', '武汉九峰森林动物园', '东湖小梅岭', '盘龙城遗址', '湖北美术学院', '武汉市基督教武昌堂', '国立武汉大学牌楼(新)', '武汉音乐学院', '龙降坪国际滑雪场', '洪山宝塔', '谭鑫培公园', '中山公园', '江汉关博物馆', '九真桃源', '楚河汉街', '小南湖公园', '清河桥', '起义门', '东湖磨山风景区', '武汉天地', '武汉理工大学', '5D星空错觉艺术馆', '搁笔亭', '武汉园博园-汉口里', '武汉花博汇', '花楼街', '古琴台', '石门峰纪念公园-辛亥革命纪念园', '碧潭观鱼', '风光村', '禹稷行宫', '汉口圣母无原罪堂', '晴川阁', '徐东商业街', '九峰国家森林公园', '常青公园', '朴园', '湖北大学', '东湖景区磨山景区日式亭', '先月亭', '万国公园', '关山荷兰风情园', '世界城光谷步行街', '朱碑亭', '南岸嘴', '木兰水镇', '昙华林历史文化陈列馆', '武汉电视塔', '合美术馆', '武大樱花园', '平和打包厂旧址', '武汉杜莎夫人蜡像馆', '武汉大学万林艺术博物馆', '花园山牧师楼', '白云阁', '黄陂清凉寨', '昙华林', '武汉大学东湖分校东大门', '武汉大学樱园', '光谷国际网球中心', '东湖楚城', '黄鹤归来铜雕', '汉口美国领事馆旧址', '武汉大好河山休闲旅游区', '大别山南武当滑雪场', '洪山广场', '武昌红巷码头', '武汉国民政府旧址', '华中师范大学', '樱花大道', '抗洪纪念碑', '荆州长江大桥', '湖北省博物馆', '二七长江大桥', '武汉革命博物馆', '农民运动讲习所旧址', '东湖生态旅游风景区梨园', '梵高星空艺术馆', '武昌起义军政府旧址', '老斋舍', '武汉东湖牡丹园', '东湖鸟语林', '中国武钢博物馆', 'K11艺术村', '汉阳造广告产业园', '中国地质大学博物馆', '武汉体育学院', '武汉防汛纪念碑', '户部巷小吃一条街', '石榴红村', '宋庆龄旧居', '六一纪念亭', '武汉花世界', '花之都儿童乐园', '归元禅寺', '汉口日清洋行大楼旧址', '武汉美术馆', '大智门火车站', '武汉长江大桥建成纪念碑', '武汉张公山寨', '汉口粤汉码头', '大陆坊旧址', '临江大道', '古德寺', '堤角公园', '月湖桥', '西北湖绿化广场', '洞庭街', '湖北省图书馆', '武汉长江大桥', '解放公园', '武昌廉政文化公园', '《崔颢题诗图》浮雕', '湖北省美术馆', '中国地质大学', '武汉市东湖磨山植物园', '首义文化公园', '鹅池', '蛇山景区', '花山滑翔伞体验', '武汉科技馆', '武汉东西湖郁金香主题公园', '曾侯乙编钟', '光谷多莫大教堂', '武汉大学', '旺山公园', '白云洞军事旅游风景区', '禹碑', '武汉大学樱花节', '东湖梅园', '光谷天地', '武汉琴台大剧院', '后襄河公园', '普愿禅寺', '张之洞与武汉博物馆', '楚望台遗址公园', '江汉关大楼旧址', '汉正街', '王家墩公园', '汉口近代建筑群', '石门峰名人文化公园', '汉阳造艺术区', '恒河生态园', '汉阳树', '武汉大学珞珈山', '宝通禅寺', '青龙山森林公园', '楚天台', '长江武汉关', '武汉别克.汉秀剧场', '琴台公园', '武汉杂技厅', '东湖听涛景区', '汉绣博物馆', '雁洲索桥', '龙灵山生态公园', '中国科学院武汉植物园', '神农架国际滑雪场', '东湖落雁岛', '武汉东湖海洋乐园', '东湖荷园', '农耕年华', '蓝波湾庄园', '珞珈山街', '詹天佑故居', '青山公园', '武汉大学-图书馆', '长春街', '异国风情园', '黎黄陂路', '东湖南路水生所', '莲溪寺', '翟雅阁博物馆', '汉阳公园', '宝岛公园', '沙湖公园', '金银湖湿地公园', '中南民族大学', '古卓刀泉寺', '紫阳公园', '巴公房子', '木兰古门', '绿野仙踪', '木兰湖旅游度假区', '喷泉公园', '失落之塔', '木兰草原风景区-草原牧场', '武汉海昌极地海洋公园', '中山舰博物馆', '施洋烈士陵园', '木兰山风景区', '毛泽东词亭', '北洋桥', '汉口江滩', '长春观', '汉口东正教堂', '墨水湖', '黎黄陂路街头博物馆', '木兰花海乐园景区', '汤湖公园', '大成路夜市', '木兰清凉寨风景区', '东湖南路凌波门', '九宫山滑雪场', '木兰草原', '晴川桥', '京汉铁路总工会旧址', '星期8小镇武汉站', '马鞍山森林公园', '蔡甸消泗油菜花', '十八栋', '姚家山风景区', '武昌江滩', '马投潭遗址公园', '403国际艺术中心', '武汉胜天生态农庄', '鹦鹉洲长江大桥', '汤逊湖', '崇真堂', '天行洲', '意大利风情街', '凤娃古寨', '农讲所旧址纪念馆', '中科院水生生物博物馆', '道观河风景区', '汉口江滩边芦苇丛', '紫薇都市田园', '后官湖', '螃蟹甲', '吴家花园', '长江观景第一台', '石瑛故居', '胜像宝塔', '武汉欢乐谷', '华中科技大学', '木兰花乡', '江汉路步行街', '龙王庙公园', '东湖杉美术馆', '极乐汤(金银潭店)', '武汉两江游览(夜游长江)', '武汉博物馆', '罗汉堂', '藏龙岛', '越王勾践剑', '中山大道', '武汉大学工学部', '木兰天池', '东湖樱花园', '锦里沟', '龟山公园', '天兴洲', '得胜桥', '阅马场', '铁门关', '毛泽东同志旧居', '汉口水塔', '东湖生态旅游风景区', '武汉园博园', '屈原纪念馆', '黄鹤楼', '吉庆街', '月湖风景区', '九女墩', '中共五大会址纪念馆', '八七会议会址', '湖北中医药大学', '醉美西湖观光游乐园', '大禹神话园', '后官湖湿地公园', '江夏区大花山', '灵泉寺', '武汉大学信息学部', '武汉SPACE酒吧', '恐龙化石博物馆', '武汉琴台钢琴博物馆', '江滩公园']
#     random.shuffle(li)
#     ans = "根据您的喜好，为您推荐以下几个景点：<br>{}<br>{}<br>{}<br>{}<br>{}".format(li[0],li[1],li[2],li[3],li[4])
#     # summary='none'
#     # tel='none'
#     # itime='none'
#     # img='none'
#     # wea='none'
#
#     db = pymysql.connect(host='127.0.0.1', user='root', password='123', database='yao')
#     # 创建游标
#     cursor = db.cursor()
#     sql2 = 'select * from middlescene'
#     cursor.execute(sql2)
#     work_data3=cursor.fetchall()
#     print(work_data3)
#     text='n'
#     l = []
#     if request.method == "POST":
#         text = request.POST.get('data')
#         print(text)
#         if(text!=None):
#             for i in work_data3:
#                 print(i)
#                 if (text in i):
#                     l = list(i)
#                     break
#                 else:
#                     print('{}暂时不在景点库中'.format(text))
#             else:
#                 ans = "不好意思，请重新输入，小呆的景点库中没有你输入的景点哦！"
#
#
#
#
#     print('l:{}'.format(l))
#     # sql2='delete from middlescene'
#     # cursor.execute(sql2)
#     # cursor.connection.commit()
#     return render(request, 'activity2.html', {
#         "data": json.dumps(data,ensure_ascii=False),
#         "link":json.dumps(links,ensure_ascii=False),
#         "resdata":json.dumps(ans,ensure_ascii=False),
#         "summary":json.dumps(l[0],ensure_ascii=False),
#         "tel":json.dumps(l[1],ensure_ascii=False),
#         "itime":json.dumps(l[2],ensure_ascii=False),
#         "img":json.dumps(l[4],ensure_ascii=False),
#         "jdname":json.dumps(l[3],ensure_ascii=False),
#     })
#
#



def imglist(request):
    return render(request,'imglist.html')


# 登录界面
def login(request):
    return render(request,'login.html')
def getRandomChar():
    #定义函数获取随机字符
    num=str(randint(0,9))
    lower=chr(randint(97,122))
    upper=chr(randint(65,90))
    char=choice([num,lower,upper])
    return char
def createImg(request):
    img=Image.new(mode="RGB",size=(160,30),color=(100,100,100))
    draw=ImageDraw.Draw(img)
    font=ImageFont.truetype(font="arial.ttf",size=24)
    code=''
    for i in range(5):
        c=getRandomChar()
        draw.text((10+30*i,2),text=c,fill=(255,255,255),font=font)
        code+=c
    request.session['randomcode']=code
    f=open("test.png","wb")
    img.save(f,format("png"))
    f.close()
    return FileResponse(open("test.png",'rb'))
def verifyCode(request):
    out='验证码不正确'
    if request.POST['code'].upper()==request.session['randomcode'].upper():
        out="验证码正确"
    return HttpResponse(out)
def check(order):
    if len(order) < 8:
        return False
    strengthRegex = re.compile('[a-zA-Z]+')  # 至少有一个字母
    if strengthRegex.findall(order) == []:
        return False
    strengthRegex = re.compile('\d+')  # 至少有一个数字
    if strengthRegex.findall(order) == []:
        return False
    return True
# 定义一个函数，用来保存注册的数据
def save(request):
    has_regiter = 0  # 用来记录当前账号是否已存在，0：不存在 1：已存在
    a = request.POST  # 获取post()请求
    # print(a)
    # 通过get()请求获取前端提交的数据
    userName = a['username']
    passWord = a['password']
    if not check(passWord):
        return HttpResponse('密码需要包括字母和数字，且不小于八位数！')
    # print(userName,passWord)
    # 连接数据库
    db = pymysql.connect(host='127.0.0.1', user='root', password='123', database='drug')
    # 创建游标
    cursor = db.cursor()
    # SQL语句
    sql1 = 'select * from drug_admin1'
    # 执行SQL语句
    cursor.execute(sql1)
    # 查询到所有的数据存储到all_users中
    all_users = cursor.fetchall()
    i = 0
    while i < len(all_users):
        if userName in all_users[i]:
            ##表示该账号已经存在
            has_regiter = 1
        i += 1
    out = 0
    if request.POST['code'].upper() == request.session['randomcode'].upper():
        out =1
    if has_regiter == 0:
        # 将用户名与密码插入到数据库中
        sql2 = 'insert into drug_admin1(name,pwd) values(%s,%s)'
        cursor.execute(sql2, (userName, passWord))
        db.commit()
        cursor.close()
        db.close()
        return HttpResponse('注册成功')
    else:
        cursor.close()
        db.close()
        if(out==0):
            return HttpResponse('注册失败：验证码错误')
        else:
            return HttpResponse('注册失败：该账号已存在')
def query(request):
    a = request.POST
    userName = a['username']
    passWord = a['password']
    if not check(passWord):
        return HttpResponse('密码需要包括字母和数字，且不小于八位数！')
    user_tup = (userName, passWord)
    db = pymysql.connect(host='127.0.0.1', user='root', password='123', database='drug')
    cursor = db.cursor()
    sql = 'select * from drug_admin1'
    cursor.execute(sql)
    all_users = cursor.fetchall()
    cursor.close()
    db.close()
    has_user = 0
    i = 0
    while i < len(all_users):
        if user_tup == all_users[i]:
            has_user = 1
        i += 1
    out = 0
    if request.POST['code'].upper() == request.session['randomcode'].upper():
        out = 1
    if has_user == 1 and out==1:
        return render(request, 'activity.html')
        # return HttpResponse('登录成功')
    else:
        if(out==0):
            return HttpResponse('登录失败：验证码错误')
        else:
            return HttpResponse('登录失败：用户名或密码有误')

