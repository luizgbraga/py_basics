# importar biblioteca
import random;

# inteiro aleatório de a até b
aleatorio = random.randint(0, 100);

print(aleatorio);

# float aleatório de 0 a 1
rand = random.random();

print(rand);

# float aleatório de a até b
numero = random.uniform(0, 100);

print(numero);

seq = [2, 5, 8, 3, 5, 4, 9, 12, 9, 9, 11, 10, 18];

# amostra aleatória de k elementos 
print(random.sample(seq, 5));

# escolha de um elemento aleatóriod a sequência
print(random.choice(seq));