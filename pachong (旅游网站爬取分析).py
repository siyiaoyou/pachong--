import urllib.request #导入urllib.request包
import requests #导入requests包.此包是用Python语言编写,基于urllib,采用Apache2 Licensed开源协议的HTTP库.它比 urllib 更加方便,可以节约我们大量的工作.
from bs4 import BeautifulSoup
import xlwt #导入Excel包
mingc=[]#建立存储网站名称的空列表
paim=[]#建立存储网站周排名的空列表
defen=[]#建立存储网站得分的空列表
zhqt=[]#建立存储网站周排名以及与其同节点数据的空列表
jies=[]#建立存储网站介绍的空列表

r=requests.get('http://top.chinaz.com/hangye/index_jiaotonglvyou_lvyou.html')#获取网站（'http://top.chinaz.com/hangye/index_jiaotonglvyou_lvyou.html'）的源代码到r
if r.status_code==200: #确保读取源代码正常
    r.encoding = 'utf-8'#将文本编码格式定为utf-8 ，便于读取
    html=r.text #将代码改为text格式存入html
    soup = BeautifulSoup(html,"html.parser")#将html用BeautifulSoup转化后存入soup
    #从文档中找到所有<h3,class_="rightTxtHead">标签（网站名称）的链接: 
    for link in soup.find_all('h3',class_="rightTxtHead"):
        mingc.append(link.get_text())#向对应列表中添加网站名称
    #从文档中找到所有<p,class_="RtCData">标签（网站周排名以及与其同节点数据）的链接:    
    for link in soup.find_all('p',class_="RtCData"):
        zhqt.append(link.get_text())#向对应列表中添加网站周排名以及与其同节点数据
    #从文档中找到所有<div,class_="RtCRateCent">标签（网站得分）的链接:    
    for link in soup.find_all('div',class_="RtCRateCent"):
        defen.append(link.get_text()[5:])#向对应列表中添加网站得分
    #从文档中找到所有<p,class_="RtCInfo">标签（网站介绍）的链接:    
    for link in soup.find_all('p',class_="RtCInfo"):
        jies.append(link.get_text()[5:])#向对应列表中添加网站介绍
 
i=0#确保列表内容从0开始转换
while i<30:#确保转换的列表内容不为空
    j=i*4
    paim.append(zhqt[j][9:])#清除与周排名相同节点的无用数据,向周排名列表中添加周排名
    i=i+1#确保列表内序号依次增加
 
i=0#确保列表内容从0开始打印
while i<30:#确保打印列表内容不为空
    print()#打印换行
    print(i+1)#打印网站序号
    print(mingc[i])#打印网站名称
    print("  周排名："+paim[i])#打印网站周排名
    print("  网站得分："+defen[i])#打印网站得分
    print("  网站介绍："+jies[i])#打印网站介绍
    i=i+1#确保列表内序号依次增加
    
excelTabel= xlwt.Workbook()#创建excel对象
sheet1=excelTabel.add_sheet('wangzhang',cell_overwrite_ok=True)#在创建的Excel表格中创建名为'wangzhang'的工作空间
sheet1.write(0,0,'网站名称')#向Excel表格A1框中输入标题“网站名称”
sheet1.write(0,1,'周排名')#向Excel表格B1框中输入标题“周排名”
sheet1.write(0,2,'网站得分')#向Excel表格C1框中输入标题“网站得分”
sheet1.write(0,3,'网站介绍')#向Excel表格D1框中输入标题“网站介绍”

i=0#确保列表内容从0开始输入表格
t=1#确保Excel表格中框从第二行开始
while t<31: #确保输入Excel表格框中的列表内容不为空
    sheet1.write(t,0,mingc[i])#向Excel表格与A1同列的框中依次输入各网站名称
    sheet1.write(t,1,paim[i])#向Excel表格与B1同列的框中依次输入各网站周排名
    sheet1.write(t,2,defen[i])#向Excel表格与C1同列的框中依次输入各网站得分
    sheet1.write(t,3,jies[i])#向Excel表格与D1同列的框中依次输入各网站介绍
    i=i+1#确保列表内序号依次增加
    t=t+1#跳转Excel表行数
excelTabel.save('wangzhang.xlsx')#保存名为'wangzhang.xlsx'的Excel表格
