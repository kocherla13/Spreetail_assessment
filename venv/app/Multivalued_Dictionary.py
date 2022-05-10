class MultiValuedDictionary:
    def __init__(self):
        self.multivalued_dictionary = {}

    def print_spec(self):
        print("-------------------------------------------------------------------")
        print("ADD 'key' 'member'\nREMOVE 'key' 'member'\nREMOVEAll 'key'\n""MEMBERS 'key'"
              "\nKEYEXISTS 'key'\nMEMBEREXISTS 'key' 'member'"
              "\nKEYS\nCLEAR\nALLMEMBERS\nITEMS\nQUIT\n")
        print("-------------------------------------------------------------------")

    def add(self, command_list_args):
        """
        Adds a member to a collection for a given key.
        Displays an error if the member already exists for the key.
        :param command_list_args:
        :return: None
        """
        if command_list_args[1] not in self.multivalued_dictionary:
            self.multivalued_dictionary[command_list_args[1]] = {command_list_args[2]}
            print("Added")
        elif command_list_args[2] not in self.multivalued_dictionary[command_list_args[1]]:
            self.multivalued_dictionary[command_list_args[1]].add(command_list_args[2])
            print("Added")
        else:
            print("Error, Member already exists for the key")

    def removeall(self, command_list_args):
        """
        Removes all members for a key and removes the key from the dictionary.
        Displays an error if the key does not exist.
        :param command_list_args:
        :return: None
        """
        if command_list_args[1] not in self.multivalued_dictionary:
            print("ERROR, key does not exist")
        else:
            del self.multivalued_dictionary[command_list_args[1]]
            print("Removed")

    def remove(self, command_list_args):
        """
        Removes a member from a key. If the last member is removed from the key, the key is removed from the dictionary.
        If the key or member does not exist, displays an error.
        :param command_list_args:
        :return: None
        """
        if command_list_args[1] not in self.multivalued_dictionary:
            print("ERROR, key does not exist")
            return
        if command_list_args[2] not in self.multivalued_dictionary[command_list_args[1]]:
            print("ERROR, Member does not exist in the key")
            return
        else:
            self.multivalued_dictionary[command_list_args[1]].remove(command_list_args[2])
            if not self.multivalued_dictionary[command_list_args[1]]:
                del self.multivalued_dictionary[command_list_args[1]]
            print("Removed")
            return

    def keyexists(self, command_list_args):
        """
        Returns whether a key exists or not.
        :param command_list_args:
        :return: None
        """
        print(True) if command_list_args[1] in self.multivalued_dictionary else print(False)

    def memberexists(self, command_list_args):
        """
        Displays whether a member exists within a key. Displays false if the key does not exist.
        :param command_list_args:
        :return: None
        """
        try:
            print(True) if command_list_args[2] in self.multivalued_dictionary[command_list_args[1]] else print(False)
        except:
            print(False)

    def members(self, command_list_args):
        """
        Displays the collection of strings for the given key. Return order is not guaranteed.
        Displays an error if the key does not exists.
        :param command_list_args:
        :return: None
        """

        try:
            if self.multivalued_dictionary[command_list_args[1]]:
                for i in self.multivalued_dictionary[command_list_args[1]]:
                    print(i)
        except:
            print("Error, key doesn't exits")

    def keys(self):
        """
        Displays all the keys in the dictionary. Order is not guaranteed.
        :return: None
        """
        if self.multivalued_dictionary:
            [print(i) for i in self.multivalued_dictionary]

        else:
            print("(empty set)")

    def allmembers(self):
        """
        Displays all the members in the dictionary.
        Displays nothing if there are none. Order is not guaranteed.
        """
        if self.multivalued_dictionary:
            for members in self.multivalued_dictionary.values():
                for member in members:
                    print(member)
        else:
            print("(empty set)")

    def items(self):
        """
        Displays all keys in the dictionary and all of their members.
        Displays nothing if there are none. Order is not guaranteed.
        """
        count = 1
        if self.multivalued_dictionary:
            for key, members in self.multivalued_dictionary.items():
                for member in members:
                    print(str(count) + ") " + key + " : " + member)
                    count += 1
        else:
            print("(empty set)")

    def clear(self):
        """
        Removes all keys and all members from the dictionary.
        """
        self.multivalued_dictionary = {}
        print('Cleared')


if __name__ == '__main__':
    multivalued_dictionary = MultiValuedDictionary()
    print("-------------------------------------------------------------------\n")
    print("Hello Welcome to Multivalued Dictionary Application To get Started Please Enter Any of the Following")
    multivalued_dictionary.print_spec()

    while True:
        print("-------------------------------------------------------------------")
        # Takes the input from CLI
        command = input("Enter The Command ")

        command = command.strip()
        # Splits the input command to a list called command_list
        command_list = ' '.join(command.split(' ')).split()
        # A dictionary that store the command and the number of words expected in the command
        method_arguments_limit = {'add': 3, 'remove': 3, 'removeall': 2, 'members': 2,
                                  'keyexists': 2, 'memberexists': 3, 'keys': 1,
                                  'clear': 1, 'allmembers': 1, 'items': 1, 'quit': 1}

        try:
            if command:
                command_list[0] = command_list[0].lower()
                if command_list[0] == 'quit':
                    print("Thank you Have a nice day! ")
                    break
                # check if command_list[0] string has any function with its name and check the arguments count
                if command_list[0] in dir(MultiValuedDictionary) and \
                        len(command_list) == method_arguments_limit[command_list[0]]:
                    # Calling a Method dynamically using the command_list[0] string
                    if method_arguments_limit[command_list[0]] == 1:
                        getattr(multivalued_dictionary, command_list[0])()
                    else:
                        getattr(multivalued_dictionary, command_list[0])(command_list)
                else:
                    print("Invalid command Please check the Parameters")
                    multivalued_dictionary.print_spec()

        except Exception as e:
            print('exception occurred : ' + str(e))
            print("-------------------------------------------------------------------")
