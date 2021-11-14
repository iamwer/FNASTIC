s = input()
answer = ""
s = s.lower()
for i in range(len(s)):
    if s.count(s[i]) > 1:
        answer += ")"
    else:
        answer += "("
print(answer)
