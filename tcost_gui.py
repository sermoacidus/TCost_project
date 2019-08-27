import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd






# from main import main_code

#тестовая функция
def count_the_cost():
    # main_code()
    info_result.configure(text=int(b[0].digitin_entry.get()))
    print(a[3].textincombobox.get())
    print(a[4].textincombobox.get())
    print(a[5].textincombobox.get())
    print(c[1].ifconsumerornot.get())
    #print(if0.ifconsumerornot.get())

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
    def __init__(self, row_inp, column_inp, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=row_inp, column=column_inp)
        self['text'] = 'Грузополучатель?'
        self.ifconsumerornot = tk.BooleanVar()
        self['variable'] = self.ifconsumerornot
        self['onvalue'] = True
        self['offvalue'] = False

def onFrameConfigure(container):
    container.configure(scrollregion=container.bbox("all"))

root = tk.Tk()
root.geometry('450x400') #TODO: центрирование
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
    c[i] = CheckbuttonP(i+1, 3, main_window)

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
