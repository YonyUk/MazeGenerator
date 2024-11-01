import numpy as np

# def expand_maze(table,alpha=(2,2)):
#     x = table.shape[0] // 2 + 1 + alpha[0]*(table.shape[0] // 2)
#     y = table.shape[1] // 2 + 1 + alpha[1]*(table.shape[1] // 2)
#     new_map = np.zeros((x,y))
#     for i in range(table.shape[0] - 1):
#         for j in range(table.shape[1] - 1):
#             if table[i,j] == -1:
#                 new_map[(alpha[0] + 1)*i,(alpha[1] + 1)*j] = -1
#                 pass
#             pass
#         pass
#     for i in range(table.shape[0]):
#         new_map[i,table.shape[1] - 1] = -1