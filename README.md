Rotas Principais

1. Listar carros

URL: `/`
Nome da Rota: `carro_listar`
View Responsável: `CarroListView`
Template: `loja/listar.html`

![Listar](screenshots/Listar.png)

2. Detalhar carros

URL: `/carro/<int:pk>/`
Nome da Rota (Django): `carro_detalhe`
View Responsável: `CarroDetailView`
Template: `loja/detalhe.html`

![Detalhar](screenshots/Detalhar.png)

3. Adicionar carros

URL: `/carro/novo/`
Nome da Rota (Django): `carro_novo`
View Responsável: `CarroCreateView`
Template: `loja/form.html`

![Adicionar](screenshots/Cadastrar.png)
![Adicionar](screenshots/AposCadastrar.png)

4. Editar carros

URL: `/carro/<int:pk>/editar/`
Nome da Rota (Django): `carro_editar`
View Responsável: `CarroUpdateView`
Template:** `loja/form.html`

![Editar](screenshots/Editar.png)

5. Deletar carros

URL: `/carro/<int:pk>/deletar/`
Nome da Rota (Django):** `carro_deletar`
View Responsável:`CarroDeleteView`
Template:`loja/confirm_delete.html`

![Deletar](screenshots/Deletar.png)


### ATIVIDADE DE PAGINAÇÃO E FILTROS ###

1 - Escolhi fazer em um CRUD separado do projeto final para não correr risco de bagunçar tudo. Além do fato de trabalhar em um projeto
menor possibilita ver melhor como o sistema funciona. 
Busquei uma forma mais "simples" e "limpa" de fazer um filtro. O objetivo principal é implementar, no projeto final, um sistema de filtro que 
interfira o mínimo possível nas views, acredito que isso deixa o código mais limpo, organizado e fácil de ser explicado.

2 - Coloquei os filtros utilizados no projeto final em si, que são o nome do veículo e a marca e o ano do modelo, acredito que sejam os mais
úteis em um sistema dessa natureza.

3 - Algumas, em especial na implementação dessa nova forma de inserir filtros, resolvi com IA.