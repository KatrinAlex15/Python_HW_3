from string_utils import StringUtils

utils = StringUtils()


def test_capitilize():
    assert utils.capitilize("man") == "Man"
    assert utils.capitilize("mAn") == "Man"
    assert utils.capitilize("") == ""
    assert utils.capitilize("   ") == "   "


def test_trim():
    assert utils.trim("  man") == "man"
    assert utils.trim("") == ""
    assert utils.trim("   ") == ""


def test_to_list():
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list("1:2:3:4", ":") == ["1", "2", "3", "4"]
    assert utils.to_list("") == []
    assert utils.to_list("   ") == []
    assert utils.to_list(" ", " ") == [" ", " "]


def test_contains():
    assert utils.contains("man", "m") is True
    assert utils.contains("man", "g") is False
    assert utils.contains(" ", "m") is False


def test_delete_symbol():
    assert utils.delete_symbol("Man", "M") == "an"
    assert utils.delete_symbol("Tropical", "a") == "Tropicl"
    assert utils.delete_symbol("HomeWork", "Work") == "Home"
    assert utils.delete_symbol("", "a") == ""
    assert utils.delete_symbol("House", "w") == "House"


def test_start_with():
    assert utils.starts_with("HomeWork", "H") is True
    assert utils.starts_with("Homework", "O") is False


def test_end_with():
    assert utils.end_with("Tropical", "l") is True
    assert utils.end_with("Tropical", "q") is False


def test_is_empty():
    assert utils.test_is_empty("") is True
    assert utils.test_is_empty("   ") is True
    assert utils.test_is_empty("man") is False


def test_list_to_string():
    assert utils.list_to_string([1, 2, 3]) == "1, 2, 3"
    assert utils.list_to_string(["my", "house"]) == "my, house"
    assert utils.list_to_string(["My", "House"], "-") == "My-House"
    assert utils.list_to_string([]) == ""
    assert utils.list_to_string([""]) == ""

