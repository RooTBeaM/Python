from turtle import clear


text1 = open('text csv/test_text_1.txt','w',encoding='UTF-8')

text1.write('sentent 1')
text1.write('sentent 2')
text1.write('sentent 3')
text1.write('\nsentent 4')
text1.write('\nsentent 5')
text1.write('\nsentent 6')

text1.close()

#################################################################

data = open('text csv/test_text_1.txt','r',encoding='UTF-8')
print(data.read())

# read specific line
print(data.readline())

data.seek(0)
print(data.readline())

data.seek(1) # text positions
print(data.readline())

# text positions
data.seek(0) 
# text positions
print(data.readline(10)) 

# continue read from last position
print(data.readlines())


data.close()

################################################################

text2 = open('text csv/test_text_2.txt','w',encoding='UTF-8')

text2.write('sentent 1')
text2.write('sentent 2')
text2.write('sentent 3')
text2.write('\nsentent 4')
text2.write('\nsentent 5')
text2.write('\nsentent 6')

text2.close()


data2 =  open('text csv/test_text_2.txt','a+',encoding='UTF-8')
print('text before editing')
data2.seek(0)
print(data2.read())

data2.write('\nsentent 7\nsentent 8')
print('text after editing')
data2.seek(0)
print(data2.read())

data2.write('\nsentent 9\nsentent 100000')
print('text after editing 2')
data2.seek(0)
print(data2.read())

data2.close()