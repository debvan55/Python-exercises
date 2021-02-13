#Exercise 6

def lett_M():
    print('#   #')
    print('## ##')
    print('# # #')
    print('#   #')
    print('#   #')
    print(' ')
    
def lett_I():
    print(' ### ')
    print('  #  ')
    print('  #  ')
    print('  #  ')
    print(' ### ')
    print(' ')
    
def lett_S():
    print(' ####')
    print('#    ')
    print(' ### ')
    print('    #')
    print('####')
    print(' ')
    
def lett_P():
    print('#### ')
    print('#   #')
    print('#### ')
    print('#    ')
    print('#    ')
    print(' ')
    
def syllab_1(f,f2):
    f()
    f2()

def syllab_2ice(f,f2,f3):
    def again():
        f()
        f2()
        f3()
    again()
    again()
        
def print_mississippi():
    syllab_1(lett_M,lett_I)
    syllab_2ice(lett_S,lett_S,lett_I)
    lett_P(), syllab_1(lett_P,lett_I)

print_mississippi()