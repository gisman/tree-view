import os
import sys
import argparse

"""
linux tree utility의 개선.

bigdata 분석 및 문서화에 활용하기 좋은 기능을 추가.

## 요건
    * tree 구조 출력
    * size: human readable
    * file count
    * file list limit
    * 📂 이모지

"""


DIRS_ONLY = False
LEVEL = -1
MAX_FILES = 4


def human_readable_size(size):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.0f}{unit}"
        size /= 1024


def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def has_sibling(root, dirs_only):
    parent_dir = os.path.dirname(root)
    if not parent_dir:
        return False

    sibling_dirs = [
        d for d in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, d))
    ]
    sibling_dirs.sort()

    if not dirs_only:
        sibling_dirs += [
            d
            for d in os.listdir(parent_dir)
            if os.path.isfile(os.path.join(parent_dir, d))
        ]

    if sibling_dirs[-1] == os.path.basename(root):
        return False

    sibling_dirs.remove(os.path.basename(root))

    return len(sibling_dirs) > 0


def print_dir(
    directory,
    parent_has_sibling=False,
    depth=0,
    tree_lines=[""],
):
    if LEVEL > -1 and depth > LEVEL:
        return

    for root, dirs, files in os.walk(directory):
        dir_name = os.path.basename(os.path.normpath(root))
        dir_size = get_directory_size(root)
        dir_has_sibling = False
        if depth > 0:
            if parent_has_sibling:
                tree_lines[depth - 1] = "│   "
            else:
                if depth > 1:
                    tree_lines[depth - 1] = "    "

            dir_has_sibling = has_sibling(directory, DIRS_ONLY)

        file_count_str = f"    {len(files):,}개의 파일" if len(files) > 0 else ""

        print(
            f'{"".join(tree_lines)}📂 {dir_name} [{human_readable_size(dir_size)}{file_count_str}]'
        )
        dirs.sort()

        # print directories recursively
        for i, dir in enumerate(dirs):
            tl = tree_lines.copy()
            if i == len(dirs) - 1 and (DIRS_ONLY or len(files) == 0):  # last element
                tl.append("└──")
            else:
                tl.append("├──")

            print_dir(
                f"{directory}/{dir}",
                parent_has_sibling=dir_has_sibling,
                depth=depth + 1,
                tree_lines=tl,
            )

        if DIRS_ONLY:
            return

        print_files(root, files, tree_lines, dir_has_sibling)
        return


def print_files(root, files, tree_lines, parent_has_sibling):
    files.sort()
    PARENT_LINE = "│" if parent_has_sibling else ""
    path_line = f'{"".join(tree_lines[:-1])}{PARENT_LINE}'
    if len(tree_lines) > 1:
        path_line += "   "

    for i, name in enumerate(files[:MAX_FILES]):
        file_path = os.path.join(root, name)
        file_size = os.path.getsize(file_path)

        is_last = i == len(files[:MAX_FILES]) - 1

        print(
            path_line,
            f'{"└" if is_last else "├"}── {name} [{human_readable_size(file_size)}]',
            sep="",
        )

    #  (7,477 more files)
    # if len(files) > MAX_FILES:
    #     print(
    #         path_line,
    #         f"   ({len(files) - MAX_FILES:,} more files)",
    #         sep="",
    #     )


def main(directory):
    print_dir(directory)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="List directory contents.",
        epilog="github: https://github.com/gisman/tree-view",
    )

    # 디렉토리만 출력하는 옵션
    parser.add_argument("directory", help="Directory to read")
    parser.add_argument(
        "-d", action="store_true", help="List directories only", default=False
    )

    # 출력 Depth를 제한하는 옵션. 기본값은 -1
    parser.add_argument(
        "-L",
        "--level",
        type=int,
        help="Descend only level directories deep",
        default=-1,
    )

    # 디렉토리 내의 파일을 최대 N개 까지만 출력하는 옵션. 기본값은 4
    parser.add_argument(
        "-n",
        "--max-files",
        type=int,
        help="Print only N files in each directory",
        default=4,
    )

    args = parser.parse_args()

    DIRS_ONLY = args.d
    LEVEL = args.level
    if args.max_files < 0:
        MAX_FILES = 1000000  # 100만개로 제한
    else:
        MAX_FILES = args.max_files

    # check if the directory exists
    if not os.path.isdir(args.directory):
        print("The directory does not exists.")
        sys.exit

    main(args.directory)
