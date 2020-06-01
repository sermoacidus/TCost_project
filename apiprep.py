import pandas as pd
import tcost_gui

transfer = tcost_gui.main_dict
amount_of_receivers = set()
cumul_of_rec = {}

#получаем информацию о количестве активных групп доставки
for k,v in transfer.items():
    amount_of_receivers.add(v[0])

#формируем словарь, где ключ - номер группы доставки
for i in amount_of_receivers:
    cumul_of_rec[str(i)] = 0

print(amount_of_receivers)
print(cumul_of_rec)

#для каждой группы доставки суммируем кол-во доставляемых ящиков
for i in amount_of_receivers:
    for k,v in transfer.items():
        if v[0] == i:
            cumul_of_rec[str(i)] += v[2]

result_of_module = {}
df = pd.read_excel('data_set_for_TCost.xlsx')

# создает словарь с наименование города доставки, где значение - суммарное кол-во коробок
for groupnam,boxes in cumul_of_rec.items():
    for cons,options in transfer.items():
        for gp in range(0,len(df.values)):
            if options[0] == int(groupnam) and options[1] is True:
                if cons == df.values[gp][0]:
                    result_of_module[df.values[gp][2]] = boxes

