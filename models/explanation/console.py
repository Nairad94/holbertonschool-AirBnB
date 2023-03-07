#!/usr/bin/python3
""" Console for the AirBnB """
import cmd # es un módulo de Python que proporciona una estructura para crear un intérprete de línea de comandos
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
    prompt = "(hbnb) " # es el prompt que se muestra en la consola
    # es un diccionario que asigna los nombres de las clases de modelo a las clases reales.
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
        """ No hace nada cuando se le da vacío + enter """
        pass

    def do_create(self, arg):
        """ do_create es un método que crea una nueva instancia de la clase de modelo especificada por el usuario.
        Si no se especifica un argumento, se muestra un mensaje de error. Si el argumento no es una clase de modelo válida, se muestra otro mensaje de error.
        Si todo está bien, se crea la instancia, se guarda en el archivo JSON y se muestra el ID de la instancia """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.dic_classes:
            print("** class doesn't exist **")
        else:
            instance = HBNBCommand.dic_classes[arg]()
            storage.save()
            print(instance.id)

    def do_show(self, arg):
        """ Imprime la representación de una instancia basada en el nombre de la clase y la identificación """
        args = arg.split() # divide los argumentos por espacio en una lista de palabras
        if not arg: # si el argumento está vacío, muestra un mensaje de error
            print("** class name missing **")
        elif args[0] not in HBNBCommand.dic_classes: # si el primer elemento de la lista de argumentos no está en el diccionario dic_classes de la clase HBNBCommand, muestra un mensaje de error
            print("** class doesn't exist **")
        elif len(args) == 1: # si la lista de argumentos solo tiene una palabra, muestra un mensaje de error 
            print("** instance id missing **")
        else:
        """ de lo contrario, crea una cadena que contiene la clase y el id separados por un punto,
            busca en el diccionario __objects del objeto storage y comprueba si la clave creada está en el diccionario.
            se encuentra, se imprime la representación de la instancia correspondiente, de lo contrario, se muestra un mensaje de error """
            key = args[0] + "." + args[1]
            all_arg = storage.all()
            if key in all_arg.keys():
                print(all_arg[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """ se utiliza para eliminar una instancia basada en el nombre de la clase y el ID. """
        args = arg.split() # divide los argumentos por espacio en una lista de palabras
        if not arg: # si el argumento está vacío, muestra un mensaje de error
            print("** class name missing **")
        elif args[0] not in HBNBCommand.dic_classes: # si el primer elemento de la lista de argumentos no está en el diccionario dic_classes de la clase HBNBCommand, muestra un mensaje de error
            print("** class doesn't exist **")
        elif len(args) == 1: # si la lista de argumentos solo tiene una palabra, muestra un mensaje de error
            print("** instance id missing **")
        else:
            """ Si se proporciona tanto el nombre de la clase como el ID de la instancia, creamos una clave key concatenando el nombre de la clase y el ID de la instancia,
            y luego verificamos si la clave key existe en el diccionario all_arg que contiene todas las instancias. Si la clave existe,
            eliminamos la instancia y guardamos los cambios utilizando la función save() de la clase storage. Si la clave no existe, imprimimos un mensaje de error """
            key = args[0] + "." + args[1]
            all_arg = storage.all()
            if key in all_arg.keys():
                del all_arg[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """ Imprime todas las cadenas de todas las instancias basadas o no en el nombre de la clase """
        args = arg.split()
        if len(args) > 0 and args[0] not in HBNBCommand.dic_classes:
            print("** class doesn't exist **")
        else:
            objects = storage.all() # Obtiene todas las instancias almacenadas en el archivo JSON utilizando el método all() de la variable storage, que es una instancia de la clase FileStorage.
            print([str(objects[obj]) for obj in objects]) # Crea una lista de representaciones en string de cada objeto en objects utilizando una comprensión de lista y la función str(), y luego la imprime.

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding or updating attribute """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.dic_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            setattr(storage.all()[key], args[2], args[3])
            storage.save()
        """ En este caso, la función setattr() toma tres argumentos: el objeto cuyo atributo se establecerá, el nombre del atributo que se establecerá y el valor que se establecerá para el atributo.
        El valor del atributo se toma del cuarto argumento args[3], mientras que el nombre del atributo se toma del tercer argumento args[2].
        El objeto cuyo atributo se establecerá se obtiene de la instancia correspondiente almacenada en storage.all()[key].
        Finalmente, el método do_update llama al método save() del objeto storage para guardar los cambios realizados en el archivo JSON de almacenamiento."""

if __name__ == '__main__':
    HBNBCommand().cmdloop()