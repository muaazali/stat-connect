import os
import time
import psutil
import subprocess
import py3nvml
import clr
clr.AddReference(r'lib/OpenHardwareMonitorLib')
from OpenHardwareMonitor.Hardware import Computer
c = Computer()
c.CPUEnabled = True
c.GPUEnabled = True
c.Open()

def get_cpu_temperature():
    cpuTemps = []
    hardware = c.Hardware[0]
    for a in range(0, len(hardware.Sensors)):
        # print(hardware.Sensors[a].Identifier)
        if "/temperature" in str(hardware.Sensors[a].Identifier):
            cpuTemp = hardware.Sensors[a].get_Value()
            cpuTemps.append(cpuTemp)
            hardware.Update()
    return cpuTemps
        
def get_gpu_temperature():
    gpuTemps = []
    hardware = c.Hardware[1]
    for a in range(0, len(hardware.Sensors)):
        # print(hardware.Sensors[a].Identifier)
        if "/temperature" in str(hardware.Sensors[a].Identifier):
            gpuTemp = hardware.Sensors[a].get_Value()
            gpuTemps.append(gpuTemp)
            hardware.Update()
    return gpuTemps

def main():
    prevCpuTemps = []
    prevGpuTemps = []
    while True:
        # Get the latest temps
        cpuTemps = get_cpu_temperature()
        gpuTemps = get_gpu_temperature()
        
        # If the temps are 0, use the previous temps
        prevCpuTemps = cpuTemps
        if len(gpuTemps) > 0:
            if gpuTemps[0] == 0:
                gpuTemps = prevGpuTemps
            else:
                prevGpuTemps = gpuTemps
            
        # Print out the temps
        os.system('cls')
        if cpuTemps:
            print(f"CPU Temperature: {cpuTemps}")
        else:
            print("Unable to retrieve CPU temperature.")
            
        if gpuTemps:
            print(f"GPU Temperature: {gpuTemps}")
        else:
            print("Unable to retrieve GPU temperature.")
        time.sleep(1)

if __name__ == "__main__":
    main()