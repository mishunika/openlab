from docker.client import Client
from docker.utils import kwargs_from_env

cli = Client(**kwargs_from_env())
container = cli.create_container(image='busybox:latest', command='/bin/echo 2342', rm=True)
print(container)
response = cli.start(container=container.get('Id'))
print(container)
print(response)
print(container.logs())
print(cli.version())
