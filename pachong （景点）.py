import urllib.request #导入urllib.request包
import requests #导入requests包.此包是用Python语言编写,基于urllib,采用Apache2 Licensed开源协议的HTTP库.它比 urllib 更加方便,可以节约我们大量的工作.
from bs4 import BeautifulSoup
import xlwt #导入Excel包
 
mingc=[]#建立存储景点名称的空列表
jis=[]#建立存储景点级数的空列表
red=[]#建立存储景点热度的空列表
jiag=[]#建立存储景点价格的空列表
yuexl=[]#建立存储景点月销量的空列表
diz=[]#建立存储景点地址的空列表
ted=[]#建立存储景点特点的空列表

r=requests.get('http://piao.qunar.com/ticket/list.htm?keyword=%E5%BF%85%E6%B8%B8%E6%99%AF%E7%82%B9&region=%E7%A7%A6%E7%9A%87%E5%B2%9B&from=mpshouye_hotdest_theme')#获取网站（‘http://piao.qunar.com/ticket/list.htm?keyword=%E5%BF%85%E6%B8%B8%E6%99%AF%E7%82%B9&region=%E7%A7%A6%E7%9A%87%E5%B2%9B&from=mpshouye_hotdest_theme'）的源代码到r
if r.status_code==200: #确保读取源代码正常
    r.encoding = 'utf-8'#将文本编码格式定为utf-8 ，便于读取
    html=r.text #将代码改为text格式存入html
    soup = BeautifulSoup(html,"html.parser")#将html用BeautifulSoup转化后存入soup

    #print(soup.prettify())

    #从文档中找到所有<a>标签的链接:
    #for link in soup.find_all('a'):
        #print(link.get('href'))#print(link['href'])#节点属性
        #print(link.name)#节点名字
        #print(link.get_text())#节点文字
    
    #从文档中找到所有<h3,class_="sight_item_caption">标签（景点名称）的链接:
    for link in soup.find_all('h3',class_="sight_item_caption"):
        mingc.append(link.get_text())#向对应列表中添加景点名称
    #从文档中找到所有<span,class_="level">标签（景点级数）的链接:    
    for link in soup.find_all('span',class_="level"):
        jis.append(link.get_text())#向对应列表中添加景点级数
    #从文档中找到所有<span,class_="product_star_level">标签（景点热度）的链接:    
    for link in soup.find_all('span',class_="product_star_level"):
        red.append(link.get_text()[2:])#向对应列表中添加景点热度
    #从文档中找到所有<span,class_="sight_item_price">标签（景点价格）的链接:    
    for link in soup.find_all('span',class_="sight_item_price"):
        jiag.append(link.get_text()[1:-2])#向对应列表中添加景点价格
    #从文档中找到所有<span,class_="hot_num">标签（景点月销量）的链接:
    for link in soup.find_all('span',class_="hot_num"):
        yuexl.append(link.get_text())#向对应列表中添加景点月销量
    #从文档中找到所有<p,class_="address color999">标签（景点地址）的链接:    
    for link in soup.find_all('p',class_="address color999"):
        diz.append(link.get_text()[3:-2])#向对应列表中添加景点地址
    #从文档中找到所有<div,class_="intro color999">标签（景点特点）的链接:
    for link in soup.find_all('div',class_="intro color999"):
        ted.append(link.get_text())#向对应列表中添加景点特点

i=0#确保列表内容从0开始打印
while i<10: #确保打印列表内容不为空
    print()#打印换行
    print(i+1)#打印景点序号
    print(mingc[i])#打印景点名称
    if i<5: #确保打印列表内容不为空
        print("  "+jis[i])#打印景点级数
    print("  热度："+red[i])#打印景点热度
    if i<9: #确保打印列表内容不为空
        print("  价格："+jiag[i])#打印景点价格
        print("  月销量："+yuexl[i])#打印景点月销量
    print("  地址："+diz[i]+"\n  特点："+ted[i])#打印景点地址和景点特点
    i=i+1#确保列表内序号依次增加
    
excelTabel= xlwt.Workbook()#创建excel对象
sheet1=excelTabel.add_sheet('jingdian',cell_overwrite_ok=True)#在创建的Excel表格中创建名为'jingdian'的工作空间
sheet1.write(0,0,'景点名')#向Excel表格A1框中输入标题“景点名”
sheet1.write(0,1,'景点热度')#向Excel表格B1框中输入标题“景点热度”
sheet1.write(0,2,'景点价格')#向Excel表格C1框中输入标题“景点价格”
sheet1.write(0,3,'景点月销量')#向Excel表格D1框中输入标题“景点月销量”
sheet1.write(0,4,'景点地址')#向Excel表格E1框中输入标题“景点地址”
sheet1.write(0,5,'景点特点')#向Excel表格F1框中输入标题“景点特点”

i=0#确保列表内容从0开始输入表格
t=1#确保Excel表格中框从第二行开始
while t<11: #确保输入Excel表格框中的列表内容不为空
    sheet1.write(t,0,mingc[i])#向Excel表格与A1同列的框中依次输入各景点名称
    sheet1.write(t,1,red[i])#向Excel表格与B1同列的框中依次输入各景点热度
    if t<10: #确保输入Excel表格框中的列表内容不为空
        sheet1.write(t,2,jiag[i])#向Excel表格与C1同列的框中依次输入各景点价格
        sheet1.write(t,3,yuexl[i])#向Excel表格与D1同列的框中依次输入各景点月销量
    sheet1.write(t,4,diz[i])#向Excel表格与E1同列的框中依次输入各景点地址
    sheet1.write(t,5,ted[i])#向Excel表格与F1同列的框中依次输入各景点特点
    i=i+1#确保列表内序号依次增加
    t=t+1#跳转Excel表行数
excelTabel.save('jingdian.xlsx')#保存名为'jingdian.xlsx'的Excel表格

