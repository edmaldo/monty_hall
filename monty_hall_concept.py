import random

print("Monty Hall Game!")
print("To win a prize you must choose between three doors: One's a winner; Two are losers.")
print("You pick a door and the host reveals there is a loser in the door next to yours.")
print("You know can now switch your original door if you please. But it that a smart choice?")
print("Here we can calculate exactly what your chances of winning will be!")


def user_prompt(prompt, default=None):
    """Allow use of default values in input."""
    prompt = f"\n {prompt} [{default}] runs or type an amount: "
    response = input(prompt)
    if not response and default:
        return default
    else:
        return response


num_runs = int(user_prompt("See outcome for", "20000"))

first_door_wins = 0
switch_door_wins = 0
doors = ['a', 'b', 'c']

for i in range(num_runs):
    winner = random.choice(doors)
    pick = random.choice(doors)

    if pick == winner:
        first_door_wins += 1
    else:
        switch_door_wins += 1


print(f"\nWins staying with original door = {first_door_wins}")
print(f"Wins if you switched doors = {switch_door_wins}")
print(f"Probability of winning with first door: {(first_door_wins / num_runs):.2}")
print(f"Probability of winning by switching: {(switch_door_wins / num_runs):.2}")

input("\n[press enter to stop program]")