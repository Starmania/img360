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
python main.py <pitch> <yaw> <roll> <image1_or_glob> [<image2_or_glob> ...]
```

- `<pitch>`: The pitch adjustment in degrees.
- `<yaw>`: The yaw adjustment in degrees.
- `<roll>`: The roll adjustment in degrees.
- `<image1_or_glob>`: The path to the first image or a glob pattern to match multiple images.
- `[<image2_or_glob> ...]`: Additional image paths or glob patterns.

Example:

```sh
python main.py 0 -30 0 "images/*.jpg"
```

### Graphical User Interface

To launch the graphical user interface, run the following command:

```sh
python main.py <image>
```

- `<image>`: The path to a single image.

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

ImportError: DLL load failed: The specified module could not be found.?

If this happens on Windows, make sure you have Visual C++ redistributable 2015 installed. If you are using older Windows version than Windows 10 and latest system updates are not installed, Universal C Runtime might be also required.

### On Linux

When running with GUI, you may encounter the following error:

```

```

I don't know how to fix this yet. If you know how to fix this, please let me know.

## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.
