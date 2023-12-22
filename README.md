# EV Leakage Calculator Usage Guide

This guide provides instructions on how to use the `EV_Leakage_Calculator.py` script to estimate leakage resistances (`LEAK1` and `LEAK2`) and maximum leakage current in an Electric Vehicle (EV) battery system using the associated circuit diagram.

## Prerequisites

Before running the script, ensure you have the following:
- Python environment capable of handling `input()` statements.
- Voltage measurements from your EV battery system corresponding to the points indicated in the circuit diagram.

## Circuit Diagram

Refer to the circuit diagram available at [Leakage Circuit Diagram](https://github.com/mackelec/EVleakageCalculator/blob/main/Leakage.PNG) to identify the measurement points for voltage values required by the script.

## Running the Script

1. Start the `EV_Leakage_Calculator.py` script in a Python environment.
2. When prompted, enter the value for `R1` in ohms (Ω). If it is the standard 100kΩ, you can press Enter to use the default value.
3. Input the `Vbattery` voltage, which is the voltage across the EV battery terminals from `+Vb` to `-Vb`.
4. Provide `VL1`, the voltage from the positive terminal to the chassis (earth) without any resistors in place.
5. Provide `VL2`, the voltage from the negative terminal to the chassis (earth) without any resistors in place.
6. Connect `R1` in the circuit as shown in the diagram, and input the measured voltage `V1` from the positive terminal to the chassis (earth) with `R1` connected.

## Output

After entering all the voltage measurements, the script will calculate and display the following:
- Estimated leakage resistance from the positive terminal to earth (`LEAK1`).
- Estimated leakage resistance from the negative terminal to earth (`LEAK2`).
- The total leakage current (`Ileak`) in milliamperes (mA).
- Maximum leakage current limited by `LEAK2` if the positive terminal is connected to earth.
- Maximum leakage current limited by `LEAK1` if the negative terminal is connected to earth.

The script will print these values to the console.

## Notes

- Ensure all measurements are accurate and taken with the appropriate safety precautions.
- The script assumes ideal conditions; real-world factors may lead to variations in calculations.

## Support

For any issues or queries related to the script or measurements, please [open an issue](https://github.com/mackelec/EVleakageCalculator/issues) in this repository.
