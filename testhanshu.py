def tag(name, *content, cls=None, **attrs):
    """生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
        for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %(name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

print(tag('br'))#传入单个定位参数， 生成一个指定名称的空标签。
print(tag('p', 'hello'))#第一个参数后面的任意个参数会被 *content 捕获， 存入一个元组。
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', id=33))#tag 函数签名中没有明确指定名称的关键字参数会被 **attrs 捕获， 存入一个字典。
print(tag('p', 'hello', 'world', cls='sidebar'))#cls 参数只能作为关键字参数传入。
print(tag(content='testing', name="img"))#调用 tag 函数时， 即便第一个定位参数也能作为关键字参数传入。
my_tag = {'name': 'img', 'title': 'Sunset Boulevard','src': 'sunset.jpg', 'cls': 'framed'}
print(tag(**my_tag))#在 my_tag 前面加上 **， 字典中的所有元素作为单个参数传入， 同名键会绑定到对应的具名参数上， 余下的则被 **attrs 捕获。


def f1():
    print("666")
def f2():#函数名可以作为函数的返回值。
    return f1
f2()()


def f3():
    print("777")
def f4(f3):#函数名可以作为参数；
    return f3
f4(f3)()

def f5():
    def f6():#函数名可以作为函数的返回值。
        print("888")
    return f6
f5()()


#闭包函数的运用，引用外层的函数。
def func():
    name = 'eva'
    def inner():
        print(name)
    return inner

func() # 直接执行func，并没有调用到func里面的inner函数，不会输出eva
f = func()
f() # 相当于是执行func()(),而func()中返回了inner函数，
    # 所以又相当于是在func函数体内部中执行func(inner),所以就能正常执行了。