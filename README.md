# EV Leakage Calculator Usage Guide

This guide provides instructions on how to use the `EV_Leakage_Calculator.py` script to estimate leakage resistances (`LEAK1` and `LEAK2`) and maximum leakage current in an Electric Vehicle (EV) battery system. Follow the steps below, using the associated circuit diagram as a reference.

## Prerequisites

Before running the script, ensure you have the following:
- A Python environment capable of handling `input()` statements.
- Voltage measurements from your EV battery system according to the points indicated in the circuit diagram.

## Circuit Diagram

Refer to the circuit diagram below to identify the measurement points for voltage values required by the script:

![Leakage Circuit Diagram](https://github.com/mackelec/EVleakageCalculator/blob/main/Leakage.PNG)

## Running the Script

1. Start the `EV_Leakage_Calculator.py` script in a Python environment.
2. When prompted, enter the value for `R1` in ohms (Ω). If it is the standard 100kΩ, you can simply press Enter to use the default value.
3. Input the `Vbattery` voltage, which is the voltage across the EV battery terminals from `+Vb` to `-Vb`.
4. Provide `VL1`, the voltage from the positive terminal to the chassis (earth) without any resistors in place.
5. Provide `VL2`, the voltage from the negative terminal to the chassis (earth) without any resistors in place.
6. Connect `R1` as shown in the diagram, and input the measured voltage `V1` from the positive terminal to the chassis with `R1` connected.

## Output

The script calculates and displays:
- Estimated leakage resistance from the positive terminal to earth (`LEAK1`).
- Estimated leakage resistance from the negative terminal to earth (`LEAK2`).
- The total leakage current (`Ileak`) in milliamperes (mA).
- Maximum leakage current limited by `LEAK2` if the positive terminal is connected to earth.
- Maximum leakage current limited by `LEAK1` if the negative terminal is connected to earth.

The values will be printed to the console.

## Notes

- Accurate measurements are critical. Ensure they are taken according to the diagram and with proper safety precautions.
- The script assumes ideal conditions; real-world factors may affect the results.

## Support

For any issues or queries related to the script or measurements, please [open an issue](https://github.com/mackelec/EVleakageCalculator/issues) in this repository.
