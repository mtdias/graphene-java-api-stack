#### **Pré-requisitos**
Para utilizar este plugin, é necessário ter uma aplicação baseada na `Stack Web API com Spring` e criada pela `CLI` do `StackSpot`, que você pode baixar [**aqui**](https://stackspot.com/).

Além disso, você precisará ter:
- JDK >= 8 instalada
- O projeto deve ser criado a partir do template `spring-web-api-template` para que o plugin seja aplicado corretamente.

Na pasta do projeto, basta digitar o seguinte comando para aplicar o plugin:
```bash
stk apply plugin graphene-java-api-stack/db-relational-plugin
```

É possível selecionar as configurações para as seguintes bases relacionais suportadas:

[PostgreSQL](https://www.postgresql.org/)
[MariaDB](https://mariadb.org/)

