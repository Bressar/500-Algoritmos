""" display é mais útil para exibir objetos ricos em formatação dentro de notebooks Jupyter. Como tabulate retorna uma string formatada, display(tabela) ainda mostrará o texto normalmente, assim como print. Se estiver usando um notebook e quiser exibir HTML, pode alterar o tablefmt para 'html' e usar display(HTML(tabela)), importando HTML de IPython.core.display.

Se estiver usando Jupyter Notebook e quiser garantir que tudo funcione corretamente, também pode instalar o Jupyter:

bash

pip install jupyter
 """




from tabulate import tabulate
from IPython.display import display

dados = [
    ['Nome', 'Idade', 'Telefone'],
    ['Creuza', 99, '000234576'],
    ['Osnezio', 102, '666777888']
]

tabela =tabulate(dados, headers='firstrow', tablefmt='grid')

print(tabela)

display(tabela)