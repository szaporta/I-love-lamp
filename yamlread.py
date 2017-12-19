yaml_list = []

with open('mysql.yaml', 'r') as file_read:
    for line in file_read:
        yaml_list.append(line)
        
print(yaml_list)

with open('mysql.yaml', 'w') as file_write:
    for yaml_line in yaml_list:
        if '    # user: my_username' in yaml_line:
            file_write.write('    user: datadog\n')
        elif '    # pass: my_password' in yaml_line:
            file_write.write('    pass: hKsJzswSeY=J88vSQixGdxb1')
        else:
            file_write.write(yaml_line)
