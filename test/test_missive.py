from app.missive import Missive


def test_message():
    missive = Missive("hello")
    assert missive.print_missive() == "Your missive is: hello"
