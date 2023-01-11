import numpy as np



def read_matrix():
    f = open("ASC_MAT_NORM_GEN", "r")
    file_header = f.readline().split()
    num_para, num_cond_eq = int(file_header[0])+1, int(file_header[1])
    row = np.array([])
    raw_data = f.readlines()
    normal_matrix = np.zeros((num_para-1,num_para-1))
    read_position = 0
    rows = []
    for i in range(0,num_para):
        row = np.zeros((num_para-1))
        real_row = raw_data[read_position:read_position+i+1]
        for j in range(len(real_row)):
            real_row[i] = float(real_row[i].split()[0])
        read_position += i+1
        rows.append(row)
        row = np.hstack((real_row,row[len(real_row):]))
        normal_matrix[:,i] = row


    for i in range(1,num_para-1):
       normal_transpose = np.transpose(normal_matrix)
       new_part = normal_transpose[i][:i]
       oldPart = normal_matrix[i,i:] 
       new_row = np.hstack((new_part,oldPart))
       normal_matrix[i] = np.hstack((new_part,oldPart))

    f.close()
    return normal_matrix

normal_matrix=read_matrix()



