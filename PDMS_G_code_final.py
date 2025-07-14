import math
import matplotlib.pyplot as plt

def calculate_extrusion(prev_E, delta, u, R, v):
    """
    Calculate the extrusion value E based on the provided formula.
    E_new = E_previous + 3.87 * (delta / u) * R^2 * v / 4
    """
    E_new = prev_E + (3.87 * (delta / u) * math.pi * (R ** 2) * v)/30
    return E_new

def calculate_flow_rate(gamma, D, n):
    """
    Calculate the volumetric flow rate Q using the shear rate formula.
    """
    R = D / 2  # Radius of the nozzle
    Q = (gamma * math.pi * (R ** 3) * n) / (3 * n + 1)*60 # mm^3/min
    return Q

def calculate_extrusion_speed(Q, R):
    """
    Calculate the extrusion speed v using the speed ratio (v/u).
    """
    v = Q / (math.pi * R ** 2)  # mm/min, Extrusion speed based on Q and cross-sectional area
    return v

def generate_gcode(deltax, deltay, u1, u2, u3, R, v):
    """
    Generate G-code for the three specified lines.
    """
    gcode = []
    coords = []  # To store coordinates for visualization

    # Initial coordinates and extrusion
    a = b = 0
    d = 0  # Initial extrusion value
    z = 0  # Initial Z-height

    # Line 1 (Initial point)
    gcode.append(f"G1 X{a} Y{b} Z{z} E{d:.5f} F{u1}")
    coords.append((a, b))

    # Line 2
    E2 = calculate_extrusion(d, deltax, u1, R, v)
    gcode.append(f"G1 X{a + deltax} Y{b} Z0 E{E2:.5f} F{u1}")
    coords.append((a + deltax, b))

    # Line 3
    E3 = calculate_extrusion(E2, deltay, u1, R, v)
    gcode.append(f"G1 X{a + deltax} Y{b + deltay} Z0 E{E3:.5f} F{u1}")
    coords.append((a + deltax, b + deltay))
    
    # Line 4
    E4 = calculate_extrusion(E3, deltax, u1, R, v)
    gcode.append(f"G1 X{a} Y{b + deltay} Z0 E{E4:.5f} F{u1}")
    coords.append((a, b + deltay))
    
    # Line 5
    E5 = calculate_extrusion(E4, deltay, u1, R, v)
    gcode.append(f"G1 X{a} Y{b + 2*deltay} Z0 E{E5:.5f} F{u1}")
    coords.append((a, b + 2*deltay))

    # Line 6
    E6 = calculate_extrusion(E5, deltax, u1, R, v)
    gcode.append(f"G1 X{a + deltax} Y{b + 2*deltay} Z0 E{E6:.5f} F{u1}")
    coords.append((a + deltax, b + 2*deltay))
    
    # Line 7
    E7 = calculate_extrusion(E6, deltay, u1, R, v)
    gcode.append(f"G1 X{a + deltax} Y{b + 3*deltay} Z0 E{E7:.5f} F{u1}")
    coords.append((a + deltax, b + 3*deltay))
    
    # Line 8
    E8 = calculate_extrusion(E7, deltax, u1, R, v)
    gcode.append(f"G1 X{a} Y{b + 3*deltay} Z0 E{E8:.5f} F{u1}")
    coords.append((a, b + 3*deltay))
    
    # Line 9
    E9 = calculate_extrusion(E8, deltay, u1, R, v)
    gcode.append(f"G1 X{a} Y{b + 4*deltay} Z0 E{E9:.5f} F{u1}")
    coords.append((a, b + 4*deltay))
    
    # Line 10
    E10 = calculate_extrusion(E9, deltax, u1, R, v)
    gcode.append(f"G1 X{a + deltax} Y{b + 4*deltay} Z2 E{E10:.5f} F{u1}")
    coords.append((a + deltax, b + 4*deltay))    

    # Line 11
    E11 = calculate_extrusion(E10, deltay, u1, R, v)
    gcode.append(f"G1 X{a + deltax} Y{b + 5*deltay} Z2 E{E11:.5f} F{u1}")
    coords.append((a + deltax, b + 5*deltay))
    
    # Line 12
    E12 = calculate_extrusion(E11, deltax, u1, R, v)
    gcode.append(f"G1 X{a} Y{b + 5*deltay} Z2 E{E12:.5f} F{u1}")
    coords.append((a, b + 5*deltay))
    
    # Line 13
    E13 = calculate_extrusion(E12, deltay, u1, R, v)
    gcode.append(f"G1 X{a} Y{b + 6*deltay} Z2 E{E13:.5f} F{u1}")
    coords.append((a, b + 6*deltay))
    
    # Line 14
    E14 = calculate_extrusion(E13, deltax, u1, R, v)
    gcode.append(f"G1 X{a + deltax} Y{b + 6*deltay} Z2 E{E14:.5f} F{u1}")
    coords.append((a + deltax, b + 6*deltay))
    
    # Line 15
    E15 = calculate_extrusion(E14, deltay, u1, R, v)
    gcode.append(f"G1 X{a + deltax} Y{b + 7*deltay} Z2 E{E15:.5f} F{u1}")
    coords.append((a + deltax, b + 7*deltay))
    
    # Line 16
    E16 = calculate_extrusion(E15, deltax, u1, R, v)
    gcode.append(f"G1 X{a} Y{b + 7*deltay} Z2 E{E16:.5f} F{u1}")
    coords.append((a, b + 7*deltay))
    
    # Line 17
    E17 = calculate_extrusion(E16, deltay, u1, R, v)
    gcode.append(f"G1 X{a} Y{b + 8*deltay} Z2 E{E17:.5f} F{u1}")
    coords.append((a, b + 8*deltay))
    
    # Line 18
    E18 = calculate_extrusion(E17, deltax, u1, R, v)
    gcode.append(f"G1 X{a + deltax} Y{b + 8*deltay} Z2 E{E18:.5f} F{u1}")
    coords.append((a + deltax, b + 8*deltay))
    
    # Line 19
    E19 = calculate_extrusion(E18, deltay, u1, R, v)
    gcode.append(f"G1 X{a + deltax} Y{b + 9*deltay} Z2 E{E19:.5f} F{u1}")
    coords.append((a + deltax, b + 9*deltay))
    
    # Line 20
    E20 = calculate_extrusion(E19, deltax, u1, R, v)
    gcode.append(f"G1 X{a} Y{b + 9*deltay} Z4 E{E20:.5f} F{u1}")
    coords.append((a, b + 9*deltay))
    
    # Line 21
    E21 = calculate_extrusion(E20, deltay, u1, R, v)
    gcode.append(f"G1 X{a} Y{b + 10*deltay} Z4 E{E21:.5f} F{u1}")
    coords.append((a, b + 10*deltay))
 
    # Line 22
    E22 = calculate_extrusion(E21, deltax, u1, R, v)
    gcode.append(f"G1 X{a + deltax} Y{b + 10*deltay} Z4 E{E22:.5f} F{u1}")
    coords.append((a + deltax, b + 10*deltay))

    # Line 23
    E23 = calculate_extrusion(E22, deltay, u1, R, v)
    gcode.append(f"G1 X{a + deltax} Y{b + 11*deltay} Z4 E{E23:.5f} F{u1}")
    coords.append((a + deltax, b + 11*deltay))
    
    # Line 24
    E24 = calculate_extrusion(E23, deltax, u1, R, v)
    gcode.append(f"G1 X{a} Y{b + 11*deltay} Z4 E{E24:.5f} F{u1}")
    coords.append((a, b + 11*deltay))
    
    # Line 25
    E25 = calculate_extrusion(E24, deltay, u1, R, v)
    gcode.append(f"G1 X{a} Y{b + 12*deltay} Z4 E{E25:.5f} F{u1}")
    coords.append((a, b + 12*deltay))
    
    # Line 26
    E26 = calculate_extrusion(E25, deltax, u1, R, v)
    gcode.append(f"G1 X{a + deltax} Y{b + 12*deltay} Z4 E{E26:.5f} F{u1}")
    coords.append((a + deltax, b + 12*deltay))
    
    # Line 27
    E27 = calculate_extrusion(E26, deltay, u1, R, v)
    gcode.append(f"G1 X{a + deltax} Y{b + 13*deltay} Z4 E{E27:.5f} F{u1}")
    coords.append((a + deltax, b + 13*deltay))
    
    # Line 28
    E28 = calculate_extrusion(E27, deltax, u1, R, v)
    gcode.append(f"G1 X{a} Y{b + 13*deltay} Z4 E{E28:.5f} F{u1}")
    coords.append((a, b + 13*deltay))
    
    # Line 29
    E29 = calculate_extrusion(E28, deltay, u1, R, v)
    gcode.append(f"G1 X{a} Y{b + 14*deltay} Z4 E{E29:.5f} F{u1}")
    coords.append((a, b + 14*deltay))
    
    # Line 30
    E30 = calculate_extrusion(E29, deltax, u1, R, v)
    gcode.append(f"G1 X{a + deltax + 10} Y{b + 14*deltay} Z4 E{E30:.5f} F{u1}")
    coords.append((a + deltax + 10, b + 14*deltay))
    
    # Line 31
    E31 = calculate_extrusion(E30, deltay, u1, R, v)
    gcode.append(f"G1 X{a + deltax + 10} Y{b} Z0 E{E30:.5f} F{u1}")
    coords.append((a + deltax + 10, b))
    
    #Square number 4
    
    # Line 32
    E32 = calculate_extrusion(E31, deltax, u2, R, v)
    gcode.append(f"G1 X{a + 20 + 2*deltax} Y{b} Z0 E{E32:.5f} F{u2}")
    coords.append((a + 20 + 2 * deltax, b))

    # Line 33
    E33 = calculate_extrusion(E32, deltay, u2, R, v)
    gcode.append(f"G1 X{a + 20 + 2* deltax} Y{b + deltay} Z0 E{E33:.5f} F{u2}")
    coords.append((a + 20 + 2* deltax, b + deltay))
    
    # Line 34
    E34 = calculate_extrusion(E33, deltax, u2, R, v)
    gcode.append(f"G1 X{a + 20 + deltax} Y{b + deltay} Z0 E{E34:.5f} F{u2}")
    coords.append((a + 20 + deltax, b + deltay))
    
    # Line 35
    E35 = calculate_extrusion(E34, deltay, u2, R, v)
    gcode.append(f"G1 X{a + 20 + deltax} Y{b + 2*deltay} Z0 E{E35:.5f} F{u2}")
    coords.append((a + 20 + deltax, b + 2*deltay))

    # Line 36
    E36 = calculate_extrusion(E35, deltax, u2, R, v)
    gcode.append(f"G1 X{a + 20 + 2* deltax} Y{b + 2*deltay} Z0 E{E36:.5f} F{u2}")
    coords.append((a + 20 + 2* deltax, b + 2*deltay))
    
    # Line 37
    E37 = calculate_extrusion(E36, deltay, u2, R, v)
    gcode.append(f"G1 X{a + 20 + 2*deltax} Y{b + 3*deltay} Z0 E{E37:.5f} F{u2}")
    coords.append((a + 20 + 2* deltax, b + 3*deltay))
    
    # Line 38
    E38 = calculate_extrusion(E37, deltax, u2, R, v)
    gcode.append(f"G1 X{a + 20 + deltax} Y{b + 3*deltay} Z0 E{E38:.5f} F{u2}")
    coords.append((a + 20 + deltax, b + 3*deltay))
    
    # Line 39
    E39 = calculate_extrusion(E38, deltay, u2, R, v)
    gcode.append(f"G1 X{a + 20 + deltax} Y{b + 4*deltay} Z0 E{E39:.5f} F{u2}")
    coords.append((a + 20 + deltax, b + 4*deltay))
    
    # Line 40
    E40 = calculate_extrusion(E39, deltax, u2, R, v)
    gcode.append(f"G1 X{a + 20 + 2* deltax} Y{b + 4*deltay} Z2 E{E40:.5f} F{u2}")
    coords.append((a + 20 + 2 * deltax, b + 4*deltay))    

    # Line 41
    E41 = calculate_extrusion(E40, deltay, u2, R, v)
    gcode.append(f"G1 X{a + 20 + 2 * deltax} Y{b + 5*deltay} Z2 E{E41:.5f} F{u2}")
    coords.append((a + 20 + 2 * deltax, b + 5*deltay))
    
    # Line 42
    E42 = calculate_extrusion(E41, deltax, u2, R, v)
    gcode.append(f"G1 X{a + 20 + deltax} Y{b + 5*deltay} Z2 E{E42:.5f} F{u2}")
    coords.append((a + 20 + deltax, b + 5*deltay))
    
    # Line 43
    E43 = calculate_extrusion(E42, deltay, u2, R, v)
    gcode.append(f"G1 X{a + 20 + deltax} Y{b + 6*deltay} Z2 E{E43:.5f} F{u2}")
    coords.append((a + 20 + deltax, b + 6*deltay))
    
    # Line 44
    E44 = calculate_extrusion(E43, deltax, u2, R, v)
    gcode.append(f"G1 X{a + 20 + 2* deltax} Y{b + 6*deltay} Z2 E{E44:.5f} F{u2}")
    coords.append((a + 20 + 2*deltax, b + 6*deltay))
    
    # Line 45
    E45 = calculate_extrusion(E44, deltay, u2, R, v)
    gcode.append(f"G1 X{a + 20 + 2*deltax} Y{b + 7*deltay} Z2 E{E45:.5f} F{u2}")
    coords.append((a + 20 + 2*deltax, b + 7*deltay))
    
    # Line 46
    E46 = calculate_extrusion(E45, deltax, u2, R, v)
    gcode.append(f"G1 X{a + 20 + deltax} Y{b + 7*deltay} Z2 E{E46:.5f} F{u2}")
    coords.append((a + 20 + deltax, b + 7*deltay))
    
    # Line 47
    E47 = calculate_extrusion(E46, deltay, u2, R, v)
    gcode.append(f"G1 X{a + 20 + deltax} Y{b + 8*deltay} Z2 E{E47:.5f} F{u2}")
    coords.append((a + 20 + deltax, b + 8*deltay))
    
    # Line 48
    E48 = calculate_extrusion(E47, deltax, u2, R, v)
    gcode.append(f"G1 X{a + 20 + 2* deltax} Y{b + 8*deltay} Z2 E{E48:.5f} F{u2}")
    coords.append((a + 20  + 2*deltax, b + 8*deltay))
    
    # Line 49
    E49 = calculate_extrusion(E48, deltay, u2, R, v)
    gcode.append(f"G1 X{a + 20 + 2* deltax} Y{b + 9*deltay} Z2 E{E49:.5f} F{u2}")
    coords.append((a + 20 + 2*deltax, b + 9*deltay))
    
    # Line 50
    E50 = calculate_extrusion(E49, deltax, u2, R, v)
    gcode.append(f"G1 X{a + 20 + deltax} Y{b + 9*deltay} Z4 E{E50:.5f} F{u2}")
    coords.append((a + 20 + deltax, b + 9*deltay))
    
    # Line 51
    E51 = calculate_extrusion(E50, deltay, u2, R, v)
    gcode.append(f"G1 X{a + 20 + deltax} Y{b + 10*deltay} Z4 E{E51:.5f} F{u2}")
    coords.append((a + 20 + deltax, b + 10*deltay))
 
    # Line 52
    E52 = calculate_extrusion(E51, deltax, u2, R, v)
    gcode.append(f"G1 X{a + 20 + 2*deltax} Y{b + 10*deltay} Z4 E{E52:.5f} F{u2}")
    coords.append((a + 20 + 2*deltax, b + 10*deltay))

    # Line 53
    E53 = calculate_extrusion(E52, deltay, u2, R, v)
    gcode.append(f"G1 X{a + 20 + 2*deltax} Y{b + 11*deltay} Z4 E{E53:.5f} F{u2}")
    coords.append((a + 20 + 2* deltax, b + 11*deltay))
    
    # Line 54
    E54 = calculate_extrusion(E53, deltax, u2, R, v)
    gcode.append(f"G1 X{a + 20 + deltax} Y{b + 11*deltay} Z4 E{E54:.5f} F{u2}")
    coords.append((a + 20 + deltax, b + 11*deltay))
    
    # Line 55
    E55 = calculate_extrusion(E54, deltay, u2, R, v)
    gcode.append(f"G1 X{a + 20 + deltax} Y{b + 12*deltay} Z4 E{E55:.5f} F{u2}")
    coords.append((a + 20 + deltax, b + 12*deltay))
    
    # Line 56
    E56 = calculate_extrusion(E55, deltax, u2, R, v)
    gcode.append(f"G1 X{a + 20 + 2*deltax} Y{b + 12*deltay} Z4 E{E56:.5f} F{u2}")
    coords.append((a + 20 + 2*deltax, b + 12*deltay))
    
    # Line 57
    E57 = calculate_extrusion(E56, deltay, u2, R, v)
    gcode.append(f"G1 X{a + 20 + 2*deltax} Y{b + 13*deltay} Z4 E{E57:.5f} F{u2}")
    coords.append((a + 20 + 2*deltax, b + 13*deltay))
    
    # Line 58
    E58 = calculate_extrusion(E57, deltax, u2, R, v)
    gcode.append(f"G1 X{a + 20 + deltax} Y{b + 13*deltay} Z4 E{E58:.5f} F{u2}")
    coords.append((a + 20 + deltax, b + 13*deltay))
    
    # Line 59
    E59 = calculate_extrusion(E58, deltay, u2, R, v)
    gcode.append(f"G1 X{a + 20 + deltax} Y{b + 14*deltay} Z4 E{E59:.5f} F{u2}")
    coords.append((a + 20 + deltax, b + 14*deltay))
    
    # Line 60
    E60 = calculate_extrusion(E59, deltax, u2, R, v)
    gcode.append(f"G1 X{a + 2*deltax + 30} Y{b + 14*deltay} Z4 E{E60:.5f} F{u2}")
    coords.append((a + 2*deltax + 30, b + 14*deltay))
    
    # Line 61
    E61 = calculate_extrusion(E60, deltax, u2, R, v)
    gcode.append(f"G1 X{a + 2*deltax + 30} Y{b} Z0 E{E60:.5f} F{u2}")
    coords.append((a + 2*deltax + 30, b))
    
    #Square #5
    
    # Line 62
    E62 = calculate_extrusion(E61, deltax, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 3*deltax} Y{b} Z0 E{E62:.5f} F{u3}")
    coords.append((a + 40 + 3 * deltax, b))

    # Line 63
    E63 = calculate_extrusion(E62, deltay, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 3* deltax} Y{b + deltay} Z0 E{E63:.5f} F{u3}")
    coords.append((a + 40 + 3* deltax, b + deltay))
    
    # Line 64
    E64 = calculate_extrusion(E63, deltax, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 2*deltax} Y{b + deltay} Z0 E{E64:.5f} F{u3}")
    coords.append((a + 40 + 2*deltax, b + deltay))
    
    # Line 65
    E65 = calculate_extrusion(E64, deltay, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 2*deltax} Y{b + 2*deltay} Z0 E{E65:.5f} F{u3}")
    coords.append((a + 40 + 2*deltax, b + 2*deltay))

    # Line 66
    E66 = calculate_extrusion(E65, deltax, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 3* deltax} Y{b + 2*deltay} Z0 E{E66:.5f} F{u3}")
    coords.append((a + 40 + 3* deltax, b + 2*deltay))
    
    # Line 67
    E67 = calculate_extrusion(E66, deltay, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 3*deltax} Y{b + 3*deltay} Z0 E{E67:.5f} F{u3}")
    coords.append((a + 40 + 3* deltax, b + 3*deltay))
    
    # Line 68
    E68 = calculate_extrusion(E67, deltax, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 2*deltax} Y{b + 3*deltay} Z0 E{E68:.5f} F{u3}")
    coords.append((a + 40 + 2*deltax, b + 3*deltay))
    
    # Line 69
    E69 = calculate_extrusion(E68, deltay, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 2*deltax} Y{b + 4*deltay} Z0 E{E69:.5f} F{u3}")
    coords.append((a + 40 + 2*deltax, b + 4*deltay))
    
    # Line 70
    E70 = calculate_extrusion(E69, deltax, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 3* deltax} Y{b + 4*deltay} Z2 E{E70:.5f} F{u3}")
    coords.append((a + 40 + 3 * deltax, b + 4*deltay))    

    # Line 71
    E71 = calculate_extrusion(E70, deltay, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 3 * deltax} Y{b + 5*deltay} Z2 E{E71:.5f} F{u3}")
    coords.append((a + 40 + 3 * deltax, b + 5*deltay))
    
    # Line 72
    E72 = calculate_extrusion(E71, deltax, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 2*deltax} Y{b + 5*deltay} Z2 E{E72:.5f} F{u3}")
    coords.append((a + 40 + 2*deltax, b + 5*deltay))
    
    # Line 73
    E73 = calculate_extrusion(E72, deltay, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 2*deltax} Y{b + 6*deltay} Z2 E{E73:.5f} F{u3}")
    coords.append((a + 40 + 2*deltax, b + 6*deltay))
    
    # Line 74
    E74 = calculate_extrusion(E73, deltax, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 3* deltax} Y{b + 6*deltay} Z2 E{E74:.5f} F{u3}")
    coords.append((a + 40 + 3*deltax, b + 6*deltay))
    
    # Line 75
    E75 = calculate_extrusion(E74, deltay, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 3*deltax} Y{b + 7*deltay} Z2 E{E75:.5f} F{u3}")
    coords.append((a + 40 + 3*deltax, b + 7*deltay))
    
    # Line 76
    E76 = calculate_extrusion(E75, deltax, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 2*deltax} Y{b + 7*deltay} Z2 E{E76:.5f} F{u3}")
    coords.append((a + 40 + 2*deltax, b + 7*deltay))
    
    # Line 77
    E77 = calculate_extrusion(E76, deltay, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 2*deltax} Y{b + 8*deltay} Z2 E{E77:.5f} F{u3}")
    coords.append((a + 40 + 2*deltax, b + 8*deltay))
    
    # Line 78
    E78 = calculate_extrusion(E77, deltax, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 3* deltax} Y{b + 8*deltay} Z2 E{E78:.5f} F{u3}")
    coords.append((a + 40  + 3*deltax, b + 8*deltay))
    
    # Line 79
    E79 = calculate_extrusion(E78, deltay, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 3* deltax} Y{b + 9*deltay} Z2 E{E79:.5f} F{u3}")
    coords.append((a + 40 + 3*deltax, b + 9*deltay))
    
    # Line 80
    E80 = calculate_extrusion(E79, deltax, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 2*deltax} Y{b + 9*deltay} Z4 E{E80:.5f} F{u3}")
    coords.append((a + 40 + 2*deltax, b + 9*deltay))
    
    # Line 81
    E81 = calculate_extrusion(E80, deltay, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 2*deltax} Y{b + 10*deltay} Z4 E{E81:.5f} F{u3}")
    coords.append((a + 40 + 2*deltax, b + 10*deltay))
 
    # Line 82
    E82 = calculate_extrusion(E81, deltax, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 3*deltax} Y{b + 10*deltay} Z4 E{E82:.5f} F{u3}")
    coords.append((a + 40 + 3*deltax, b + 10*deltay))

    # Line 83
    E83 = calculate_extrusion(E82, deltay, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 3*deltax} Y{b + 11*deltay} Z4 E{E83:.5f} F{u3}")
    coords.append((a + 40 + 3* deltax, b + 11*deltay))
    
    # Line 84
    E84 = calculate_extrusion(E83, deltax, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 2*deltax} Y{b + 11*deltay} Z4 E{E84:.5f} F{u3}")
    coords.append((a + 40 + 2*deltax, b + 11*deltay))
    
    # Line 85
    E85 = calculate_extrusion(E84, deltay, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 2*deltax} Y{b + 12*deltay} Z4 E{E85:.5f} F{u3}")
    coords.append((a + 40 + 2*deltax, b + 12*deltay))
    
    # Line 86
    E86 = calculate_extrusion(E85, deltax, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 3*deltax} Y{b + 12*deltay} Z4 E{E86:.5f} F{u3}")
    coords.append((a + 40 + 3*deltax, b + 12*deltay))
    
    # Line 87
    E87 = calculate_extrusion(E86, deltay, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 3*deltax} Y{b + 13*deltay} Z4 E{E87:.5f} F{u3}")
    coords.append((a + 40 + 3*deltax, b + 13*deltay))
    
    # Line 88
    E88 = calculate_extrusion(E87, deltax, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 2*deltax} Y{b + 13*deltay} Z4 E{E88:.5f} F{u3}")
    coords.append((a + 40 + 2*deltax, b + 13*deltay))
    
    # Line 89
    E89 = calculate_extrusion(E88, deltay, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 2*deltax} Y{b + 14*deltay} Z4 E{E89:.5f} F{u3}")
    coords.append((a + 40 + 2*deltax, b + 14*deltay))
    
    # Line 90
    E90 = calculate_extrusion(E89, deltax, u3, R, v)
    gcode.append(f"G1 X{a + 40 + 3*deltax} Y{b + 14*deltay} Z30 E{E89:.5f} F{u3}")
    coords.append((a + 40 + 3*deltax, b + 14*deltay))
    
    return "\n".join(gcode), coords

