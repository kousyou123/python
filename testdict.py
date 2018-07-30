d={"姓名":"向翔","性别":"男"}
print(d)
print(d.get("姓名"))#取值
d["姓名"]="Kevin"#修改值
print(d)
d["age"]=31#增加值
print(d)
d.pop("性别")#删除值 del(d["性别"])
print(d)
d1={"姓名":"Python","birthday":"1987"}
d.update(d1)#字典拼接
print(d)
for x in d.keys():#所有键值
    print(x)
for y in d.values():#所有值
    print(y)
for a,b in d.items():#所有键值对
    print(a,b)
#字典推导
DIAL_CODES = [ (86, 'China'),(91, 'India'),(1, 'United States'),(62, 'Indonesia'),(55, 'Brazil'),(92, 'Pakistan'),(880, 'Bangladesh'),(234, 'Nigeria'),(7, 'Russia'),(81, 'Japan'),]
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)