lines = open("input.txt").read().splitlines()
zero_passes = 0
pointer = 50

for line in lines:
    direction = -1 if line[0] == "L" else 1
    for x in range(abs(int(line[1:]) * direction)):
        pointer = (pointer + direction) % 100
        if pointer == 0: zero_passes += 1

print("Password is", zero_passes)

