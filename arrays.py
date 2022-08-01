list = [2, 5, 2, 8, 5, 3, 3, 3, 9, 11, 2, 45, 6, 8, 15];
names = ['Biulee', 'Coinador', 'Braga'];

# tamanho da array (length)

tamanho = len(list);

print(tamanho);

# soma dos elementos

soma = sum(list);
soma_nomes = sum(names);

print(soma_nomes);

print(soma);

# máximo elemento

print(max(list));

# mínimo elemento

print(min(list));

# posição de elementos

print(list.index(max(list)));

# adicionar um elemento no final (append)

list.append(14);

print(list);

# contar ocorrências de um elemento (count)

ocorrencia = list.count(2);

print(ocorrencia);

# remover o último elemento e retorná-lo (pop)

last = list.pop();

print(list);
print(last);

# remover o i-ésimo elemento e retorná-lo (pop(i))

i = list.pop(5);

print(list);
print(i);

# odernar a array: podemos ordenar modificando a array original ou não
# sorted: não modifica, só retorna

ordered_list = sorted(list);

print(ordered_list, list);

# sort: modifica

list.sort();

print(list);

# a ordenação de palavras é por ordem alfabética:

frutas = ['uva', 'abacate', 'melão', 'melancia', 'banana', 'abacaxi', 'caju'];

frutas.sort();
print(frutas);

# inverter a array (também é um método que modifica a array original)

list.reverse();

print(list);

# remover a primeira ocorrência (remove)

list.remove(2);

print(list);

# remove todos os elementos da array

list.clear();

print(list);

# verificar se um número está na array

if 11 in list:
    print('O número 11 está na array!');

# printar todos os elementos

for el in list: 
    print(el);