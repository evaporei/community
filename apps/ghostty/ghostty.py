from talon import Context, Module, actions

ctx = Context()
mod = Module()

mod.apps.ghostty = "app.name: Ghostty"
mod.apps.ghostty = """
os: mac
and app.bundle: com.mitchellh.ghostty
"""
ctx.matches = r"""
app: ghostty
"""

directories_to_remap = {}
directories_to_exclude = {}

# doesn't work
@mod.action_class
class Actions:
    def jelly():
        actions.insert("jj ")
        # actions.key("j-j")

@ctx.action_class("user")
class UserActions:
    def tab_jump(number: int):
        actions.key(f"cmd-{number}")

    def tab_final():
        actions.key("cmd-9")

    def terminal_clear_screen():
        """Clear screen"""
        actions.key("ctrl-l")