def plot_printing_pattern(coords):
    """
    Plot the 2D printing pattern based on the coordinates.
    """
    x_vals, y_vals = zip(*coords)
    plt.figure(figsize=(6, 6))
    plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='b')
    plt.title("2D Printing Pattern")
    plt.xlabel("X (mm)")
    plt.ylabel("Y (mm)")
    plt.grid(True)
    plt.xlim(min(x_vals) - 10, max(x_vals) + 10)
    plt.ylim(min(y_vals) - 10, max(y_vals) + 10)
    plt.show()

# User inputs
deltax = float(input("Enter the value of deltax (in mm): "))
deltay = float(input("Enter the value of deltay (in mm): "))
u1 = float(input("Enter the nozzle speed (mm/min) for squares 123: "))  # Feedrate
u2 = float(input("Enter the nozzle speed (mm/min) for squares 456: "))  # Feedrate
u3 = float(input("Enter the nozzle speed (mm/min) for squares 789: "))  # Feedrate
D = float(input("Enter the nozzle diameter (mm): "))  # Nozzle radius
Gamma = float(input("Enter the shear rate (1/s): "))  # Shear rate for flow rate calculation
R = D/2  # Nozzle diameter
n = float(input("Enter the power law index (n): "))  # Power-law index for the flow rate calculation

