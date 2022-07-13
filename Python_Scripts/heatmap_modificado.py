# -*- Coding: UTF-8 -*-
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

# -----
folderName = "chairqp32"

Bloco_X = 4
Bloco_Y = 16
# -----

blockSize = "%dx%d" % (Bloco_X, Bloco_Y)
fid = open('/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName+'/saida'+blockSize+'.md','r')

# @iagostorch BEGIN
# Indicam se a CU foi codificada com um modo intra tradicional, ou se alguma das novas ferramentas foi utilizada
# Olhei alguns arquivos .md no Google Drive e não encontrei nenhum caso onde 
# mais de uma flag estava ativa ao mesmo tempo (com exceção de MIP e MIPT, que é o MIP transposto -- um caso especial do MIP)
IS_MRL = np.zeros((2048, 4096))
IS_ISP = np.zeros((2048, 4096))
IS_MIP = np.zeros((2048, 4096))
IS_NORMAL = np.zeros((2048, 4096))
# As matrizes abaixo servem pra contabilizar os modos DC/Planar/Angular 
# dentro do universo dos blocos codificados com NORMAL -- i.e., modos tradicionais
IS_NORMAL_DC = np.zeros((2048, 4096))
IS_NORMAL_PLANAR = np.zeros((2048, 4096))
IS_NORMAL_ANGULAR = np.zeros((2048, 4096))
# Apenas indica quais CUs foram testadas. Usei um novo nome pra não bagunçar o que vocês já faziam
IS_TESTED = np.zeros((2048, 4096))

# Proporção de MRL, ISP, MIP ou Normal DENTRE TODOS OS BLOCOS TESTADOS
IS_MRL_RATE = np.zeros((2048, 4096))
IS_ISP_RATE = np.zeros((2048, 4096))
IS_MIP_RATE = np.zeros((2048, 4096))
IS_NORMAL_RATE = np.zeros((2048, 4096))

# Proporção de DC, Planar e Angular APENAS DENTRO DOS NORMAIS
IS_NORMAL_DC_RATE = np.zeros((2048, 4096))
IS_NORMAL_PLANAR_RATE = np.zeros((2048, 4096))
IS_NORMAL_ANGULAR_RATE = np.zeros((2048, 4096))
# @iagostorch END

print("CONTABILIZANDO OCORRENCIAS...")
prevline = ""
for line in fid:
	if "Posicao " in prevline:
		# Pega os valores da posição X e Y da CU atual
		posX = line.split(',')[1]
		posY = line.split(',')[2]
		# Posicao (poc, x, y, depth, qt, bt, tt):
		# 1, 3264, 1600, 1, 0, 0 ---> [1, 3264, 1600, 1, 0, 0]
		#                              0    1     2   3  4  5
	if "Best " in prevline:
		# Pega os valores das flags do melhor
		MIPFlag = line.split(',')[2] # 0 ou 1
		ISPFlag = line.split(',')[4] # 0 ou 1 ou 2
		MRLFlag = line.split(',')[5] # 0 ou 1
		DCFlag = line.split(',')[6] # Qualquer coisa [0,66]
		PLANARFlag = line.split(',')[6] # Qualquer coisa [0,66]
		

		# @iagostorch BEGIN
		# Armazena a mesma coisa que DCFlag e PLANARFlag, mas fica mais explícito que pode conter o índice dos modos angulares...
		ModeIdx = line.split(',')[6] 

		# Contabiliza a CU atual
		# print("Pre-For-1")
		for i in range(Bloco_Y):
			# print("Pre-For-2")
			for j in range(Bloco_X):
				# print("Testando...")
				IS_TESTED[int(posY)+i][int(posX)+j] = IS_TESTED[int(posY)+i][int(posX)+j] + 1

		# Verifica se foi MRL, ISP, MIP, ou NORMAL (normal = nenhum dos anteriores)

		# CU codificada com MRL. A ferramenta MRL suporta todos os angulares + DC, mas por enquanto não estamos intressados nisso
		if(int(MRLFlag) > 0): 
			for i in range(Bloco_Y):
				for j in range(Bloco_X):
					IS_MRL[int(posY)+i][int(posX)+j] = IS_MRL[int(posY)+i][int(posX)+j] + 1
		
		# CU codificada com ISP. A ferramenta ISP também suporta os angulares + DC + Planar, mas por enquanto não estamos interessados nisso
		elif(int(ISPFlag) > 0): 
			for i in range(Bloco_Y):
				for j in range(Bloco_X):
					IS_ISP[int(posY)+i][int(posX)+j] = IS_ISP[int(posY)+i][int(posX)+j] + 1

		# CU codificada com MIP. A ferramenta MIP suporta um conjunto de modos baseados em multiplicação matriz-vetor, 
		# e o "índice" desses modos usa a mesma flag dos modos angulares. Por enquanto não nos preocupamos com isso
		elif(int(MIPFlag) > 0): 
			for i in range(Bloco_Y):
				for j in range(Bloco_X):
					IS_MIP[int(posY)+i][int(posX)+j] = IS_MIP[int(posY)+i][int(posX)+j] + 1					

		# Se não foi MRL ou ISP ou MIP, então devemos ter feito a codificação com os modos tradicionais...
		else: 
			for i in range(Bloco_Y):
				for j in range(Bloco_X):
					# Contabilizamos que essa CU foi codificada com ALGUM MODO tradicional...
					IS_NORMAL[int(posY)+i][int(posX)+j] = IS_NORMAL[int(posY)+i][int(posX)+j] + 1								
					if(int(ModeIdx) == 0): # Além de ser um modo tradicional, é o modo PLANAR
						# print("IDX=0")
						IS_NORMAL_PLANAR[int(posY)+i][int(posX)+j] = IS_NORMAL_PLANAR[int(posY)+i][int(posX)+j] + 1
					elif(int(ModeIdx) == 1): # Além de ser um modo tradicional, é o modo DC
						IS_NORMAL_DC[int(posY)+i][int(posX)+j] = IS_NORMAL_DC[int(posY)+i][int(posX)+j] + 1
						# print("IDX=1")
					else: 
						# Não é nem Planar e nem DC, só pode ser um modo angular...
						IS_NORMAL_ANGULAR[int(posY)+i][int(posX)+j] = IS_NORMAL_ANGULAR[int(posY)+i][int(posX)+j] + 1
						# print("IDX>=2")
		# @iagostorch END

	prevline = line
# #ENDFOR

print("CONTABILIZANDO RATE...")
# @iagostorch BEGIN
for i in range(2048):
	for j in range(4096):
		if(IS_TESTED[i][j]==0): # Se não testamos essa CU, todos os rates são zero...
			# print("ENTROU NO IF")
			IS_MRL_RATE[i][j] = 0
			IS_ISP_RATE[i][j] = 0
			IS_MIP_RATE[i][j] = 0
			IS_NORMAL_RATE[i][j] = 0
			IS_NORMAL_DC_RATE[i][j] = 0
			IS_NORMAL_PLANAR_RATE[i][j] = 0
			IS_NORMAL_ANGULAR_RATE[i][j] = 0
		else:
			# print("ENTROU NO ELSE")
			# Proporção de cada modo "geral" dentre TODOS OS BLOCOS TESTADOS
			IS_MRL_RATE[i][j] = IS_MRL[i][j]/IS_TESTED[i][j]
			IS_ISP_RATE[i][j] = IS_ISP[i][j]/IS_TESTED[i][j]
			IS_MIP_RATE[i][j] = IS_MIP[i][j]/IS_TESTED[i][j]
			IS_NORMAL_RATE[i][j] = IS_NORMAL[i][j]/IS_TESTED[i][j]
			# Proporção dos modos tradicionais (DC, Planar e Angulares) APENAS DENTRO DOS BLOCOS COM PREDIÇÃO INTRA "NORMAL"
			if(IS_NORMAL[i][j]==0): # Evita divisão por zero
				IS_NORMAL_DC_RATE[i][j] = 0
				IS_NORMAL_PLANAR_RATE[i][j] = 0
				IS_NORMAL_ANGULAR_RATE[i][j] = 0
			else:
				IS_NORMAL_DC_RATE[i][j] = IS_NORMAL_DC[i][j]/IS_NORMAL[i][j]
				IS_NORMAL_PLANAR_RATE[i][j] = IS_NORMAL_PLANAR[i][j]/IS_NORMAL[i][j]
				IS_NORMAL_ANGULAR_RATE[i][j] = IS_NORMAL_ANGULAR[i][j]/IS_NORMAL[i][j]

print("SALVANDO ARQUIVOS...")
# SALVA OS MAPAS EM ARQUIVOS .csv
blockSize = "_%dx%d" % (Bloco_X, Bloco_Y)
np.savetxt("/home/otavio/Downloads/VTM_16/Python_Scripts/"+folderName+"/Rate_MRL"+blockSize+".csv", IS_MRL_RATE,delimiter=',',fmt='%f')
np.savetxt("/home/otavio/Downloads/VTM_16/Python_Scripts/"+folderName+"/Rate_ISP"+blockSize+".csv", IS_ISP_RATE,delimiter=',',fmt='%f')
np.savetxt("/home/otavio/Downloads/VTM_16/Python_Scripts/"+folderName+"/Rate_MIP"+blockSize+".csv", IS_MIP_RATE,delimiter=',',fmt='%f')
np.savetxt("/home/otavio/Downloads/VTM_16/Python_Scripts/"+folderName+"/Rate_Normal"+blockSize+".csv", IS_NORMAL_RATE,delimiter=',',fmt='%f')

np.savetxt("/home/otavio/Downloads/VTM_16/Python_Scripts/"+folderName+"/Rate_Normal_DC"+blockSize+".csv", IS_NORMAL_DC_RATE,delimiter=',',fmt='%f')
np.savetxt("/home/otavio/Downloads/VTM_16/Python_Scripts/"+folderName+"/Rate_Normal_Planar"+blockSize+".csv", IS_NORMAL_PLANAR,delimiter=',',fmt='%f')
np.savetxt("/home/otavio/Downloads/VTM_16/Python_Scripts/"+folderName+"/Rate_Normal_Angular"+blockSize+".csv", IS_NORMAL_ANGULAR_RATE,delimiter=',',fmt='%f')

# SOMA OS MODOS ISP, MRL, MIP E NORMAL PRA DESCOBRIR A COBERTURA TOTAL
soma = IS_MRL_RATE + IS_ISP_RATE + IS_MIP_RATE + IS_NORMAL_RATE
np.savetxt("/home/otavio/Downloads/VTM_16/Python_Scripts/"+folderName+"/Rate_MRL+ISP+MIP+Normal"+blockSize+".csv", soma, delimiter=',', fmt='%f')

# @iagostorch END
