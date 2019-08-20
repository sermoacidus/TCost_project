import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

def count_the_cost():
    if var_for_gp1 == False:
        info_result.configure(text=int(message_from_box_amount1))

class LabelP(tk.Label):
    def __init__(self,row_inp,column_inp, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=row_inp,column=column_inp)

class Combobox_p


root = tk.Tk()

df = pd.read_excel('data_set_for_TCost.xlsx')
for i in range(0,len(df.values)):
    gp_label = LabelP(i+1, 1, root, text = df.values[i][0])




group_combobox1 = ttk.Combobox(root, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], height=13)
group_combobox1.set('введи группу')
group_combobox1.grid(row=1, column=2)
group_combobox2 = ttk.Combobox(root, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], height=13)
group_combobox2.set('введи группу')
group_combobox2.grid(row=2, column=2)

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
