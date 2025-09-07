import cv2
import argparse
import glob
from pathlib import Path
import shutil

files = ["erase.png","flip.png"]
# Create a list of all the input image files
FILES = []
for i in files:
    FILES += glob.glob(i)

# Get the filename from the output path
filename = "test.mp4"
print(f'Creating video "{filename}" from images "{FILES}"')

# Load the first image to get the frame size
frame = cv2.imread(FILES[0])
height, width, layers = frame.shape
print(height,width)
# Create a VideoWriter object to write the video file
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(filename=filename, fourcc=fourcc, fps=24, frameSize=(width, height))

# Loop through the input images and add them to the video
for image_path in FILES:
    print(f'Adding image "{image_path}" to video "{filename}"... ')
    video.write(cv2.imread(image_path))

# Release the VideoWriter and move the output file to the specified location
cv2.destroyAllWindows()
video.release()
#shutil.move(filename, args.output)
