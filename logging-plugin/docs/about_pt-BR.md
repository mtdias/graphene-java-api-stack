## Visão Geral
### Como o Logging Plugin funciona

Quando aplicado, este plugin adiciona um arquivo `logback-spring.xml`, configurado para uso da lib **Logstash Logback Encoder**, ao diretório `{projectRoot}/src/main/resources`.

Ao iniciar a aplicação, o output dos logs se dará automaticamente em formato JSON.

Confira mais informações sobre como customizar o output dos logs por meio do [**Logstash Logback Encoder**](https://github.com/logfellow/logstash-logback-encoder).
