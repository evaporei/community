tag: terminal
and tag: user.cargo
-
cargo {user.cargo_command} [<user.cargo_arguments>]:
    args = cargo_arguments or ""
    "cargo {cargo_command}{args} "

bike <user.cargo_arguments>: "{cargo_arguments}"
