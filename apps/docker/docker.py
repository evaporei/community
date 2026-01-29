import csv
import os
from pathlib import Path

from talon import Context, Module, actions, resource

mod = Module()
ctx = Context()

mod.list("docker_command", desc="Docker commands.")
mod.list("docker_argument", desc="Command-line docker options and arguments.")
mod.list("docker_compose_command", desc="Docker Compose commands.")
mod.list("docker_compose_argument", desc="Command-line docker compose options and arguments.")


@mod.capture(rule="{user.docker_argument}+")
def docker_arguments(m) -> str:
    """A non-empty sequence of docker command arguments, preceded by a space."""
    return " " + " ".join(m.docker_argument_list)


@mod.capture(rule="{user.docker_compose_argument}+")
def docker_compose_arguments(m) -> str:
    """A non-empty sequence of docker compose command arguments, preceded by a space."""
    return " " + " ".join(m.docker_compose_argument_list)
