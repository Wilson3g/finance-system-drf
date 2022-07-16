# Controle financeiro - Em desenvolvimento

Cadastro de contas a pagar e a receber com geração de relatório e mensagens via telegram sobre contas próximas ao vencimento.

# Tecnologias empregas
- Python - 3.9.0
- Django - 4.0.5
- Postgres - 12.2
- Redis - 6.2
- Docker - 20.10.12


# Funcionalidades
- Cadastro de contas a pagar;
- Cadastrp de contas a receber;
- Cadastro de tags para agrupamento de contas;
- Geração de relatórios;
- Disparo de mensagens via Telegram para contas próximas ao vencimento.

## Instalação com docker

Este projeto utiliza o docker e o docker-compose para facilitar a instalação do projeto. Como pré-requisito é necessário ter esses dois softawares instalados.

Versão necessária do Docker: >= 20.10.12 <br>
Versão necessária do Docker Compose: >= 1.29.2 <br><br>

Subir containers.
```bash
docker-compose up
```

Entrar no container do projeto.
```bash
docker exec -it finance_finance_1 bash
```

Executar migrations.
```bash
python manage.py migrate
```

## Testes
Entrar no container do projeto.
```bash
docker exec -it finance_finance_1 bash
```

Executar todos os testes.
```bash
python manage.py test
```

## Contribuição

Pull requests são muito bem vindos.

Por favor, lembre-se de manter os testes atualizados ao subir um PR.
