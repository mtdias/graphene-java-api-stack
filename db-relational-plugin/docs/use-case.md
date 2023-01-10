## **Use Case**
This use case starts Java projects with Spring Boot using Maven or Gradle. It provides support to integrate relational databases, adding the corresponding dependence on the build tool according to the user's choice.

It also configures the appropriate connection driver and adds initial properties to the application.yaml. It configures the docker-compose, quickly enabling the connection between the application and the database.

### **Overview**
[**db-relational-plugin**](https://github.com/stack-spot/graphene-java-api-stack/tree/main/db-relational-plugin) adds to Stack the ability to integrate with relational databases.

### **Requirements**
See below what you need:
- [**STK CLI**](https://stackspot.com/login?route=/download/cli)
- [**Java >= 8**](https://openjdk.org/)
- [**Git**](https://git-scm.com/)

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
+--------------+---------------------------------+-----------------+
| name         | description                     | version(latest) |
+--------------+---------------------------------+-----------------+
| spring-web-  | Template for Web APIs based on  | no release      |
| api-template | Java with Spring Boot and       |                 |
|              | other Spring technologies.      |                 |
+--------------+---------------------------------+-----------------+
```

**The command below lists all the available plugins locally:**
```bash
stk list plugin
```

**Output example:**
```bash
Stack: graphene-java-api-stack
+-----------------+------------------------------------------+-----------------+
| name            | description                              | version(latest) |
+-----------------+------------------------------------------+-----------------+
| db-relational-p | Plugin to configure a relational         | no release      |
| lugin           | database at project                      |                 |
|                 |                                          |                 |
+-----------------+------------------------------------------+-----------------+

```

### Installation
To create an application and configure all the plugins related to the **db-relational**, execute the command below in your terminal:
```bash
stk create app meu-teste-app --stackfile graphene-java-api-stack/db-relational
```