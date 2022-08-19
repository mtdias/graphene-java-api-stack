## **Caso de Uso**
Este Caso de Uso é ideal para a inicialização de projetos Java com Spring Boot e gradle com suporte a observabilidade.

### **Visão Geral**
O Plugin [**metrics-plugin**](https://github.com/stack-spot/graphene-java-api-stack/tree/main/metrics-plugin) adiciona na Stack a capacidade de provisionar métricas ao projeto.

O Plugin [**tracing-plugin**](https://github.com/stack-spot/graphene-java-api-stack/tree/main/tracing-plugin) adiciona na Stack a capacidade de provisionar _tracing_ ao projeto.

### **Pré-requisitos**
Para usar o Plugin é preciso ter instalado os itens abaixo:

- [**Instalação StakSpot CLI**](https://docs.stackspot.com/v3.0.0/os-cli/installation/)
- [**Java >= 8**](https://openjdk.org/)
- [**Git**](https://git-scm.com/)

### **Recomendado**
É recomendada a utilização de algumas ferramentas para desenvolvimento, como por exemplo, o [**LocalStack**](https://github.com/localstack/localstack).

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
+-------------------------+-----------------------------------------------------------+------------------+-----------------+
| name                    | description                                               | types            | version(latest) |
+-------------------------+-----------------------------------------------------------+------------------+-----------------+
| spring-web-api-template | Template para Web APIs baseadas em Java com Spring Boot e | ['app-template'] | no release      |
|                         | outras tecnologias Spring.                                |                  |                 |
+-------------------------+-----------------------------------------------------------+------------------+-----------------+
```

**Listagem plugins disponíveis localmente:**
```bash
stk list plugin
```

**Exemplo output:**
```bash
Stack: graphene-java-api-stack
+----------------+--------------------------------------------------------------+---------+-----------------+
| name           | description                                                  | types   | version(latest) |
+----------------+--------------------------------------------------------------+---------+-----------------+
| metrics-plugin | Este plugin adiciona funcionalidades de obtenção de métricas | ['app'] | no release      |
|                | da aplicação por meio do componente Spring Actuator.         |         |                 |
|                |                                                              |         |                 |
| tracing-plugin | Plugin para configuração de Tracing                          | ['app'] | no release      |
+----------------+--------------------------------------------------------------+---------+-----------------+
```

### Instalacao
Para criar uma aplicação e já configurar o plugin na aplicação, copie e cole o comando abaixo no seu terminal:
```bash
stk create app meu-teste-app --stackfile graphene-java-api-stack/observability
```
