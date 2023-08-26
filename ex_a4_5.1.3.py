h_i = int (input('Qual hora deseja iniciar?'))
h_f = int (input('Qual hora deseja terminar?'))
while ((h_i > h_f) or (h_i < 0) or (h_i > 23) or (h_f < 0) or (h_f > 23)):
    h_i = int (input('Qual hora deseja iniciar?'))
    h_f = int (input('Qual hora deseja terminar?'))
for h in range(h_i,h_f + 1):
    for m in range(0,60):
        for s in range(0,60):
            print(h,':',m,':',s,'h','.')