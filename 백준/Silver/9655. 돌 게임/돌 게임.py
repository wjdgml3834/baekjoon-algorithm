N = int(input())
winner = ''

if N % 2 == 1:
    winner = 'SK'
else:
    winner = 'CY'
    
print(winner)