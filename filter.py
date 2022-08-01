# o filter retorna uma array de tamanho menor ou igual à original
# esse método aplica uma condição para filtrar elementos da array

def is_even(x):
    if (x % 2 == 0):
        return True;
    else:
        return False;

seq = [1, 2, 3, 4, 5, 6];

evens = list(filter(is_even, seq));

print(evens);

# ou, com lambda functions:

odds = list(filter(lambda x : x % 2 != 0, seq));

print(odds);