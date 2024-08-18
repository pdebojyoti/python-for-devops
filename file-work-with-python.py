def update_file(file_path, key, value):
    with open(file_path, 'r') as z:
        read_line = z.readlines()
    
    with open(file_path, 'w') as z:
        for i in read_line:
            if key in i:
                z.write(key + '=' + value + '\n')
            else:
                z.write(i)

config_file = 'server.conf'
key_to_update = 'TIMEOUT'
new_value = '100'  # New maximum connections allowed

update_file(config_file, key_to_update, new_value)