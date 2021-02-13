import sys,os

def is_float(value):
    """Checks wether the parameter 'value' could be changed to a 'float'.
       Returns a boolean value."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def csv2list(filepath):
    """Return a list of tuples corresponding to a row in a CSV file.
       Empty lines are not counted and numeric values are type(float)"""
    rows =[element.split(", \n") for element in[i.strip() for i in open(filepath, 'r').readlines()]]
    rows = [i.strip().split(", ") for i in [x[len(x)-1] for x in [x for x in rows if x !=['']]]]
    for elements in rows:
        try:
            elements[0] = float(elements[0])
        except ValueError:
            pass
        finally:
            for i in range(0,len(elements)-1):
                if is_float(elements[i]):
                    elements[i] = float(elements[i])
                else:
                    pass
    return [tuple(i) for i in rows] #returns a LIST of tuples

def list2csv(L, filepath):
    """Creates or overwrite the file given in parameter 'filepath' with the content of 'L'."""
    file_content = open(filepath, "w+" )
    for _element in L:
        count = 0
        while count < len(_element)-1 :
            file_content.write("{}, ".format(_element[count]))
            count +=1
        if count == len(_element)-1 and _element == L[len(L)-1]:
            break
        elif count == len(_element)-1:
            file_content.write("{}\r\n".format(_element[count]))
    try:
        file_content.write("{}".format([i[len(i)-1] for i in L][len(L)-1])) #AQUI SE QUEDA!
    except IndexError:
        pass
    file_content.close()
    #print(open(filepath,'r').read())
    pass

def sortcsv(argv):
    """ Checks for several parameters that results, if successful on the total execution of the function itself.
       In this case, parameter 'argv' will be overwritten over the indicated path, modifying the [data]
       by the parameter given."""
    sortcolumn = 1 # Default value
    if len(argv) not in [1,2]:
        return (os.EX_USAGE,"Usage: sortcsv <filepath> [<sortcolumn>]")
    else:
        if argv[0].lower().endswith('.csv'):
            try:
                if not isinstance(argv[1],int):
                    return (os.EX_DATAERR,"Error: the sort column must be an integer")
                else:
                    if os.path.exists(argv[0]):
                        try:
                            f_path = argv[0]
                            sortcol = argv[1]
                            contenido = csv2list(f_path)
                            if sortcol < 1 or sortcol > len(contenido):
                                return (os.EX_DATAERR,"Error: cannot sort by column {}. For {} column must be 1 to {}.".format(sortcol,f_path,len(contenido[0])))
                        except:
                            return (os.EX_IOERR,"Error: could not read file")# EXCEPTION RAISE AS PER 2.3.6.1 ???
                        finally:
                            f_path = argv[0]
                            sortcol = argv[1]
                            sortcolumn = sortcol
                            contenido = csv2list(f_path)
                            data = [contenido[i] for i in range(1,len(contenido))]
                            data.sort(key=lambda row: row[sortcolumn-1])
                            data.insert(0, contenido[0])
                            list2csv(data, f_path)
                            #print("ALL GOOD!")
                    else:
                        return (os.EX_IOERR,"Error: could not read file")
            except IndexError:
                try:
                    f_path = argv[0]
                    contenido = csv2list(f_path)
                    data = [contenido[i] for i in range(1,len(contenido))]
                    data.sort(key=lambda row: row[sortcolumn-1])
                    data.insert(0, contenido[0])
                    list2csv(data, f_path)
                    #print("ALL GOOD!")
                except:
                    if not os.path.exists(argv[0]):
                        return (os.EX_IOERR,"Error: could not read file")
        else:
            return (os.EX_DATAERR,"Error: sortcsv only works on .csv files")
    return (os.EX_OK,"")

if __name__ == "__main__":
    exit_code, message = sortcsv(sys.argv[1:])
    print(message)
    exit(exit_code)
