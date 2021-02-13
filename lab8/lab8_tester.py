import os
import shutil
import traceback

import sortcsv
import wc

class clr:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def test(label, testf):
    try:
        if testf():
            print(f"{clr.OKGREEN}PASS: {clr.ENDC}" + label)
        else:
            print(f"{clr.FAIL}FAIL: {clr.ENDC}" + label)
    except:
        print(f"{clr.FAIL}FAIL: {clr.ENDC}" + label)
        print("Failed with this error:")
        traceback.print_exc()

print("wc tests (count_words):")

test("Empty set of lines returns (0,0,0)", lambda: (0,0,0) == wc.count_words([]))
test("Single line with single character returns (1,1,1)", lambda: (1,1,1) == wc.count_words(["a"]))
test("Single line with two characters returns (1,1,2)", lambda: (1,1,2) == wc.count_words(["ab"]))
test("Any non-whitespace characters count as characters", lambda: (1,1,6) == wc.count_words(["'a'!b?"]))
test("Non-whitespace characters count as characters but not as separate words", lambda: (1,2,6) == wc.count_words(["'a'! b?"]))
test("Two words detected in single line with two words", lambda: 2 == wc.count_words(["a b"])[1])
test("Multiple lines are detected", lambda: 2 == wc.count_words(["a", "b"])[0])
test("Whitespace-only lines don't have words or chars", lambda: (1,0,0) == wc.count_words(["   \t"]))
test("Empty lines count as lines but don't increase word count", lambda: (2,2,2) == wc.count_words(["","a b"]))
test("Sequential spaces don't increase word count", lambda: 2 == wc.count_words(["a     b"])[1])
test("Typical input yields correct result", lambda: (3, 8, 34) == wc.count_words(["The quick brown", "fox jumps over", "lazy dogs."]))
test("Works with file handle instead of list", lambda: (7, 21, 35) == wc.count_words(open("testdata/test.csv")))
print()

print("wc tests (wc):")

test("Returns exit code EX_USAGE when argv length is not 1", lambda: os.EX_USAGE == wc.wc([])[0] and os.EX_USAGE == wc.wc(['a', 'b'])[0])
test("Returns correct message when argv length is not 1", lambda: "Usage: wc <filepath>" == wc.wc([])[1] and "Usage: wc <filepath>" == wc.wc(['a', 'b'])[1])
test("Returns exit code EX_NOINPUT when path doesn't exist", lambda: os.EX_NOINPUT == wc.wc(['foo.bar'])[0])
test("Returns correct message when path doesn't exist", lambda: "The path foo.bar does not exist" == wc.wc(['foo.bar'])[1])
test("Returns exit code EX_IOERR when file can't be read", lambda: os.EX_IOERR == wc.wc(['testdata/binaryfile.png'])[0])
test("Returns correct message when file can't be read", lambda: "Could not count words in testdata/binaryfile.png" == wc.wc(['testdata/binaryfile.png'])[1])
test("Returns exit code EX_OK when everything works", lambda: os.EX_OK == wc.wc(['testdata/words.txt'])[0])
test("Returns correct message when everything works", lambda: "lines: 4, words: 26, chars: 110" == wc.wc(['testdata/words.txt'])[1])
print()


print("sortcsv tests (csv2list):")

test("Returns list", lambda: isinstance(sortcsv.csv2list("testdata/test.csv"), list))
test("Returns list of tuples", lambda: all(isinstance(sortcsv.csv2list(filepath)[0], tuple) for filepath in ["testdata/just-header.csv", "testdata/one-col.csv", "testdata/one-row.csv"]))
test("Returns [] for empty file", lambda: [] == sortcsv.csv2list("testdata/empty.csv"))
test("Skips empty lines", lambda: 3 == len(sortcsv.csv2list("testdata/empty-line.csv")))
test("Strips whitespace from individual text elements", lambda: 'header2' == sortcsv.csv2list("testdata/just-header.csv")[0][1])
test("Converts numeric values to float", lambda: 12345 == sortcsv.csv2list("testdata/one-numeric-val.csv")[1][0])
test("Returns correct list for file with only header", lambda: [('header1', 'header2', 'header3')] == sortcsv.csv2list("testdata/just-header.csv"))
test("Returns correct list for single-data-row file", lambda: [('name', 'hair', 'eyes'), ("Ali", "black", "brown")] == sortcsv.csv2list("testdata/one-row.csv"))
test("Returns correct list for single-data-column file", lambda: [('header',), ('cat',), ('dog',), ('cow',), ('horse',), ('chicken',), ('pig',), ('sheep',), ('duck',)] == sortcsv.csv2list("testdata/one-col.csv"))
expected = [
    ('name', 'age', 'weight', 'height', 'hair', 'eyes'),
    ('Ali', 42, 49.9, 1.54, 'black', 'brown'),
    ('Billie', 78, 54.43, 1.71, 'gray', 'gray'),
    ('Charlie', 34, 121.11,  1.88, 'red', 'green'),
    ('Dani', 26, 90.2, 1.9, 'blonde', 'blue')
]
test("Returns correct list for typical mixed data", lambda: expected == sortcsv.csv2list("testdata/people.csv") )
print()


print("sortcsv tests (list2csv):")
def is_correct_file(student_filepath, teacher_filepath):
    """Returns True if the student's file is the same as the contents in the teacher's file"""
    studentfile = open(student_filepath)
    teacherfile = open(teacher_filepath)
    return studentfile.readlines() == teacherfile.readlines()

