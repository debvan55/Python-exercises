# Lab 7, Exercise 1

import random

def gimme_half(n,randVal):
    """Generates a tuple with two random values.
       Parameter 'n' returns a random number in a range of 0,'n';
       'randVal' takes a list and "choose" an item from it randomly."""
    random_value = random.randrange(1,n)
    random_choice = random.choice(randVal)
    
    return [random_value,random_choice]# Returns a list.
        
def generate_creature():
    """Generates a dictionary. Values are generated randomly with help of 'gimme_half' function."""
    #Call of Duty Operator names & their descriptions.
    cod_Ops = ["Mace","Victor Zakhaev","Farah Karim", "John Price", "Simon 'Ghost' Riley", "Sebastian Krueger"]
    op_descript = ["Sniper", "Advanced-Assault", "Mounted-Gunner", "Commando", "Elite-Trooper", "Assault-Infantry"]
    
    keyS=("aggressiveness","type","size","descriptor",)
    black_list = []
    
    for value in gimme_half(6,cod_Ops):
        black_list.append(value)
    for value in gimme_half(6,op_descript):
        black_list.append(value)
    
    black_list = dict(zip(keyS,tuple(black_list)))
    return black_list

def description(diccionario):
    """This function returns a string made with the help of dictionaries."""
    sizeS = {1:"teensy", 2:"small", 3:"midsize", 4:"large",5:"huge"}
    aggressiv = {1:"is safe for children to handle", 2:"rarely bites",3:"probably won't bite",\
                 4:"will attack if approached", 5:"wants to eat your face off"}
    string = "The "+diccionario['descriptor']+" "+diccionario['type']+" is a "+sizeS[diccionario['size']]+\
             " creature that "+aggressiv[diccionario['aggressiveness']]    
    #print(string)
    return string

def list_of_dics(lista):
    """Generates a list of dictionaries with the values of parameter 'lista'."""
    lista_deDics = [lista() for _ in range(10)]
    #print(lista_deDics)
    return lista_deDics

def menagerie_stats(creaturelist,key):
    """Returns a dictionary that is a histogram of the different values for the given 'key',
       in a list of dictionaries of 'creaturelist'."""
    status = {}#Empty dictionary
    for item in creaturelist:
        status[item[key]] = status.get(item[key],0)+1
    #print(status)
    return status
