#!/usr/bin/python3
""" module cmd entry point of the command interpreter:"""
import cmd
from models import storage
from models.base_model import BaseModel

classes = ['BaseModel']


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

    def do_create(self, args):
        """ create a new instance of a class and prints the id """
        if len(args) == 0:
            print("** class name missing **")
        elif args not in classes:
            print("** class doesn't exist **")
        else:
            for i in classes:
                if i == args:
                    a1 = str(args) + '()'
                    a = eval(a1)
            print(a.id)
            a.save()
        pass

    def do_show(self, args):
        """ Prints the str of an instance of a class name and id """
        words = args.split(' ')
        if len(args) == 0:
            print("** class name missing **")
            return
        elif words[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(words) == 1:
            print("** instance id missing **")
            return
        all = storage.all()
        s = words[0] + '.' + words[1]
        for obj_id in all.keys():
            if s == obj_id:
                obj = all[obj_id]
                print(obj)
                return
        print("** no instance found **")
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
