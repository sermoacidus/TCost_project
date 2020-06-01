import requests
import apiprep
import config
import pandas as pd

URL = "https://api.jde.ru/vD/calculator/PriceAddress?"


def main_code(resdict):
    """
    возвращает город и цену доставки полученных на выход данных
    """
    for deliverytarget, boxes_amount in resdict.items():
        params = {"addr_from": "Тверь",
                  "addr_to": deliverytarget,
                  "type": "1",
                  "weight": config.BOXWEIGHT,
                  "volume": config.BOXVOLUME,
                  "quantity": boxes_amount,
                  "pickup": '1',
                  "delivery": '1',
                  "user": config.USER,
                  "token": config.TOKEN}
        r = requests.get(URL, params=params)
        print(r.json()['price'], type(r.json()['price']))
        yield int(r.json()['price'])


a = main_code(apiprep.result_of_module)
new_column = []
df = pd.read_excel('data_set_for_TCost.xlsx')
for gp in range(0, len(df.values)):
    for deltarget, boxes in apiprep.result_of_module.items():
        i = 0
        if deltarget == df.values[gp][2]:
            new_column.append(int(next(a)))
            i = 1
            break
    if i == 0:
        new_column.append(None)
df['price'] = new_column
df.to_excel('data_set_for_TCost.xlsx', sheet_name='with_price', index=False)
