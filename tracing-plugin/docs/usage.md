# Uso

É possível aplicar este Plugin em uma aplicação do tipo APP utilizando a linha de comando da Stackspot (STK CLI). Para isso, basta executar o seguinte comando:
```bash
stk apply plugin graphene-java-api-stack/tracing-plugin
```

> Os passos abaixo mostram como importar a Stack em um ambiente local:

### **Pré-requisitos**

Para usar este plugin, você precisa ter instalado na sua máquina os seguintes itens: 
- [**STK CLI**](https://docs.stackspot.com/v3.7.0/docs/stk-cli/installation/)
- [**Java**](https://openjdk.org/)
- [**Git**](https://git-scm.com/)

### **Configuração do STK CLI**
Execute o comando abaixo para atualizar localmente o catálogo que contém o **OpenAPI Plugin**:
```bash
stk import stack https://github.com/stack-spot/graphene-java-api-stack
```

**Listagem de Templates disponíveis localmente:**
```bash
stk list template
```

**Exemplo de output:**
```bash
Stack: graphene-java-api-stack
+-------------------------+-----------------------------------------------------------+------------------+-----------------+
| name                    | description                                               | types            | version(latest) |
+-------------------------+-----------------------------------------------------------+------------------+-----------------+
| spring-web-api-template | Template para Web APIs baseadas em Java com Spring Boot e | ['app-template'] | no release      |
|                         | outras tecnologias Spring.                                |                  |                 |
+-------------------------+-----------------------------------------------------------+------------------+-----------------+
```

**Listagem de Plugins disponíveis localmente:**
```bash
stk list plugin
```

**Exemplo de output:**
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
