tag: terminal
and tag: user.odin
-
odin {user.odin_command} [<user.odin_arguments>]:
    args = odin_arguments or ""
    "odin {odin_command}{args} "

loki <user.odin_arguments>: "{odin_arguments}"

odin format$: "odinfmt -w .\n"
