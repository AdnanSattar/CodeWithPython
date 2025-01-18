import hashlib

def calculate_file_hash(file_path):
    """
    Calculate the SHA-1 hash of the given file in chunks to handle large files.
    :param file_path: Path to the file to be hashed.
    :return: SHA-1 hash as a hexadecimal string.
    """
    sha1_hash = hashlib.sha1()
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(1024):  # Read the file in 1024-byte chunks
                sha1_hash.update(chunk)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except IOError as e:
        print(f"Error: Unable to read the file '{file_path}'. Details: {e}")
        return None

    return sha1_hash.hexdigest()

def compare_files(file1, file2):
    """
    Compare two files by their SHA-1 hash values.
    :param file1: Path to the first file.
    :param file2: Path to the second file.
    """
    hash1 = calculate_file_hash(file1)
    hash2 = calculate_file_hash(file2)

    if hash1 is None or hash2 is None:
        print("Comparison could not be completed due to errors.")
        return

    if hash1 == hash2:
        print("The files are identical.")
    else:
        print("The files are not identical.")

if __name__ == "__main__":
    file1 = "pd1.pdf"  # Replace with the path to your first file
    file2 = "pd1.pdf"  # Replace with the path to your second file

    compare_files(file1, file2)
