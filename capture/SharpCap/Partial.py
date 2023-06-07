# Capture .ser files for 2 seconds at 1000x1000 resolution
#
# Uses user settings for exposure and gain
# Forces resolution, binning, colour space
# Returns to users resolution
#####################################################################################

import time
 
path = r'C:\DEB\Partial' # path for main capture folder

### Initial Setup ####################################################################
SharpCap.Settings.UseSubFolders = False
SharpCap.Settings.CaptureFolder = path
SharpCap.TargetName = 'partial'
SharpCap.SelectedCamera = SharpCap.Cameras[0]
SharpCap.SelectedCamera.LiveView = True

#reset values for returning at end of collection
reset_area = SharpCap.SelectedCamera.Controls.Resolution.Value

#Force values
SharpCap.SelectedCamera.Controls.Binning.Value = '1'
SharpCap.SelectedCamera.Controls.OutputFormat.Automatic = False
SharpCap.SelectedCamera.Controls.ColourSpace.Value = 'MONO16'
SharpCap.SelectedCamera.Controls.Resolution.Value = '1000x1000'

### Capture images ####################################################################
local_time = time.localtime()
str_time = time.strftime("%Y-%m-%dT%H_%M_%S",local_time)

SharpCap.SelectedCamera.Controls.OutputFormat.Value = 'PNG file (*.png)'
SharpCap.SelectedCamera.CaptureSingleFrameTo(path+r'\partial '+str_time+'.png')

SharpCap.SelectedCamera.Controls.OutputFormat.Value = 'SER file (*.ser)'   
SharpCap.SelectedCamera.PrepareToCapture()
SharpCap.SelectedCamera.RunCapture()
time.sleep(2)
SharpCap.SelectedCamera.StopCapture()  

### Reset resolution ###################################################################
SharpCap.SelectedCamera.Controls.Resolution.Value = reset_area 

# END OF PROGRAM