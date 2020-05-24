from code import Main

Main()

try:
    arq = open('log.txt', 'w')
    arq.close()
except:
    pass

quit()
