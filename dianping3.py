# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 22:56:09 2019

@author: lenovo
"""

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from scrapy.http import HtmlResponse
from datetime import datetime
import re
import time
import uuid
import random
import pymysql
import requests
from lxml import etree

connect = pymysql.Connect(
    host='*****',
    port=3306,
    user='root',
    passwd='*****',
    db='ctrip_gengxin',
    use_unicode=1,
    charset='utf8'
)
_css_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }

font_size = 14
start_y = 23

class XiechengDriverService(object):
    def __init__(self):
        self.driver = webdriver.Chrome()       
        self.listPageInfo = []       
        self.hotelItem = {}        
        self.commList = []
        #self.urls=['http://you.ctrip.com/sight/beijing1/234.html','http://you.ctrip.com/sight/beijing1/229.html','http://you.ctrip.com/sight/beijing1/231.html','http://you.ctrip.com/sight/yanqing770/230.html','http://you.ctrip.com/sight/beijing1/5174.html','http://you.ctrip.com/sight/beijing1/233.html','http://you.ctrip.com/sight/huairou120418/243.html']
        self.urls=[
#                'http://www.dianping.com/shop/18099895/review_all',
#                'http://www.dianping.com/shop/1596235/review_all',
#                "http://www.dianping.com/shop/1596313/review_all",
#               
#                
#                'http://www.dianping.com/shop/1596247/review_all',
#                'http://www.dianping.com/shop/14888419/review_all',
#                'http://www.dianping.com/shop/1596271/review_all',
#                'http://www.dianping.com/shop/2753767/review_all',
#                'http://www.dianping.com/shop/1596061/review_all',
#                'http://www.dianping.com/shop/1880545/review_all',
#                'http://www.dianping.com/shop/58866802/review_all',
#                'http://www.dianping.com/shop/56699685/review_all',
#                'http://www.dianping.com/shop/2760076/review_all',
#                'http://www.dianping.com/shop/2335780/review_all',
#                'http://www.dianping.com/shop/2396437/review_all',
#                'http://www.dianping.com/shop/1596076/review_all',
#                'http://www.dianping.com/shop/5513228/review_all',
#                'http://www.dianping.com/shop/1595869/review_all',
#                'http://www.dianping.com/shop/4292697/review_all',
#                'http://www.dianping.com/shop/1596085/review_all',
#                'http://www.dianping.com/shop/1596256/review_all',
#                'http://www.dianping.com/shop/67269808/review_all',
#                'http://www.dianping.com/shop/2688748/review_all',
#                'http://www.dianping.com/shop/1596298/review_all',
#                'http://www.dianping.com/shop/6442847/review_all',
#                'http://www.dianping.com/shop/3677188/review_all',
#                'http://www.dianping.com/shop/1596040/review_all',
#                'http://www.dianping.com/shop/24739966/review_all',
#                'http://www.dianping.com/shop/3434356/review_all',
#                'http://www.dianping.com/shop/2658808/review_all',
#                'http://www.dianping.com/shop/1596055/review_all',
#                'http://www.dianping.com/shop/18548006/review_all',
#                'http://www.dianping.com/shop/18432263/review_all',
#                
#                'http://www.dianping.com/shop/67829297/review_all',
                ##'http://www.dianping.com/shop/69304873/review_all',
#                'http://www.dianping.com/shop/123081604/review_all',
#                'http://www.dianping.com/shop/2592592/review_all',
#                'http://www.dianping.com/shop/3290719/review_all',
#                'http://www.dianping.com/shop/20947662/review_all',
#                'http://www.dianping.com/shop/66319804/review_all',
#                'http://www.dianping.com/shop/2648206/review_all',
#                'http://www.dianping.com/shop/45047391/review_all',
#                'http://www.dianping.com/shop/4112317/review_all',
#                'http://www.dianping.com/shop/2542099/review_all',
#                'http://www.dianping.com/shop/1596301/review_all',
#                'http://www.dianping.com/shop/79206670/review_all',
#                'http://www.dianping.com/shop/4283137/review_all',
#                'http://www.dianping.com/shop/65305061/review_all',
#                'http://www.dianping.com/shop/1596208/review_all',
#                'http://www.dianping.com/shop/1596217/review_all',
#                'http://www.dianping.com/shop/57165085/review_all',
#                'http://www.dianping.com/shop/2048314/review_all',
#                'http://www.dianping.com/shop/13813558/review_all',
#                'http://www.dianping.com/shop/69779087/review_all',
#                'http://www.dianping.com/shop/57732031/review_all',
#                'http://www.dianping.com/shop/1596211/review_all',
#                'http://www.dianping.com/shop/8884544/review_all',
#                'http://www.dianping.com/shop/4528167/review_all',
#                'http://www.dianping.com/shop/1596079/review_all',
#                'http://www.dianping.com/shop/1596079/review_all',
#                'http://www.dianping.com/shop/10742930/review_all',
#                'http://www.dianping.com/shop/4084528/review_all',
#                'http://www.dianping.com/shop/3070387/review_all',
               ## 'http://www.dianping.com/shop/132812621/review_all',
#                'http://www.dianping.com/shop/4734682/review_all',
#                'http://www.dianping.com/shop/76973503/review_all',
#                'http://www.dianping.com/shop/22219638/review_all',
#                'http://www.dianping.com/shop/2474395/review_all',
#                'http://www.dianping.com/shop/61440674/review_all',
#                'http://www.dianping.com/shop/1596073/review_all',
#                'http://www.dianping.com/shop/56622302/review_all',
#                'http://www.dianping.com/shop/1596088/review_all',
#                'http://www.dianping.com/shop/66612296/review_all',
#                'http://www.dianping.com/shop/3581626/review_all',
#                'http://www.dianping.com/shop/48823989/review_all',
#                'http://www.dianping.com/shop/58837946/review_all',
#                'http://www.dianping.com/shop/2576617/review_all',
#                'http://www.dianping.com/shop/1596046/review_all',
#                'http://www.dianping.com/shop/2329183/review_all',
#                'http://www.dianping.com/shop/4678067/review_all',
#                
#                'http://www.dianping.com/shop/2248099/review_all',
#                'http://www.dianping.com/shop/1596265/review_all',
#                'http://www.dianping.com/shop/2210521/review_all',
#                'http://www.dianping.com/shop/2864704/review_all',
#                'http://www.dianping.com/shop/2455783/review_all',
#                'http://www.dianping.com/shop/2709859/review_all',
#                'http://www.dianping.com/shop/1596955/review_all',
#                'http://www.dianping.com/shop/1592719/review_all',
#                'http://www.dianping.com/shop/47839907/review_all',
#                'http://www.dianping.com/shop/1595992/review_all',
#                'http://www.dianping.com/shop/1596259/review_all',
#                'http://www.dianping.com/shop/1595860/review_all',
                ##'http://www.dianping.com/shop/126291024/review_all',
#                'http://www.dianping.com/shop/58936826/review_all',
#                'http://www.dianping.com/shop/2106397/review_all',
#                'http://www.dianping.com/shop/3081007/review_all',
#                'http://www.dianping.com/shop/5661856/review_all',
#                'http://www.dianping.com/shop/2901448/review_all',
#                'http://www.dianping.com/shop/56686325/review_all',
#                'http://www.dianping.com/shop/2253211/review_all',
#                'http://www.dianping.com/shop/4285456/review_all',
#                'http://www.dianping.com/shop/2614315/review_all',
#                'http://www.dianping.com/shop/2542318/review_all',
                ##'http://www.dianping.com/shop/9588163/review_all',
#                'http://www.dianping.com/shop/4677505/review_all',
#                'http://www.dianping.com/shop/5669216/review_all',
#                'http://www.dianping.com/shop/1596268/review_all',
#                'http://www.dianping.com/shop/5642190/review_all',
#                'http://www.dianping.com/shop/83461384/review_all',
#                'http://www.dianping.com/shop/19601729/review_all',
#                'http://www.dianping.com/shop/15298433/review_all',
                
                
#                'http://www.dianping.com/shop/1705777/review_all',
#                'http://www.dianping.com/shop/2294980/review_all',
#                'http://www.dianping.com/shop/6105063/review_all',
#                'http://www.dianping.com/shop/1705768/review_all',
#                'http://www.dianping.com/shop/1705747/review_all',
#                'http://www.dianping.com/shop/4698755/review_all',
#                'http://www.dianping.com/shop/1705546/review_all',
#                'http://www.dianping.com/shop/58565973/review_all',
#                'http://www.dianping.com/shop/2456362/review_all',
#                'http://www.dianping.com/shop/4509472/review_all',
#                'http://www.dianping.com/shop/58858730/review_all',
#                'http://www.dianping.com/shop/5191653/review_all',
#                'http://www.dianping.com/shop/5530878/review_all',
#                'http://www.dianping.com/shop/10786999/review_all',
#                'http://www.dianping.com/shop/2107627/review_all',
#                'http://www.dianping.com/shop/1705540/review_all',
#                'http://www.dianping.com/shop/58927969/review_all',
#                'http://www.dianping.com/shop/1705735/review_all',
#                'http://www.dianping.com/shop/23989186/review_all',
#                'http://www.dianping.com/shop/23575117/review_all',
#                'http://www.dianping.com/shop/57163400/review_all',
#                'http://www.dianping.com/shop/18127665/review_all',
#                'http://www.dianping.com/shop/2256268/review_all',
#                'http://www.dianping.com/shop/5195148/review_all',
#                'http://www.dianping.com/shop/1705465/review_all',
#                'http://www.dianping.com/shop/1706500/review_all',
#                'http://www.dianping.com/shop/5285479/review_all',
#                
#                'http://www.dianping.com/shop/1753672/review_all',
#                'http://www.dianping.com/shop/1753657/review_all',
#                'http://www.dianping.com/shop/59165671/review_all',
#                'http://www.dianping.com/shop/1753576/review_all',
#                'http://www.dianping.com/shop/49001680/review_all',
#                'http://www.dianping.com/shop/92469579/review_all',
#                'http://www.dianping.com/shop/5389604/review_all',
#                'http://www.dianping.com/shop/23395995/review_all',
#                'http://www.dianping.com/shop/9965576/review_all',
#                'http://www.dianping.com/shop/17992099/review_all',
                ##'http://www.dianping.com/shop/79516893/review_all',
                #'http://www.dianping.com/shop/1753594/review_all',
              
#                
#                'http://www.dianping.com/shop/13686065/review_all',
#                'http://www.dianping.com/shop/5663025/review_all',
#                'http://www.dianping.com/shop/1989808/review_all',
#                'http://www.dianping.com/shop/3014395/review_all',
#                'http://www.dianping.com/shop/50518219/review_all',
#                'http://www.dianping.com/shop/1989790/review_all',
#                'http://www.dianping.com/shop/1989736/review_all',
#                'http://www.dianping.com/shop/1989826/review_all',
#                'http://www.dianping.com/shop/23646240/review_all',
#                'http://www.dianping.com/shop/2621623/review_all',
#                'http://www.dianping.com/shop/4088203/review_all',
#                'http://www.dianping.com/shop/3998404/review_all',
#                'http://www.dianping.com/shop/5663178/review_all',
#                'http://www.dianping.com/shop/5597488/review_all',
                #'http://www.dianping.com/shop/4721724/review_all',
#                'http://www.dianping.com/shop/5662351/review_all',
#                'http://www.dianping.com/shop/5108250/review_all',
#                'http://www.dianping.com/shop/1989814/review_all',
#                'http://www.dianping.com/shop/4088203/review_all',
#                'http://www.dianping.com/shop/22420640/review_all',
#                
#                'http://www.dianping.com/shop/67723384/review_all',
#                'http://www.dianping.com/shop/2974006/review_all',
#                'http://www.dianping.com/shop/76267904/review_all',
#                'http://www.dianping.com/shop/2972959/review_all',
#                'http://www.dianping.com/shop/21570780/review_all',
#                'http://www.dianping.com/shop/5304249/review_all',
#                'http://www.dianping.com/shop/58565054/review_all',
#                'http://www.dianping.com/shop/5279114/review_all',
#                'http://www.dianping.com/shop/9313258/review_all',
#                
#                'http://www.dianping.com/shop/1581970/review_all',
#                'http://www.dianping.com/shop/1581907/review_all',
#                'http://www.dianping.com/shop/1581526/review_all',
#                'http://www.dianping.com/shop/37771701/review_all',
#                'http://www.dianping.com/shop/14168639/review_all',
#                'http://www.dianping.com/shop/10286000/review_all',
#                'http://www.dianping.com/shop/1581961/review_all',
#                'http://www.dianping.com/shop/57731997/review_all',
#                'http://www.dianping.com/shop/9313635/review_all',
#                'http://www.dianping.com/shop/77261447/review_all',
#                'http://www.dianping.com/shop/58566481/review_all',
#                'http://www.dianping.com/shop/1581994/review_all',
#                'http://www.dianping.com/shop/6068624/review_all',
#                'http://www.dianping.com/shop/3430027/review_all',
#                'http://www.dianping.com/shop/5721148/review_all',
#                'http://www.dianping.com/shop/1582297/review_all',
#                'http://www.dianping.com/shop/1581439/review_all',
#                'http://www.dianping.com/shop/16401068/review_all',
#                'http://www.dianping.com/shop/1581550/review_all',
                
#                'http://www.dianping.com/shop/17937302/review_all',
#                'http://www.dianping.com/shop/2401852/review_all',
#                'http://www.dianping.com/shop/13893919/review_all',
#                'http://www.dianping.com/shop/58819852/review_all',
#                'http://www.dianping.com/shop/80272244/review_all',
                
                ##汕头
#                'http://www.dianping.com/shop/2821510/review_all',
#                'http://www.dianping.com/shop/57397080/review_all',
#                'http://www.dianping.com/shop/19816671/review_all',
#                'http://www.dianping.com/shop/21920723/review_all',
#                'http://www.dianping.com/shop/2957539/review_all',
#                'http://www.dianping.com/shop/4017838/review_all',
#                'http://www.dianping.com/shop/58804501/review_all',
#                ###韶关
#                'http://www.dianping.com/shop/1925944/review_all',
#                'http://www.dianping.com/shop/2473711/review_all',
#                'http://www.dianping.com/shop/19587986/review_all',
#                'http://www.dianping.com/shop/16217837/review_all',
#                'http://www.dianping.com/shop/36066062/review_all',
#                'http://www.dianping.com/shop/3287869/review_all',
#                'http://www.dianping.com/shop/9316559/review_all',
#                'http://www.dianping.com/shop/3261919/review_all',
#                'http://www.dianping.com/shop/3183502/review_all',
#                'http://www.dianping.com/shop/5659837/review_all',
#                'http://www.dianping.com/shop/3287890/review_all',
#                'http://www.dianping.com/shop/57415605/review_all',
#                'http://www.dianping.com/shop/3289474/review_all',
#                'http://www.dianping.com/shop/32381013/review_all',
#                ##河源
#                'http://www.dianping.com/shop/21078665/review_all',
#                'http://www.dianping.com/shop/19589015/review_all',
#                'http://www.dianping.com/shop/9314234/review_all',
#                'http://www.dianping.com/shop/2787181/review_all',
#                'http://www.dianping.com/shop/3715228/review_all',
#                'http://www.dianping.com/shop/9314237/review_all',
#                'http://www.dianping.com/shop/13756540/review_all',
#                'http://www.dianping.com/shop/5583360/review_all',
#                ##梅州
#                'http://www.dianping.com/shop/9315592/review_all',
#                'http://www.dianping.com/shop/2393209/review_all',
#                'http://www.dianping.com/shop/32603636/review_all',
#                'http://www.dianping.com/shop/16392790/review_all',
#                'http://www.dianping.com/shop/5464686/review_all',
#                'http://www.dianping.com/shop/2393188/review_all',
#                'http://www.dianping.com/shop/69924434/review_all',
#                'http://www.dianping.com/shop/4542973/review_all',
#                'http://www.dianping.com/shop/2950750/review_all',
#                'http://www.dianping.com/shop/67835356/review_all',
                ##'http://www.dianping.com/shop/15857531/review_all',
#                'http://www.dianping.com/shop/68243007/review_all',
#                'http://www.dianping.com/shop/22155020/review_all',
#                
#                #惠州
#                'http://www.dianping.com/shop/2684230/review_all',
#                'http://www.dianping.com/shop/2392513/review_all',
#                'http://www.dianping.com/shop/58846470/review_all',
#                'http://www.dianping.com/shop/58923058/review_all',
#                'http://www.dianping.com/shop/3181876/review_all',
#                'http://www.dianping.com/shop/92150748/review_all',
#                'http://www.dianping.com/shop/92150748/review_all',
#                'http://www.dianping.com/shop/5532208/review_all',
#                'http://www.dianping.com/shop/4714316/review_all',
#                'http://www.dianping.com/shop/50547490/review_all',
#                'http://www.dianping.com/shop/17205734/review_all',
#                'http://www.dianping.com/shop/50614756/review_all',
#                'http://www.dianping.com/shop/3127642/review_all',
#                'http://www.dianping.com/shop/5192711/review_all',
#                'http://www.dianping.com/shop/12368397/review_all',
#                'http://www.dianping.com/shop/66029730/review_all',
#                'http://www.dianping.com/shop/10338152/review_all',
                
                #汕尾
#                'http://www.dianping.com/shop/5650884/review_all',
#                'http://www.dianping.com/shop/67517287/review_all',
#                'http://www.dianping.com/shop/5504340/review_all',
#                'http://www.dianping.com/shop/48281530/review_all',
#                'http://www.dianping.com/shop/15590883/review_all',
#                'http://www.dianping.com/shop/24332073/review_all',
#                'http://www.dianping.com/shop/36104258/review_all',
#                
#                #中山
#                'http://www.dianping.com/shop/2713882/review_all',
#                'http://www.dianping.com/shop/72476720/review_all',
#                'http://www.dianping.com/shop/5208194/review_all',
#                'http://www.dianping.com/shop/14180416/review_all',
                ##'http://www.dianping.com/shop/59424444/review_all',
                #江门
#                'http://www.dianping.com/shop/56683862/review_all',
#                'http://www.dianping.com/shop/20776623/review_all',
#                'http://www.dianping.com/shop/57732121/review_all',
#                'http://www.dianping.com/shop/9314826/review_all',
#                'http://www.dianping.com/shop/2453629/review_all',
#                'http://www.dianping.com/shop/18064254/review_all',
#                'http://www.dianping.com/shop/16500110/review_all',
#                'http://www.dianping.com/shop/2626717/review_all',
#                'http://www.dianping.com/shop/2625916/review_all',
#                'http://www.dianping.com/shop/14983186/review_all',
#                
#                #阳江
#                'http://www.dianping.com/shop/18251698/review_all',
#                'http://www.dianping.com/shop/57732360/review_all',
#                'http://www.dianping.com/shop/5172132/review_all',
#                'http://www.dianping.com/shop/4103396/review_all',
#                'http://www.dianping.com/shop/4498967/review_all',
#                'http://www.dianping.com/shop/56670967/review_all',
#                'http://www.dianping.com/shop/58856742/review_all',
#                'http://www.dianping.com/shop/4724287/review_all',
#                'http://www.dianping.com/shop/3344890/review_all',
#                
#                #湛江
#                'http://www.dianping.com/shop/2403454/review_all',
#                'http://www.dianping.com/shop/9318062/review_all',
#                'http://www.dianping.com/shop/97560324/review_all',
#                'http://www.dianping.com/shop/58093801/review_all',
#                'http://www.dianping.com/shop/13621696/review_all',
#                'http://www.dianping.com/shop/73606726/review_all',
#                'http://www.dianping.com/shop/13428912/review_all',
#                'http://www.dianping.com/shop/3122704/review_all',
#                'http://www.dianping.com/shop/19657947/review_all',
#                
#                #茂名
#                'http://www.dianping.com/shop/4291439/review_all',
#                'http://www.dianping.com/shop/4170801/review_all',
#                'http://www.dianping.com/shop/15914642/review_all',
#                'http://www.dianping.com/shop/23202428/review_all',
#                'http://www.dianping.com/shop/58580988/review_all',
#                'http://www.dianping.com/shop/9032859/review_all',
#                'http://www.dianping.com/shop/13426370/review_all',
#                
#                #肇庆
#                'http://www.dianping.com/shop/2475775/review_all',
#                'http://www.dianping.com/shop/14137807/review_all',
#                'http://www.dianping.com/shop/22959396/review_all',
#                'http://www.dianping.com/shop/23654451/review_all',
#                'http://www.dianping.com/shop/21022704/review_all',
#                'http://www.dianping.com/shop/21022704/review_all',
#                'http://www.dianping.com/shop/2094361/review_all',
#                'http://www.dianping.com/shop/5366562/review_all',
                
#                #清远
#                'http://www.dianping.com/shop/2792674/review_all',
#                'http://www.dianping.com/shop/23184237/review_all',
#                'http://www.dianping.com/shop/3269440/review_all',
#                'http://www.dianping.com/shop/9316140/review_all',
#                'http://www.dianping.com/shop/58564955/review_all',
#                'http://www.dianping.com/shop/9324911/review_all',
#                'http://www.dianping.com/shop/16112596/review_all',
#                'http://www.dianping.com/shop/23176383/review_all',
#                'http://www.dianping.com/shop/20725069/review_all',
#                'http://www.dianping.com/shop/56607994/review_all',
#                'http://www.dianping.com/shop/110559318/review_all',
#                'http://www.dianping.com/shop/5275740/review_all',
#                'http://www.dianping.com/shop/56817678/review_all',
#                'http://www.dianping.com/shop/16944948/review_all',
#                'http://www.dianping.com/shop/9316161/review_all',
#                'http://www.dianping.com/shop/16944741/review_all',
#                'http://www.dianping.com/shop/63262891/review_all',
#                'http://www.dianping.com/shop/22248184/review_all',
                
                #揭阳
                'http://www.dianping.com/shop/4107736/review_all',
                'http://www.dianping.com/shop/22319728/review_all',
                'http://www.dianping.com/shop/20631115/review_all',
                'http://www.dianping.com/shop/5325742/review_all',
                'http://www.dianping.com/shop/66800296/review_all',
                'http://www.dianping.com/shop/66804534/review_all',
                'http://www.dianping.com/shop/92991388/review_all',
                #云浮
                'http://www.dianping.com/shop/16391857/review_all',
                'http://www.dianping.com/shop/56595710/review_all',
                'http://www.dianping.com/shop/9039440/review_all',
                'http://www.dianping.com/shop/14707630/review_all',
                'http://www.dianping.com/shop/15987406/review_all',
               
      




        ]
        # 打开携程首页
    def start(self):
        for url1 in self.urls:
            print(url1)
            self.driver.get(url1)
            # 将界面最大化
            #self.driver.maximize_window()
            self.driver.implicitly_wait(30)
            self.crawlxiecheng()




    def crawlxiecheng(self):
        # 单页循环次数
        loopNum = 0

        ifHandle = False
        
        #获取总页面数
        time.sleep(30)
        self.driver.find_element_by_partial_link_text("推荐排序").click()
        self.driver.find_element_by_partial_link_text("最新点评").click()
        css_link = self.get_css_link(url = self.driver.page_source)
        font_dict = self.get_font_dict(css_link1 = css_link)
        print(font_dict)
        
        pageNum = 2800
        while(pageNum>=1):
            # 循环次数加1
            loopNum = loopNum + 1
            #if (len(re.findall('pkg_page',self.driver.page_source)) == 0):
              #  break

            target = self.driver.find_element_by_class_name(
                'NextPage')
            y = target.location['y']
            # print y
            y = y - 100
            print(y)

            js = "var q=document.documentElement.scrollTop=" + str(y)
            self.driver.execute_script(js)

            time.sleep(5)
         
            if u"下一页" in self.driver.page_source:

                if ifHandle == False:
                    doc = self.get_conment_page(page_source = self.driver.page_source,font_dict = font_dict)
                    a = self.crawllianjie(doc)
                    if(a ==2):
                        break
                    ifHandle = True

                try:
                    #print u"下一页" in self.driver.page_source
                    if u"下一页" in self.driver.page_source:
                        pageNum = pageNum - 1
                        #self.driver.maximize_window()
                        #self.driver.implicitly_wait(30)
                        self.driver.find_element_by_partial_link_text("下一页").click()
                        #self.driver.find_element_by_xpath("//div[@class='weiboitem active']/div[@class='comment_ctrip']/div[@class='ttd_pager cf']/div[@class='pager_v1']/a[@class='nextpage']").click()
                        ifHandle = False
                        loopNum = 0

                        time.sleep(3)
                        print ("页数：" + str(pageNum))
                        #print 'num =' + num, type(int(num))
                        num1 = 2800 - pageNum + 1
                        print ('num1 = ' + str(num1))


                except:
                    pageNum = pageNum + 1




        return False if pageNum > 1 else True

    def crawllianjie(self, doc):
        #print page_sourse
        #response1 = HtmlResponse(url="my HTML string", body=page_sourse, encoding="utf-8")
        city = doc.xpath("//div[@class='list-crumb']/a[1]/text()")[0]
        city = city.split('周')[0]
        
        
        for li in doc.xpath('//*[@class="reviews-items"]/ul/li'):
            if li.xpath('.//a[@class="name"]/text()'):
                name = li.xpath('.//a[@class="name"]/text()')[0].strip('\n\r \t')
            else:
                name = li.xpath('.//span[@class="name"]/text()')[0].strip('\n\r \t')
    
            time1 = li.xpath('div/div[@class="misc-info clearfix"]/span[1]/text()')[0]
            time1 = time1.strip()
            jingqu = li.xpath('div/div[@class="misc-info clearfix"]/span[2]/text()')[0]
            jingqu = jingqu.strip()
            ID = li.xpath('div/div[@class="misc-info clearfix"]/span[3]/a[1]/@data-id')[0]
            comment = ''.join(li.xpath('.//div[@class="review-words Hide"]/text()')).strip('\n\r \t')
            if not comment:
                comment = ''.join(li.xpath('.//div[@class="review-words"]/text()')).strip('\n\r \t')
            #print(name,time1,jingqu,ID,comment)
            #print(time1)
            #time1 = time1.split()[0]
            #print(time1)
            if(re.findall('更新于',time1)):
                time1 = time1.split('更新于')[1]
            else:
                time1 = time1
            print(time1,city,comment)
        
        
        #A = response1.xpath("//div[@class='reviews-items']/ul/li")
        #print A
            cursor = connect.cursor()

        # 获取每个酒店的链接
        
            
            if(time1 < '2019-01-01'):
                return(2)
                continue

            sql = "INSERT IGNORE INTO 19_dazhong_2(name, time, jingqu, ID, comment,city) VALUES ( '%s', '%s', '%s', '%s', '%s','%s'  )"
            data = (name,time1,jingqu,ID,comment,city)
            try:
                cursor.execute(sql % data)
            except:
                print(ID)

            connect.commit()

          
        #xiechengService.saveListPageInfo()

        print(len(self.listPageInfo))
        self.listPageInfo = []





    #def saveListPageInfo(self):
      #  self.xiechengDao.savehotellink(self.listPageInfo)

    def depose(self):
        self.driver.close()
        
    def get_css_link(self,url):
        try:
            
            
            html = url
            css_link = re.search(r'<link re.*?css.*?href="(.*?svgtextcss.*?)">', html)
            #print(css_link)
            assert css_link
            css_link = 'http:' + css_link[1]
            return css_link
        except:
            None 
            
    def get_font_dict(self,css_link1):
        res = requests.get(css_link1, headers=_css_headers)
            
        html = res.text
        #print(html)
        
        svg_url = re.findall('background-image: url\((.*?)\);background-repeat: no-repeat;', html)
        #print("svg_url",svg_url)
        svg_url = svg_url[0]
        #print ("svg_url",svg_url)
        if svg_url.startswith('//'):
            svg_url = 'http:' + svg_url
            
        #background_image_link = re.search(r'background-image:.*?\((.*?svg)\)', html)
        #assert background_image_link
        #background_image_link = 'http:' + background_image_link[1]
        background_image_link = svg_url
        print('----------' * 40)
        print(background_image_link)
        print('---------------' * 40)
        html = re.sub(r'span.*?\}', '', html)
        group_offset_list = re.findall(r'\.([a-zA-Z0-9]{5,6}).*?round:(.*?)px (.*?)px;', html)
        font_dict_by_offset = self.get_font_dict_by_offset(background_image_link)
        font_dict = {}
        for class_name, x_offset, y_offset in group_offset_list:
            x_offset = x_offset.replace('.0', '')
            y_offset = y_offset.replace('.0', '')
    
    
            try:
                font_dict[class_name] = font_dict_by_offset[int(y_offset)][int(x_offset)]
    
            except:
                font_dict[class_name] = ''
        return font_dict
    
    def get_font_dict_by_offset(self,url):
        res = requests.get(url, headers=_css_headers)
        html = res.text
        font_dict = {}
        y_list = re.findall(r'd="M0 (\d+?) ', html)
        if y_list:
            font_list = re.findall(r'<textPath .*?>(.*?)<', html)
            for i, string in enumerate(font_list):
                y_offset = start_y - int(y_list[i])
                sub_font_dict = {}
                for j, font in enumerate(string):
                    x_offset = -j * font_size
                    sub_font_dict[x_offset] = font
    
                font_dict[y_offset] = sub_font_dict
    
        else:
            font_list = re.findall(r'<text.*?y="(.*?)">(.*?)<', html)
    
            for y, string in font_list:
                y_offset = start_y - int(y)
                sub_font_dict = {}
                for j, font in enumerate(string):
                    x_offset = -j * font_size
                    sub_font_dict[x_offset] = font
    
                font_dict[y_offset] = sub_font_dict
        #print(font_dict)
        return font_dict
    
    def get_conment_page(self,page_source,font_dict):
        html = page_source
        
        class_set = set()
        for span in re.findall(r'<svgmtsi class="([a-zA-Z0-9]{5,6})"></svgmtsi>', html):
            class_set.add(span)
        for class_name in class_set:
            try:
                html = re.sub('<svgmtsi class="%s"></svgmtsi>' % class_name, font_dict[class_name], html)
    
            except:
                html = re.sub('<svgmtsi class="%s"></svgmtsi>' % class_name, '', html)
        doc = etree.HTML(str(html))
        return doc


if __name__=="__main__":
    xiechengService = XiechengDriverService()
    xiechengService.start()

    xiechengService.depose()
    
    





