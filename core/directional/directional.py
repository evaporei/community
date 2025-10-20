from talon import Context, Module, actions

mod = Module()
mod.tag("directional")

ctx_browser = Context()
ctx_browser.matches = r"""
tag: browser
"""

ctx_mac = Context()
ctx_mac.matches = r"""
os: mac
"""


@ctx_browser.action_class("user")
class BrowserActions:
    pass


@ctx_mac.action_class("user")
class MacActions:
    pass


@mod.action_class
class Actions:
    pass
