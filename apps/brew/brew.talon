tag: terminal
and tag: user.brew
-
brew {user.brew_command} [<user.brew_arguments>]:
    args = brew_arguments or ""
    "brew {brew_command}{args} "

brew [<user.brew_arguments>]:
    args = brew_arguments or ""
    "brew{args} "
