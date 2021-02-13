#Exercise1
randomNum = 32
dinner = 18
itsLate = ((dinner + randomNum)%24)

print('It will be '+ str(itsLate) +':00!!, '+ str(randomNum) + ' hours late for supper at ' + str(dinner) + ':00.')

# def am_I_late(randomNum,dinner):
#     print('It will be '+ str((dinner + randomNum)%24) +':00!!, '+ str(randomNum) + ' hours late for supper at ' + str(dinner) + ':00.')
# 
# am_I_late(8,19)  