frase = 'o rato roeu a roupa do rei de Roma';

# tamanho (length)
print(len(frase));

# concatenação
concat = frase + ' e a minha também!';
print(concat);

# um caracter da string
print(frase[2]);

# um pedaço da string
print(frase[2:11]);

# capitalizar a primeira letra somente (não modifica, só retorna)
print(frase.capitalize());

# tudo em letras maiúsuculas (não modifica, só retorna)
print(frase.upper());

# tudo em letras minúsculas (idem)
print(frase.lower());

# eliminar espaços no início e fim da string (idem)
fruta = '    banana    ';
print(fruta.strip());

# separar em qualquer caracter (idem)
print(frase.split(' '));
print(frase.split('r'));

# achar pedaços
print(frase.find('rei'));

# substituir pedaços (idem)
print(frase.replace('do rei', 'da rainha'));

# separar em quebras de linha
text = 'Oi, sou o Luiz.\nTenho 19 anos.\nEstudo no IME';
print(text.splitlines());

# capitaliza o primeiro caracter de cada palavra
print(frase.title());

# lower vira upper e vice-versa
print(frase.swapcase());
