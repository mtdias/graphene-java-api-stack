This plugin adds the functionality to obtain metrics, enabling endpoints to monitoring and publish auditory events in your application, making use of Spring Bott Actuator.
- **Health**: Spring Boot Actuator enables endpoints to monitor and interact with your application, for example the endpoint `health` gives basic information of health check in your application.

> To test, start the application and make a GET request to `/actuator/health`.
- **Metrics**: O Spring Boot Actuator gives dimensional metrics with [Micrometer](https://micrometer.io)
- **Audit**: O Spring Boot Actuator has a flexible framework of auditory that publish evens to an `AuditEventRepository`. This can be very useful to reports. For example, with the Spring Security, the events of authentication will be published automatically.
