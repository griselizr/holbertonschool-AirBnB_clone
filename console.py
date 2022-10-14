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

    def do_all(self, args):
        """ Prints all string representation of all instances """
        if len(args) == 0:
            all = storage.all()
            new = []
            for obj_id in all.keys():
                obj = all[obj_id]
                new.append("{}".format(obj))
            print(new)
        elif args not in classes:
            print("** class doesn't exist **")
        elif args in classes:
            all_objs = storage.all()
            for obj_id in all.keys():
                key1 = obj_id.split('.')
                if key1[0] == args:
                    obj = all_objs[obj_id]
                    print("{}".format(obj))

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
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
        for key, value in all.items():
            if s in key:
                del all[str(s)]
                storage.save()
                return
        print("** no instance found **")

    def do_update(self, args):
        """ Updates an instance based on the class name and id
        by adding or updating attribute """
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
        if len(words) == 3:
            print("** value missing **")
            return
        s1 = words[0] + '.' + words[1]
        all = storage.all()
        for key, value in all.items():
            if s1 in key:
                if len(words) == 2:
                    print("** attribute name missing **")
                    return
                if words[3][0] == "\"" and words[3][-1] == "\"":
                    setattr(value, words[2], words[3][1:-1])
                    storage.save()
                    return
                setattr(value, words[2], words[3])
                storage.save()
                return
        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
