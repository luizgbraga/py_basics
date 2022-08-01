# para printar informações na tela, basta usar print('');

print('Hello, world!');
print("Hello, world!");

# tanto faz aspas duplas ou simples
# o ponto e vírgula é opcional

# variáveis no print...

nome = 'Luiz';

print(nome);

# ou

print('Meu nome é {}'.format(nome));

# se a variável for um número, devemos transformá-la numa string

idade = 19;

print('Meu nome é Luiz e tenho ' + str(idade) + ' anos');

print('Meu nome é {} e tenho {} anos'.format(nome, idade));