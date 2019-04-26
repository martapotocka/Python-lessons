# uzywajac lambdy i funkcji filter
# stworz liste wszystkich wielkich liter, jakie znajduja sie w podanym stringu

s = 'Wszyscy Ogladaja Gre O Tron'

#S = ['W', 'O', 'G', 'O', 'T']

S = list(filter(lambda letter: letter.isupper(), s))
print(S)
