from datetime import date
import time
import datetime

myBirthday = date(1985,2,2)
gBirthday = date(2014,3,22)
nBirthday = date(2014,1,31)
today = date.today()

life = today - myBirthday
gAge = gBirthday - today
nAge = nBirthday - today

print('岁数计算器')
print('周岁  28岁  周岁算法：每过一个生日就长一岁。')
print('虚岁  29岁  虚岁算法：一出生就是一岁，然后，每过一个春节就长一岁。')
print('生肖  牛')
print('星座  白羊座')
print('公历出生日期：1985年03月22日')
print('农历生日日期：1985年二月初二 （乙丑年 己卯月 庚申日）')
print('你已经在这个世界上蹦跶了：%s天' % life.days)
print('距离29周岁2014年03月22日还有%d天分秒' , gAge.days)
print('距离30虚岁2014年一月三十一日还有天' , nAge.days)
print('')

