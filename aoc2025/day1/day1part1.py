lines = open("input.txt").read().splitlines()
times_at_zero = 0
pointer = 50

for line in lines:
    pointer = (pointer + int(line[1:]) * (-1 if line[0] == "L" else 1)) % 100
    if pointer == 0: times_at_zero += 1

print("Password is", times_at_zero)

