def read_csv(file_path: str)->list[str]:
    data = []
    temp = ''
    data_temp = []
    with open(file_path, 'r') as file:
        for line in file:
            for char in line:
                if char != ';' and char != '\n':
                    temp += char
                else:
                    data_temp.append(temp)
                    temp = ''
            data.append(data_temp)
            data_temp = []
    return data

def write_csv(file_path: str,data: list[str])->str:
    with open(file_path, 'w') as csvfile:
        csvfile.write(data)
        
def join_array(data:list[str])->str:
    csv = ''
    for i in range(len(data)):
        for j in range(len(data[0])):
            if j == (len(data[0])-1):
                csv+=data[i][j]
                csv += '\n'
            else:
                csv+=data[i][j]
                csv+=';'
    return csv

def generate_id(data:list[str])->int:
    num_id = len(data)
    # for i in range(len(data)):
    #     if num_id == data[i][0]:
    #         return generate_id(data)
    return num_id
    
if __name__ == '__main__':
    data = read_csv('data/user.csv')
    print(data)
    print(join_array(data))
    print(generate_id(data))
    
    
