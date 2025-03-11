import glob
import os
import sys

from img360_recadrer.batch_process import process_image
from img360_recadrer.gui import launch_ui


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--help":
        print("Usage: \npython main.py" +
              " <pitch> <yaw> <roll> <image1_or_glob> [<image2_or_glob> ...]")
        print("Or with GUI: python main.py <image>")
        sys.exit(0)

    if len(sys.argv) == 2:
        if not os.path.exists(sys.argv[1]):
            print(f"Error: {sys.argv[1]} not found!")
            sys.exit(1)
        launch_ui(sys.argv[1])
        sys.exit(0)

    if len(sys.argv) < 5:
        print("Usage: python main.py" +
              " <pitch> <yaw> <roll> <image1_or_glob> [<image2_or_glob> ...]")
        sys.exit(1)

    pitch = int(sys.argv[1]) - 180
    yaw = int(sys.argv[2]) - 180
    roll = int(sys.argv[3]) - 180
    image_patterns = sys.argv[4:]

    image_paths = []
    for pattern in image_patterns:
        image_paths.extend(glob.glob(pattern))

    for image_path in image_paths:
        process_image(image_path, pitch, yaw, roll)


if __name__ == "__main__":
    main()
