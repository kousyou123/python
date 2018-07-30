import configparser
config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9',
                     'ForwardX11':'yes'
                     }
config['bitbucket.org'] = {'User':'hg'}
config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}
with open('example.ini', 'w') as configfile:
    config.write(configfile)

config = configparser.ConfigParser()
#---------------------------查找文件内容,基于字典的形式
print(config.sections())        #  显示[] ，默认，因这个时候还不知道要读取哪个配置文件的内容
config.read('example.ini')      #  读取前面创建好的那个配置文件示例内容
print(config.sections())        #  这回显示出['bitbucket.org', 'topsecret.server.com']
print('bytebong.com' in config) #  判断有无此参数在配置文件中 False
print('bitbucket.org' in config) # 判断有无此参数在配置文件中 True
print(config['bitbucket.org']["user"])  # 类似字典通过key找值 hg
print(config['DEFAULT']['Compression']) # yes
print(config['topsecret.server.com']['ForwardX11'])  # no
print(config['bitbucket.org'])          # 查看对象 <Section: bitbucket.org>

for key in config['bitbucket.org']:     # 注意,有default会默认default的键
    print(key)
# user
# compressionlevel
# serveraliveinterval
# forwardx11
# compression

print(config.options('bitbucket.org'))  # 同for循环,找到'bitbucket.org'下所有键
print(config.items('bitbucket.org'))    # 找到'bitbucket.org'下所有键值对
# [('compressionlevel', '9'), ('serveraliveinterval', '45'), ('forwardx11', 'yes'), ('compression', 'yes'), ('user', 'hg')]
print(config.get('bitbucket.org','compression')) # yes       get方法Section下的key对应的value


config = configparser.ConfigParser()
config.read('example.ini')
config.add_section('yuan')
# 注，此时还只是在内存中读取出配置文件内容，
# 并在内存中添加了，还需执行最下方的写入句柄操作才能生效，下面的操作同理
config.remove_section('bitbucket.org')
config.remove_option('topsecret.server.com', "forwardx11")
# remove 移除
config.set('topsecret.server.com', 'k1', '11111')
config.set('yuan', 'k2', '22222')
# set 增加或修改
config.write(open('example.ini', "w"))