print('Note: please do not type anything other than rock,paper or scissors and only press enter once after you write your choice(please type in lower cases)')
from time import sleep#importing sleep module inside the time module
point_person=0#this is a variable
point_cpu=0#this is a variable
print(' ')
sleep(3)
#round one
print('round one')
q=input('choose:rock,paper,scissors: ')
if q == 'scissors':#a if statment
 print('cpu chooses rock')
 print('cpu wins round one')
 point_cpu=point_cpu+1#adding 1 to a variable
if q =='paper':
 print('cpu chooses rock')
 print("you win round one")
 point_person=point_person+1
if q =='rock':
 print("cpu chooses scissors")
 print('you win round one')
 point_person=point_person+1

print(' ')
sleep(2)
#round two
print('round two')
w=input('choose:rock,paper,scissors: ')
if w == 'scissors':
 print('cpu chooses paper')
 print('you win round two')
 point_person=point_person+1
if w =='paper':
 print('cpu chooses scissors')
 print("cpu wins round two")
 point_cpu=point_cpu+1
if w =='rock':
 print("cpu chooses scissors")
 print('you win round two')
 point_person=point_person+1

print(' ')
sleep(2)
#round three
print('round three')
e=input('choose:rock,paper,scissors: ')
if e == 'scissors':
 print('cpu chooses paper')
 print('you win round three')
 point_person=point_person+1
if e =='paper':
 print('cpu chooses ')
 print("you win round three")
 point_person=point_person+1
if e =='rock':
 print("cpu chooses paper")
 print('cpu wins round three')
 point_cpu=point_cpu+1

print(' ')
sleep(2)
#round four
print('round four')
r=input('choose:rock,paper,scissors: ')
if r == 'scissors':
 print('cpu chooses rock')
 print('cpu win round four')
 point_cpu=point_cpu+1
if r =='paper':
 print('cpu chooses rock')
 print("you win round four")
 point_person=point_person+1
if r =='rock':
 print("cpu chooses scissors")
 print('you win round four')
 point_person=point_person+1
 
print(' ')
sleep(2)
#round five
print('round five')
t=input('choose:rock,paper,scissors: ')
if t == 'scissors':
 print('cpu chooses rock')
 print('you win round five')
 point_person=point_person+1
if t =='paper':
 print('cpu chooses scissors')
 print("cpu win round five")
 point_cpu=point_cpu+1
if t =='rock':
 print("cpu chooses scissors")
 print('you win round five')
 point_person=point_person+1

print(' ')
sleep(2)
print('GAME OVER')
print(' ')
sleep(1)
if  point_cpu > point_person:
  print('cpu wins good luck next time!!!')
if  point_cpu < point_person:
  print('congratulations you win!!!')
if  point_cpu == point_person:
  print('can you please avoid typing words other than rock,paper or scissors for a pleasent experience next time you play this game.')

print(' ')
sleep(1)
print('bye')
