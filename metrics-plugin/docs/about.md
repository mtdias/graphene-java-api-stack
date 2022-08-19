Este plugin adiciona funcionalidades de `obtenção de métricas`, `disponibilização de endpoints de monitoramento` e `publicação de eventos de auditoria` em sua aplicação por meio do componente Spring Boot Actuator.

 - **Health**: Spring Boot Actuator disponibiliza endpoints para monitorar e interagir com a sua aplicação. Além dos endpoints embarcados do Spring Boot, você pode adicionar enpoints customizados. Por exemplo, o endpoint `health` provê informações básicas de health check da sua aplicação (para testar, inicie a aplicação e faça uma chamada GET para `/actuator/health`).
 - **Metrics**: O Spring Boot Actuator provê métricas dimensionais por meio da integração com [Micrometer](https://micrometer.io)
 - **Audit**: O Spring Boot Actuator tem um flexível framework de auditoria que publica eventos para um `AuditEventRepository`. Isso pode ser muito útil para reports. Por exemplo, em conjunto com o Spring Security eventos de autenticação serão publicados automaticamente.


