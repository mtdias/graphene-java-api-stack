#### **Configurações automáticas**

O plugin cria automaticamente um XML de configuração logback (implementação default) do Spring Boot:

```xml
<configuration>
  <appender name="jsonConsoleAppender" class="ch.qos.logback.core.ConsoleAppender">
    <encoder class="net.logstash.logback.encoder.LogstashEncoder"/>
  </appender>
  <root level="INFO">
    <appender-ref ref="jsonConsoleAppender"/>
  </root>
</configuration>
```

O plugin também adiciona a dependência `net.logstash.logback:logstash-logback-encoder:7.2` ao Gradle/Maven.