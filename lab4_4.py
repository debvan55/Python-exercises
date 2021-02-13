#Lab 4 Exercise 4

def is_numeric(n):
    """Takes one parameter and checks; it returns a boolean value."""
    func_input = isinstance(n,(int,float))
    if func_input:
        return func_input
    return func_input

def series(r1,r2):
    """Outputs the resistance of the series circuit:
       using the 'series_Ohms' expression """
    if is_numeric(r1):
        if is_numeric(r2):
            series_Ohms = r1+r2 # Ω Series expression
            return series_Ohms
        pass
    return None
    
def parallel(r1,r2):
    """Outputs the resistance of the parallel circuit:
       using the 'parallel_Ohms' expression """
    if is_numeric(r1):
        if is_numeric(r2):
            parallel_Ohms = 1/(1/r1+1/r2) # Ω Parallel expression
            return parallel_Ohms
        pass
    return None

#4.3 Use the series and parallel functions you just created
#to write a SINGLE print statement that calculates
#the total resistance of the following circuit.

#dos = series(parallel(8,8),2)
#tres= series(parallel(4,12),3)
#cuatro = parallel(dos,tres)
#cinco = series(cuatro,7)
#seis= series(parallel(series(parallel(8,8),2),series(parallel(4,12),3)),7)

print(series(parallel(series(parallel(8,8),2),series(parallel(4,12),3)),7))