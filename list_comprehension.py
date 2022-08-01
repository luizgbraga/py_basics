# list comprehension é criar uma nova array com operações com outra array

arr = [1, 2, 3, 4, 5];

squared = [i ** 2 for i in arr];
print(squared);

# podemos usar com ifs também
# exemplo: retornar somente números pares

even = [i for i in arr if i % 2 == 0];
print(even);

# exemplo complicado: transposição de matrizes

matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]];

transpose = [[linha[i] for linha in matriz] for i in range(4)];

print(transpose);