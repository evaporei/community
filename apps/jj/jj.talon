tag: terminal
and tag: user.jj
-
jelly {user.jj_command} [<user.jj_arguments>]:
    args = jj_arguments or ""
    "jj {jj_command}{args} "

# Special commands
jelly init$: "jj git init --colocate\n"

jelly: "jj "

butter <user.jj_arguments>: "{jj_arguments} "
