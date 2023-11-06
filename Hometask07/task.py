import os

def rename_files(desired_name, num_digits, source_extension, target_extension, name_range=None):
    """
    Rename files in the current directory with the desired name and a sequential number.
    :param desired_name: str, the desired name for the files
    :param num_digits: int, the number of digits in the sequential number
    :param source_extension: str, the extension of the source files to be renamed
    :param target_extension: str, the extension of the target files after renaming
    :param name_range: tuple, optional range of characters to keep from the original filename
    """
    counter = 1
    for filename in os.listdir('.'):
        if filename.endswith(source_extension):
            if name_range:
                original_name = filename[name_range[0]:name_range[1]]
            else:
                original_name = os.path.splitext(filename)[0]
            new_name = f'{desired_name}_{counter:0{num_digits}d}.{target_extension}'
            os.rename(filename, new_name)
            counter += 1



# Rename all .jpg files in the current directory to "image_001.jpg", "image_002.jpg", etc.
rename_files('image', 3, '.jpg', 'jpg')

# Rename all .png files in the current directory to "file_01.png", "file_02.png", etc.,
# keeping only characters 2-5 from the original filename.
rename_files('file', 2, '.png', 'png', (2, 6))