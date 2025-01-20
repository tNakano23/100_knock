s1 = "paraparaparadise"
s2 = "paragraph"

def n_gram_ex(s, n): #1行バージョン
  return [ s[i:i+n] for i in range(len(s)-n+1)]

X = n_gram_ex(s1, 2)
Y = n_gram_ex(s2, 2)

t = set(X) | set(Y)
u = set(X) & set(Y)
v = set(X) - set(Y)

print(t)
print(u)
print(v)

# {'pa', 'ap', 'ad', 'di', 'se', 'ar', 'gr', 'ph', 'ra', 'is', 'ag'}
# {'ra', 'pa', 'ap', 'ar'}
# {'is', 'di', 'se', 'ad'}

#-----------------------------------------------------

if "se" in X:
  print("X:exist.")
else:
  print("X:dont exist.")

if "se" in Y:
  print("Y:exist.")
else:
  print("Y:dont exist.")

# X:exist.
# Y:dont exist.
