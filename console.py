#!/usr/bin/python3
# Command interpreter for AirBnB project
import cmd, sys, gc
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    instances = []

    def do_create(self, name):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not name:
            print("** class name missing **")
            return
        try:
            self.name = eval(name)()
        except NameError:
            print("** class doesn't exist **")
            return
        my_model = self.name
        self.instances.append(my_model)
        print(my_model.id)

    def do_show(self, *args): # name=None, id=None):
        """Prints the string representation of an instance based on the class name and id"""
        params = ' '.join(args)
        params = params.split(' ')

        if len(params[0]) == 0:
            print("** class name missing **")
            return

        if len(params) == 1:
            print("** instance id missing **")
            return

        name = params[0]
        id = params[1]


        self.name = eval(name)()
        # print("hi", self.name.__class__.__name__, "bye", BaseModel.__class__.__name__)

        if self.name.__class__.__name__ != "BaseModel":
        # try:
        #     self.name = eval(name)()
        # except NameError:
            print("** class doesn't exist **")
            return

        self.id = id

        # print("hello", self.name.__class__.__name__)
        # print("goodbye", vars(self.name))

        for obj in gc.get_objects():
            if isinstance(obj, BaseModel):
                print(obj)

        for inst in self.instances:
            if inst.id == self.id:
                print(self.name)
                return
            else:
                print("** no instance found **")
                return

        # try:
        #     self.id = my_model.id
        # except NameError:
        #     print("** no instance found **")
        #     return


    def do_destroy(self, name, id):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        if not name:
            print("** class name missing **")
        if not id:
            print("** instance id missing **")
        if not attr_name:
            print("** attribute name missing **")
        if not attr_val:
            print("** value missing **")

    def do_all(self, name=None):
        """Prints all string representation of all instances based or not on the class name"""

        for obj in gc.get_objects():
            if isinstance(obj, BaseModel):
                print(obj)


    def do_update(self, name, id, attr_name, attr_val):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        if not name:
            print("** class name missing **")
        if not id:
            print("** instance id missing **")


    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ Press Ctrl-d to exit the program """
        print()
        return True

    def emptyline(self):
        """Do nothing when user enters nothing and presses Enter.
        Default is to repeat last command entered.
        """
        pass

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("EOF: Press Ctrl-d to exit the program")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
