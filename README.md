# Projetos do curso de "Computação inspirada na natureza" (UNESP - 2023)
Este repositório é dedicada a organizaçaõ de projetos e atividades do curso de
"Computação inspirada na natureza" da UNESP.

## Organização do projeto
O projeto é organizado da seguinte forma:

Dentro da pasta `src` você pode encontrar todos os exercícios que foram passados durante as aulas, cada uma das pastas irá conter um arquivo nomeado como `main.py` e será através dele que os algoritmos devem ser executados.

Quanto ao resultado da execução dos algoritmos, será criada uma pasta chamada `outpup` na raiz do projeto executado, e lá serão encontrados os arquivos referentes a execução daquele exercício específico.

## Projetos presentes no repositório

`hill_climbing_simulated_annealing` -> Algoritmo desenvolvido com o intuíto de mensurar o tempo de execução de várias variações do algoritmo de _Hill Climbing_, comparando o tempo de execução destes algoritmos em paralelo ao algoritmo de _Simulated Annealing_;

# Como compilar o projeto
Primeiro, recomendo que crie uma instância virtual do Python `>=` 3.10.X.
Para isso, na raiz do repositório:
```sh
python -m venv venv
```

Após criar e ativar a sua nova instância, novamente na raiz do repositório execute:
```sh
pip install -r requirements.txt
```

Agora basta navegar até o algoritmo que deseja executar usando o comando `cd src/<nome_do_projeto>` e executar o mesmo usando o seguinte comando:
```sh
python main.py
```