import voltage_drop as vd
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox

# setting up GUI
root = tk.Tk()
root.title('Voltage Drop Calculator')
root.resizable(width=False, height=False)

heading_font = Font(size=10, weight='bold')


#   function to allow only digit entry
def digit_input(inp):
    if str.isdigit(inp) or inp == '':
        return True
    else:
        return False


tab_control = ttk.Notebook(root)  # Creating tabs in Voltage Drop Calculator for various functions

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Calculator')
tab_control.pack(expand=1, fill='both')

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Formula')
tab_control.pack(expand=1, fill='both')

#     ---------------------------------------BEGIN Calculate GUI (tab1) ---------------------------------------
#  begin code for phase buttons
ph = tk.IntVar()  # variable to track three phase or single phase
ph.set(3)
lbl1_phase = tk.Label(tab1, text='Phase: ')
lbl1_phase.grid(row=1, column=0, sticky=tk.E)
lbl1_phase.configure(font=heading_font)

btn1t1_3phase = tk.Radiobutton(tab1, text='Three Phase', indicatoron=0, width=10, padx=15, variable=ph, value=3)
btn1t1_3phase.grid(row=1, column=1)

btn2t1_1phase = tk.Radiobutton(tab1, text='Single Phase', indicatoron=0, width=10, padx=15, variable=ph, value=1)
btn2t1_1phase.grid(row=1, column=2)
#  end code for phase buttons

#  begin code for conductor type buttons
cmat = tk.IntVar()  # variable to track three phase or single phase
cmat.set(1)
lbl2_cmat = tk.Label(tab1, text='Conductor material: ')
lbl2_cmat.grid(row=2, column=0, sticky=tk.E)
lbl2_cmat.configure(font=heading_font)

btn3t1_cu = tk.Radiobutton(tab1, text='Copper', indicatoron=0, width=10, padx=15, variable=cmat, value=1)
btn3t1_cu.grid(row=2, column=1, )

btn4t1_al = tk.Radiobutton(tab1, text='Aluminum', indicatoron=0, width=10, padx=15, variable=cmat, value=2)
btn4t1_al.grid(row=2, column=2, )
#  end code for conductor type buttons

#  begin code for conductor size buttons
c_unit = tk.IntVar()  # variable to track three phase or single phase
c_unit.set(1)
lbl3_csize = tk.Label(tab1, text='Select conductor size: ')
lbl3_csize.grid(row=3, column=0, sticky=tk.E)
lbl3_csize.configure(font=heading_font)


def c_unit_select(x):  # function to determine which list 'AWG' or 'Metric' is shown in combobox for conductor size
    if x == 1:
        cbox1t1_csize['values'] = vd.awg_size
    elif x == 2:
        cbox1t1_csize['values'] = vd.metric_size
    else:
        print('Error')


f1 = tk.Frame(tab1)
f1.grid(row=3, column=2)

btnt1_awg = tk.Radiobutton(f1, text='AWG', variable=c_unit, value=1, command=lambda: c_unit_select(1))
btnt1_awg.grid(row=1, column=1, sticky=tk.W)

btnt1_metric = tk.Radiobutton(f1, text='Metric', variable=c_unit, value=2, command=lambda: c_unit_select(2))
btnt1_metric.grid(row=1, column=2, sticky=tk.W)

clicked3 = tk.StringVar()
clicked3.set('Select')

cbox1t1_csize = ttk.Combobox(tab1, state='readonly', width=12, textvariable=clicked3)
cbox1t1_csize['values'] = vd.awg_size
cbox1t1_csize.grid(row=3, column=1, sticky=tk.W)
#   end code for conductor size buttons

#   begin code for number of sets entry
default_psets = tk.StringVar(tab1, value='')

lbl4_psets = tk.Label(tab1, text='Number of parallel sets: ')
lbl4_psets.grid(row=4, column=0, sticky=tk.E)
lbl4_psets.configure(font=heading_font)

ent1t1_psets = tk.Entry(tab1, textvariable=default_psets, width=15, borderwidth=2)
ent1t1_psets.grid(row=4, column=1, sticky=tk.W)
reg1 = ent1t1_psets.register(digit_input)
ent1t1_psets.config(validate='all', validatecommand=(reg1, '%P'))

