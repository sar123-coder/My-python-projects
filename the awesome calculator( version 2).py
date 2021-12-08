from time import sleep
print('choose what you want to do: addition,subracttion,comparition,multiplecation or divition(please type what you want to do in the exact written format )')

z=input('type your choice here: ')

if z=='comparition':
 q=int(input('enter your first number to compare: '))
 w=int(input('enter your second number to compare: '))
 print(' ')
 sleep(1)
 if q>w:
  print(q,' is greater than ',w)
 if w>q:
  print(w,' is greater than ',q)
 if q==w:
  print(q,' is equal to ',w)
 print(' ')
 print('bye')

if z=='addition':
 sleep(1)
 q=int(input('enter your first number to add: '))
 w=int(input('enter your second number to add: '))
 sleep(1)
 print(' ')
 print('the addition of the numbers you wrote are: ',q+w)
 print(' ')
 print('bye')

if z=='subracttion':
 sleep(1)
 q=int(input('enter your first number to subract: '))
 w=int(input('enter your second number to subract: '))
 sleep(1)
 print(' ')
 print('the subraction of the numbers you wrote are: ',q-w)
 print(' ')
 print('bye')

if z=='multiplecation':
 sleep(1)
 q=int(input('enter your first number to multiply: '))
 w=int(input('enter your second number to multiply: '))
 sleep(1)
 print(' ')
 print('the multiplecation of your numbers are: ',q*w)
 print(' ')
 print('bye')

if z=='divition':
 sleep(1)
 q=int(input('enter your first number to divide: '))
 w=int(input('enter your second number to divide: '))
 sleep(1)
 print(' ')
 print('the divition of your numbers are: ',q/w)
 print(' ')
 print('bye')
