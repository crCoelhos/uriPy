n = int(input()); #quantidade de grupos

for i in range(n):
    entrada = [int(x) for x in str(input()).split()]; #quantidade de alunos + numero secreto
    alunos = entrada[0];
    scrt = entrada[1];
    entrada = [int(x) for x in str(input()).split()]; #chute dos alunos
    a = 999 #indexador;
    indice = 999 #indexador;
    
    for j in range(alunos): #se a diferença entre o palpite 1 e a senha for menor que a diferença entre o palpite 2 e a senha, palpite 1 chegou mais perto
        if a > abs(scrt - entrada[j]):
            a = abs(scrt - entrada[j]);
            indice = j;
    print(indice + 1);