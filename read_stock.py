import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from datetime import datetime
import tushare as ts
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# 农林牧渔
# 002299 圣农发展 002458 益生股份 002234 民和股份 002746 仙坛股份 600598 北大荒
# 采掘
# 002738 中矿资源 603505 金石资源 601808 中海油服 000923 河钢资源 601898 中煤能源
# 化工
# 300487 蓝晓科技 002440 闰土股份 300777 中简科技 002643 万润股份 603026 石大胜华
# 钢铁
# 002318 久立特材 603878 勿进不锈 002110 三钢闽光 600019 宝钢股份 600782 新钢股份
# 有色金属
# 000975 银泰黄金 600459 贵研铂业 60167 明泰铝业 002182 云海金属  601212 白银有色
# 电子
# 603160 汇顶科技 002415 海康威视 603068 博通集成 603290 斯达半导 300735 光宏科技
# 家用电器
# 000810 创维数字 002759 天际股份 000333 美的集团 002242 九阳股份 000921 海信家电
# 食品饮料
# 000568 泸州老窖 000858 五粮液 000895 双汇发展 600779 水井坊 603711 香飘飘
# 纺织服装
# 002832 比音勒芬 300577 开润股份 600398 海澜之家 002563 森马服饰 603365 水晶家纺
# 轻工制造
# 603318 梦百合 603195 公牛集团 002803 吉宏股份 002798 帝欧家居 002867 周大生
# 医药生物
# 002262 恩华药业 002901 大博医疗 300401 花园生物 300326 凯利泰 300725 药石科技
# 公用事业
# 603393 新天然气 000720 新能泰山 600025 华能水电 000027 深圳能源 601985 中国核电
# 交通运输
# 002928 华夏航空 002352 顺丰控股 001965 招商公路 601021 春秋航空 600368 五洲交通
# 房地产
# 000402 金融街 000732 泰禾集团 000069 华侨城A 000006 深振业A 002146 荣盛发展
# 商业贸易
# 002127 南极电商 300755 华致酒业 002818 富森美 002024 苏宁易购 601933 永辉超市
# 休闲服务
# 600138 中青旅  300662  科锐国际   601888 中国国旅 603136 天目湖 002059 云南旅游
# 综合
# 000009 中国宝安  300797 钢研纳克 600603 广汇物流 300012 华测检测 600811 东方集团
# 建筑材料
# 000877 天山股份 000672 山峰水泥 600720 祁连山 000401 冀东水泥 600449 宁夏建材
# 建筑装饰
# 600846 同济科技 603466 风语筑 300384 三联虹普 600170 上海建工 601186 中国铁建
# 电气设备
# 002851 麦格米特 603489 八方股份 300443 金雷股份 603606 东方电缆 603218 日月股份
# 国防军工
# 300719 安达维尔  002013 中航机电 300034 钢研高纳 600038 中值股份 000547 航天发展
# 计算机
# 300773 拉卡拉 000997 新大陆 600728 佳都科技 300166 东方国信 601360 三六零
# 传媒
# 002607 中公教育 300059 东方财富 300043 星辉娱乐 002621 美吉姆 002555 三七娱乐
# 通信
# 002194 武汉凡谷 300628 亿联网路 300603 立昂技术 002115 三维通信 600522 中天科技
# 银行
# 601229 上海银行 600000 浦发银行 600919 江苏银行 601166 新业银行 601988 中国银行
# 非银金融
# 600643 爱建集团 603300 华铁应急 600901 江苏租赁 600390 五矿资本 000563 陕国投A
# 汽车
# 601965 中国汽研 002328 新朋股份 600933 爱柯迪 601311 骆驼股份 000338 潍柴动力
# 机械设备
# 002698 博时科技 002975 博杰股份  002972 科安达 603666 亿嘉和 300417 南华仪器


