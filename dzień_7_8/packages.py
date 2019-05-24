# pakiet jest folderem, ktory zawiera w sobie jeden lub wiecej modul
# oraz plik __init__.py
# plik ten jest KONIECZNY aby poinformowac Pythona, ze dany folder jest modulem
# plik __init__.py moze, ale nie musi byc pusty

# importowanie metoda 1
# from my_package import module_in_package
#
# module_in_package.function_four()

# importowanie metoda 2
# import my_package.module_in_package
#
# my_package.module_in_package.function_four()

# importowanie z uzyciem as
# import my_package.module_in_package as m1
# from package_name.module_name import function_name as function_x
# m1.function_four()

# ex78_packages.py

# wiecej o __init__.py

#__init__.py MOZE byc pusty i w tej roli słuzy jedynie do poinformowania Pythona,
# ze dany folder jest pakietem

# __init__.py moze rowniez zawierac wewnętrzną konfiguracje, np.:
# from .moduł import funkcja
# from pakiet.moduł import funkcja
#(konieczna kropka lub nazwa pakietu, ponieważ Python
# będziesz szukał nazwy modułu w katalogu, z ktorego uruchamiamy skrypt!)
# parametr __all__ = ['modul1', 'modul2']
# pozwala podac liste modulow, ktore maja byc automatycznie
# zaladowane przy from pakiet import *

# sprojmy przetestowac to na pakiecie matematyka

from matematyka import *
# print(pomnoz_a_przez_b(10,20))
# print(pole_trapezu(10,20,30))

print(algebra.pomnoz_a_przez_b(10,20))
print(geometria.pole_trapezu(10,20,30))

# ex_79_packages.py
