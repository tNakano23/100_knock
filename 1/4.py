s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
t = s.split()
u = [1, 5, 6, 7, 8, 9, 15, 16, 19]
w = []

for i,item in enumerate(t):
  if i+1 in [1,5,6,7,8,9,15,16,19]:
    w.append(item[:1])
  else:
    w.append(item[:2])

x = {item: index+1 for index, item in enumerate(w)}

print(x)
# {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20}


