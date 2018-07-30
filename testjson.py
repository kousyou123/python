
# sort_keys=True 对（键）字母进行排序；
# indent 行缩进几个字节；
# separators=(',', ':') 对字典以指定的符号进行分隔；
# ensure_ascii=False 显示中文。
# Skipkeys：默认值是False，
# 如果dict的keys内的数据不是python的基本类型(str,unicode,int,long,float,bool,None)，设置为False时，
# 就会报TypeError的错误。此时设置成True，则会跳过这类key 。

# ensure_ascii:，当它为True的时候，所有非ASCII码字符显示为\uXXXX序列，
# 只需在dump时将ensure_ascii设置为False即可，此时存入json的中文即可正常显示。) 

# indent：应该是一个非负的整型，如果是0就是顶格分行显示，如果为空就是一行最紧凑显示，
# 否则会换行且按照indent的数值显示前面的空白分行显示，这样打印出来的json数据也叫pretty-printed json 

# separators：分隔符，实际上是(item_separator, dict_separator)的一个元组，默认的就是(‘,’,’:’)；
# 这表示dictionary内keys之间用“,”隔开，而KEY和value之间用“：”隔开。 

# sort_keys：将数据根据keys的值进行排序。 
import  json  
data = {'username':['李雷', '韩梅梅'], 'idenu':'student', 'age':14}
json_dic2 = json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
print(json_dic2)

