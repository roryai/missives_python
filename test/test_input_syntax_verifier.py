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
        assert verifier.check_name(name) is not True

def test_names_cannot_be_over_30_chars():
    name = "This is one char over 30 limit!"
    assert verifier.check_name(name) is False
