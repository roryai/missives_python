from app.input_syntax_verifier import InputSyntaxVerifier

verifier = InputSyntaxVerifier()


def test_name_must_begin_with_two_letters():
    names = [
        "AB",
        "Ab 2",
        "AB $3.50",
        "AB $3.50  "
    ]
    for name in names:
        assert verifier.check_name(name) is True


def test_name_can_be_up_to_30_chars_long():
    names = [
        "This is exactly 30 chars, see!",
    ]
    for name in names:
        assert verifier.check_name(name) is True


def test_names_cannot_have_spaces_numbers_or_special_chars_in_first_two_chars():
    names = [
        "A B",
        "2AB",
        "!AB",
        " Ab"
    ]
    for name in names:
        assert verifier.check_name(name) is False


def test_names_cannot_be_over_30_chars():
    name = "This is one char over 30 limit!"
    assert verifier.check_name(name) is False


def test_message_is_verified_when_it_contains_at_least_10_chars():
    messages = [
        "1234567890",
        "123 4567890",
        "abcdefghij",
        "abcde   fghij",
        "abcde12345",
        "!@£$%^&*()",
        "abc123&*()",
        "abc1   23&*()",
    ]
    for message in messages:
        assert verifier.check_message_min_length(message) is True


def test_message_is_not_verified_when_it_contains_less_than_10_chars():
    messages = [
        "123456789",
        "123456 789",
        "abcdefghi",
        "abcdefg hi",
        "          ",
        "    123456789      ",
    ]
    for message in messages:
        assert verifier.check_message_min_length(message) is False


def test_message_is_verified_if_exactly_1000_chars_in_length():
    message_of_1000_chars = """
    This is a time machine that allows you to send messages to people in the future.
    
    It was discovered aboard the wreck of the Mary Celeste, in the captain's cabin.
    
    The machine was operational and running at the time of discovery.
    
    It is made of exotic materials, some of which were previously unknown to science.
    
    Messages can be recorded by many means, including using a pen or stylus.
    A keyboard has been deemed to be the most desirable interface for 21st century 
    users due to its familiarity.
    
    The machine does not record the electrical output from the keyboard. Instead, it
    records the intent of the user as expressed through the choices they make about
    which keys to press. When a robot presses the keys nothing happens.
    
    The mechanism by which this machine operates is unknown, as is the origin or 
    identity of the creators.
    
    We do not know who else may be reading your messages.
    
    just a few more chars123"""
    assert verifier.check_message_max_length(message_of_1000_chars) is True


def test_message_is_not_verified_if_over_1000_chars_in_length():
    message_of_1001_chars = """
    This is a time machine that allows you to send messages to people in the future.
    
    It was discovered aboard the wreck of the Mary Celeste, in the captain's cabin.
    
    The machine was operational and running at the time of discovery.
    
    It is made of exotic materials, some of which were previously unknown to science.
    
    Messages can be recorded by many means, including using a pen or stylus.
    A keyboard has been deemed to be the most desirable interface for 21st century 
    users due to its familiarity.
    
    The machine does not record the electrical output from the keyboard. Instead, it
    records the intent of the user as expressed through the choices they make about
    which keys to press. When a robot presses the keys nothing happens.
    
    The mechanism by which this machine operates is unknown, as is the origin or 
    identity of the creators.
    
    We do not know who else may be reading your messages.
    
    just a few more chars1234"""

    assert verifier.check_message_max_length(message_of_1001_chars) is False

