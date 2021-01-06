import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths


    Requirements:

    Can use:
      os.path.isdir(path)
      os.path.isfile(path)
      os.listdir(directory)
      os.path.join(...

    Can't use:
      os.walk(...)
    """

    def find_files_recursive(suffix, path, found_files):

        items = os.listdir(path)

        for item in items:

            item_path = os.path.join(path, item)

            if os.path.isdir(os.path.join(item_path)):
                find_files_recursive(suffix, item_path, found_files)

            if os.path.isfile(item_path):
                if item_path.endswith(suffix):
                    found_files.append(item_path)

    found_files = []

    if os.path.isdir(path):
        find_files_recursive(suffix, path, found_files)

    return found_files


def test_find_files_in_path_when_files_exist():

    path = './problem2-data/testdir'
    found_files = find_files('.c', path)
    print("Pass: Found '{}' .c files. Should found '4'.".format(len(found_files)) if len(found_files) == 4 else "Fail")

    found_files.sort()
    for found_file in found_files:
        print(found_file)


def test_find_files_in_path_when_files_dont_exist():

    path = './problem2-data/testdir'
    found_files = find_files('.txt', path)
    print("Pass: Found '{}' .txt files. Should found '0'.".format(len(found_files)) if len(found_files) == 0 else "Fail")

    found_files.sort()
    for found_file in found_files:
        print(found_file)


def test_find_files_in_path_when_path_doesnt_exist():

    path = './problem2-data/testdir_not_exist'
    found_files = find_files('.c', path)
    print("Pass: Found '{}' files in path that doesn't exist. Should found '0'.".format(len(found_files)) if len(found_files) == 0 else "Fail")

    found_files.sort()
    for found_file in found_files:
        print(found_file)


if __name__ == "__main__":
    test_find_files_in_path_when_files_exist()
    test_find_files_in_path_when_files_dont_exist()
    test_find_files_in_path_when_path_doesnt_exist()
