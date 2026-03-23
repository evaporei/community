from talon import Context, Module

mod = Module()
ctx = Context()

mod.list("brew_command", desc="Homebrew commands.")
mod.list("brew_argument", desc="Command-line Homebrew options and arguments.")


@mod.capture(rule="{user.brew_argument}+")
def brew_arguments(m) -> str:
    """A non-empty sequence of Homebrew command arguments, preceded by a space."""
    return " " + " ".join(m.brew_argument_list)
