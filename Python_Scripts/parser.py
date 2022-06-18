fid = open('/home/otavio/Downloads/VTM_16/Python_Scripts/ChairQP32/4x4.csv','r')

for line in fid:
    values = line.split(';')
    #Posicao
    posicao = values[0].split(',')
    print('Posicao (poc, x, y, depth, qt, bt, tt):')
    print(str(posicao).replace('[','').replace(']','').replace("'",''))
    print()

    #Best
    best = values[7].split(',')
    print('\tBest (lfnstIdx,mtsflag,mip,mipt,isp,mrl,mode,cost')
    print("\t\t"+str(best).replace('[','').replace(']','').replace("'",'').replace('\\n',''))
    print()

fid.close()