from loguru import logger
import pandas as pd
import tcost_gui

logger.debug('Transferring info from UI...')
transfer = tcost_gui.main_dict
logger.debug('Transferring info from UI..SUCCESS')
logger.info(transfer)

amount_of_receivers = set()
cumul_of_rec = {}

# получаем информацию о количестве активных групп доставки
logger.debug('set of active delivery groups forming --->')
for k, v in transfer.items():
    amount_of_receivers.add(v[0])
logger.info(amount_of_receivers)

# формируем словарь, где ключ - номер группы доставки
logger.debug('dict of active delivery groups as keys forming --->')
for i in amount_of_receivers:
    cumul_of_rec[str(i)] = 0
logger.info(cumul_of_rec)

# для каждой группы доставки суммируем кол-во доставляемых ящиков
for i in amount_of_receivers:
    for k, v in transfer.items():
        if v[0] == i:
            cumul_of_rec[str(i)] += v[2]

result_of_module = {}

logger.debug('Uploading consumers.xls')
df = pd.read_excel('data_set_for_TCost.xlsx')

# создает словарь с наименование города доставки, где значение - суммарное кол-во коробок
logger.debug('making dict with final results---->')
for groupnam, boxes in cumul_of_rec.items():
    for cons, options in transfer.items():
        for gp in range(0, len(df.values)):
            if options[0] == int(groupnam) and options[1] is True:
                if cons == df.values[gp][0]:
                    result_of_module[df.values[gp][2]] = boxes
logger.info(result_of_module)
