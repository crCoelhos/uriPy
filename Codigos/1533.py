while True:
    suspeitos = int(input());#numero de suspeitos
    if(suspeitos == 0):
        break;
    grau = input().split();#grau de suspeitabilidade
    
    for i in range(suspeitos):
        grau[i] = int(grau[i]);        
    v = sorted(grau, key=int);

    for indiceS, i in enumerate(grau): #indexa a lista de suspeitos
        if i == v[suspeitos-2]:
            print(indiceS+1); #pega o segundo mais suspeito
            break;