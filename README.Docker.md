### Building and running your application

This functionality requires a docker environment such as docker desktop (windows) or docker engine (linux). 

When you're ready, start your mcp server by running:
`docker compose up --build`.

Your eu-ai-act mcp server will be available at http://localhost:8001/mcp. Update the configuration of your AI applications and agents to use this endpoint instead of the stdio path. 

### Deploying your application to the cloud

First, build your image, e.g.: `docker build -t myapp .`.
If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t myapp .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.

### References
* [Docker's Python guide](https://docs.docker.com/language/python/)