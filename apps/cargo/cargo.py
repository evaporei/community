import csv
import os
from pathlib import Path

from talon import Context, Module, actions, resource

mod = Module()
ctx = Context()

mod.list("cargo_command", desc="Cargo commands.")
mod.list("cargo_argument", desc="Command-line cargo options and arguments.")


@mod.capture(rule="{user.cargo_argument}+")
def cargo_arguments(m) -> str:
    """A non-empty sequence of cargo command arguments, preceded by a space."""
    return " " + " ".join(m.cargo_argument_list)
