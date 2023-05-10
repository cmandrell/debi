# Capture .ser file for 5 seconds for editing
# also captures a single .png file for each .ser as quick reference
#
# Forces resolution, binning, colour space
# Returns to users resolution
#
# Uses user settings for exposure, gain, etc.
# 
# Change path variable below to match your system (Probably need to add automation of this)
#####################################################################################

import time
 
path = r'C:\DEB\Exmouth\NoFilter\Partial' # path for folder 

### Initial Setup ####################################################################

SharpCap.Settings.CaptureFolder = path

SharpCap.SelectedCamera = SharpCap.Cameras[0]
SharpCap.SelectedCamera.LiveView = True

#####reset values for returning to live mode at end of collection
reset_area = SharpCap.SelectedCamera.Controls.Resolution.Value

SharpCap.SelectedCamera.Controls.Binning.Value = '1'
SharpCap.SelectedCamera.Controls.OutputFormat.Automatic = False

SharpCap.SelectedCamera.Controls.ColourSpace.Value = 'MONO16'

##########Opting for selecting from max of available resolutions instead of hardcoding value that might not exist
#SharpCap.SelectedCamera.Controls.Resolution.Value = '3096x2078'
SharpCap.SelectedCamera.Controls.Resolution.Value = SharpCap.SelectedCamera.Controls.Resolution.AvailableValues[0]

######################################################################################

### Capture images ####################################################################
SharpCap.SelectedCamera.Controls.OutputFormat.Value = 'PNG file (*.png)'
SharpCap.SelectedCamera.CaptureSingleFrame()

SharpCap.SelectedCamera.Controls.OutputFormat.Value = 'SER file (*.ser)'   
SharpCap.SelectedCamera.PrepareToCapture()
SharpCap.SelectedCamera.RunCapture()
time.sleep(5)
SharpCap.SelectedCamera.StopCapture()  
#######################################################################################

SharpCap.SelectedCamera.Controls.Resolution.Value = reset_area 
#######################################################################################


### END OF PROGRAM ####################################################################
