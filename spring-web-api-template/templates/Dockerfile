#OFICIAL docker-hub image eclipse-temuriun for Java {{project_java_version}}
FROM eclipse-temurin:{{project_java_version}}
RUN mkdir app

{%set jar_path = "build/libs" if build_tool == "Gradle" else "target" %}
ADD {{jar_path}}/{{project_name}}-*-final.jar ./app/springApp.jar

EXPOSE ${SERVER_PORT}
ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom","-jar","./app/springApp.jar"]