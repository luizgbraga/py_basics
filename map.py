# map leva cada elemento de uma array a outro mediante a uma transformação
# ele mapeia uma array para outra

def squared(x):
    return x ** 2;

seq = [1, 2, 3, 4, 5];

squared_seq = list(map(squared, seq));

print(squared_seq);

# com funções lambda não precisamos definir a função anteriormente

doubled_seq = list(map(lambda x : 2 * x, seq));

print(doubled_seq);