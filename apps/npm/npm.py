from talon import Context, Module

mod = Module()
ctx = Context()

mod.list("npm_command", desc="npm commands.")
mod.list("npm_argument", desc="Command-line npm options and arguments.")


@mod.capture(rule="{user.npm_argument}+")
def npm_arguments(m) -> str:
    """A non-empty sequence of npm command arguments, preceded by a space."""
    return " " + " ".join(m.npm_argument_list)
