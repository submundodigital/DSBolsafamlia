
## Estudo sobre Junções no DataFrame no estilo de banco de dados  
### Capítulo 8 PAG 292
>#### Estudo realizado com base no livro 'Python para análise de dados' 


>  Contato

> * [Linkedin](www.linkedin.com/in/isweluiz)

#### Iremos utilizar operações merge e join, ambas combinam conjunto de dados associando linhas por meio de uma ou mais chaves. Essas operação são constantemente utilizadas banco de dados relacionais 



```python
#importando as bibiliotecas que serão utilizadas abs
import pandas as pd
import numpy as np
import random
```


```python
#Exemplo simples
#ciando o 1º data frame 

df1 = pd.DataFrame({'key': ['b','b','a','c','a','a','b'],
                   'data2': range(7)}) #Mesma quantidade de objetos na coluna key 
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data2</th>
      <th>key</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>b</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>b</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>a</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>c</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>a</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>a</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>b</td>
    </tr>
  </tbody>
</table>
</div>




```python
#ciando o 2º data frame 

df2 = pd.DataFrame({'key': ['a','b','d'],
                   'data2': range(3)})
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data2</th>
      <th>key</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>a</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>b</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>d</td>
    </tr>
  </tbody>
</table>
</div>




```python
'''Vamos fazer aqui uma junção de many-to-one; os dados de df1 contêm várias linhas de rótulo a e b, enquanto no df2 temos apenas uma 
linha para cada valor na coluna key''' 
##Vamos chamar o argumento merge 
pd.merge(df1,df2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data2</th>
      <th>key</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>b</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1,df2, on='key')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data2_x</th>
      <th>key</th>
      <th>data2_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>b</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>b</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>b</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>a</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>a</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>a</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
'''Se os nomes das colunas forem diferentes, nós podemos especificá-las separadamente'''

df3 = pd.DataFrame({'lkey': ['b','b','a','c','a','a','b'],
                   'data2': range(7)}) #Mesma quantidade de objetos na coluna key 

df4 = pd.DataFrame({'rkey': ['a','b','d'],
                   'data2': range(3)})
```


```python
pd.merge(df3,df4, left_on='lkey', right_on='rkey')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data2_x</th>
      <th>lkey</th>
      <th>data2_y</th>
      <th>rkey</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>b</td>
      <td>1</td>
      <td>b</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>b</td>
      <td>1</td>
      <td>b</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>b</td>
      <td>1</td>
      <td>b</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>a</td>
      <td>0</td>
      <td>a</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>a</td>
      <td>0</td>
      <td>a</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>a</td>
      <td>0</td>
      <td>a</td>
    </tr>
  </tbody>
</table>
</div>




```python
'''
Os valores (c) e (d) e os dados associados estão ausentes no resultado. Por padrão o merge executa uma junção do tipo  inner (interna) 
as chaves nos valores são intersecção ou conjunto comum que se encontra nas duas tabelas.
'''

# Outras opções são 'left' , 'right' e 'outer', que faz a juntação externa (outer join), efetua união das chaves, combinando
# o efeito da aplicação das junções tanto à esquerda quanto a direita


pd .merge(df3,df4 , how='outer')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data2</th>
      <th>lkey</th>
      <th>rkey</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>b</td>
      <td>a</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>b</td>
      <td>b</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>a</td>
      <td>d</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>c</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>a</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>a</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>b</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Criando um dataframe mais exemplicado com dados 
#Nome, idades e contato
dados1 = pd.DataFrame({'Nomes':['Luiz' , 'Eduardo', 'Pereira'],
                     'Idades': ['15', '21', '33'],
                      'Contato': ['isweluiz@hotmail.com', 'linkedin.com/in/isweluiz', '61 9999999']})

dados2 = pd.DataFrame({'Nomes':['Gabrielle' , 'Cândido', 'Alves'],
                     'Idades': ['19', '12', '13'],
                      'Contato': ['gabi@hotmail.com', 'linkedin.com/in/gabi', '61 666666']})
```


```python
dados1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Contato</th>
      <th>Idades</th>
      <th>Nomes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>isweluiz@hotmail.com</td>
      <td>15</td>
      <td>Luiz</td>
    </tr>
    <tr>
      <th>1</th>
      <td>linkedin.com/in/isweluiz</td>
      <td>21</td>
      <td>Eduardo</td>
    </tr>
    <tr>
      <th>2</th>
      <td>61 9999999</td>
      <td>33</td>
      <td>Pereira</td>
    </tr>
  </tbody>
</table>
</div>




```python
dados2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Contato</th>
      <th>Idades</th>
      <th>Nomes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>gabi@hotmail.com</td>
      <td>19</td>
      <td>Gabrielle</td>
    </tr>
    <tr>
      <th>1</th>
      <td>linkedin.com/in/gabi</td>
      <td>12</td>
      <td>Cândido</td>
    </tr>
    <tr>
      <th>2</th>
      <td>61 666666</td>
      <td>13</td>
      <td>Alves</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Mesclando os dataframes e atribuindo ao novo data frame dados3
dados3 = pd.merge(dados1,dados2, how='outer')
dados3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Contato</th>
      <th>Idades</th>
      <th>Nomes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>isweluiz@hotmail.com</td>
      <td>15</td>
      <td>Luiz</td>
    </tr>
    <tr>
      <th>1</th>
      <td>linkedin.com/in/isweluiz</td>
      <td>21</td>
      <td>Eduardo</td>
    </tr>
    <tr>
      <th>2</th>
      <td>61 9999999</td>
      <td>33</td>
      <td>Pereira</td>
    </tr>
    <tr>
      <th>3</th>
      <td>gabi@hotmail.com</td>
      <td>19</td>
      <td>Gabrielle</td>
    </tr>
    <tr>
      <th>4</th>
      <td>linkedin.com/in/gabi</td>
      <td>12</td>
      <td>Cândido</td>
    </tr>
    <tr>
      <th>5</th>
      <td>61 666666</td>
      <td>13</td>
      <td>Alves</td>
    </tr>
  </tbody>
</table>
</div>




```python
dados3.dtypes
```




    Contato    object
    Idades     object
    Nomes      object
    dtype: object




```python
dados4 = dados3
```


```python
#Transformando a coluna idade em inteiro
dados4['Idades'] = dados4['Idades'].astype(int)
dados4.dtypes
```




    Contato    object
    Idades      int32
    Nomes      object
    dtype: object




```python
contatos = pd.merge(dados1, dados2 , on=['Contato', 'Contato'], how='outer')
contatos
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Contato</th>
      <th>Idades_x</th>
      <th>Nomes_x</th>
      <th>Idades_y</th>
      <th>Nomes_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>isweluiz@hotmail.com</td>
      <td>15</td>
      <td>Luiz</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>linkedin.com/in/isweluiz</td>
      <td>21</td>
      <td>Eduardo</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>61 9999999</td>
      <td>33</td>
      <td>Pereira</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>gabi@hotmail.com</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>19</td>
      <td>Gabrielle</td>
    </tr>
    <tr>
      <th>4</th>
      <td>linkedin.com/in/gabi</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>12</td>
      <td>Cândido</td>
    </tr>
    <tr>
      <th>5</th>
      <td>61 666666</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>13</td>
      <td>Alves</td>
    </tr>
  </tbody>
</table>
</div>




```python
contatos['Contato']
```




    0        isweluiz@hotmail.com
    1    linkedin.com/in/isweluiz
    2                  61 9999999
    3            gabi@hotmail.com
    4        linkedin.com/in/gabi
    5                   61 666666
    Name: Contato, dtype: object


