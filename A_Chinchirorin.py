Dice = list(map(int, input().split()))

if Dice[0]==Dice[1]:
    print(Dice[2])
elif Dice[0]==Dice[2]:
    print(Dice[1])
elif Dice[1]==Dice[2]:
    print(Dice[0])
else:
    print(0)