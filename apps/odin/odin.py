import csv
import os
from pathlib import Path

from talon import Context, Module, actions, resource

mod = Module()
ctx = Context()

mod.list("odin_command", desc="Odin commands.")
mod.list("odin_argument", desc="Command-line odin options and arguments.")


@mod.capture(rule="{user.odin_argument}+")
def odin_arguments(m) -> str:
    """A non-empty sequence of odin command arguments, preceded by a space."""
    return " " + " ".join(m.odin_argument_list)
