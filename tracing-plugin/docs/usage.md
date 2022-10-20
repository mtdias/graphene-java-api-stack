### **Use**

It's possible to apply this in an application of type APP with the StackSpot CLI. Run the command below to add the plugin in your application:
```bash
stk apply plugin graphene-java-api-stack/tracing-plugin
```

> The steps below show how to import a Stack in your local environment:

### **Requirements**

To use this plugin, you need to install the following items: 
- [**STK CLI**](https://docs.stackspot.com/v3.7.0/docs/stk-cli/installation/)
- [**Java**](https://openjdk.org/)
- [**Git**](https://git-scm.com/)

### **Configuration of STK CLI**
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

**Output example:**
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
To create an application and configure all plugins related to observability, copy and paste the command below on your terminal:
```bash
stk create app meu-teste-app --stackfile graphene-java-api-stack/observability
```
