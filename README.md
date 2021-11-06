# django-task-scheduler

Projeto de estudo de uma aplicação Django que utiliza o django-apscheduler para realizar tarefas agendadas

## Ambiente de desenvolvimento

### Dependências

- docker
- docker-compose

### Subir app django

```
docker-compose up
```

### Subir scheduler

```
docker-compose run --rm app python -W ignore manage.py runapscheduler
```
