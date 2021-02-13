#Lab 6 Exercise 3

def sum_region(numlist,region):
    """Returns the sum of all the elements inside the 'region'
       of the 'numlist' array of lists."""

    x_1 = region[0][0]#'region' works as two "coordenates" of the 'numlist' matrix     
    x_2 = region[1][0]
    y_1 = region[0][1]
    y_2 = region[1][1]
    
    lista_uno= []
    lista_dos = []
    
    for end in numlist[:x_2+1]:
        lista_uno.append(end[:y_2+1])
    for start in lista_uno[x_1:]:
        lista_dos.append(start[y_1:])

    new_list = []
    for i in range(len(lista_dos)):
        new_list = new_list + lista_dos[i]
    new_list = sum(new_list)
    print(new_list)
    return new_list

# var_M = [[1,2,3,4,5],[5,3,4,1,2],[4,1,5,2,3]]
# sum_region(var_M,[[1,1],[1,2]])
# sum_region(var_M, [[0,2],[2,3]])
# sum_region(var_M, [[2,3],[2,3]])
# sum_region(var_M,[[0,0],[1,2]])