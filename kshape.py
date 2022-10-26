#Name: Marcela Soriano Cornejo
#Email: marcela.sorianocornejo40@myhunter.cuny.edu
#Date: September 23, 2022
#This program asks user for a message and then prints the message, one fewer word per line until there is only one word, then add one word a line until becoming the original message

phrase=input('Enter a phrase: ')
words=phrase.split()

for i in range(len(words),0,-1):
    print(' '.join(words[:i]))
    
for i in range(len(words)-1):
    print(' '.join(words[:i+2]))