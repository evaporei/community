from talon import Context, Module, actions, app

ctx = Context()
mod = Module()

mod.apps.snowman = "app.name: Snowman"
mod.apps.snowman = """
os: mac
app.bundle: com.agoodsnowman

"""
ctx.matches = r"""
app: agoodsnowman
"""


@ctx.action_class("user")
class UserActions:
    pass
