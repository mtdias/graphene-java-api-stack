## **Use Case**
This use case is ideal to initialize Java projects with Spring Boot and gradle or maven with observability support.

### **Overview**
[**metrics-plugin**](https://github.com/stack-spot/graphene-java-api-stack/tree/main/metrics-plugin) adds to the Stack the capacity to provide _metrics_ to a project.

[**tracing-plugin**](https://github.com/stack-spot/graphene-java-api-stack/tree/main/tracing-plugin) adds to the Stack the capacity to provide _tracing_ to a project.

[**logging-plugin**](https://github.com/stack-spot/graphene-java-api-stack/tree/main/logging-plugin) adds to the stack the capacity to provide _logs_ to a project.

### **Requirements**
See below the items you need to have installed on your machine:

- [**StakSpot CLI**](https://docs.stackspot.com/v3.0.0/os-cli/installation/)
- [**Java >= 8**](https://openjdk.org/)
- [**Git**](https://git-scm.com/)

- It's a recommendation to use development tools like [**LocalStack**](https://github.com/localstack/localstack).

### Stack CLI Configuration
To import/update the local catalog with the Graphene Java API Stack, execute the command below:
```bash
stk import stack https://github.com/stack-spot/graphene-java-api-stack
```

**The command below lists all templates locally available:**
```bash
stk list template
```

**Output example:**
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
|                |                                                              |         |                 |
| logging-plugin | This plugin gives a pre configured structure logs in JSON    | ['app'] | no release      |
|                | format.                                                      |         |                 |
+----------------+--------------------------------------------------------------+---------+-----------------+
```

### Install
To create an application and configure all plugins related to observability, copy and paste the command below in the terminal:
```bash
stk create app meu-teste-app --stackfile graphene-java-api-stack/observability
```
