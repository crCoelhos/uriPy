n,m = map(int,input().split())
mat = []
resposta = None #so pra facilitar na intergação com a soma la na frente

for i in range(n): #inserção de N linhas de valores
    produtividade = input();
    lista = produtividade.split();
    listai = [];

    for x in lista:
        listai.append(int(x));
    mat.append(listai);


for i in range(n): #faz a soma do trilho
    soma = 0;
    for j in range(m):
        soma = soma+mat[i][j];
    if resposta == None:
        resposta = soma;
    else:
        resposta = max(resposta, soma);

for j in range(m):
    soma = 0;
    for i in range(n):
        soma = soma+mat[i][j];

    resposta = max(resposta, soma); #max() tira o maior do array pra exibir a resposta

print(resposta);