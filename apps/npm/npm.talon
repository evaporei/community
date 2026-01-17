tag: terminal
and tag: user.npm
-
n p m {user.npm_command} [<user.npm_arguments>]:
    args = npm_arguments or ""
    "npm {npm_command}{args} "

n p m [<user.npm_arguments>]:
    args = npm_arguments or ""
    "npm{args} "

node flag <user.npm_arguments>: "{npm_arguments} "