#   end code for number of sets entry

#   begin code for conductor length entry
default_clen = tk.StringVar(tab1, value='')

lbl5_clen = tk.Label(tab1, text='Conductor length: ')
lbl5_clen.grid(row=5, column=0, sticky=tk.E)
lbl5_clen.configure(font=heading_font)

ent2t1_clen = tk.Entry(tab1, textvariable=default_clen, width=15, borderwidth=2)
ent2t1_clen.grid(row=5, column=1, sticky=tk.W)
reg2 = ent2t1_clen.register(digit_input)
ent2t1_clen.config(validate='all', validatecommand=(reg2, '%P'))

clicked_unit = tk.StringVar()
clicked_unit.set('ft')

cboxt1_unit = ttk.Combobox(tab1, state='readonly', width=5, textvariable=clicked_unit)
cboxt1_unit['values'] = 'ft', 'mm', 'M'
cboxt1_unit.grid(row=5, column=2, sticky=tk.W)
#   end code for conductor length entry

#   begin code for Voltage entry
default_volt = tk.StringVar(tab1, value='')

lbl6_volt = tk.Label(tab1, text='Enter voltage (V): ')
lbl6_volt.grid(row=6, column=0, sticky=tk.E)
lbl6_volt.configure(font=heading_font)

ent3t1_volt = tk.Entry(tab1, textvariable=default_volt, width=15, borderwidth=2)
ent3t1_volt.grid(row=6, column=1, sticky=tk.W)
reg3 = ent3t1_volt.register(digit_input)
ent3t1_volt.config(validate='all', validatecommand=(reg3, '%P'))
#   end code for voltage entry

#   begin code for current entry
default_current = tk.StringVar(tab1, value='')

lbl7_current = tk.Label(tab1, text='Enter current (A): ')
lbl7_current.grid(row=7, column=0, sticky=tk.E)
lbl7_current.configure(font=heading_font)

ent4t1_current = tk.Entry(tab1, textvariable=default_current, width=15, borderwidth=2)
ent4t1_current.grid(row=7, column=1, sticky=tk.W)
reg4 = ent4t1_current.register(digit_input)
ent4t1_current.config(validate='all', validatecommand=(reg4, '%P'))
#   end code for current entry

#   begin code for pf entry

# commented code within pf entry is to allow for user input - currently disabled.
# default_pf = tk.StringVar(tab1, value='0.85')

lbl8_pf = tk.Label(tab1, text='Power factor (pf): ')
lbl8_pf.grid(row=8, column=0, sticky=tk.E)
lbl8_pf.configure(font=heading_font)

lbl9_pf = tk.Label(tab1, text='0.85')
lbl9_pf.grid(row=8, column=1, sticky=tk.W)
lbl9_pf.configure(font=heading_font)

# commented code within pf entry is to allow for user input - currently disabled.
# ent5t1_pf = tk.Entry(tab1, textvariable=default_pf, width=10, borderwidth=2)
# ent5t1_pf.grid(row=8, column=1, sticky=tk.W)
# reg5 = ent5t1_pf.register(digit_input)
# ent5t1_pf.config(validate='all', validatecommand=(reg5, '%P'))

#   end code for pf entry

#  begin code for conduit type menu
lbl10_conduit = tk.Label(tab1, text='Select conduit type: ')
lbl10_conduit.grid(row=9, column=0, sticky=tk.E)
lbl10_conduit.configure(font=heading_font)

clicked4 = tk.StringVar()
clicked4.set('Select')

cbox2t1_conduit = ttk.Combobox(tab1, state='readonly', width=12, textvariable=clicked4)
cbox2t1_conduit['values'] = vd.conduit_type
cbox2t1_conduit.grid(row=9, column=1, sticky=tk.W)
#   end code for conduit type menu

#   result box
result = tk.StringVar()

lbl11_result = tk.Label(tab1, textvariable=result)
lbl11_result.configure(bg='#d4d4d4')
lbl11_result.grid(row=10, column=2, sticky=tk.NSEW)

lbl12_result_name = tk.Label(tab1, text='Voltage drop = ')
lbl12_result_name.grid(row=10, column=1, sticky=tk.E)
lbl12_result_name.configure(font=heading_font)

