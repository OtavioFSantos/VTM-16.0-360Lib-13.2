# -*- Coding: UTF-8 -*-
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
fid = open('/home/otavio/Downloads/VTM_16/Python_Scripts/TrolleyQP22/saida64x64.md','r')

# -----
Bloco_X = 64
Bloco_Y = 64

FLAG_MIP = 0
FLAG_ISP = 0
FLAG_MRL = 0
FLAG_PLANAR = 0
FLAG_DC = 1
# -----

CU_TESTA = np.zeros((2048, 4096))
if(FLAG_MIP):
	BEST_MIP = np.zeros((2048, 4096))
	MIP_RATE = np.zeros((2048, 4096))
if(FLAG_ISP):
	BEST_ISP = np.zeros((2048, 4096))
	ISP_RATE = np.zeros((2048, 4096))
if(FLAG_MRL):
	BEST_MRL = np.zeros((2048, 4096))
	MRL_RATE = np.zeros((2048, 4096))
if(FLAG_PLANAR):
	BEST_PLANAR = np.zeros((2048, 4096))
	PLANAR_RATE = np.zeros((2048, 4096))
if(FLAG_DC):
	BEST_DC = np.zeros((2048, 4096))
	DC_RATE = np.zeros((2048, 4096))

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
		
		# Testa a CU
		for i in range(Bloco_Y):
			for j in range(Bloco_X):
				CU_TESTA[int(posY)+i][int(posX)+j] = CU_TESTA[int(posY)+i][int(posX)+j] + 1
		
		# MIP FLAG / DC / PLANAR
		if(FLAG_MIP):
			if(int(MIPFlag) > 0):
				for i in range(Bloco_Y):
					for j in range(Bloco_X):
						BEST_MIP[int(posY)+i][int(posX)+j] = BEST_MIP[int(posY)+i][int(posX)+j] + 1		
		if(FLAG_DC):
			if(int(MIPFlag) <= 0):
				if(int(DCFlag) == 1):
					for i in range(Bloco_Y):
						for j in range(Bloco_X):
							BEST_DC[int(posY)+i][int(posX)+j] = BEST_DC[int(posY)+i][int(posX)+j] + 1
		if(FLAG_PLANAR):
			if(int(MIPFlag) <= 0):		
				if(int(PLANARFlag) == 0):
					for i in range(Bloco_Y):
						for j in range(Bloco_X):
							BEST_PLANAR[int(posY)+i][int(posX)+j] = BEST_PLANAR[int(posY)+i][int(posX)+j] + 1

		# ISP FLAG
		if(FLAG_ISP):
			if(int(ISPFlag) > 0):
				for i in range(Bloco_Y):
					for j in range(Bloco_X):
						BEST_ISP[int(posY)+i][int(posX)+j] = BEST_ISP[int(posY)+i][int(posX)+j] + 1

		# MRL FLAG
		if(FLAG_MRL):
			if(int(MRLFlag) > 0):
				for i in range(Bloco_Y):
					for j in range(Bloco_X):
						BEST_MRL[int(posY)+i][int(posX)+j] = BEST_MRL[int(posY)+i][int(posX)+j] + 1

	prevline = line
#ENDFOR

# MIP RATE
if(FLAG_MIP):
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA[i][j] == 0):
				MIP_RATE[i][j] = 0
			else:
				MIP_RATE[i][j] = BEST_MIP[i][j]/CU_TESTA[i][j] 

# ISP RATE
if(FLAG_ISP):
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA[i][j] == 0):
				ISP_RATE[i][j] = 0
			else:
				ISP_RATE[i][j] = BEST_ISP[i][j]/CU_TESTA[i][j] 

# MRL RATE
if(FLAG_MRL):
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA[i][j] == 0):
				MRL_RATE[i][j] = 0
			else:
				MRL_RATE[i][j] = BEST_MRL[i][j]/CU_TESTA[i][j] 

# PLANAR RATE
if(FLAG_PLANAR):
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA[i][j] == 0):
				PLANAR_RATE[i][j] = 0
			else:
				PLANAR_RATE[i][j] = BEST_PLANAR[i][j]/CU_TESTA[i][j] 

# DC RATE
if(FLAG_DC):
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA[i][j] == 0):
				DC_RATE[i][j] = 0
			else:
				DC_RATE[i][j] = BEST_DC[i][j]/CU_TESTA[i][j] 

# MAPA DE CALOR
if(FLAG_MIP):
	plt.imshow(MIP_RATE, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')
if(FLAG_ISP):
	plt.imshow(ISP_RATE, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')
if(FLAG_MRL):
	plt.imshow(MRL_RATE, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')
if(FLAG_PLANAR):
	plt.imshow(PLANAR_RATE, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')
if(FLAG_DC):
	plt.imshow(DC_RATE, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')

plt.colorbar()
plt.show()

fid.close()