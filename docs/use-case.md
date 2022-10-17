## **Use Case**
This use case is ideall to initizalize Java projects with Spring Boot and gradle or maven with observability support.

### **General Vision**
[**metrics-plugin**](https://github.com/stack-spot/graphene-java-api-stack/tree/main/metrics-plugin) adds in the stack the capacity to provide _metrics_ to the project.

[**tracing-plugin**](https://github.com/stack-spot/graphene-java-api-stack/tree/main/tracing-plugin) adds in the stack the capacity to provide _tracing_ to the project.

[**logging-plugin**](https://github.com/stack-spot/graphene-java-api-stack/tree/main/logging-plugin) adds in the stack the capacity to provide _logs_ to the project.

### **Pré-requirements**
To use this plugin is need to install the itens below:

- [**StakSpot CLI**](https://docs.stackspot.com/v3.0.0/os-cli/installation/)
- [**Java >= 8**](https://openjdk.org/)
- [**Git**](https://git-scm.com/)

### **Recommended**
It's recommended to use some developer tools like [**LocalStack**](https://github.com/localstack/localstack).

### Stack CLI Configuration
Execute the command below to import/update the local catalog witch contain the Graphene Java API Stack
```bash
stk import stack https://github.com/stack-spot/graphene-java-api-stack
```

**The command below lists all templates locally available:**
```bash
stk list template
```

**Exemple output:**
```bash
Stack: graphene-java-api-stack
+-------------------------+-----------------------------------------------------------+------------------+-----------------+
| name                    | description                                               | types            | version(latest) |
+-------------------------+-----------------------------------------------------------+------------------+-----------------+
| spring-web-api-template | Template for Web APIs based on Java with Spring Boot and  | ['app-template'] | no release      |
|                         | others Spring technologies.                               |                  |                 |
+-------------------------+-----------------------------------------------------------+------------------+-----------------+
```

**The command below lists all plugins locally available:**
```bash
stk list plugin
```

**Exemple output:**
```bash
Stack: graphene-java-api-stack
+----------------+--------------------------------------------------------------+---------+-----------------+
| name           | description                                                  | types   | version(latest) |
+----------------+--------------------------------------------------------------+---------+-----------------+
| metrics-plugin | This plugin adds functionalities to obtain metrics of the    | ['app'] | no release      |
|                | application using Spring Actuator component.                 |         |                 |
|                |                                                              |         |                 |
| tracing-plugin | This plugin adds functionalities to trace of the application | ['app'] | no release      |
|                | using Jaeger                                                 |         |                 |
+----------------+--------------------------------------------------------------+---------+-----------------+
```

### Install
To create an application and configure all plugins related to observability, copy and paste the command below in the terminal:
```bash
stk create app meu-teste-app --stackfile graphene-java-api-stack/observability
```
