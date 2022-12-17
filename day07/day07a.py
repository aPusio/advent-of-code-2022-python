from bigtree import Node, print_tree, find_children, find_attrs

inputFile = "./input.txt"
exampleInputFile = "./input-example.txt"


if __name__ == '__main__':
    with open(exampleInputFile, 'r') as file:
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
                current_node = Node(folder_name, file_type="folder", size=0, parent=current_node)
        elif line[0].isnumeric():
            words = line.split(" ")
            # print(f'{words[0]}, {words[1]}')
            Node(words[1], file_type="file", size=int(words[0]), parent=current_node)
    print_tree(root, attr_list=["file_type", "size"])

    files = find_attrs(root, "file_type", "file")
    for file in files:
        parent_node = file.parent
        new_size = parent_node.get_attr("size") + file.get_attr("size")
        parent_node.set_attrs({"size": new_size})
        print(file)
    print_tree(root, attr_list=["file_type", "size"])
    print(result)
