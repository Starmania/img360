import os

import cv2

from .batch_process import process_image
from .utils import rotate_360_image


def launch_ui(image_path):
    # Preserve transparency if PNG
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # Create a window
    cv2.namedWindow("360° Image Rotation", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("360° Image Rotation", 1000, 500)

    def do_nothing(x):
        pass

    # Create trackbars for Roll, Pitch, and Yaw
    cv2.createTrackbar(
        "Pitch", "360° Image Rotation", 0, 180, do_nothing
    )  # -180 to 180
    cv2.setTrackbarMin("Pitch", "360° Image Rotation", -180)

    cv2.createTrackbar("Yaw", "360° Image Rotation", 0, 180, do_nothing)  # -180 to 180
    cv2.setTrackbarMin("Yaw", "360° Image Rotation", -180)

    cv2.createTrackbar("Roll", "360° Image Rotation", 0, 180, do_nothing)  # -180 to 180
    cv2.setTrackbarMin("Roll", "360° Image Rotation", -180)

    # Display the original image
    cv2.imshow("360° Image Rotation", rotate_360_image(img, 0, 0, 0))

    # Real-time adjustment loop
    pitch, yaw, roll = 0, 0, 0
    try:
        while True:
            # Get trackbar positions
            last_pitch, last_yaw, last_roll = pitch, yaw, roll

            pitch = cv2.getTrackbarPos("Pitch", "360° Image Rotation")
            yaw = cv2.getTrackbarPos("Yaw", "360° Image Rotation")
            roll = cv2.getTrackbarPos("Roll", "360° Image Rotation")

            if (pitch, yaw, roll) != (last_pitch, last_yaw, last_roll):
                # Apply transformations
                rotated_img = rotate_360_image(img, pitch, yaw, roll)
                cv2.imshow("360° Image Rotation", rotated_img)

            # Press 's' to save, 'q' to quit
            key = cv2.waitKey(10)
            if key == ord("s"):
                process_image(image_path, pitch, yaw, roll)
            elif key == ord("q"):
                break
    except cv2.error:
        pass

    cv2.destroyAllWindows()


if __name__ == "__main__":
    launch_ui("efd6e4e489abc775c16b1d743682354376d0c1b9.jpeg")
