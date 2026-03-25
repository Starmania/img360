import os
import sys
import subprocess
import json
from shutil import which

import cv2

from .utils import rotate_360_image


def process_image(image_path, auto_adjust, pitch, yaw, roll, quality=95, compression=1):

    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        print(f"Error loading image {image_path}")
        return

    is_processed = True
    update_exif = True
    
    if which("exiftool") is not None:
        process = subprocess.run(["exiftool", "-j", "-XMP-GPano:PosePitchDegrees", "-XMP-GPano:PoseHeadingDegrees", "-XMP-GPano:PoseRollDegrees", image_path], text=True, capture_output=True, check=True)
        pitchyawroll = json.loads(process.stdout)[0]
    
    if auto_adjust:
        if which("exiftool") is None:
            print(
                "ExifTool is not installed or not found in PATH. Can't use --auto-adjust option without ExifTool. Please install it before proceeding."
            )
            sys.quit(1)

        elif pitchyawroll.get("PosePitchDegrees") is not None and pitchyawroll.get("PoseHeadingDegrees") is not None and pitchyawroll.get("PoseRollDegrees") is not None:
            pitch = -1 * pitchyawroll.get("PosePitchDegrees")
            yaw = -1 * pitchyawroll.get("PoseHeadingDegrees")
            roll = -1 * pitchyawroll.get("PoseRollDegrees")
            newpitch = 0
            newyaw = 0
            newroll = 0
        else:
            print(
                f"Can't find pitch, yaw, roll values in image exif metadata. Nothing to do for image {image_path}."
            )
            is_processed = False
    
    else:
        if which("exiftool") is None:
            print(
                "ExifTool is not installed or not found in PATH. Image metadata will not be copied or corrected."
            )
            update_exif = False
        elif pitchyawroll.get("PosePitchDegrees") is not None and pitchyawroll.get("PoseHeadingDegrees") is not None and pitchyawroll.get("PoseRollDegrees") is not None:
            oldpitch = pitchyawroll.get("PosePitchDegrees")
            oldyaw = pitchyawroll.get("PoseHeadingDegrees")
            oldroll = pitchyawroll.get("PoseRollDegrees")
            newpitch  = round(pitch + oldpitch, 1)
            newyaw = round(yaw + oldyaw, 1)
            newroll = round(roll + oldroll, 1)
        else:
            print(
                "Can't find pitch, yaw, roll values in image exif metadata. These values will not be updated in rotated image."
            )
            update_exif = False
            
    if is_processed:
        rotated_img = rotate_360_image(img, pitch, yaw, roll)

        # Extract file extension
        file_extension = os.path.splitext(image_path)[-1]
        save_path = os.path.join('ajusted', os.path.split(image_path)[1])

        # Ensure high-quality saving
        if file_extension.lower() in [".jpg", ".jpeg"]:
            cv2.imwrite(save_path, rotated_img, [cv2.IMWRITE_JPEG_QUALITY, quality])
        elif file_extension.lower() in [".png"]:
            cv2.imwrite(save_path, rotated_img, [cv2.IMWRITE_PNG_COMPRESSION, compression])
        else:
            cv2.imwrite(save_path, rotated_img)
        
        # Write exif metadata with pitch, yaw, roll correction if available
        if which("exiftool") is not None:
            subprocess.run(["exiftool", "-TagsFromFile", image_path, "-overwrite_original", save_path], check=True)
            if update_exif:
                subprocess.run(["exiftool", f"-XMP-GPano:PosePitchDegrees={newpitch}", f"-XMP-GPano:PoseHeadingDegrees={newyaw}", f"-XMP-GPano:PoseRollDegrees={newroll}", "-overwrite_original", save_path], check=True)

        print(
            f"Image saved as {save_path} with JPEG quality of {quality} and PNG compression of {compression}!"
        )
