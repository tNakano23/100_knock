s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
t = s.split()
u = []

for v in t:
    v = v.strip(".").strip(",")
    u.append(len(v))

print(u)
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]