lbl13_NEC = tk.Label(tab1, text='(NEC recommends < 3%)')
lbl13_NEC.grid(row=11, column=1, columnspan=2, sticky=tk.NSEW)
# lbl13_NEC.configure(font=heading_font)

# buttons
button_calc1 = tk.Button(tab1, text='Calculate', command=lambda: button_calculate())
button_calc1.grid(row=10, column=0, sticky=tk.NSEW)

button_clear1 = tk.Button(tab1, text='Clear', command=lambda: button_clear())
button_clear1.grid(row=11, column=0, sticky=tk.NSEW)
#     ---------------------------------------BEGIN Calculate GUI (tab1) ---------------------------------------

#     ---------------------------------------BEGIN Formula (tab2) ---------------------------------------------
lbl1t2_3ph_title = tk.Label(tab2, text='3-Phase Voltage:')
lbl1t2_3ph_title.grid(row=0, column=0, sticky=tk.W)
lbl1t2_3ph_title.configure(font=heading_font)

lbl1t2_3ph_formula = tk.Label(tab2, text='V = [√(3) x (Z x I x (length/1000)] × 1/(set of parallel conductors)')
lbl1t2_3ph_formula.grid(row=1, column=0, sticky=tk.W)

lbl1t2_1ph_title = tk.Label(tab2, text='1-Phase Voltage:')
lbl1t2_1ph_title.grid(row=2, column=0, sticky=tk.W)
lbl1t2_1ph_title.configure(font=heading_font)

lbl1t2_1ph_formula = tk.Label(tab2, text='V = [2 x (Z x I x (length/1000)] × 1/(set of parallel conductors)')
lbl1t2_1ph_formula.grid(row=3, column=0, sticky=tk.W)

lbl1t2_variable = tk.Label(tab2, text='Variables:')
lbl1t2_variable.grid(row=4, column=0, sticky=tk.W)
lbl1t2_variable.configure(font=heading_font)

lbl1t2_Z = tk.Label(tab2, text='Z = Impedance = (R x cos\u03B8) + (X x sin\u03B8)')
lbl1t2_Z.grid(row=5, column=0, sticky=tk.W)

lbl1t2_theta = tk.Label(tab2, text='\u03B8 = Power factor angle = arccos(pf) ')
lbl1t2_theta.grid(row=6, column=0, sticky=tk.W)

lbl1t2_R = tk.Label(tab2, text='R = Resistance (NEC Chapter 9 - Table 9)')
lbl1t2_R.grid(row=7, column=0, sticky=tk.W)

lbl1t2_X = tk.Label(tab2, text='X = Reactance (NEC Chapter 9 - Table 9)')
lbl1t2_X.grid(row=8, column=0, sticky=tk.W)

lbl1t2_I = tk.Label(tab2, text='I = Current')
lbl1t2_I.grid(row=9, column=0, sticky=tk.W)

lbl1t2_V = tk.Label(tab2, text='V = System Voltage')
lbl1t2_V.grid(row=10, column=0, sticky=tk.W)

lbl1t2_L = tk.Label(tab2, text='length = Conductor length')
lbl1t2_L.grid(row=11, column=0, sticky=tk.W)


#     ---------------------------------------END Formula (tab2) ---------------------------------------


# begin button function declarations

# function to get reactance from dict based on c_mat, conductor_size and conduit_type
def if_metric(conductor_unit, conductor_size):
    if conductor_unit == 2:
        conductor_size = vd.metric_awg.get(conductor_size)
        print(conductor_size)
        return conductor_size
    else:
        print(conductor_size)
        return conductor_size


def get_reactance(conductor_size, conduit_type):
    if conduit_type == 'Steel':
        X = vd.awg_reactance_steel.get(conductor_size)
        print(X)
        return X
    else:
        X = vd.awg_reactance_pvc_al.get(conductor_size)
        print(X)
        return X


