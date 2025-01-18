# File Hash Comparison Tool

A Python program to compare two files by calculating their SHA-1 hash values. This tool is designed to handle large files efficiently by reading them in chunks.

## Features

- **Efficient File Handling**: Reads files in small chunks to support large file sizes.
- **Robust Error Handling**: Provides informative error messages if files are missing or inaccessible.
- **Modular Design**: Code is organized into reusable functions for easy maintenance and scalability.

## Requirements

- Python 3.8 or higher

## Usage

1. Place the files you want to compare in the project directory or provide their full paths.
2. Modify the `file1` and `file2` variables in the script to specify the paths of the files to compare.
3. Run the program:
   ```bash
   python file_hash_comparison.py
   ```
4. The program will output whether the files are identical or not.

## Example

For two identical files (`example1.pdf` and `example2.pdf`), the output will be:
```
The files are identical.
```
For two different files, the output will be:
```
The files are not identical.
```

## Acknowledgements

Special thanks to the Python community for their tools and libraries that made this project possible.

## Author

- **Adnan Sattar**  
  [GitHub Profile](https://github.com/AdnanSattar)