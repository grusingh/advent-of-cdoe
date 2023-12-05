def read_input(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()
    values = []
    for line in lines:
        values.append(line.strip())
    return values
