# coding=utf-8


def get_name(app_key):
    appName = {'24532550': '手机百度', '24648154': '快手', '24648319': '快手', '24588013': 'uc', '23261993': '今日头条',
               '24716461': '抖音'}

    return appName[app_key]


print(get_name("24532550"))
