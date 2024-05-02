
def genSubPaths():
    target = 'rap://openplugin/9631867?_rapjson_=https%3A%2F%2Fg.alicdn.com%2Frap%2F9631867%2F1.17.12%2Frap.json'
    (_host, _path) = target.split('?')

    subPaths = {
        '铺货成功': '/record?tab=success',
        '铺货中': '/record?tab=process',
        '铺货失败': '/record?tab=fail',
        '出单计划': '/index?nav=order-plan',
        '同步商品': '/sync-page',
        '订单设置': '/order-auto',
        '铺货设置': '/index?scene_type=shop_distribute_settings',
        '商品管理': '/index?activeKey=product-relation',
        '订单管理': '/index?activeKey=order'
    }
    outShops = [
        {
            "code": "2981741264",
            "channel": "thyny",
            'nick': '淘宝促销专家'
        },
        {
            "code": "4463798",
            "channel": "douyin",
            'nick': '抖店测试店铺'
        },
        {
            "code": "448139443",
            "channel": "pinduoduo",
            'nick': '拼多多威灵顿庄园'
        },
        {
            "code": "3",
            "channel": "xiaohongshu",
            'nick': '小红书测试店'
        }
    ]

    paths = []

    for fun, subPath in subPaths.items():

        for shop in outShops:
            code, channel, nick = shop.values()
            path = {}
            path['title'] = f'{fun} - {nick}'
            c = '&' if '?' in subPath else '?'
            path['target'] = f'{_host}{subPath}{c}outShopCode={code}&channel={channel}&{_path}'

            paths += [path]

    return paths


def genTxt():
    paths = genSubPaths()

    try:
        with open('链接.txt', 'w', encoding='utf-8') as fs:
            for path in paths:
                fs.write(f'{path["title"]}: {path["target"]} \n')

    except FileNotFoundError:
        print("文件不存在！")
    except LookupError:
        print("使用了未知编码")
    except UnicodeDecodeError:
        print("读取文件时解码错误")
    except IOError:
        print("读写文件时发生错误！")


genTxt()
