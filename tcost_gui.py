from loguru import logger
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

#создание словаря с вводными данными
def count_the_cost():
    for n in range(len(df.values)):
        try:
            group_number = int(a[n].textincombobox.get())
            is_receiver = c[n].ifconsumerornot.get()
            boxes_amount = int(b[n].digitin_entry.get())
        except:
            logger.info(df.values[n][0] + ' в разнарядке не присутствует')
            continue
        main_dict[df.values[n][0]] = (group_number, is_receiver, boxes_amount)
    root.destroy()
    logger.debug('Closing UI')

class LabelP(tk.Label):
    def __init__(self,row_inp,column_inp, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=row_inp,column=column_inp)

class ComboboxP(ttk.Combobox):
    def __init__(self, row_inp, column_inp, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=row_inp, column=column_inp)
        self.set('re')
        self.textincombobox = tk.StringVar()
        self['textvariable'] = self.textincombobox
        self['values'] = [n for n in range(1,14)]
        self['height'] = 13
        self['width'] = 5

class EntryP(tk.Entry):
    def __init__(self, row_inp, column_inp, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=row_inp, column=column_inp)
        self.digitin_entry = tk.StringVar()
        self['textvariable'] = self.digitin_entry
        self['width'] = 3

class CheckbuttonP(tk.Checkbutton):
    def __init__(self, row_inp, column_inp, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=row_inp, column=column_inp)
        self['text'] = 'Грузополучатель?'
        self.ifconsumerornot = tk.BooleanVar()
        self.name = name
        self['variable'] = self.ifconsumerornot
        self['onvalue'] = True
        self['offvalue'] = False


def onFrameConfigure(container):
    container.configure(scrollregion=container.bbox("all"))


main_dict = {}

logger.debug('Creating UI...')
root = tk.Tk()
root.geometry('515x840+650+100')
container = tk.Canvas(root)
main_window = tk.Frame(container)
scr = ttk.Scrollbar(root, orient="vertical", command=container.yview)
container.configure(yscrollcommand=scr.set)
container.pack(side="left", fill="both", expand=True)
scr.pack(side="right", fill="y")
container.create_window((1, 1), window=main_window, anchor="nw")
main_window.bind("<Configure>", lambda event, container=container: onFrameConfigure(container))

#подгрузка базы грузополучателей
logger.debug('Uploading consumers.xls')
df = pd.read_excel('data_set_for_TCost.xlsx')

#Перечень грузополучателей (1ый столбец)
logger.debug('Drawing labels')
gp = []
for i in range(0, len(df.values)):
    gp.append('gp' + str(i))
    gp[i] = LabelP(i + 1, 1, main_window, text=df.values[i][0])

#является ли грузополучателем или же потребитель по укрупнению
logger.debug('Placing Checkbuttons')
c = []
for i in range(0, len(df.values)):
    c.append('if'+str(i))
    c[i] = CheckbuttonP(i+1, 3, c[i], main_window)

#кол-во мест
logger.debug('Placing Entries (for number of boxes)')
b = []
for i in range(0, len(df.values)):
    b.append('digit_in_entry'+str(i))
    b[i] = EntryP(i+1, 4, main_window)

#Выбор группы грузополучателей по укрупнению (до 13 групп)
logger.debug('Placing Compoboxes(Groups of Consumers)')
a = []
for i in range(0, len(df.values)):
    a.append('group_combobox'+str(i))
    a[i] = ComboboxP(i+1, 2, main_window)

logger.debug('Placing Button and #result# field')
confirm_button = tk.Button(main_window, text='Рассчитать -->', command=count_the_cost)
confirm_button.grid(row=len(df.values)+2, column=1)

info_result = tk.Label(main_window, text='Стоимость доставки:________')
info_result.grid(row=len(df.values)+2, column=2, columnspan=3)

logger.info('UI is finished. Calling the loop')
root.mainloop()
