#%%writefile "teste.py"

import random
import pandas as pd

def gera_loja(tam_loja, val_max_prod, vol_max_prod, qtd_max_prod):
  random.seed(12)
  loja = pd.DataFrame({'Valor' : [random.randint(1, val_max_prod) for i in range(tam_loja)], \
                       'Volume' : [random.randint(1, vol_max_prod) for i in range(tam_loja)], \
                       'Quantidade' : [random.randint(1, qtd_max_prod) for i in range(tam_loja)]})
  loja.index.name = ('Produto')
  return loja

loja = gera_loja(6, 10, 10, 10)
#loja

from IPython.lib.display import join
lista = []
loja['Quantidade'] += 1

def recursivo(loja, indice_atual = 0, combinacao_atual = []):
    if indice_atual == len(loja): 
        lista.append(combinacao_atual.copy())
        #print(combinacao_atual)
        
        
    else:        
        for valor in range(loja.Quantidade[indice_atual]):
            recursivo(loja, indice_atual + 1, combinacao_atual + [valor])

recursivo(loja)

df = pd.DataFrame(lista)
#df

lucro_volume = []

for i in range(len(df)):
  valores = loja.Valor.values * df.iloc[i].values
  volumes = loja.Volume.values * df.iloc[i].values
  lucro_volume.append([valores.sum(), volumes.sum()])

df_adiciona_lucro_volume = pd.DataFrame(lucro_volume, columns = ['Lucro', 'Volume'])
df_adiciona_lucro_volume.insert(0, 'Combinacao', df.apply(lambda x: ' '.join(map(str, x)), axis=1))

#print(df_adiciona_lucro_volume)

VOLUME_MAXIMO_MOCHILA = 43
df_capacidade = df_adiciona_lucro_volume[df_adiciona_lucro_volume.Volume <= VOLUME_MAXIMO_MOCHILA]

lucro = df_capacidade['Lucro'].max()
comb = df_capacidade[df_capacidade['Lucro'] == lucro]

#print(comb)

#!python teste.py

import time
import pandas as pd
testes = []

for exec in range(1000):
  tmp_initial = time.time()  
  #!python teste.py
  tmp_final = time.time()
  tmp_diff = tmp_final - tmp_initial
  testes.append(tmp_diff)

teste = pd.DataFrame(data=testes, columns= ['Tempo'])
teste

teste.to_csv("Tempo_testes.csv", index=False)
