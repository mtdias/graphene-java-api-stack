
## Web API com Spring Boot

This template aims to accelerate the development and publishing of Web APIs for Cloud Native environments with Spring Boot and other Spring technologies.

### **Requirements**
- [**docker >= 20.10.12**](https://docs.docker.com/engine/install/)
- [**docker compose >= v2.11.2**](https://docs.docker.com/compose/install/)

#####  (First of All)
- Build the application using **gradle or maven**. E.g:
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

##### (Option 1). Run application via docker compose
-   It's possible to run the docker compose directly using the default profile, or configure a specific profile through the environment variable **SPRING_PROFILES_ACTIVE**.
- #### E.g:
    - To run the default profile it's necessary configure docker compose as showed bellow
        ```yaml
            environment:
              SPRING_PROFILES_ACTIVE:
        ```
    - To run a specific profile it's necessary configure docker compose as showed bellow
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

##### (Option 2). Run application via dockerfile
- Run the following commands:
    - To run a specific profile it's necessary to export the environment variable **SPRING_PROFILES_ACTIVE** setting one of the profiles (dev, hom or prod),
      or you run directly to run using the default profile.
         ```bash
            docker build . -t {{project_artifact_id}}:1.0.0
            docker run --name {{project_artifact_id}}-app -p 8080:8080 -d {{project_artifact_id}}:1.0.0
        ```


#### (Option 4).Run application directly
-  After had been executed the build, you can run the application jar through the follow command:
    ```
        java -jar build/libs/{{project_artifact_id}}-{{project_version}}-final.jar 
    ```
- You can run a specific profile setting the following configuration:
    - -Dspring.profiles.active=dev,hom or prod

- ### Full e.g:
    ```
        java -jar -Dspring.profiles.active=dev,hom or prod build/libs/{{project_artifact_id}}-{{project_version}}-final.jar 
    ```
