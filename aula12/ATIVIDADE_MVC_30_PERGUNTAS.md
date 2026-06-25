# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: Arthur Assis dos Santos
- Turma: 3c2

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.

Pasta models, ./models

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?

O banco se chama streamflix.db (ou instance/streamflix.db). A configuração fica no app.py (ou config.py) na linha
app.config['SQLALCHEMY_DATABASE_URI'], que faz o Flask criar o arquivo sozinho.

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?

FilmeFavorito (no arquivo models/filme_favorito.py) e HistoricoBusca (no arquivo models/historico_busca.py).

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?

Herdam de db.Model. Elas ganham o ID automático (id), a habilidade de fazer buscas (query.filter/query.all) e o controle de salvamento (db.session).

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?

O nome é favoritos. Usamos __tablename__ para forçar letras minúsculas e plural no banco, evitando que o SQLAlchemy crie a tabela como FilmeFavorito (CamelCase), o que quebra as boas práticas.

**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?

É a coluna tmdb_id (ou filme_id). Ela tem unique=True (para não repetir o mesmo filme) e nullable=False (porque o ID é obrigatório).

**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?

Ele checa se o filme já existe usando cls.query.filter_by().first(). Se já existir, ele ignora para não dar erro. Se for novo, ele cria o objeto, joga na sessão (add) e salva (commit).

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?

Está na classe HistoricoBusca (models/historico_busca.py), no método listar_recentes.

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.

Só alguns campos para não pesar o banco. Em FilmeFavorito guardamos: tmdb_id, titulo, poster_path e data_lancamento.

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?

Exporta o db e as classes FilmeFavorito e HistoricoBusca. Isso serve como um "atalho" para o controller importar tudo direto da pasta models, sem precisar digitar o caminho de cada arquivo.

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).

São 3 Blueprints: main_bp (prefixo /), filmes_bp (prefixo /filmes) e favoritos_bp (prefixo /favoritos).

**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?

Está em controllers/filmes_controller.py e a função é a populares().

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).

 Ela busca os dados chamando o serviço da API (tmdb_api.get_populares()) e puxa os dados de paginação ou histórico antes de mandar pro HTML.

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?

 O controller de busca (em filmes_controller ou main_controller). Ele usa o model HistoricoBusca logo nas primeiras linhas da função usando HistoricoBusca.registrar(termo) ou db.session.add()

**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?

 Exige o método POST. A URL fica algo como http://localhost:5000/favoritos/adicionar/550.

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?

Se der None, o controller faz um if not filme: e dispara um abort(404) para mostrar a tela de erro, ou joga o usuário para a home com um aviso via flash.

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).

No app.py, usando as linhas:
Python
app.register_blueprint(main_bp)
app.register_blueprint(filmes_bp)
app.register_blueprint(favoritos_bp)

**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?

 O main_controller.py. Ele envia a lista de filmes em destaque e o histórico de buscas_recentes.

**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?

 É um Serviço (Helper). Quem chama são os Controllers para isolar o código que faz requisições Web (requests.get) do resto da lógica das rotas.

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.

Vem de request.args (via GET), porque o termo aparece direto na URL (/buscar?q=avatar). O request.form só seria usado se os dados fossem enviados escondidos via POST.

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?

Ficam na pasta views/templates/.

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?

 É o views/templates/layout.html. Os outros usam o comando {% extends 'layout.html' %} no topo e jogam o conteúdo dentro de blocos {% block conteudo %}.

**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.

 Os links usam o url_for: main.index (Início), filmes.populares (Populares), favoritos.lista (Favoritos), main.historico (Histórico) e main.sobre (Sobre).

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?

No arquivo views/templates/filmes/detalhe.html. A variável vem do controller, que pegou esses dados chamando a camada de Service.

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?

 É um pedaço reutilizável (componente/partial). Páginas como index.html ou populares.html incluem ele usando {% include 'filmes/_card.html' %} dentro de um for.

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?

O controller manda uma variável chamada eh_favorito (True ou False). O HTML usa {% if eh_favorito %} para decidir se mostra o botão de "Salvar" ou "Remover".

**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?

 Fica em views/static/css/style.css e o layout.html carrega usando:
{{ url_for('static', filename='css/style.css') }}.

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.

Usa o loop {% for filme in favoritos %}. Na tabela aparecem: filme.titulo, filme.data_lancamento e filme.tmdb_id.

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?

É uma trava para o modo de demonstração. Quem manda essa variável para todos os templates de uma vez é o @app.context_processor lá no app.py.

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.

O fluxo é esse aqui:
View (detalhe.html): Usuário clica em "Salvar" e envia um formulário POST com o ID do filme.
Controller (favoritos_controller.py): Recebe o POST, pega os dados do filme e chama o Model.
Model (filme_favorito.py): O método adicionar() roda o db.session.add() e salva com db.session.commit().
Redirect: O Controller manda uma mensagem flash de sucesso e dá um redirect de volta para a página de detalhes, que agora carrega com o botão "Remover".

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
