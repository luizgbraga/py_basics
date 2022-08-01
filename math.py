# os operadores matemáticos são muito parecidos com C
import math;

# soma
print(2 + 5);

# produto
print(2 * 5);

# exponenciação
print(2 ** 5);

# divisão
print(22 / 6);

# divisão inteira
print(22 // 6);

# resto (mod)
print(22 % 6);

x = -22.34891

# valor absoluto (módulo)
print(abs(x));

# conversão para inteiro
print(int(x));

# conversão para float
print(float(x));

# números complexos: complex(re, im)
print(complex(2, 3)); 

# conjugado do número complexo
z = complex(3, 5);
print(z.conjugate());

# função piso
piso = math.floor(x);
print(piso);

# função teto
teto = math.ceil(x);
print(teto);

# fatorial
fatorial = math.factorial(5);
print(fatorial);

# exponencial (e^x)
print(math.exp(2));

# combinação simples (n escolhe k)
print(math.comb(8, 3));