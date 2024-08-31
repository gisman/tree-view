import os
import sys

"""## 요건
    * zip, tar, tar.gz 지원 안 함. 압축 풀고 실행.
    * size(human readable)
    * file count
    * 3 files as example
    * 📂 이모지
    * works on directory
* tree 구조로 출력


│   └── [ 12K]  viz_flow_occ_dilate_1
│       ├── [144K]  000000_10.png
│       ├── [195K]  000001_10.png
│       ├── [167K]  000002_10.png


최종 결과물
│   └📂 viz_flow_occ_dilate_1 [ 12M]
│       ├ 000000_10.png [144K]
│       ├ 000001_10.png [195K]
│       ├ 000002_10.png [167K]
│       └ 123,456 개의 파일이 더 있음
"""


def human_readable_size(size):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.0f} {unit}"
        size /= 1024


def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def has_sibling_directory(root):
    parent_dir = os.path.dirname(root)
    if not parent_dir:
        return False

    sibling_dirs = [
        d for d in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, d))
    ]
    sibling_dirs.sort()

    sibling_dirs += [
        d for d in os.listdir(parent_dir) if os.path.isfile(os.path.join(parent_dir, d))
    ]

    if sibling_dirs[-1] == os.path.basename(root):
        return False

    sibling_dirs.remove(os.path.basename(root))

    return len(sibling_dirs) > 0


def print_dir(directory, parent_has_sibling=False, depth=0, tree_lines=[""]):

    for root, dirs, files in os.walk(directory):
        dir_name = os.path.basename(os.path.normpath(root))
        dir_size = get_directory_size(root)
        has_sibling = False
        if depth > 0:
            if parent_has_sibling:
                tree_lines[depth - 1] = "│   "
            else:
                if depth > 1:
                    tree_lines[depth - 1] = "    "

            has_sibling = has_sibling_directory(directory)

        # if len(files) > 0:
        #     parent_has_sibling = True
        #     tree_lines[-1] = "└── "
        print(f'{"".join(tree_lines)}📂 {dir_name} [{human_readable_size(dir_size)}]')
        dirs.sort()

        # print directories recursively
        # tl = tree_lines.copy()
        for i, dir in enumerate(dirs):
            tl = tree_lines.copy()
            if i == len(dirs) - 1 and len(files) == 0:  # last element
                tl.append("└──")
            else:
                tl.append("├──")

            print_dir(
                f"{directory}/{dir}",
                parent_has_sibling=has_sibling,
                depth=depth + 1,
                tree_lines=tl,
            )

        # print files
        files.sort()
        # tree_lines.append("├── ")
        PARENT_LINE = "│" if has_sibling else ""
        for i, name in enumerate(files[:4]):
            file_path = os.path.join(root, name)
            file_size = os.path.getsize(file_path)
            # total_files += 1
            # total_size += file_size
            is_last = i == len(files[:4]) - 1
            # if len(dirs) > 0:
            #     is_last = False

            if "tl" in locals():
                print(
                    f'{"".join(tl[:-1])}{"└" if is_last else "├"}── {name} [{human_readable_size(file_size)}]'
                )
            else:
                print(
                    f'{"".join(tree_lines[:-1])}{PARENT_LINE}   {"└" if is_last else "├"}── {name} [{human_readable_size(file_size)}]'
                )

        if len(files) > 4:
            print(f'{"".join(tree_lines[:-1])}{PARENT_LINE}       ({len(files) - 4:,} more files)')

        return
        # print(f"dirs: {dirs}")
        # print(f"files: {files}")


def main(directory):
    print_dir(directory)


# def main_old(directory):
#     total_files = 0
#     total_size = 0

#     tree_line = [
#         "",
#     ] * 10
#     for root, dirs, files in os.walk(directory):
#         dirs.sort()
#         files.sort()

#         relative_root = os.path.relpath(root, directory)
#         if relative_root == ".":  # root directory
#             depth = 0
#             dir_name = "."
#         else:
#             depth = relative_root.count(os.sep) + 1
#             dir_name = os.path.basename(root)
#         dir_size = get_directory_size(root)

#         tree_line[depth] = "│"

#         # readable_dir_size = human_readable_size(dir_size)
#         if depth == 0:
#             print(f"📂 {dir_name} [{human_readable_size(dir_size)}]")
#         else:
#             print(
#                 f'{"  ".join(tree_line)}├── 📂 {dir_name} [{human_readable_size(dir_size)}]'
#                 # f'{"│   " * (depth-1)}├── 📂 {dir_name} [{human_readable_size(dir_size)}]'
#             )

#         for i, name in enumerate(files[:4]):
#             file_path = os.path.join(root, name)
#             file_size = os.path.getsize(file_path)
#             total_files += 1
#             total_size += file_size
#             is_last = i == len(files[:4]) - 1
#             # if len(dirs) > 0:
#             #     is_last = False
#             print(
#                 f'{"│   " * (depth+1)}{"└" if is_last else "├"}── {name} [{human_readable_size(file_size)}]'
#             )

#         if len(files) > 3:
#             print(f'{"│   " * (depth+1)}     ({len(files) - 4} more files)')

#     # print(f"\nTotal number of files: {total_files}")
#     # print(f"Total size: {total_size / (1024 * 1024):.2f} MB")


def print_usage():
    print("Usage: python Main.py <dir>")
    print("dir: directory to read")


if __name__ == "__main__":
    # read arguments from command line
    args = sys.argv
    if len(args) > 1:
        directory = args[1]
    else:
        print_usage()
        exit(1)

    main(directory)
