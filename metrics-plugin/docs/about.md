Este plugin adiciona funcionalidades que permitem a obtenção de métricas, disponibilização de endpoints de monitoramento e publicação de eventos de auditoria da sua aplicação por meio do componente Spring Boot Actuator.

 - **Health**: Endpoints do Spring Boot Actuator permitem monitorar e interagir com a sua aplicação. O Spring Boot possui diversos desses endpoints pré-configurados e você também pode adicionar os seus. Por exemplo, o endpoint `health` provê informações básicas de health check da sua aplicação (para testar, basta subir sua aplicação e fazer uma chamada GET ao endpoint `/actuator/health`).
 - **Metrics**: O Spring Boot Actuator provê métricas dimensionais por meio da integração com [Micrometer](https://micrometer.io)
 - **Audit**: O Spring Boot Actuator tem um flexível framework de auditoria que publica eventos para um `AuditEventRepository`. Se o Spring Security estiver configurado, ele publica eventos de autenticação automaticamente, por exemplo. Isso pode ser muito útil para reports, dentre outras coisas.


