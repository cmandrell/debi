# This is based on Jeff O's version 3 script.
# It's written for sharpcap's IronPython interpreter
# You must have the Pro version sharpcap ($18/year) to use it.


# set Output format to FITS
# set colour space to mono16
# 8 bit will not work
# set capture area to Full Sensor
# set binning to 1
# You Must Have Google Desktop G:\Drive setup for this script to work https://www.google.com/drive/download/
# This script writes to LiveTest LunarEclipse07112022 folder


import time
import os
from SharpCap.UI import CaptureLimitType
from System import TimeSpan

for q in range (0,200):
    print("1ms File1 has been created")
    SharpCap.SelectedCamera = SharpCap.Cameras[0]
    SharpCap.SelectedCamera.Controls.Exposure.ExposureMs = 1.0
    SharpCap.Settings.CaptureFolder = r'G:\.shortcut-targets-by-id\1m-ssz9RCqSr0kBxhFcc3yI-IHx80j3su\LiveTests\LunarEclipse07112022'
    SharpCap.TargetName = "Observer1_LunarEclipse11072022_1ms"
    SharpCap.SelectedCamera.CaptureSingleFrame()
    print("60ms File2 has been created")    
    SharpCap.SelectedCamera.Controls.Exposure.ExposureMs = 60.0
    SharpCap.Settings.CaptureFolder = r'G:\.shortcut-targets-by-id\1m-ssz9RCqSr0kBxhFcc3yI-IHx80j3su\LiveTests\LunarEclipse07112022'
    SharpCap.TargetName = "Observer1_LunarEclipse11072022_60ms"
    SharpCap.SelectedCamera.CaptureSingleFrame() 
    print("600ms File3 has been created")    
    SharpCap.SelectedCamera.Controls.Exposure.ExposureMs = 600.0
    SharpCap.Settings.CaptureFolder = r'G:\.shortcut-targets-by-id\1m-ssz9RCqSr0kBxhFcc3yI-IHx80j3su\LiveTests\LunarEclipse07112022'
    SharpCap.TargetName = "Observer1_LunarEclipse11072022_600ms"
    SharpCap.SelectedCamera.CaptureSingleFrame() 
    print("9s File4 has been created")    
    SharpCap.SelectedCamera.Controls.Exposure.ExposureMs = 9000.0
    SharpCap.Settings.CaptureFolder = r'G:\.shortcut-targets-by-id\1m-ssz9RCqSr0kBxhFcc3yI-IHx80j3su\LiveTests\LunarEclipse07112022'
    SharpCap.TargetName = "Observer1_LunarEclipse11072022_9s"
    SharpCap.SelectedCamera.CaptureSingleFrame()       
    
    while True:
      if not SharpCap.SelectedCamera.Capturing :
        break
      time.sleep(0.5) 
    time.sleep(59)

