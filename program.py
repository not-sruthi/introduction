#count words + charas in introduction

intro = input('Introduce yourself! ')
wordCount = 1
charaCount = 0
symbols= [' ', '.', ',', '/','!','?',':',';','*',"'",'"','#','@','$','%','^','&','(',')','=','+','-','_','<','>',"`",'~',']','[','\'']
for letter in intro:
    if (letter not in symbols):
        charaCount = charaCount+1
    if (letter==' '):
        wordCount = wordCount+1
    
print()
print('The number of letters in your introduction is: ', charaCount)
print()
print('The number of words in your introduction is: ', wordCount)