tag: terminal
and tag: user.docker
-
docker {user.docker_command} [<user.docker_arguments>]:
    args = docker_arguments or ""
    "docker {docker_command}{args} "

docker compose {user.docker_compose_command} [<user.docker_compose_arguments>]:
    args = docker_compose_arguments or ""
    "docker compose {docker_compose_command}{args} "

moby <user.docker_arguments>: "{docker_arguments} "
moby compose <user.docker_compose_arguments>: "{docker_compose_arguments} "
