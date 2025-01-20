s = "I am an NLPer"

def n_gram(s, n):
    lst = []
    for i in range(len(s)-n+1):
        lst.append((s[i:i+n]))
    return lst

def n_gram_ex(s, n): #1行バージョン
  return [ s[i:i+n] for i in range(len(s)-n+1)]

#=====================================================

t = n_gram(s, 2)
u = n_gram_ex(s, 2)

print(t)
print(u)

# ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
# ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']

#-----------------------------------------------------

t2 = n_gram(s.split(), 2)
u2 = n_gram_ex(s.split(), 2)

print(u2)
print(t2)

# ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
# ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']

