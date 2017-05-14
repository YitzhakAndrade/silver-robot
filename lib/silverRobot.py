import os
import sys
from decimal import Decimal
import operator
import numpy as np

# ============================================

mat = []
matsum = dict()
matix = []

# ============================================

def initialize():
	global mat, matsum, matix
	mat = []
	matsum = dict()
	matix = []

def insert(num, ix):
	global mat, matsum, matix

	if len(mat) <= ix:
		mat.append([])
	if ix not in matsum:
		matsum[ix] = 0

	ix = updateIndex()
	mat[ix].append(num)
	matsum[ix] += num

def reduceMatSum():
	return # lento
	valmin = min(matsum.values())
	for i in matsum:
		matsum[i] -= valmin

def updateIndex():
	global mat, matsum, matix

	reduceMatSum()

	matix = sorted(matsum.items(), key=operator.itemgetter(1))
	if len(matix) <= 0: 
		return 0
	return matix[0][0]

def printDiffMax():
	diffMax = str(matix[len(matix)-1][1])
	print('Diferenca maxima entre os grupos: ' + diffMax)

def saveOutput():
	curpath = os.path.dirname(os.path.abspath(__file__))
	filepath = curpath + '/../temp/' + 'result.txt'
	f = open(filepath, 'w')
	for i in mat:
		linha = (str(sum(i)) + ';' +  ';'.join(map(str, i)))
		f.write(linha+'\n')
	f.close()

def printGlobals():
	global mat, matsum, matix
	print('========================================')
	print()
	print('mat')	
	#print(mat) # demora muito
	print('temp/result.txt')
	print()
	print()
	print('matsum')
	print(matsum)
	print()
	print()
	print('matix')
	print(matix)
	print()
	print('========================================')	

def run(nums, classes):
	global mat, matsum, matix	

	initialize()
	nums.sort(reverse=True)

	for i in range(0, len(nums)):
		ix = i % classes
		insert(nums[i], ix)

	saveOutput()