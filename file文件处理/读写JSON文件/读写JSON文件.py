import json

"""读写JSON文件"""
mydict = {
    'name': '骆昊',
    'age': 38,
    'qq': 957658,
    'friends': ['Jack', 'Kim'],
    'cars': [
        {'brand': 'BYD', 'max_speed': 180},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 320}
    ]
}
try:
    with open('mydict.json', 'w', encoding='utf-8') as fs:
        json.dump(mydict,fs)
        print('1. ',json.dumps(mydict))

    with open('mydict.json', 'r', encoding='utf-8') as fs:
        data = json.load(fs)
        print('2. ',data)

    with open('mydict.json', 'r', encoding='utf-8') as fs:
        data = fs.read()
        print('3. ',json.loads(data)["name"])


except FileNotFoundError:
    print("文件不存在！")
except LookupError:
    print("使用了未知编码")
except UnicodeDecodeError:
    print("读取文件时解码错误")
except IOError:
    print("读写文件时发生错误！")

