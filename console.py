#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """ command Prompt """
    prompt = "(hbnb) "

    def do_EOF(self, args):
        """CTRl-D to exit\n"""
        print()
        return True

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
