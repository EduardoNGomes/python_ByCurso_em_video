#Tipos de dados

n1 = input('Digite algo ')
print('O tipo primitivo desse valor e {}!'.format(type(n1)))
print('So tem espacos? {}!'.format(n1.isspace()))
print('E um numero? {}!'.format(n1.isnumeric()))
print('E alfabetico? {}!'.format(n1.isalpha()))
print('E alfanumerico? {}'.format(n1.isalnum()))
print('Esta em maiusculas? {}'.format(n1.isupper()))
print('Esta em minuscula? {}'.format(n1.islower()))
print('Esta capitalizada? {}'.format(n1.istitle()))
