## Intro

This is a template for writing a modern Python backend application or microservice, using what I personally feel are best practices and patterns. It is minimal and independent of any major frameworks. I have used this at my last few projects in production and it has worked very well, and it contains my ongoing learnings and iterations.

I didn't feel like writing a code generator, so to use this, just copy the repo and delete the parts you don't need, and customize it however you like, Joel and Steve :).
I think it is a good starting point as is with a lot of useful defaults, but you can obviously customize it, swap our libraries/technologies, etc.

Kein Deutsch, es tut mir nicht leid...

### Features:

- GraphQL server
- gRPC server (for use as microservice)
- Easy local development with docker-compose
- Deployment with AWS ECS
- CLI management commands
- Unit testing
- Basic user session/auth features

### Libraries/Technologies used:

- Python3
- Flask + uwsgi + nginx (for web)
- Graphene (for graphql)
- gRPC + protobuf3 (for grpc server)
- Celery (for async worker jobs)
- APScheduler for periodic jobs
- SQLAlchemy ORM
- PostgreSQL database
- Redis for Celery queue
- Supervisor for process management
- Docker
- pytest

### Further Technologies to be used:

- Kotlin (mobile app)
- Runtastic API
- AWS Cloud

### Original Developers:

augusto Chow
Augusto Da Silva
