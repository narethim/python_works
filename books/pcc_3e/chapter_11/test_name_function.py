from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formated_name = get_formatted_name('janis', 'joplin')
    assert formated_name == 'Janis Joplin'


def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    formated_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formated_name == 'Wolfgang Amadeus Mozart'