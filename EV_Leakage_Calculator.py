def calculate_leakage_resistances_and_max_leakage_current():
    # Ask for the resistor values
    r1_value = float(input("Enter the value for R1 in ohms (Ω), if not 100kΩ: ") or 100000)
    #r2_value = float(input("Enter the value for R2 in ohms (Ω), if not 100kΩ: ") or 100000)

    # Ask for the voltage measurements
    v_battery = float(input("Enter the voltage of the EV battery from +Vb to -Vb (V): "))
    vl1 = float(input("Enter the voltage from the positive terminal to earth without any resistors (V): "))
    vl2 = float(input("Enter the voltage from the negative terminal to earth without any resistors (V): "))
    # Connect R1 and measure
    V1 = float(input("Now, connect R1. Enter the voltage from the positive terminal to earth with R1 connected (V): "))

    
    Vbattery = v_battery
    VL1 = vl1
    VL2 = vl2
    R1 = r1_value
    # Calculate the leakage resistances
    LEAK1 = R1 * (-V1 * VL1 - V1 * VL2 + VL1 * Vbattery) / (V1 * VL2)
    LEAK2 = (v_battery - V1) / (V1/r1_value + V1/LEAK1)
    Ileak = v_battery / (LEAK1 + LEAK2) * 1000


    # Calculate the maximum leakage current limited by the opposite leakage resistance and convert to mA
    max_leakage_current_pos_mA = (v_battery / LEAK2 * 1000) if LEAK2 != float('inf') else 'Undefined'
    max_leakage_current_neg_mA = (v_battery / LEAK1 * 1000) if LEAK1 != float('inf') else 'Undefined'

    # Print the results in mA
    print(f"\nEstimated leakage resistance from positive terminal to earth: {LEAK1:.2f} Ω")
    print(f"Estimated leakage resistance from negative terminal to earth: {LEAK2:.2f} Ω")
    print(f"Leakage current: {Ileak} mA")
    print(f"Maximum leakage current limited by LEAK2 if positive terminal is connected to earth: {max_leakage_current_pos_mA} mA")
    print(f"Maximum leakage current limited by LEAK1 if negative terminal is connected to earth: {max_leakage_current_neg_mA} mA")

# Uncomment the last line and run this function in a Python environment that supports input
calculate_leakage_resistances_and_max_leakage_current()
