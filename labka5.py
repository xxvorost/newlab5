class File:

    def __init__(self, name, extension, size):
        self.name = name
        self.extension = extension
        self.size = size

    def __str__(self):
        return f"{self.name}.{self.extension} ({self.size} байт)"


class Folder:

    def __init__(self, name):
        self.name = name
        self.files = []
        self.folders = []

    def __str__(self):
        return f"{self.name} ({len(self.files)} файлів, {len(self.folders)} папок)"

    def add_file(self, file):
        self.files.append(file)

    def add_folder(self, folder):
        self.folders.append(folder)

    def get_files(self):
        return self.files

    def get_folders(self):
        return self.folders

    def get_path(self):
        path = self.name
        for folder in self.folders:
            path = f"{path}/{folder.name}"
        return path


root = Folder("Корень")

root.add_file(File("файл1.txt", "txt", 100))
root.add_file(File("файл2.jpg", "jpg", 200))

folder1 = Folder("Папка1")
folder2 = Folder("Папка2")
root.add_folder(folder1)
root.add_folder(folder2)

folder1.add_file(File("файл3.docx", "docx", 300))
folder2.add_file(File("файл4.pdf", "pdf", 400))


def print_tree(folder, indent=0):
    for file in folder.get_files():
        print(f"-" * 25)
        print(f"{' ' * indent}{file}")
    for folder in folder.get_folders():
        print_tree(folder, indent + 1)


print_tree(root)
