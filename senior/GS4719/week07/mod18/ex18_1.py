# file write
# fp = open('note.txt', 'w')
# fp.write('中央大學\n')
# fp.write('ncu\n')
# print('Write two data to note.txt!')
# fp.close()

fp = open('note.txt', 'a')
fp.write('ncu.edu.tw\n')
print('Append one data to note.txt!')
fp.close()
