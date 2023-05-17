from app.input_syntax_verifier import InputSyntaxVerifier

verifier = InputSyntaxVerifier()


def test_check_name_true():
    names = [
        "AB",
        "Ab 2",
        "AB $3.50",
        "AB $3.50  ",
        "This is exactly 30 chars, see!",
    ]
    for name in names:
        assert verifier.check_name(name) is True


def test_check_name_fails():
    names = [
        "A B",
        "2AB",
        "!AB",
        " Ab",
        "This is one char over 30 limit!",
    ]
    for name in names:
        assert verifier.check_name(name) is not True
