# os principais loops são while (fazer algo enquanto a condição for verdadeira) e for

x = 1;

while x < 10:
	print(x);
	x += 1;

array_nums = [1, 2, 3, 4, 5];

# para itens em uma array
for i in array_nums:
	print(i);

# para itens em um intervalo
for i in range(10):
	print(i);

for i in range(90, 100): 
	print(i);

# para itens em um intervalo com passo
for i in range(0, 100, 10):
	print(i);