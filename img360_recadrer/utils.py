import cv2
import numpy as np


def rotate_360_image(img, pitch, yaw, roll):
    """Applies roll, pitch, and yaw transformations to a 360° image."""
    height, width = img.shape[:2]

    pitch, yaw, roll = np.radians([pitch, yaw, roll])

    # Rotation matrices
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(pitch), -np.sin(pitch)],
                   [0, np.sin(pitch), np.cos(pitch)]])

    Ry = np.array([[np.cos(yaw), 0, np.sin(yaw)],
                   [0, 1, 0],
                   [-np.sin(yaw), 0, np.cos(yaw)]])

    Rz = np.array([[np.cos(roll), -np.sin(roll), 0],
                   [np.sin(roll), np.cos(roll), 0],
                   [0, 0, 1]])

    R = Rz @ Ry @ Rx  # Apply Roll → Yaw → Pitch order

    lon = (np.linspace(0, width-1, width) / width) * 2 * np.pi - np.pi
    lat = (np.linspace(0, height-1, height) / height) * np.pi - np.pi / 2
    lon, lat = np.meshgrid(lon, lat)

    x = np.cos(lat) * np.cos(lon)
    y = np.cos(lat) * np.sin(lon)
    z = np.sin(lat)

    # Apply rotation
    xyz = np.dot(R, np.array([x.flatten(), y.flatten(), z.flatten()]))

    lat_new = np.arcsin(xyz[2]).reshape(height, width)
    lon_new = np.arctan2(xyz[1], xyz[0]).reshape(height, width)

    # Convert back to pixel coordinates
    map_x = ((lon_new + np.pi) / (2 * np.pi) * width).astype(np.float32)
    map_y = ((lat_new + np.pi / 2) / np.pi * height).astype(np.float32)

    return cv2.remap(img, map_x, map_y, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_WRAP)