#   function to get resistance from dict based on c_mat, conductor_size and conduit_type
def get_resistance(conductor_size, conduit_type, c_mat):
    if c_mat == 1 and conduit_type == "PVC":
        R = vd.awg_cu_resistance_pvc.get(conductor_size)
        print(R)
        return R
    elif c_mat == 1 and conduit_type == 'Steel':
        R = vd.awg_cu_resistance_steel.get(conductor_size)
        print(R)
        return R
    elif c_mat == 1 and conduit_type == 'Aluminum':
        R = vd.awg_cu_resistance_al.get(conductor_size)
        print(R)
        return R

    if c_mat == 2 and conduit_type == "PVC":
        R = vd.awg_al_resistance_pvc.get(conductor_size)
        print(R)
        return R
    elif c_mat == 2 and conduit_type == 'Steel':
        R = vd.awg_al_resistance_steel.get(conductor_size)
        print(R)
        return R
    elif c_mat == 2 and conduit_type == 'Aluminum':
        R = vd.awg_al_resistance_al.get(conductor_size)
        print(R)
        return R


# function to color the result box based on calculated result - Green/Yellow/Red
def get_result(voltage_drop, vd):
    result.set(voltage_drop)
    if vd > 5.00:
        lbl11_result.configure(bg='#e65555')
    elif 3.00 <= vd <= 5.00:
        lbl11_result.configure(bg='#f5fc65')
    else:
        lbl11_result.configure(bg='#68fc65')


# function to verify that all legal values have been selected and no input is blank
def value_check():
    phase = ph.get()

    c_mat = cmat.get()

    conductor_unit = c_unit.get()

    conductor_size = cbox1t1_csize.get()
    if conductor_size == 'Select':
        tk.messagebox.showerror(message='Please make a selection.')
        return
    conductor_size = if_metric(conductor_unit, conductor_size)

    conduit_type = cbox2t1_conduit.get()
    if conduit_type == 'Select':
        tk.messagebox.showerror(message='Please make a selection.')
        return

    para_sets = ent1t1_psets.get()
    if para_sets.isnumeric():
        para_sets = float(para_sets)
        if not 0 < para_sets <= 20:
            tk.messagebox.showerror(message='Please enter a valid value for number of parallel sets (1 - 20).')
            return
    else:
        tk.messagebox.showerror(message='Please enter a valid value for number of parallel sets (1 - 20).')
        return

    input_length = ent2t1_clen.get()
    l_unit = cboxt1_unit.get()
    if input_length.isnumeric():
        input_length = float(input_length)
        input_length = float(vd.convert_length(input_length, l_unit))
    else:
        tk.messagebox.showerror(message='Please enter a value for conductor length.')
        return

    input_voltage = ent3t1_volt.get()
    if input_voltage.isnumeric():
        input_voltage = float(input_voltage)
        if not 0 < input_voltage <= 600:
            tk.messagebox.showerror(message='Please enter a valid value for voltage (1 - 600V).')
            return
    else:
        tk.messagebox.showerror(message='Please enter a valid value for voltage (1 - 600V).')
        return

    input_current = ent4t1_current.get()
    if input_current.isnumeric():
        input_current = float(input_current)
        if not 0 < input_current <= 10000:
            tk.messagebox.showerror(message='Please enter a valid value for current (1 - 10,000A).')
            return
    else:
        tk.messagebox.showerror(message='Please enter a valid value for current (1 - 10,000A).')
        return

    pf = 0.85

    return phase, c_mat, conductor_size, conduit_type, para_sets, input_length, input_voltage, input_current, pf


# calculate button uses function from voltage drop.py file
def button_calculate():
    try:
        phase, c_mat, conductor_size, conduit_type, para_sets, length, V, A, pf = value_check()
        X = get_reactance(conductor_size, conduit_type)
        R = get_resistance(conductor_size, conduit_type, c_mat)
        if phase == 1:
            str_voltage_drop, num_voltage_drop = vd.single_phase_vd(pf, R, X, length, A, V, para_sets)
            get_result(str_voltage_drop, num_voltage_drop)
            return str_voltage_drop
        elif phase == 3:
            str_voltage_drop, num_voltage_drop = vd.three_phase_vd(pf, R, X, length, A, V, para_sets)
            get_result(str_voltage_drop, num_voltage_drop)
            return str_voltage_drop
        else:
            print('Error')
    except ValueError:
        print(' value error')
        return
    except TypeError:
        print('type error')
        return


def button_clear():
    ent1t1_psets.delete(0, tk.END)
    ent2t1_clen.delete(0, tk.END)
    ent3t1_volt.delete(0, tk.END)
    ent4t1_current.delete(0, tk.END)


root.mainloop()
