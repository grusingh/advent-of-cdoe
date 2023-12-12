def read_input(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()
    values = []
    for line in lines:
        values.append(line.strip())
    return values


def write_matrix_to_file(matrix, file_name):
    with open(file_name, "w") as f:
        for row in matrix:
            f.write("".join(map(str, row)))
            f.write("\n")
