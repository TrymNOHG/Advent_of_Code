# Construct a tree for the file directory
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, path, size=0, directories=None, files=None, parent=None):
        if directories is None:
            directories = {}
        if files is None:
            files = []
        self.path = path
        self.size = size
        self.directories = directories
        self.files = files
        self.parent = parent

    def add(self, name, current_direc=None):
        string_arr = name.split(" ")
        if string_arr[0] == "dir":
            self.directories[string_arr[1]] = Directory(self.path + "/" + string_arr[1], parent=current_direc)
            return self.directories.get(string_arr[1])
        else:
            size = string_arr[0]
            name = string_arr[1]
            self.files.append(File(name, int(size)))
            self.size += int(size)

            self.update_parent_size(int(size), current_direc)

    def update_parent_size(self, size, current_node):
        parent_node = current_node.parent
        if parent_node is not None:
            parent_node.size += size
            self.update_parent_size(size, parent_node)

    def print_directory(self):
        for file in self.files:
            print(file)


"""
    The size of a directory is the size of all the files inside it.
"""


class FileSystem:
    def __init__(self, num_nodes=0, root=Directory("/"), list_of_directories=None):
        if list_of_directories is None:
            list_of_directories = {}
        self.num_nodes = num_nodes
        self.root = root
        self.list_of_directories = list_of_directories
        self.list_of_directories[root.path] = root

    def add_node(self, node, directory):
        if self.num_nodes == 0:
            self.root = node
            return

        parent_directory = self.find_directory(directory)
        if parent_directory is None:
            raise Exception(str(directory) + " is not a valid directory.")
        parent_directory.directories.add(directory)
        return

    def add(self, name, current_directory):
        new_directory = current_directory.add(name, current_directory)
        if new_directory is not None:
            self.list_of_directories[new_directory.path] = new_directory

    # def find_directory(self, directory_name, current_directory):
    #     print(directory_name)
    #     print(current_directory)
    #     assert current_directory is not None
    #     if current_directory.name == directory_name:
    #         return current_directory
    #     else:
    #         for direct in current_directory.directories:
    #             print("hi")
    #             current_directory = self.find_directory(directory_name, direct)
    #     return current_directory

    """
        In order to only allow people to navigate downwards the tree, and not jump to random places, the
        find_directory method above should be implemented.
    """

    def find_directory(self, directory_name):
        return self.list_of_directories.get(directory_name)

    def print(self):
        current_node = self.root
        while current_node is not None:
            print(current_node.path)
            print(current_node.files)


elf_file_system = FileSystem()


def navigate_directory(cwd):
    if ".." in command:
        return cwd.parent if cwd.parent is not None else elf_file_system.root
        # Name of this type of structuring ^^ Ternary operation
    elif "/" in command:
        return elf_file_system.root
    else:
        return elf_file_system.find_directory(cwd.path + "/" + command.strip("\n").split("$ ")[1].split(" ")[1])


with open("input.txt") as shell_commands:
    cwd = elf_file_system.root
    index = 0
    for command in shell_commands:
        if "$ ls" in command:
            continue
        elif "$ cd" in command:
            cwd = navigate_directory(cwd)
        else:
            elf_file_system.add(command.strip("\n"), cwd)

        index += 1
    total_size = 0

    # print(sum(list(filter(lambda direct -> direct.size <= 100000, elf_file_system.list_of_directories.values()))))

    # Part 1.
    for directory in elf_file_system.list_of_directories.values():
        if directory.size <= 100000:
            total_size += directory.size

    print("The total size of directories under 100000 is " + str(total_size))

    # Part 2.
    space_left = 70000000 - elf_file_system.root.size

    min_file_needed = elf_file_system.root

    if space_left < 30000000:
        extra_space_needed = 30000000 - space_left
        for directory in elf_file_system.list_of_directories.values():
            if extra_space_needed <= directory.size < min_file_needed.size:
                min_file_needed = directory

    print("The smallest file needed to be deleted is " + str(min_file_needed.size))

if __name__ == '__main__':
    print()
