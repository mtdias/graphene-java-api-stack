O plugin adiciona ao arquivo docker-compose.yaml o trecho de código necessário para subir uma base de dados local. Para mais informações dos paramêtros de cada imagem, confira abaixo:

[**PostgreSQL**](https://hub.docker.com/_/postgres)
[**MariaDB**](https://hub.docker.com/_/mariadb)

As dependência e trechos de código necessários são adicionados para a aplicação se conectar à bases de dados relacionais.

O plugin adiciona as dependências necessárias conforme **build_tool** selecionado no momento em que o projeto foi criado, utilizando a stack graphene-java-api-stack:

MariaDB

**Gradle:**  
`implementation group: 'org.springframework.boot', name: 'spring-boot-starter-data-jpa'`
`implementation group: 'org.mariadb.jdbc', name: 'mariadb-java-client', version: '3.0.8'`
`testImplementation group: 'org.testcontainers', name: 'junit-jupiter', version: '1.17.3'`
`testImplementation group: 'org.testcontainers', name: 'mariadb', version: '1.17.3'`

**Maven:**  
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
    <groupId>org.mariadb.jdbc</groupId>
    <artifactId>mariadb-java-client</artifactId>
    <version>3.0.8</version>
</dependency>
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>1.17.3</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>mariadb</artifactId>
    <version>1.17.4</version>
    <scope>test</scope>
</dependency>
```

PostgreSQL

**Gradle:**  
`implementation group: 'org.springframework.boot', name: 'spring-boot-starter-data-jpa'`
`implementation group: 'org.postgresql', name: 'postgresql', version: '42.5.0'`
`testImplementation group: 'org.testcontainers', name: 'junit-jupiter', version: '1.17.3'`
`testImplementation group: 'org.testcontainers', name: 'postgresql', version: '1.17.3'`

**Maven:**  
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.5.0</version>
</dependency>
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>1.17.3</version>
    <scope>test</scope>
  </dependency>
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>postgresql</artifactId>
    <version>1.17.3</version>
    <scope>test</scope>
</dependency>
```

As configurações necessárias são adicionadas ao arquivo application.yaml para a aplicação se conectar na base de dados. Confira o exemplo para PostgreSQL:

**application.yaml:**  
```yaml
  datasource:
    driver-class-name: org.postgresql.Driver
    url: jdbc:postgresql://localhost:5432/test
    username: user
    password: password
  jpa:
    show-sql: true
    database-platform: org.hibernate.dialect.PostgreSQLDialect
```

Utilize variáveis de ambiente para subir o seu projeto em ambiente produtivo!
