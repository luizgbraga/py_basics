# os relacionais têm uma leve diferença quanto a escrita
# usamos agora or, and e not (||, &&, !)

x = 2;
y = 10;

print(x > 2 and y > 5);
print(x > 2 or y > 5);

print(not x > 2 and y > 5);