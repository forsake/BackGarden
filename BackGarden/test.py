# -* - coding: UTF-8 -* -  

import configparser

conf = configparser.ConfigParser()
conf.read("test.conf")

# 获取指定的section， 指定的option的值
name = conf.get("section1", "name")
print(name)
age = conf.get("section1", "age")
print(age)

#获取所有的section
sections = conf.sections()
print(sections)

#写配置文件

# 更新指定section, option的值
conf.set("section2", "port", "8081")

# 写入指定section, 增加新option的值
conf.set("section2", "IEPort", "80")

# 添加新的 section
conf.add_section("new_section12")
conf.set("new_section12", "new_option12", "http://www.liyuan.me")

# 写回配置文件
conf.write(open("test.conf","w"))
