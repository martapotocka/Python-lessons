S = ["aa", "aba", "1", "22", "kajak", "35", "333"]

# uzywajac list comprehension stworz liste stringow
# ktore sa dluzsze lub rowne niz 2 i maja taki sam znak na poczatku i koncu

N = [string for string in S if len(string) >= 2 if string[0] == string[-1]]
print(N)








# F = [s for s in S if len(s) > 2 if s[0] == s[-1]]
# print(F)
