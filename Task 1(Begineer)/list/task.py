# 1. Calculate the number of members in the Justice League.
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
num=len(justice_league)
print(num)

# 2. Batman recruited Batgirl and Nightwing as new members. Add them to your list.
justice_league.append("Batgirl , Nightwing")
print(justice_league)

# 3. Wonder Woman is now the leader of the Justice League. Move her to the beginning of the list.
justice_league.remove("Wonder Woman")
justice_league.insert(0,"Wonder Woman")
print(justice_league)

# 4. Aquaman and Flash are having conflicts, and you need to separate them.
justice_league.remove("Green Lantern")
justice_league.insert(justice_league.index("Flash"), "Green Lantern")
print( justice_league)

# 5. The Justice League faced a crisis, and Superman decided to assemble a new team. 

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("new team:", justice_league)

# 6. Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.
justice_league.sort()
print( justice_league)

# Bonus: Who is the new leader?
new_leader = justice_league[0]
print(" new leader :", new_leader)
