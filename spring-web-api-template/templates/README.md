
## Web API com Spring Boot

Este template visa acelerar o desenvolvimento e publicação de Web APIs para ambientes Cloud Native com Spring Boot e outras tecnologias Spring.

### **Pré-requisitos**
- [**docker >= 20.10.12**](https://docs.docker.com/engine/install/)
- [**docker compose >= v2.11.2**](https://docs.docker.com/compose/install/)

#####  (Primeiros passos)
- Realizar o build da aplicação através do **gradle ou maven**. Ex:
  - Linux
      ```bash
      #Maven:
        ./mvnw clean install
      #OR Gradle
        ./gradlew build
      ```
  - Windows
      ```bash
      #Maven: 
          mvnw clean install**
      #OR Gradle: 
          gradlew build
      ``` 

##### (Opção 1). Executar a aplicação através do docker compose
- É possível executar a aplicação diretamente usando o perfil padrão, ou configurar um perfil específico através da variável de ambiente **SPRING_PROFILES_ACTIVE**.     
- #### Ex:
  - Para executar a aplicação utilizando o perfil padrão, é nececssário configurar o docker compose como mostrado abaixo:
      ```yaml
          environment:
            SPRING_PROFILES_ACTIVE:
      ```
  - Para executar através de um perfil específico, é necessário configurar o docker compose conforme mostrado abaixo:
     ```yaml
         environment:
           SPRING_PROFILES_ACTIVE: dev, hom or prod
     ```
  - Up container:
     ```bash
         docker compose up --build
     ``` 
  - Down container:
     ```bash
        docker compose down
     ```

##### (Opção 2). Executar a aplicação através do dockerfile
- Executar os seguintes comandos:
  - Para executar um perfil específico, é necessário exportar a variável de ambiente **SPRING_PROFILES_ACTIVE**, atribuindo um dos seguintes profiles (dev, hom or prod), ou
executar diretamente usando o perfil padrãot profile.
       ```bash
          docker build . -t {{project_artifact_id}}:1.0.0
          docker run --name {{project_artifact_id}}-app -p 8080:8080 -d {{project_artifact_id}}:1.0.0
      ```
    
#### (Opção 3). Execução do jar
- Depois que o build tiver sido executado através do gradle ou maven, você pode executar o jar da aplicação através dos seguintes comandos: 
    ```
        java -jar build/libs/{{project_artifact_id}}-{{project_version}}-final.jar 
    ```
- Você pode executar um perfil específico através das seguintes parametrizações:
   - -Dspring.profiles.active=dev,hom or prod
  
- ### Exemplo completo da execução: 
    ```
        java -jar -Dspring.profiles.active=dev,hom or prod build/libs/{{project_artifact_id}}-{{project_version}}-final.jar 
    ```
