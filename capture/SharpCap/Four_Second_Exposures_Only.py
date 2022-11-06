# This is based on Jeff O's version 3 script.
# It's written for sharpcap's IronPython interpreter
# You must have the Pro version sharpcap ($18/year) to use it.


# set Output format to FITS
# set colour space to mono16
# 8 bit will not work
# set capture area to Full Sensor
# set binning to 1
# You Must Have Google Desktop G:\Drive setup for this script to work https://www.google.com/drive/download/
# This script writes to LiveTest LunarEclipse08112022 folder
# Please replace Observer___ with Observer"Your Initials Here"_
# In SharpCap settings it is best to remove all formatting to your fits file naming or you will create multiple sub_folders on the DEB drive
# **** New File and Folder name ****
# Updated 11_5_2022 I changed the date to *** 08112022 *** from 07112022
# Updated 11_6_2022
# **** This is Four Second Exposures Only ****


import time
import os

for q in range (0,360):
    print("4s File4 has been created")    
    SharpCap.SelectedCamera.Controls.Exposure.ExposureMs = 4000.0
    SharpCap.Settings.CaptureFolder = r'G:\.shortcut-targets-by-id\1m-ssz9RCqSr0kBxhFcc3yI-IHx80j3su\LiveTests\LunarEclipse08112022'
    SharpCap.TargetName = "Observer_JMW_LunarEclipse11082022_4s"
    SharpCap.SelectedCamera.CaptureSingleFrame()       
    
    while True:
      if not SharpCap.SelectedCamera.Capturing :
        break
      time.sleep(0.5) 
    time.sleep(58.8)