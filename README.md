# prova2mod10

Este repositório contem uma aplicação que gerencia blog post. Ela contem uma api em fast api, um sistema de logs que guarda informações no arquivo ./api/app.log e um gateway utilizando nginx

## Como Executar

A aplicação por ser dockerizada pode ser iniciada usando somente o comando:

```bash
docker compose up
```

para verificar as rotas disponíveis pode se utilizar a coleção do insomnia InsomniaCollection.json presente na raiz do repositório ou acessar o link do swagger da api através do link:
[swagger](http://localhost:5001/docs)