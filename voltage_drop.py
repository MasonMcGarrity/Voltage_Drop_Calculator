# this module contains all NEC values from ch.9/Table.9 as well as awg/metric wire sizes and voltage drop functions
import math

# tuple of NEC conductor sizes in AWG/kcmil
awg_size = ('#14', '#12', '#10', '#8', '#6', '#4', '#3', '#2', '#1', '1/0', '2/0', '3/0', '4/0',
            '250 kcmil', '300 kcmil', '350 kcmil', '400 kcmil', '500 kcmil', '600 kcmil', '750 kcmil', '1000 kcmil')

# tuple of standard conductor sizes in metric (mm^2)
metric_size = ('2.5 mm\N{SUPERSCRIPT TWO}', '4 mm\N{SUPERSCRIPT TWO}', '6 mm\N{SUPERSCRIPT TWO}',
               '10 mm\N{SUPERSCRIPT TWO}', '16 mm\N{SUPERSCRIPT TWO}', '25 mm\N{SUPERSCRIPT TWO}',
               '35 mm\N{SUPERSCRIPT TWO}', '50 mm\N{SUPERSCRIPT TWO}', '70 mm\N{SUPERSCRIPT TWO}',
               '80 mm\N{SUPERSCRIPT TWO}', '95 mm\N{SUPERSCRIPT TWO}', '120 mm\N{SUPERSCRIPT TWO}',
               '150 mm\N{SUPERSCRIPT TWO}', '185 mm\N{SUPERSCRIPT TWO}', '240 mm\N{SUPERSCRIPT TWO}',
               '300 mm\N{SUPERSCRIPT TWO}', '400 mm\N{SUPERSCRIPT TWO}', '500 mm\N{SUPERSCRIPT TWO}')

# dict for converting from metric to awg
metric_awg = {'2.5 mm\N{SUPERSCRIPT TWO}': '#14', '4 mm\N{SUPERSCRIPT TWO}': '#12', '6 mm\N{SUPERSCRIPT TWO}': '#10',
              '10 mm\N{SUPERSCRIPT TWO}': '#8', '16 mm\N{SUPERSCRIPT TWO}': '#6', '25 mm\N{SUPERSCRIPT TWO}': '#4',
              '35 mm\N{SUPERSCRIPT TWO}': '#2', '50 mm\N{SUPERSCRIPT TWO}': '#1', '70 mm\N{SUPERSCRIPT TWO}': '1/0',
              '80 mm\N{SUPERSCRIPT TWO}': '2/0', '95 mm\N{SUPERSCRIPT TWO}': '3/0', '120 mm\N{SUPERSCRIPT TWO}': '4/0',
              '150 mm\N{SUPERSCRIPT TWO}': '300 kcmil', '185 mm\N{SUPERSCRIPT TWO}': '350 kcmil',
              '240 mm\N{SUPERSCRIPT TWO}': '400 kcmil', '300 mm\N{SUPERSCRIPT TWO}': '500 kcmil',
              '400 mm\N{SUPERSCRIPT TWO}': '600 kcmil', '500 mm\N{SUPERSCRIPT TWO}': '1000 kcmil'}

# tuple of standard conduit types
conduit_type = ('PVC', 'Aluminum', 'Steel')

# tuple of Reactance (X) for PVC/Al conduit based on AWG size measured in ft - NEC Ch.9 Table 9
xl_ft_pvc_al = (0.058, 0.054, 0.050, 0.052, 0.051, 0.048, 0.047, 0.045, 0.046, 0.044, 0.043, 0.042,
                0.041, 0.041, 0.041, 0.040, 0.040, 0.039, 0.039, 0.038, 0.037)

# tuple of Reactance (X) for steel conduit based on AWG size measured in ft - NEC Ch.9 Table 9
xl_ft_steel = (0.073, 0.068, 0.063, 0.065, 0.064, 0.060, 0.059, 0.057, 0.057, 0.055, 0.054, 0.052, 0.051, 0.052,
               0.051, 0.050, 0.049, 0.048, 0.048, 0.048, 0.046)

# tuple of Resistance (R) of copper wire and PVC Conduit - NEC Ch.9 Table 9
r_cu_pvc = (3.1, 2.0, 1.2, 0.78, 0.49, 0.31, 0.25, 0.19, 0.15, 0.12, 0.10, 0.077, 0.062, 0.052, 0.044, 0.038,
            0.033, 0.027, 0.023, 0.019, 0.015)

# tuple of Resistance (R) of copper wire and Al Conduit - NEC Ch.9 Table 9
r_cu_al = (3.1, 2.0, 1.2, 0.78, 0.49, 0.31, 0.25, 0.20, 0.16, 0.13, 0.10, 0.082, 0.067, 0.057, 0.049, 0.043,
           0.038, 0.032, 0.028, 0.024, 0.019)