# Calculate the flow rate (Q) based on shear rate, nozzle diameter, and power law index
Q = calculate_flow_rate(Gamma, D, n)

# Calculate the extrusion speed (v) based on the flow rate (Q) and nozzle radius (R)
v = calculate_extrusion_speed(Q, R)

# Generate G-code and store the coordinates for visualization
gcode, coords = generate_gcode(deltax, deltay, u1, u2, u3, R, v)

# Output the G-code
print("\nGenerated G-code:")
print("v")
print(gcode)

print("\n### calculated and Input Values ###")
print(f"deltax= {deltax} mm")
print(f"deltay= {deltay} mm")
print(f"u123 (nozzle speed at squares #123)= {u1} mm/min")
print(f"u456 (nozzle speed for squares #456)= {u2} mm/min")
print(f"u789 (nozzle speed for squares #789)= {u3} mm/min")
print(f"Extrusion speed (v)= {v:.5f} mm/min")
print(f"Nozzle diameter (D)= {D:.5f} mm")
print(f"Shear rate= {Gamma:.5f} 1/s")
print(f"Flow rate (Q)= {Q:.5f} mm³/min")

# Save G-code to file
with open("generated_gcode_with_visualization.gcode", "w") as f:
    f.write(gcode)

print("\nG-code saved to generated_gcode_with_visualization.gcode")

# Plot the 2D printing pattern
plot_printing_pattern(coords)
