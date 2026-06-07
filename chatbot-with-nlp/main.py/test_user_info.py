from user_info import get_user_name

def test_get_user_name():
    assert get_user_name("Irina") == "Hello, Irina!"
    
def test_get_user_name_empty():
    assert get_user_name("") == "You need to introduce yourself!"