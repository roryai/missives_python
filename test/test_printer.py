from datetime import datetime


from app.missive import Missive
from app.printer import Printer
import app.styles as styles

printer = Printer()


def test_prints_message_with_styling(capsys):
    messages = [{'text': 'test message', 'styling': styles.DEFAULT}]
    expected = '\ntest message\n'
    printer.process(messages)

    captured = capsys.readouterr()

    assert captured.out == expected


def test_prints_missive(capsys):
    default_missive = Missive(name="Rory", message="Hello there",
                              creation_time=str(datetime(2023, 4, 20, 8, 45, 20)))
    default_missive_output = "\n\nTime recorded:      Thu, 20 Apr 2023 08:45" \
                             "\nRecording location: Milky Way, Sol, Earth, British Isles, England, Devon" \
                             "\nGathering:          Burning Nest '23" \
                             "\n\nScribe:  Rory" \
                             "\nMissive: Hello there\n"

    default_missive.display_missive()
    captured = capsys.readouterr()

    assert captured.out == default_missive_output
