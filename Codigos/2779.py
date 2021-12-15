total = int(input());
compradas = int(input());

album = [0] * total;

while compradas:
    compradas -= 1;
    album[int(input())-1] = 1;
restante = album.count(0);

print(restante);