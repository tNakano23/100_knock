import random

def p10(s):
    t = s.split()

    new_words = []
    for u in t:
        if not len(u) <= 4:
            u_inner = (''.join(random.sample(u[1:-1], len(u[1:-1]))))
            u = u[0] + u_inner + u[-1]
        new_words.append(u)
    new_words = " ".join(new_words)
    return new_words

s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(p10(s))
   # I colund’t bleeive that I cuold atlucaly unsdnaetrd what I was reanidg : the pnmeohaenl power of the human mind .
    