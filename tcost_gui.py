import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

def count_the_cost():
    if var_for_gp1 == False:
        info_result.configure(text=int(message_from_box_amount1))
        print(comboboxp.textincombobox.get())
        print(comboboxp2.textincombobox.get())

class LabelP(tk.Label):
    def __init__(self,row_inp,column_inp, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=row_inp,column=column_inp)

class ComboboxP(ttk.Combobox):
    def __init__(self, row_inp, column_inp, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=row_inp, column=column_inp)
        self.set('введи группу')
        self.textincombobox = tk.StringVar()
        self['textvariable'] = self.textincombobox
        self['values'] = [n for n in range(1,14)]
        self['height'] = 13
        self['width'] = 5
    #def listen_to_text(self,textvariable):
     #   self.textvariable = textvariable
      #  self.textvariable = tk.StringVar()
    #def read_the_combobox_value(self, event):
     #   print(self.group_combobox_value)
#def initialize_all_comboboxes():
    #for i in range(0, len(df.values)):


root = tk.Tk()
#root.geometry

df = pd.read_excel('data_set_for_TCost.xlsx')

#Перечень грузополучателей (1ый столбец)
for i in range(0, len(df.values)):
    gp_label = LabelP(i+1, 1, root, text=df.values[i][0])

#Выбор группы грузополучателей по укрупнению (до 13 групп)
#group_combobox_test.listen_to_text(group_combobox_test_value)
a = []
for i in range(0, len(df.values)):
    a.append('group_combobox'+str(i))
    a[i] = ComboboxP(i+1, 2, root)
print(a[0],type(a[0]),a[1],type(a[1]),a[2],type(a[2]))
#print(a)
#for i in range(0, len(df.values)):
#    group_combobox = ComboboxP(i+1, 2, root)
#group_combobox_test['textvariable'] = group_combobox_test.textincombobox


var_for_gp1 = False
gp_main1 = tk.Checkbutton(root, text='Грузополучатель?', variable=var_for_gp1, onvalue=True, offvalue=False)
gp_main1.grid(row=1, column=3)
var_for_gp2 = False
gp_main2 = tk.Checkbutton(root, text='Грузополучатель?', variable=var_for_gp2, onvalue=True, offvalue=False)
gp_main2.grid(row=2, column=3)

message_from_box_amount1 = int()
box_amount1 = tk.Entry(root, width=3, textvariable=message_from_box_amount1)
box_amount1.grid(row=1, column=4)
box_amount2 = tk.Entry(root, width=3)
box_amount2.grid(row=2, column=4)

confirm_button = tk.Button(root, text='Рассчитать -->', command=count_the_cost)
confirm_button.grid(row=len(df.values)+2, column=1)

info_result = tk.Label(root, text='Стоимость доставки:________')
info_result.grid(row=len(df.values)+2, column=2)

root.mainloop()
