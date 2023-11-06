import os
import json
import csv
import pickle

def get_directory_info(directory):
    """
    Recursively traverse a directory and its subdirectories and save the results to json, csv and pickle files.
    :param directory: str, the path to the directory to traverse
    """
    data = []
    for root, dirs, files in os.walk(directory):
        size = 0
        for file in files:
            filepath = os.path.join(root, file)
            size += os.path.getsize(filepath)
            data.append({'name': file, 'type': 'file', 'parent': root, 'size': os.path.getsize(filepath)})
        for dir in dirs:
            dirpath = os.path.join(root, dir)
            dir_size = get_directory_size(dirpath)
            size += dir_size
            data.append({'name': dir, 'type': 'directory', 'parent': root, 'size': dir_size})
    
    # Save to json
    with open('directory_info.json', 'w') as f:
        json.dump(data, f)
    
    # Save to csv
    with open('directory_info.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'type', 'parent', 'size'])
        for item in data:
            writer.writerow([item['name'], item['type'], item['parent'], item['size']])
    
    # Save to pickle
    with open('directory_info.pickle', 'wb') as f:
        pickle.dump(data, f)

def get_directory_size(directory):
    """
    Get the total size of a directory and all its subdirectories and files.
    :param directory: str, the path to the directory
    :return: int, the size of the directory in bytes
    """
    size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            size += os.path.getsize(filepath)
    return size

# Example usage
get_directory_info('C:/Desktop/Python_deep')