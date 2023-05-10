# Capture of different exposures for number of sets of exposures,
#                                    time of run
#                                    or continuous loop of sets
# Camera in Still Mode for captures
# resets to Live mode with original exposure/gain/resolution after run
#           
# Authors:  Chris Mandrell
#           Matt Penn
# Written: 3/20/2023
# Last Edit: 4/4/2023 CM
#####################################################################################

import time
#from datetime import datetime

#date_form = datetime.now().strftime("%d_%b_%Y") 

### List of variables to be changed by user (User Input) #########################################
path = r'C:\DEB\Exmouth\NoFilter\Totality' # path for folder
#run_name = "bob"

between_exp = 0.0 # time between each exposure (seconds)
between_set = 0.0 # time between sets of exposures in exposure List (seconds)

exposure = ( 0.4, 4.0, 40.0, 400.0, 4000.0 ) # exposure tuple (ms)

Time = True # Allow capture control by time
duration = 120.0 # time in seconds - full pass of exposures even if over time

Count = False # Allow capture control by # of iterations of exposure list
number = 2 # number of iterations of exposures list

# Note: if Time and Control both False capture will run in infinite loop until manually stopped

Suppress = True # suppress camera settings data files after first iteration of captures
#####################################################################################

### Function to take images #########################################################
def Image(exposure, between_exp):

    for x in exposure:
       
        SharpCap.SelectedCamera.Controls.Exposure.ExposureMs = x
        SharpCap.SelectedCamera.CaptureSingleFrame()
        time.sleep(between_exp)
        
######################################################################################    

### Initial Setup ####################################################################

SharpCap.Settings.CaptureFolder = path
#SharpCap.TargetName = run_name

SharpCap.SelectedCamera = SharpCap.Cameras[0]
SharpCap.SelectedCamera.LiveView = False

#####reset values for returning to live mode at end of collection
reset_exp = SharpCap.SelectedCamera.Controls.Exposure.Value
reset_area = SharpCap.SelectedCamera.Controls.Resolution.Value
reset_gain = SharpCap.SelectedCamera.Controls.Gain.Value

SharpCap.SelectedCamera.Controls.Binning.Value = '1'
SharpCap.SelectedCamera.Controls.OutputFormat.Automatic = False
SharpCap.SelectedCamera.Controls.OutputFormat.Value = 'TIFF files (*.tif)'
SharpCap.SelectedCamera.Controls.ColourSpace.Value = 'MONO16'

##########Opting for selecting from max of available resolutions instead of hardcoding value that might not exist
#SharpCap.SelectedCamera.Controls.Resolution.Value = '3096x2078'
SharpCap.SelectedCamera.Controls.Resolution.Value = SharpCap.SelectedCamera.Controls.Resolution.AvailableValues[0]

SharpCap.SelectedCamera.Controls.Gain.Value = '50'

######################################################################################

### Capture images ####################################################################
if ( Time ):
    
    start = time.time()
    while ( (time.time() - start) <= duration):
        Image(exposure, between_exp)
        if Suppress:
            SharpCap.Settings.CreateCameraSettingsFile = False
        time.sleep(between_set)
        
elif ( Count ):
    i = 0
    while ( i < number ):
        Image(exposure, between_exp)
        if Suppress:
            SharpCap.Settings.CreateCameraSettingsFile = False
        i+=1
        time.sleep(between_set)
    
else:
    while ( True ):
        Image(exposure, between_exp)
        if Suppress:
            SharpCap.Settings.CreateCameraSettingsFile = False        
        time.sleep(between_set)
        
#######################################################################################

### Reset SharpCap to live mode with appropriate exposure #############################
'''
if ( SharpCap.SelectedCamera.Controls.Exposure.AutoAvailable):
    SharpCap.SelectedCamera.Controls.Exposure.Automatic = True  
else:
    SharpCap.SelectedCamera.Controls.Exposure.ExposureMs = 1.0
'''  
SharpCap.Settings.CreateCameraSettingsFile = True   
SharpCap.SelectedCamera.LiveView = True
SharpCap.SelectedCamera.Controls.Resolution.Value = reset_area 
SharpCap.SelectedCamera.Controls.Gain.Value = reset_gain 
SharpCap.SelectedCamera.Controls.Exposure.Value = reset_exp 
#######################################################################################


### END OF PROGRAM ####################################################################

'''
EDITS:

3/24/2023   CM  :   Fix bugs with running as Count
4/4/2023    CM  :   Add hardcoded camera settings in initial setup
                    Added reset values for Exposure/Resolution/Gain for returning to live mode
                    Moved run_name variable to User input section
                    
                    
'''
