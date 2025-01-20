def cipher(s):
    new_str = ""
    for t in s:
        if t.islower():
            t = chr(219 - (ord(t)))
        new_str+=str(t)
    return new_str

print(cipher("abc123ABC"))
# zyx123ABC
print(cipher("zyx123ABC"))
# abc123ABC