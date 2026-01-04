import csv
import os
from pathlib import Path

from talon import Context, Module, actions, resource

mod = Module()
ctx = Context()

mod.list("jj_command", desc="Jujutsu commands.")
mod.list("jj_argument", desc="Command-line jujutsu options and arguments.")


@mod.capture(rule="{user.jj_argument}+")
def jj_arguments(m) -> str:
    """A non-empty sequence of jujutsu command arguments, preceded by a space."""
    return " " + " ".join(m.jj_argument_list)
