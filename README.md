# automobile_project

Para rodar os pipelines do projeto, crie um ambiente virtual:
```
    python3 -m venv venv
```
Instale as dependências do projeto: 
```
   pip install -r src/requirements.txt
```
E então rode os pipelines dos projetos: 
```
    kedro run
```
Você pode analisar o fluxo do projeto com o kedro-viz:
```
    kedro viz
```
Os resultados (r2 score) de cada execução são monitorados pelo MLflow, que pode ser acessado com: 
```
    kedro mlflow ui
```
O projeto também pode ser acessado através de uma API desenvolvida em Fast-API:
```
    kedro fast-api run
```