#### **Configurações automáticas**

O plugin cria automaticamente um Bean de configuração do Tracer.

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

O plugin também adicionar a dependência `io.opentracing.contrib:opentracing-spring-jaeger-web-starter:3.1.2` ao gradle

#### **Execução em Ambiente local**

Para executar o plugin, execute o comando abaixo para disponibilizar o contêiner **`jaegertracing`**:

```
  docker run -d -p6831:6831/udp -p16686:16686 jaegertracing/all-in-one:latest
```

Para visualizar os traces, acesse [este link](http://localhost:16686/).
