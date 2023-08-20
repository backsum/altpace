from random import randrange

def rolling_dice() -> tuple: 
    first_dice = randrange(1, 7)
    second_dice = randrange(1, 7)
    dice_sum = first_dice + second_dice
    return first_dice, second_dice, dice_sum
    
first_dice, second_dice, dice_sum  = rolling_dice()
print(f"The sum of dice is {first_dice} + {second_dice} = {dice_sum}")
if dice_sum in [7, 11]:
    print("You won!")
elif dice_sum in [2, 3, 12]:
    print("You lost!")
else:
    goal_sum = dice_sum
    print(f"Now your goal sum is {goal_sum}")
    while True:
        first_dice, second_dice, dice_sum  = rolling_dice()
        print(f"The sum of dice is {first_dice} + {second_dice} = {dice_sum}")
        if dice_sum == 7:
            print("You lost!")
            break
        elif dice_sum == goal_sum:
            print("You won!")
            break