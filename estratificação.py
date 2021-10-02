# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 22:35:11 2021

@author: Jailson
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

#carrega os data frame
df = pd.read_csv('Amazon.csv')

#imprime o tipo para cada variável
df.dtypes

#imprime a soma de valores ausentes
df.isnull().sum()

#correlaciona as variáveis
corr = df.corr()

#imprime a correlação
corr

#imprime a quantidade de linhas e colunas
corr.shape

#plota o mapa de calor das correlações

plt.figure(figsize=(6,6))
sns.heatmap(corr, cbar=True, square= True, fmt='.1f', annot=True, annot_kws={'size':15}, cmap='Blues')

#remove a variavel com o menor desempenho de correlação
df = df.drop(columns=['Volume'])

##############################################################################
#separa e salva os dados em train(treinamento) e test(teste)##################
##############################################################################

#atribui o data frame na variável dados
dados = len(df)

#atribui para a variável train_size o tamanho do treinamento desejado
train_size = math.floor(0.8*dados)

#atribui para a variávl train o treinamento
train = df.head(train_size)

#atribui para a variavel test o teste
test = df.tail(len(df) -train_size)

#converte os dados de treinamento para o formato .csv
train = train.to_csv(sep = ',', header = True, index = False)

#salva o arquivo treinamento
arquivo = open('train.csv','w')
arquivo.write(train)
arquivo.close()

#converte os dados de teste para o formato .csv
test = test.to_csv(sep = ',', header = True, index = False)

#salva o arquivo treinamento
arquivo = open('test.csv','w')
arquivo.write(train)
arquivo.close()