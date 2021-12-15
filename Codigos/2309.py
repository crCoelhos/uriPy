n = int(input());
mao = []; 

contA = contB = 0; #contador de vitoria
for i in range(n): #quantidade de jogos
  maoA = maoB = 0; #contador da mão
  mao = list(map(int, input().strip().split())); #recolhe a entrada dos 6 valore
  for j in range(6): #faz a gambiarra pra dar valor as cartas e facilitar o jogo
    if mao[j] == 1:
      mao[j] = 8;
    elif mao[j] == 2:
      mao[j]= 9;
    elif mao[j] == 3:
      mao[j] = 10;
    elif mao[j] == 4:
      mao[j] = 1;
    elif mao[j] == 5:
      mao[j] = 2;
    elif mao[j] == 6:
      mao[j] = 3;
    elif mao[j] == 7:
      mao[j] = 4;
    elif mao[j] == 11:
      mao[j] = 6;
    elif mao[j] == 12:
      mao[j] = 5;
    elif mao[j] == 13:
      mao[j] = 7;

  if mao[0] >= mao[3]: #embate1
    maoA += 1;
  else:
    maoB += 1; 
    
  if mao[1] >= mao[4]: #embate2
    maoA += 1;
  else:
    maoB += 1; 
    
  if mao[2] >= mao[5]: #embate3
    maoA += 1;
  else:
    maoB += 1; 
    
  if maoA > maoB: #vitorias
    contA += 1;
  else:
    contB += 1; 
print (contA, contB);