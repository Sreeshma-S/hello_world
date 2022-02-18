import random

total_flips = int(input("Enter number of times to flip coin: "))

tail_count = 0
head_count = 0

for i in range(0, total_flips):

    rand_output = random.uniform(0, 1)

    if rand_output < 0.5:
        tail_count += 1
    else:
        head_count += 1

tail_perc = (tail_count / total_flips) * 100
head_perc = (head_count / total_flips) * 100


print("Tails percentage : ", tail_perc)
print("Heads percentage : ", head_perc)
