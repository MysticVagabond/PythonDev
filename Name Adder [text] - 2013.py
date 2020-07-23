fileName = 'Project Files/Name Adder/Code Author Adder.txt'
lineList = []
file = open(fileName, 'r')
for line in file:
    line = line[:-1]
    lineList.append(line)

file = open(fileName, 'w')
file.write('')
file = open(fileName, 'a')
for line in lineList:
    line = line + '    #AUTHOR: Stephen Fisher\n'
    file.write(line)
file.close()
input('Done')
                                                                                                                                
