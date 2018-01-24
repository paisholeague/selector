from os import system as sys
from time import sleep
from random import randint

sys("clear")

with open("matching.txt", "r") as f:
	contestants = [x.strip() for x in f.readlines()]
	f.close()

input()

for n, t in enumerate(range(0, 5)):
	sys("clear")
	print("Contestants:")
	for i in contestants:
		print(" - " + i)

	print("\n")
	dots = ""
	for i in range(0, n):
		dots += "."
	print(dots)
	sleep(1)

sys("clear")

if not len(contestants) % 2 == 0:
	if len(contestants) >= 2:
		ran = randint(0, len(contestants))
		print("Contestant " + contestants[ran] + " automatically goes through!")
		contestants.remove(contestants[ran])
	else:
		print("Contestant " + contestants[0] + " is the only contestant!")
		input()
		exit(0)

print("Matchup:")
while not len(contestants) == 0:
	if len(contestants) == 0:
		break
	p1 = contestants[randint(0, len(contestants) - 1)]
	contestants.remove(p1)
	p2 = contestants[randint(0, len(contestants) - 1)]
	contestants.remove(p2)

	print(" - " + p1 + " vs " + p2)

input()