# tuple of Resistance (R) of copper wire and steel Conduit - NEC Ch.9 Table 9
r_cu_steel = (3.1, 2.0, 1.2, 0.78, 0.49, 0.31, 0.25, 0.20, 0.16, 0.12, 0.10, 0.079, 0.063, 0.054, 0.045, 0.039,
              0.035, 0.029, 0.025, 0.021, 0.018)

# tuple of Resistance (R) of aluminum wire and PVC Conduit - NEC Ch.9 Table 9
r_al_pvc = (3.1, 3.2, 2.0, 1.3, 0.81, 0.51, 0.40, 0.32, 0.25, 0.20, 0.16, 0.13, 0.10, 0.085, 0.071, 0.061, 0.054,
            0.043, 0.036, 0.029, 0.023)

# tuple of Resistance (R) of aluminum wire and Al Conduit - NEC Ch.9 Table 9
r_al_al = (3.1, 3.2, 2.0, 1.3, 0.81, 0.51, 0.41, 0.32, 0.26, 0.21, 0.16, 0.13, 0.11, 0.090, 0.076, 0.066, 0.059,
           0.048, 0.041, 0.034, 0.027)

# tuple of Resistance (R) of aluminum wire and steel Conduit - NEC Ch.9 Table 9
r_al_steel = (3.1, 3.2, 2.0, 1.3, 0.81, 0.51, 0.40, 0.32, 0.25, 0.20, 0.16, 0.13, 0.10, 0.086, 0.072, 0.063, 0.055,
              0.045, 0.038, 0.031, 0.025)

# dict of AWG sizes (keys) and reactance (values) for pvc, Al conduit
awg_reactance_pvc_al = dict(zip(awg_size, xl_ft_pvc_al))

# dict of AWG sizes (keys) and reactance (values) for steel conduit
awg_reactance_steel = dict(zip(awg_size, xl_ft_steel))

# dict of AWG sizes (keys) and resistance (values) for CU conductors & pvc conduit
awg_cu_resistance_pvc = dict(zip(awg_size, r_cu_pvc))

# dict of AWG sizes (keys) and resistance (values) for CU conductors & Al conduit
awg_cu_resistance_al = dict(zip(awg_size, r_cu_al))

# dict of AWG sizes (keys) and resistance (values) for CU conductors & steel conduit
awg_cu_resistance_steel = dict(zip(awg_size, r_cu_steel))

# dict of AWG sizes (keys) and resistance (values) for Al conductors & pvc conduit
awg_al_resistance_pvc = dict(zip(awg_size, r_al_pvc))

# dict of AWG sizes (keys) and resistance (values) for Al conductors & Al conduit
awg_al_resistance_al = dict(zip(awg_size, r_al_al))

# dict of AWG sizes (keys) and resistance (values) for Al conductors & steel conduit
awg_al_resistance_steel = dict(zip(awg_size, r_al_steel))


def three_phase_vd(pf, R, X, length, A, V, para_sets):
    theta = math.acos(pf)
    impedance = float((R * math.cos(theta)) + (X * math.sin(theta)))
    vd_ln = impedance * (length / 1000.0) * A
    vd_ll = (math.sqrt(3) * vd_ln) * (1 / para_sets)
    percent_vd = (vd_ll / V) * 100
    clean_percent_vd = round(percent_vd, 2)
    final = str(clean_percent_vd) + "%"
    print(final)
    return final, clean_percent_vd


def single_phase_vd(pf, R, X, length, A, V, para_sets):
    theta = math.acos(pf)
    impedance = (R * math.cos(theta)) + (X * math.sin(theta))
    vd_ln = impedance * (length / 1000) * A
    vd_ln = (2 * vd_ln) * (1 / para_sets)
    percent_vd = (vd_ln / V) * 100
    clean_percent_vd = round(percent_vd, 2)
    final = str(clean_percent_vd) + "%"
    print(final)
    return final, clean_percent_vd


# function that converts metric lengths to ft for voltage drop calculation
def convert_length(input_length, l_unit):
    if l_unit == "ft":
        length_ft = round(input_length)
        print(str(length_ft) + 'ft')
        return int(length_ft)
    elif l_unit == 'mm':
        length_ft = input_length / 304.8
        length_ft = round(length_ft)
        print(str(length_ft) + 'ft')
        return int(length_ft)
    elif l_unit == 'M':
        length_ft = input_length / 0.3048
        length_ft = round(length_ft)
        print(str(length_ft) + 'ft')
        return int(length_ft)
    else:
        print('Error')
