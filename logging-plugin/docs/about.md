## General vision
### How Logging Plugin works

When applied, this plugin adds a file `logback-spring.xml` which configures the lib **Logstash Logback Encoder**, in the directory `{projectRoot}/src/main/resources`.

Starting the app, the logs output will automatically be in JSON format.

See more information about how to customize the logs output in the following link: [**Logstash Logback Encoder**](https://github.com/logfellow/logstash-logback-encoder).
