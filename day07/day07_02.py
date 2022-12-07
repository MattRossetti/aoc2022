class Directory:
    def __init__(self, dir_name, parent):
        # print(f"making dir, {dir_name}")
        self.dir_name = dir_name
        self.parent = parent
        self.subfolders = []
        self.file_storage_size = 0

    def add_subfolder(self, new_dir):
        self.subfolders.append(new_dir)
        # print(f"added {new_dir.dir_name} to {self.dir_name}")

    def find_own_and_child_storage_size(self, size=0):
        if self.subfolders is False:
            return size
        else:
            for subfolder in self.subfolders:
                size += subfolder.file_storage_size
                size += subfolder.find_own_and_child_storage_size()
        return size

    def find_folder_to_delete(self, size_to_find, small_folders=[]):
        size = self.find_own_and_child_storage_size(self.file_storage_size)
        if size >= size_to_find and self.dir_name != "/":
            # print(self.dir_name, size, size_to_find)
            small_folders.append((self.dir_name, size))
        for subfolder in self.subfolders:
            subfolder.find_folder_to_delete(size_to_find)
        return small_folders

    def __repr__(self):
        parent = self.parent
        if parent is None:
            parent_name = "N/A, top folder"
        else:
            parent_name = parent.dir_name
        repr_str = f"""
            Directory {self.dir_name}
            with parent: {parent_name}
            with subfolders: {self.subfolders}
            and file_storage_size: {self.file_storage_size}"""
        return repr_str


with open("input.txt") as file:
    lines = file.read().splitlines()
    file_structure = Directory("/", None)
    current_dir = file_structure
    for line in lines:
        # print(line)
        if line[0] == "$":
            if line[2:4] == "cd":
                if line[5:7] == "..":
                    current_dir = current_dir.parent
                for subfolder in current_dir.subfolders:
                    if line[5:] == subfolder.dir_name:
                        current_dir = subfolder
            # if line[2:4] == "ls":
                # print("ls")
        if line[0:3] == "dir":
            sub_dir = Directory(line[4:], current_dir)
            already_made = False
            for subfolder in current_dir.subfolders:
                if line[4:] == subfolder.dir_name:
                    already_made = True
            if not already_made:
                current_dir.add_subfolder(sub_dir)
        if line.split()[0].isnumeric():
            current_dir.file_storage_size += int(line.split()[0])
            # print("file")

used_space = file_structure.find_own_and_child_storage_size(
    file_structure.file_storage_size)
total_space = 70_000_000
unused_space = total_space - used_space
space_needed = 30_000_000
size_to_find = space_needed - unused_space

small_folders = file_structure.find_folder_to_delete(size_to_find)
smallest = None
smallest_value = None
for small_folder in small_folders:
    if smallest is None:
        smallest = small_folder[0]
        smallest_value = small_folder[1]
    if small_folder[1] < smallest_value:
        smallest = small_folder[0]
        smallest_value = small_folder[1]

answer = smallest_value
print(f"answer = {answer}")
