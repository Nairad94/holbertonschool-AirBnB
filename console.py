#!/usr/bin/python3
""" Console for the AirBnB """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ command interpreter """
    prompt = "(hbnb) "
    dic_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ End of File """
        return True

    def emptyline(self):
        """ Does nothing when given empty + enter """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.dic_classes:
            print("** class doesn't exist **")
        else:
            instance = HBNBCommand.dic_classes[arg]()
            storage.save()
            print(instance.id)

    def do_show(self, arg):
        """ Prints representation of an instance based on the class name and id """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.dic_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_arg = storage.all()
            if key in all_arg.keys():
                print(all_arg[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.dic_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_arg = storage.all()
            if key in all_arg.keys():
                del all_arg[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string of all instances based or not on the class name """
        args = arg.split()
        if len(args) > 0 and args[0] not in HBNBCommand.dic_classes:
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            print([str(objects[obj]) for obj in objects])

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding or updating attribute """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.dic_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        key = args[0] + '.' + args[1]
        if key not in storage.all().keys():
            print("** no instance found **")
        if len(args) == 2:
            print("** attribute name missing **")
        if len(args) == 3:
            print("** value missing **")
        instance = storage.all()[key]
        attr_name = args[2]
        try:
            attr_value = eval(args[3])
        except (NameError, ValueError):
            attr_value = args[3]
        setattr(instance, attr_name, attr_value)
        instance.save()
 
if __name__ == '__main__':
    HBNBCommand().cmdloop()
