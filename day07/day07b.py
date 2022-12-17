from bigtree import Node, print_tree, find_children, find_attrs, findall
import uuid

inputFile = "./input.txt"
exampleInputFile = "./input-example.txt"


if __name__ == '__main__':
    with open(inputFile, 'r') as file:
        lines = file.readlines()
    root = Node("/", file_type="folder", size=0)
    current_node = root
    result = 0
    for line in lines:
        line = line[:-1]
        if line == "$ cd ..":
            current_node = current_node.parent
        elif line.startswith("$ cd "):
            folder_name = line.removeprefix("$ cd ")
            # print(f' trimmed cd: {folder_name}')
            if current_node.name != folder_name and find_children(root, folder_name) is None:
                # yeah thats hack to prevent having same folders name (name have to be globally unique)
                current_node = Node(current_node.name + folder_name, file_type="folder", size=0, parent=current_node)
        elif line[0].isnumeric():
            words = line.split(" ")
            # print(f'{words[0]}, {words[1]}')
            # Node(words[1], file_type="file", size=int(words[0]), parent=current_node)
            # storing uuid instead of words[1] CARE HERE
            Node(uuid.uuid1(), file_type="file", size=int(words[0]), parent=current_node)
    print_tree(root, attr_list=["file_type", "size"])

    for i in range(root.max_depth, 1, -1):
        nodes = find_attrs(root, "depth", i)
        for node in nodes:
            parent_node = node.parent
            new_size = parent_node.get_attr("size") + node.get_attr("size")
            parent_node.set_attrs({"size": new_size})

    print_tree(root, attr_list=["file_type", "size"])

    max_size = 70000000 - 30000000
    current_size = root.size

    big_folders = findall(root, lambda node: node.file_type == "folder" and current_size - node.size <= max_size)
    result = min(big_folder.size for big_folder in big_folders)
    print(result)
