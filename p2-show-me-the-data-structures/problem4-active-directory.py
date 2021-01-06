class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    for child_group in group.get_groups():

        for user_in_group in child_group.get_users():
            if user == user_in_group:
                return True

        if child_group:
            if is_user_in_group(user, child_group):
                return True

    return False


def test_user_is_in_group():

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    empty = Group("empty")
    parent.add_group(empty)

    print("Pass: User '{}' is in group '{}'.".format(sub_child_user, parent.get_name())
          if is_user_in_group(sub_child_user, parent) is True else "Fail")


def test_user_as_empty_string():

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    empty = Group("empty")
    parent.add_group(empty)

    user = ""

    print("Pass: User '{}' is not in group '{}'.".format(user, parent.get_name())
          if is_user_in_group(user, parent) is False else "Fail")


def test_user_is_not_in_group():

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    empty = Group("empty")
    parent.add_group(empty)

    print("Pass: User '{}' is not in group '{}'.".format(sub_child_user, empty.get_name())
          if is_user_in_group(sub_child_user, empty) is False else "Fail")


if __name__ == "__main__":
    test_user_is_in_group()
    test_user_is_not_in_group()
    test_user_as_empty_string()