agriculture = ['002299', '002458', '002234', '002746', '600598']
excavation = ['002738', '603505', '601808', '000923', '601898']
chemical = ['300487', '002440', '300777', '002643', '603026']
steel = ['002318', '603878', '002110', '600019', '600782']
metals = ['000975', '600459', '600167', '002182', '601212']
electronic = ['603160', '002415', '603068', '603290', '300735']
electrical = ['000810', '002759', '000333', '002242', '000921']
food = ['000568', '000858', '000895', '600779', '603711']
cloths = ['002832', '300577', '600398', '002563', '603365']
lightIndustry = ['603318', '603195', '002803', '002798', '002867']
medical = ['002262', '002901', '300401', '300326', '300725']
public = ['603393', '000720', '600025', '000027', '601985']
transport = ['002928', '002352', '001965', '601021', '600368']
house = ['000402', '000732', '000069', '000006', '002146']
trade = ['002127', '300755', '002818', '002024', '601933']
service = ['600138', '300662', '601888', '603136', '002059']
integrated = ['000009', '300797', '600603', '300012', '600811']
building = ['000877', '000672', '600720', '000401', '600449']
decorating = ['600846', '603466', '300384', '600170', '601186']
electEquipment = ['002851', '603489', '300443', '603606', '603218']
war = ['300719', '002013', '300034', '600038', '000547']
computer = ['300773', '000997', '600728', '300166', '601360']
media = ['002607', '300059', '300043', '002621', '002555']
communication = ['002194', '300628', '300603', '002115', '600522']
bank = ['601229', '600000', '600919', '601166', '601988']
finance = ['600643', '603300', '600901', '600390', '000563']
automobile = ['601965', '002328', '600933', '601311', '000338']
mechanics = ['002698', '002975', '002972', '603666', '300417']

tickets = {'agriculture': agriculture, 'excavation': excavation, 'chemical': chemical, 'steel': steel,
           'metals': metals, 'electronic': electronic, 'electrical': electrical, 'food': food, 'cloths': cloths,
           'lightIndustry': lightIndustry, 'medical': medical, 'public': public, 'transport': transport, 'house': house,
           'trade': trade, 'service': service, 'integrated': integrated, 'building': building,
           'decorating': decorating, 'electEquipment': electEquipment, 'war': war, 'computer': computer,
           'media': media, 'communication': communication, 'bank': bank,
           'finance': finance, 'automobile': automobile, 'mechanics': mechanics}

max_min_scaler = lambda x: (x - np.min(x)) / (np.max(x) - np.min(x))
result = pd.DataFrame(columns=[])

for key, val in tickets.items():
    if key:
        print(tickets[key])
        col = ['date', 'close']
        dfAll = pd.DataFrame(columns=col)
        for item in tickets[key]:
            df = pd.read_csv(item + '.csv')
            if 'date' not in df.columns or 'close' not in df.columns:
                print(item)
                continue
            data = df.loc[:, ('date', 'close')]
            tickCol = ['date', item]
            data.columns = tickCol
            # 去量纲
            data.loc[:, item] = (data.loc[:, item] - data.loc[:, item].min()) / (
                        data.loc[:, item].max() - data.loc[:, item].min())
            # data.loc[:, item] = data.loc[:, item] / data.loc[:, item].mean()
            if dfAll.empty:
                dfAll = data
            else:
                dfAll = pd.merge(dfAll, data, how='outer', on=['date'])
        dfAll[key] = dfAll.mean(axis=1)
        if 'date' not in result.columns:
            result['date'] = dfAll['date']
        print(dfAll.head())
        result[key] = dfAll[key]

print(result.head())
result.sort_values('date', inplace=True)
result.to_csv('result.csv')

# data = df.loc[:, ('date', 'close')]
# data.loc[:, 'date'] = data.loc[:, 'date'].apply(lambda x: datetime.date(datetime.strptime(x, '%Y-%m-%d')))
# plt.plot(data.loc[:, 'date'], data.loc[:, 'close'])
# plt.show()
