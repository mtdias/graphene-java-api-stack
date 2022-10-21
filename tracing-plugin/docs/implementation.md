#### **Automatic Configurations**

The plugin creates a Bean to configure the Tracer.

```java
@org.springframework.context.annotation.Configuration
public class TracerConfig {

  @Bean
  public io.opentracing.Tracer initTracer() {
    Configuration.SamplerConfiguration samplerConfig = new Configuration
        .SamplerConfiguration()
        .withType("const")
        .withParam(1);
    return Configuration.fromEnv("<project_artifact_id>")
        .withSampler(samplerConfig).getTracer();
  }

  @Bean
  public RestTemplate restTemplate(RestTemplateBuilder restTemplateBuilder) {

    return restTemplateBuilder.build();
  }
}
```

The plugin also adds the dependency based on the selected *build_tool*:

**Gradle:**  
`io.opentracing.contrib:opentracing-spring-jaeger-web-starter:3.1.2`

**Maven:**  
```xml
<dependency>
  <groupId>io.opentracing.contrib</groupId>
  <artifactId>opentracing-spring-jaeger-starter</artifactId>
  <version>3.1.2</version>
</dependency>
```

#### **Running on Local Environment**

To use the plugin, run the command below to enable the **`jaegertracing`** container:

```
  docker run -d -p6831:6831/udp -p16686:16686 jaegertracing/all-in-one:latest
```

To see the traces, access [this URL](http://localhost:16686/).
