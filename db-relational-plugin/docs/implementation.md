#### Configurations

The plugin adds the necessary code snippet to upload a local database to the docker-compose.yaml file. For more information about the parameters of each image, see below:

[**PostgreSQL**](https://hub.docker.com/_/postgres)

[**MariaDB**](https://hub.docker.com/_/mariadb)

It also adds the dependencies and code snippets for the application to connect to relational databases.

The plugin adds the dependencies according to the *build_tool* selected when the project was created using the graphene-java-api-stack stack:

MariaDB

**Gradle:**
```gradle  
`implementation group: 'org.springframework.boot', name: 'spring-boot-starter-data-jpa'`
`implementation group: 'org.mariadb.jdbc', name: 'mariadb-java-client', version: '3.0.8'`
`testImplementation group: 'org.testcontainers', name: 'junit-jupiter', version: '1.17.3'`
`testImplementation group: 'org.testcontainers', name: 'mariadb', version: '1.17.3'`
```

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
```gradle
`implementation group: 'org.springframework.boot', name: 'spring-boot-starter-data-jpa'`
`implementation group: 'org.postgresql', name: 'postgresql', version: '42.5.0'`
`testImplementation group: 'org.testcontainers', name: 'junit-jupiter', version: '1.17.3'`
`testImplementation group: 'org.testcontainers', name: 'postgresql', version: '1.17.3'`
```

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

The settings necessary for the application to connect to the database will be added to the application.yaml file:
See the PostgreSQL example below:

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

Use environment variables to upload the project to a productive environment!
