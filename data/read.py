def read_data(name_file):
    fin = open(name_file, 'rt')
    time_table = ''
    while True:
        line = fin.readline()
        if not line:
            break
        time_table += line
    return time_table