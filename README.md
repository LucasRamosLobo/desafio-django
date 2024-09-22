# Gerenciamento de Tarefas - API Django

## Descrição

Esta é uma API simples de gerenciamento de tarefas desenvolvida com Django.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/LucasRamosLobo/desafio-django.git
    cd desafio-django
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute o servidor Django:
    ```bash
    python manage.py runserver
    ```
5. teste o endpoint api/tasks/:
    ```bash
    POST http://localhost:8000/api/tasks/
    GET http://localhost:8000/api/tasks/
    DELETE POST http://localhost:8000/api/tasks/{id}/
    PUT http://localhost:8000/api/tasks/{id}/
    Atualização parcial > PATCH http://localhost:8000/api/tasks/{id}/
    ```
6. Exemplos json POST/PUT/PATCH
   ´´´json
{
    "title": "Nova Tarefa",
    "description": "Descrição da nova tarefa."
}
   ´´´
## Testes

Para rodar os testes automatizados, execute o comando:
```bash
python tests.py

