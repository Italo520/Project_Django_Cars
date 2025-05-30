🔗 This document is also available in [English](./README.md).

# Projeto Django Carros

Esta é uma aplicação web Django para gerenciar um catálogo de carros. Ela permite aos usuários visualizar uma lista de carros disponíveis, pesquisar por modelos específicos e adicionar novos carros ao sistema. O projeto também inclui uma interface de administração para um gerenciamento mais detalhado das marcas de carros e dos registros individuais de carros.

## Funcionalidades

* **Listagem de Carros:** Visualize todos os carros em um layout de grade, exibindo foto, marca, modelo, ano de fabricação e preço.
* **Adicionar Novo Carro:** Um formulário para adicionar novos carros ao catálogo, incluindo detalhes como modelo, marca, ano de fabricação, ano do modelo, placa, valor e foto.
* **Funcionalidade de Pesquisa:** Usuários podem pesquisar carros pelo nome do modelo.
* **Gerenciamento de Marcas:** Carros são associados a marcas específicas. As marcas podem ser gerenciadas através da interface de administração do Django.
* **Upload de Imagens:** Cada registro de carro pode ter uma foto associada.
* **Painel de Administração:** A interface de administração do Django é configurada para gerenciar os modelos `Car` e `Brand`, com exibições de lista e campos de pesquisa personalizados.
* **Validações Personalizadas:**
    * O valor mínimo para um carro é de R$20.000.
    * O ano de fabricação de um carro não pode ser anterior a 1975.

## Estrutura do Projeto

Project_Django_Cars  
├── app/  
│   ├── settings.py  
│   ├── urls.py  
│   ├── asgi.py  
│   ├── wsgi.py  
│   └── templates/  
│       └── base.html  
├── cars/  
│   ├── models.py  
│   ├── views.py  
│   ├── forms.py  
│   ├── admin.py  
│   ├── apps.py  
│   ├── templates/  
│   │   ├── cars.html  
│   │   └── new_car.html  
│   └── migrations/  
├── manage.py  
├── media/  
└── db.sqlite3  


## Pré-requisitos

* Python (3.x recomendado)
* Django (O projeto usa a versão 5.2.1 conforme indicado nos arquivos de migração)
* Pillow (para manipulação de ImageField)

## Configuração e Instalação

1.  **Clone o repositório (ou baixe os arquivos):**
    ```bash
    # Se fosse um repositório git
    # git clone <url-do-repositorio>
    # cd Project_Django_Cars-e6def20114e3ef975df51d68a9d4b215b36c15e5
    ```
    Navegue até o diretório `Project_Django_Cars-e6def20114e3ef975df51d68a9d4b215b36c15e5`.

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # No Windows
    venv\Scripts\activate
    # Em macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install Django==5.2.1 Pillow
    ```

4.  **Aplique as migrações:**
    Isso criará as tabelas de banco de dados necessárias com base nos modelos.
    ```bash
    python manage.py migrate
    ```

5.  **Crie um superusuário (para acesso administrativo):**
    Siga as instruções para criar uma conta de administrador.
    ```bash
    python manage.py createsuperuser
    ```

6.  **Certifique-se de que o diretório `media` exista:**
    O arquivo `settings.py` define `MEDIA_ROOT` como `os.path.join(BASE_DIR,'media')`. Certifique-se de que um diretório chamado `media` exista no mesmo nível do seu arquivo `manage.py`. Caso contrário, crie-o.

## Executando o Projeto

1.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

2.  **Acesse a aplicação no seu navegador web:**
    * **Listagem de Carros:** [http://127.0.0.1:8000/cars/](http://127.0.0.1:8000/cars/)
    * **Adicionar Novo Carro:** [http://127.0.0.1:8000/new_car/](http://127.0.0.1:8000/new_car/)
    * **Painel de Administração:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) (Faça login com as credenciais de superusuário)

## Pontos Chave de Configuração (de `app/settings.py`)

* **`DEBUG = True`**: A aplicação está atualmente rodando em modo de depuração.
* **`INSTALLED_APPS`**: Inclui `'django.contrib.admin'`, `'django.contrib.auth'`, `'django.contrib.contenttypes'`, `'django.contrib.sessions'`, `'django.contrib.messages'`, `'django.contrib.staticfiles'`, e o app personalizado `'cars'`.
* **`DATABASES`**: Configurado para usar SQLite (`'ENGINE': 'django.db.backends.sqlite3'`) com o arquivo de banco de dados `db.sqlite3` localizado em `BASE_DIR`.
* **`TEMPLATES`**: O diretório principal de templates está configurado como `['app/templates']`.
* **`MEDIA_ROOT`**: Configurado como `os.path.join(BASE_DIR,'media')`. É aqui que os arquivos enviados (fotos dos carros) serão armazenados.
* **`MEDIA_URL`**: Configurado como `'/media/'`. Este é o prefixo da URL para acessar os arquivos de mídia.
