#### **Automatic Configurations**

The plugin automatically creates an XML with logback configurations (default implementation) of Spring Boot:

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

The plugin also adds the dependency `net.logstash.logback:logstash-logback-encoder` version `7.2` to the project (Gradle/Maven).
