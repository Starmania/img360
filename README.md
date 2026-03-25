# img360_transformer

`img360_transformer` is a Python tool for batch processing and recentering 360-degree images. It provides both a command-line interface and a graphical user interface for ease of use.

## Installation

1. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Ensure `exiftool` is installed and available in your system's PATH. You can download it from [ExifTool website](https://exiftool.org/).

## Usage

### Command-Line Interface

To use the command-line interface, run the following command:

```sh
python main.py -a -p <pitch> -y <yaw> -r <roll> <image1_or_glob> [<image2_or_glob> ...]
```

- `--auto-adjust` or `-a`: Get automagically pitch, roll, yaw from picture exif metadata (exiftool is needed).
- `--pitch` or `-p`: The pitch adjustment in degrees, float value.
- `--yaw` or `-y`: The yaw adjustment in degrees, float value.
- `--roll` or `-r`: The roll adjustment in degrees, float value.
- Optional `--quality` or `-q`: Quality of JPEG set to save the output picture, integer from 0 to 100, default 95.
- Optional `--compression` or `-c`: Compression of PNG set to save the output picture, integer from 0 to 10, default 1.
- `<image1_or_glob>`: Path to images or a glob pattern to match multiple images.

Example:

```sh
python main.py -p 0 -r -30 -y 0 -q 90 "images/*.jpg"
```

### Graphical User Interface

To launch the graphical user interface, run the following command:

```sh
python main.py <image_or_glob>
```

- `<image_or_glob>`: Path to images or a glob pattern to match multiple images, will open only the first if a list is given and no pitch, yaw, roll are provided.

Example:

```sh
python main.py "images/sample.jpg"
```

### Help

For help and usage instructions, run:

```sh
python main.py --help
```

## Potential errors

### On Windows

You may encounter the following error when running the program on Windows:

```
ImportError: DLL load failed: The specified module could not be found.
```

If this happens on Windows, make sure you have Visual C++ redistributable 2015 installed. If you are using older Windows version than Windows 10 and latest system updates are not installed, Universal C Runtime might be also required.

## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for details.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on code formatting (Black, isort).

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## Project Notes

- See [TODO.md](TODO.md) for planned features and ideas, including:
  - Implementation (or embedding) of a real 3D sphere image viewer
  - Exif metadata support
