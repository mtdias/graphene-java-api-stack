## **Use Case**
This Use Case is ideal for starting Java projects with Spring Boot and maven/gradle with relational database communication support.

### **Overview**
[**db-relational-plugin**](https://github.com/stack-spot/graphene-java-api-stack/tree/main/db-relational-plugin) adds to Stack the ability to integrate with relational databases.

### **Requirements**
See below the items you need to have installed on your machine:

- [**StakSpot CLI**](https://docs.stackspot.com/v3.0.0/os-cli/installation/)
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

**Exemplo output:**
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

**The command below lists all plugins locally available:**
```bash
stk list plugin
```

**Exemplo output:**
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

### Install
To create an application and configure all plugins related to db-relational, copy and paste the command below in your terminal:
```bash
stk create app meu-teste-app --stackfile graphene-java-api-stack/db-relational
```
