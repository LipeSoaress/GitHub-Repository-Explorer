# GitHub Repository Explorer

Aplicação web para pesquisar usuários e repositórios do GitHub utilizando a API oficial.

## Acesso à aplicação

A aplicação está disponível online:

**Live Demo:**  
...

---

## Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| Busca de repositório | Permite buscar um repositório usando o formato `usuario/repositorio`. |
| Busca de usuário | Exibe todos os repositórios públicos de um usuário. |
| Estatísticas do repositório | Mostra stars, forks, watchers e linguagem utilizada. |
| Data de atualização | Exibe a última atualização do repositório. |
| Sugestões de perfis | Permite pesquisar rapidamente desenvolvedores populares. |
| Histórico de pesquisas | Armazena consultas realizadas utilizando SQLite. |

---

## Tecnologias utilizadas

- Python  
- Flask  
- SQLite  
- HTML  
- CSS  
- JavaScript  
- GitHub REST API  

---

## Endpoints da API

### Buscar um repositório

`/repo/{owner}/{repo}`

**Exemplo:**

`torvalds/linux`

### Buscar todos os repositórios de um usuário

`/user/{username}`

**Exemplo:**

`torvalds`

---

# Observação

Este projeto utiliza a API pública do GitHub, mas não possui qualquer afiliação oficial com o GitHub.

* * *

# Licença

Este projeto utiliza a licença MIT.
