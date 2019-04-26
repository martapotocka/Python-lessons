# przy uzyciu lambdy i funkcji map() stworz liste
# zawierajaca kazda kolejna litere podanego stringa zapisana trzy razy

# przyklad: dla stringa 'ab' ma powstac lista ['aaa', 'bbb']
# d = 'ab'
# s = 'anakonda'
#
# Z = list(map(lambda c:c*3 , s))
# R = list(map(lambda c:c*3 , d))
# print(Z)
# print(R)

L = ['ab', 'anakonda', 'pyton']

def multiply_each_letter_by_3(list_of_strings):
    for string in list_of_strings:
        print(list(map(lambda c:c*3, string)))

multiply_each_letter_by_3(L)







# L = list(map(lambda l: l*3, s))
# print(L)
