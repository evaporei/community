tag: terminal
and tag: user.cargo
-
cargo {user.cargo_command} [<user.cargo_arguments>]:
    args = cargo_arguments or ""
    "cargo {cargo_command}{args} "

# # it doesn't work with or without the lines below
# cargo build$: "cargo build\n"
# cargo check$: "cargo check\n"
# cargo test$: "cargo test\n"
# cargo fmt$: "cargo fmt\n"
