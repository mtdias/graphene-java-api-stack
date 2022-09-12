
## Web API com Spring Boot

Este template visa acelerar o desenvolvimento e publicação de Web APIs para ambientes Cloud Native com Spring Boot e outras tecnologias Spring.


### Docker - Executar a Aplicação via docker container image
#####  (First of All)
- Realizar o build da aplicação utilizando **gradle ou maven**. Ex:
    - Linux
        - Maven: **./mvnw clean install**
        - Gradle: **./gradlew build**
    - Windows
        - Maven: **mvnw clean install**
        - Gradle: **gradlew build**

##### (Opção 1). Realizar o build da imagem via docker-compose
- Para subir o container:
    - **docker-compose up --build**
- Para derrubar o container:
    - **docker-compose down**

##### (Opção 2). Realizar o build da imagem via Dockerfile
- Executar os seguintes comandos:
    - **docker build . -t {{project_artifact_id}}:1.0.0**
    - **docker run --name {{project_artifact_id}}-app -p 8080:8080 -d {{project_artifact_id}}:1.0.0**