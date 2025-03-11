import os

import cv2

from .utils import rotate_360_image


def launch_ui(image_path):
    # Preserve transparency if PNG
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # Extract file extension
    file_extension = os.path.splitext(image_path)[-1].lower()

    # Create a window
    cv2.namedWindow("360° Image Rotation", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("360° Image Rotation", 1000, 500)

    def do_nothing(x):
        pass

    # Create trackbars for Roll, Pitch, and Yaw
    cv2.createTrackbar("Pitch", "360° Image Rotation",
                       180, 360, do_nothing)  # -180 to 180
    cv2.createTrackbar("Yaw", "360° Image Rotation", 180,
                       360, do_nothing)    # -180 to 180
    cv2.createTrackbar("Roll", "360° Image Rotation",
                       180, 360, do_nothing)   # -180 to 180

    # Real-time adjustment loop
    pitch, yaw, roll = 0, 0, -9999
    try:
        while True:
            # Get trackbar positions
            last_pitch, last_yaw, last_roll = pitch, yaw, roll

            pitch = cv2.getTrackbarPos("Pitch", "360° Image Rotation") - 180
            yaw = cv2.getTrackbarPos("Yaw", "360° Image Rotation") - 180
            roll = cv2.getTrackbarPos("Roll", "360° Image Rotation") - 180

            if (pitch, yaw, roll) != (last_pitch, last_yaw, last_roll):
                # Apply transformations
                rotated_img = rotate_360_image(img, pitch, yaw, roll)

            # Show image
            cv2.imshow("360° Image Rotation", rotated_img)

            # Press 's' to save, 'q' to quit
            key = cv2.waitKey(10)
            if key == ord('s'):
                # Ensure high-quality saving
                save_path = "adjusted_360_image" + file_extension
                if file_extension in ['.jpg', '.jpeg']:
                    cv2.imwrite(save_path, rotated_img, [
                                cv2.IMWRITE_JPEG_QUALITY, 100])
                elif file_extension == '.png':
                    cv2.imwrite(save_path, rotated_img, [
                                cv2.IMWRITE_PNG_COMPRESSION, 0])
                else:
                    cv2.imwrite(save_path, rotated_img)
                print(f"Image saved as {save_path} with maximum quality!")
            elif key == ord('q'):
                break
    except cv2.error:
        pass

    cv2.destroyAllWindows()


if __name__ == "__main__":
    launch_ui('efd6e4e489abc775c16b1d743682354376d0c1b9.jpeg')
