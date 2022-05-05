#!/bin/bash

MountPoint=ChangeMe

# NOTE - Replace [MountPoint] in the rclone command below
# with the rclone mount point you configured in rclone config along with the drive 
# folder you are going to use to store your images to (e.g. DEB:/Sxxx )

if [ $MountPoint = ChangeMe ] ; then
    echo "Please initialize script."
    exit 1
fi

# This script works in concert with the KStars app.
# You need to have the Imagemagick and rclone packages installed on your system
# and rclone must be configured to point to the Deb.Initiative Google Drive folder
# mount point where your images are to be stored (e.g. DEB/Sxxx, as appropriate)
# This script should be placed in and run from the folder where Kstars is 
# configured to create the 'Light' folder to store Fits file images (e.g. Kstars)
# To run, open a terminal window and navigate to the Kstars folder and execute:
#    ./convertandupload.sh
# The script will run continuously in the window waiting for a Fits file to show up in the 
# Light folder and when one shows up it will convert it using Imagemagick (convert command)
# then upload the file to your defined folder on the rclone drive (rclone command) and
# then move the Fits file to the Fits folder and the jpg file to the jpgs folder.
# The script checks for new files every 10 seconds (allows time for files to finish moving)
#
# change directory to the Light folder
cd ./Light || (echo "Light folder not found" && exit 1 )
# create the Fits and jpgs folders
[[ -d Fits ]] || mkdir Fits
[[ -d jpgs ]] || mkdir jpgs
# initialize counter and loop continuously waiting for a Fits file to show up

n=1
while [ $n -lt 2 ]
do
    files=$(ls *.fits 2>/dev/null)
    for f in  $files ; do
	# convert Fits file to a jpg file - need to play games to get the filename
	# to map over to the converted file - need to figure out how to trim .fits
	echo `date` "Converting" $f
	jf=${f%.fits}.jpg
	convert $f $jf
	if [[ -r $jf ]] ; then
		echo "Uploading" $jf
		# upload to rclone drive
		rclone copy $jf $MountPoint
		# Move the fits and jpg files to the appropriate subdirectories
		mv $jf ./jpgs
	else
		echo `date` "convert $f failed?"
	fi
	# Note that if we failed somehow, move the file, anyways.
	mv $f ./Fits
	echo `date` "Conversion and Uploading Complete"
    done
    # Sleep for 10 seconds and check again
    sleep 10
done


