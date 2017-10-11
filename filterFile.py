handle = open('test.txt','r')
handle2 = open('results.txt','w')
handle2 = open('results.txt','a')

data = handle.read()

# print(data.split(',')[-1])
# handle2.write('[')
# for obj in data.split(','):
#     handle2.write('\"'+obj.split()[-1]+'\", ')
# formattedData = handle2.read()
# print(formattedData.split()[-1])
# handle2.write(']')

maxx=''
for obj in data.split():
    # print(len(list(maxx)))
    if len(list(obj)) > len(list(maxx)):
        maxx=obj
print(maxx)

handle.close()
handle2.close()
