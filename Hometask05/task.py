import os

def parse_file_path(file_path):
    file_name, file_ext = os.path.splitext(os.path.basename(file_path))
    return (os.path.dirname(file_path), file_name, file_ext)



data = {'name1': 100, 'name2': 200, 'name3': 300}
premias = ['10.25%', '5.50%', '7.75%']
result = {name: data[name] * float(premia.strip('%')) / 100 for name, premia in zip(data.keys(), premias)}
print(result)



def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b