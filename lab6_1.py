#Lab 6 Exercise 1

def is_prime(n):
    """Checks whether the input 'n' <IT IS> or <it's NOT> a prime number.
       Returns a boolean value."""
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
   
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i = i + 6
    return True
   
def filtered(lista,f_Obj):
    """Checks for the elements in the list: 'lista' using 'is_prime'
       for prime numbers and returns a new list cointaining only those elements
       in the 'lista' parameter for which the function object parameter returned True."""
    new_list = []
    for i in lista:
        if f_Obj(i):
            new_list.append(i)
        pass
    #print(new_list)
    return new_list

def filter(lista,f_Obj):
    """Checks for the elements in the 'lista' using 'is_prime' function
       for prime numbers, and returns None. The list: 'lista' will be modified
       as it checks for prime numbers."""
    for i in list(lista):
        if not f_Obj(i):
            lista.remove(i)
    #print(lista)        
    return

#mi_lista = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

#filtered(mi_lista,is_prime)
#filter(mi_lista,is_prime)