def test_output(label, L, outname, cmpname=""):
    """Runs list2csv on the given list L and the output path 'output/'+outname
       then compares the output with the expected output in 'testdata/'+cmpname"""
    outpath = os.path.join("output", outname)
    cmppath = os.path.join("testdata", cmpname if cmpname else outname)
    try:
        sortcsv.list2csv(L, outpath)
        test(label, lambda: is_correct_file(outpath, cmppath))
    except:
        test(label, lambda: False)
        print("Failed with this error: ")
        traceback.print_exc()
    

def test_makes_file():
    sortcsv.list2csv([], "output/path-check.csv")
    test("Creates file in correct path", lambda: os.path.exists("output/path-check.csv"))
test_makes_file()

test_output("Produces empty file for empty list", [], "empty.csv")
test_output("Last line is NOT followed by a newline", [('a',)], "single.csv")
test_output("Produces header row correctly", [('header1', 'header2', 'header3')], "just-header.csv")
test_output("Handles numeric values without error", [['header'],[12345]], "one-numeric-val.csv")
test_output("Produces single-column CSV file correctly", [['header'], ['one'], ['two'], ['three']], "one-col.csv", "one-two-three.csv")
test_output("Produces single-row CSV file correctly", [['name', 'hair', 'eyes'], ['Ali', 'black', 'brown']], "one-row.csv")
test_output("Produces typical CSV file correctly", expected, "people.csv")

print()


print("sortcsv tests (sortcsv):")
def copy_to_output(name):
    srcpath = os.path.join("testdata", name)
    copypath = os.path.join("output", name)
    shutil.copy2(srcpath, copypath)

def test_sort(label, csvname, sortcol=""):
    """Runs sortcsv and compares its output with the expected output
       A copy of the 'testdata/'+csvname will be made in the 'output' directory
       sortcsv will run on the copy
       The result will be compared with the contents of 'testdata/'+csvname+'-sortcol
    """
    srcpath = os.path.join("testdata", csvname)
    testpath = os.path.join("output", csvname)
    shutil.copy2(srcpath, testpath)
    copy_to_output(csvname)
    cmppath = os.path.join("testdata", csvname + '-' + (str(sortcol) if sortcol!="" else "1"))
    try:
        sortcsv.sortcsv([testpath, sortcol] if sortcol != "" else [testpath])
        test(label, lambda: is_correct_file(testpath, cmppath))
    except:
        test(label, lambda: False)
        print("Failed with this error: ")
        traceback.print_exc()


test("Returns exit code EX_USAGE when argv length is not 1 or 2", lambda: os.EX_USAGE == sortcsv.sortcsv([])[0] and os.EX_USAGE == sortcsv.sortcsv(['a', 'b', 'c'])[0])
test("Returns correct message when argv length is not 1 or 2", lambda: "Usage: sortcsv <filepath> [<sortcolumn>]" == sortcsv.sortcsv([])[1] and "Usage: sortcsv <filepath> [<sortcolumn>]" == sortcsv.sortcsv(['a', 'b', 'c'])[1])
test("Returns exit code EX_DATAERR when file is not .csv", lambda: os.EX_DATAERR == sortcsv.sortcsv(['foo.bar'])[0])
test("Returns correct message when file is not .csv", lambda: "Error: sortcsv only works on .csv files" == sortcsv.sortcsv(['foo.bar'])[1])
copy_to_output('single2.CSV')
test("Does NOT return error message when file is .CSV (extension is case-insensitive)", lambda: "Error: sortcsv only works on .csv files" != sortcsv.sortcsv(['output/single2.CSV'])[1])
test("Returns exit code EX_DATAERR when sortcol is not a number", lambda: os.EX_DATAERR == sortcsv.sortcsv(['foo.csv', 'a'])[0])
test("Returns correct message when sortcol is not a number", lambda: "Error: the sort column must be an integer" == sortcsv.sortcsv(['foo.csv', 'a'])[1])
test("Returns exit code EX_IOERR when path doesn't exist", lambda: os.EX_IOERR == sortcsv.sortcsv(['foo.csv'])[0])
test("Returns correct message when path doesn't exist", lambda: "Error: could not read file" == sortcsv.sortcsv(['foo.csv'])[1])
copy_to_output('just-header.csv')
test("Returns exit code EX_DATAERR when sortcol is below 1", lambda: os.EX_DATAERR == sortcsv.sortcsv(['output/just-header.csv', 0])[0])
test("Returns correct message when sortcol is below 1", lambda: "Error: cannot sort by column 0. For output/just-header.csv column must be 1 to 3." == sortcsv.sortcsv(['output/just-header.csv', 0])[1])
copy_to_output('just-header.csv')
test("Returns exit code EX_DATAERR when sortcol is too large", lambda: os.EX_DATAERR == sortcsv.sortcsv(['output/just-header.csv', 4])[0])
test("Returns correct message when sortcol is too large", lambda: "Error: cannot sort by column 4. For output/just-header.csv column must be 1 to 3." == sortcsv.sortcsv(['output/just-header.csv', 4])[1])
copy_to_output('single2.CSV')
test("Returns exit code EX_OK when everything goes OK", lambda: os.EX_OK == sortcsv.sortcsv(['output/single2.CSV'])[0])
test("Returns empty message when everything goes OK", lambda: "" == sortcsv.sortcsv(['output/single2.CSV'])[1])


test_sort("Empty file remains empty", "empty.csv")
test_sort("Header-only file remains unchanged", "just-header.csv")
test_sort("Single-row file remains unchanged", "one-row.csv")
test_sort("Defaults to sorting by column 1 when sortcol not specified", "one-col.csv")
test_sort("Can sort by specific column (2)", "people.csv", 2)
test_sort("Can sort by specific column (5)", "people.csv", 5)
print()