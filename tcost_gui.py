import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

#создание словаря с вводными данными
def count_the_cost():
    global main_dict
    main_dict = {}
    for n in range(len(df.values)):
        try:
            group_number = int(a[n].textincombobox.get())
            boxes_amount = int(b[n].digitin_entry.get())
            is_receiver = c[n].ifconsumerornot.get()
        except:
            print(df.values[n][0] + ' в разнарядке не присутствует')
            continue
        main_dict[df.values[n][0]]=(group_number,is_receiver,boxes_amount)
    root.destroy()
    return main_dict

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
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


def onFrameConfigure(container):
    container.configure(scrollregion=container.bbox("all"))

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
df = pd.read_excel('data_set_for_TCost.xlsx')

#Перечень грузополучателей (1ый столбец)
gp = []
for i in range(0, len(df.values)):
    gp.append('gp' + str(i))
    gp[i] = LabelP(i + 1, 1, main_window, text=df.values[i][0])
    #print(gp[i])

#является ли грузополучателем или же потребитель по укрупнению
c = []
for i in range(0, len(df.values)):
    c.append('if'+str(i))
    c[i] = CheckbuttonP(i+1, 3, c[i], main_window)

#кол-во мест
b = []
for i in range(0, len(df.values)):
    b.append('digit_in_entry'+str(i))
    b[i] = EntryP(i+1, 4, main_window)

#Выбор группы грузополучателей по укрупнению (до 13 групп)
a = []
for i in range(0, len(df.values)):
    a.append('group_combobox'+str(i))
    a[i] = ComboboxP(i+1, 2, main_window)


confirm_button = tk.Button(main_window, text='Рассчитать -->', command=count_the_cost)
confirm_button.grid(row=len(df.values)+2, column=1)

info_result = tk.Label(main_window, text='Стоимость доставки:________')
info_result.grid(row=len(df.values)+2, column=2, columnspan=3)

root.mainloop()
