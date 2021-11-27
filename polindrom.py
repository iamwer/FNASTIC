s = input()
s = s.lower()

rev_s = s[::-1]
print('Yes', s == rev_s)
print('No', s != rev_s)

