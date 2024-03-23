#!/usr/bin/env python3
"entry point of the command interpreter:"

import cmd


class HBNBCommand(cmd.Cmd):
    "entry point of the command interpreter:"
    
    prompt = "(hbnb) "

    def do_quit(self, arg):
        "exit the program"
        return True

    def do_EOF(self, arg):
        "exit the program"
        return True

    def help(self):
        return cmd.Cmd.help(self)

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
