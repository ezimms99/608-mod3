""" Rolling 2 six-sided dice"""
import random 

#Defining frequency counters
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0
frequency7 = 0
frequency8 = 0
frequency9 = 0
frequency10 = 0
frequency11 = 0
frequency12 = 0

trials = 6_000_000

#Defining the rolls
for roll in range(trials):
    face = random.randrange(1,7) + random.randrange(1,7)

#Adding in frequency counters
    if face == 2: 
        frequency2 += 1
    elif face == 3: 
        frequency3 += 1
    elif face == 4: 
        frequency4 += 1
    elif face == 5: 
        frequency5 += 1
    elif face == 6: 
        frequency6 += 1
    elif face == 7: 
        frequency7 += 1
    elif face == 8: 
        frequency8 += 1
    elif face == 9: 
        frequency9 += 1
    elif face == 10: 
        frequency10 += 1
    elif face == 11: 
        frequency11 += 1
    elif face == 12: 
        frequency12 += 1

#Printing results
print(f'Face{"frequency":>13}')
print(f'{2:>4}{frequency2:>13}')
print(f'{3:>4}{frequency3:>13}')
print(f'{4:>4}{frequency4:>13}')
print(f'{5:>4}{frequency5:>13}')
print(f'{6:>4}{frequency6:>13}')
print(f'{7:>4}{frequency7:>13}')
print(f'{8:>4}{frequency8:>13}')
print(f'{9:>4}{frequency9:>13}')
print(f'{10:>4}{frequency10:>13}')
print(f'{11:>4}{frequency11:>13}')
print(f'{12:>4}{frequency12:>13}')


#Calculating craps vs. wins
craps = frequency2 + frequency3 + frequency12
win = frequency7 + frequency11

print('Craps:', craps/trials)
print('Win:', win/trials)
