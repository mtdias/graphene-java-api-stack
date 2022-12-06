## **Caso de Uso**
Este caso de uso inicia projetos Java com Spring Boot usando Maven ou Gradle. Ele fornece suporte para integrar bancos de dados relacionais, adicionando a dependência correspondente na ferramenta de construção de acordo com a escolha do usuário.

Ele também configura o driver de conexão apropriado e adiciona propriedades iniciais ao arquivo application.yaml. Também configura o docker-compose, permitindo realizar a conexão entre a aplicação e o banco de dados com o mínimo de esforço.

### **Visão Geral**
O Plugin [**db-relational-plugin**](https://github.com/stack-spot/graphene-java-api-stack/tree/main/db-relational-plugin) adiciona na Stack a capacidade de integração com bancos de dados relacionais.

### **Pré-requisitos**
Para usar o Plugin é preciso ter instalado:

- [**Instalação STK CLI**](https://stackspot.com/login?route=/download/cli)
- [**Java >= 8**](https://openjdk.org/)
- [**Git**](https://git-scm.com/)

### Configuração Stack CLI
Execute o comando abaixo para atualizar localmente o catálogo que contém OpenAPI plugin:
```bash
stk import stack https://github.com/stack-spot/graphene-java-api-stack
```

**Listagem template disponíveis localmente:**
```bash
stk list template
```

**Exemplo output:**
```bash
Stack: graphene-java-api-stack
+--------------+---------------------------------+-----------------+
| name         | description                     | version(latest) |
+--------------+---------------------------------+-----------------+
| spring-web-  | Template para Web APIs baseadas | no release      |
| api-template | em Java com Spring Boot e       |                 |
|              | outras tecnologias Spring.      |                 |
+--------------+---------------------------------+-----------------+
```

**Listagem plugins disponíveis localmente:**
```bash
stk list plugin
```

**Exemplo output:**
```bash
Stack: graphene-java-api-stack
+-----------------+------------------------------------------+-----------------+
| name            | description                              | version(latest) |
+-----------------+------------------------------------------+-----------------+
| db-relational-p | Plugin para configurar a base de dados   | no release      |
| lugin           | relacional no projeto.                   |                 |
|                 |                                          |                 |
| logging-plugin  | Este plugin fornece uma pré-configuração | no release      |
|                 | para logs estruturados em formato JSON.  |                 |
|                 |                                          |                 |
| metrics-plugin  | Este plugin adiciona funcionalidades de  | no release      |
|                 | obtenção de métricas da aplicação por    |                 |
|                 | meio do componente Spring Actuator.      |                 |
|                 |                                          |                 |
| tracing-plugin  | Plugin para configuração de Tracing      | no release      |
+-----------------+------------------------------------------+-----------------+

```

### Instalacao
Para criar uma aplicação e já configurar o plugin na aplicação, copie e cole o comando abaixo no seu terminal:
```bash
stk create app meu-teste-app --stackfile graphene-java-api-stack/db-relational
```
