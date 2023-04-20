from app.missive import Missive
import datetime


def test_missive_output_format(capsys):
    missive = Missive("Rory", "Hello there", datetime.datetime(2023, 4, 20, 8, 45, 20, 56178))
    missive.display_missive()
    captured = capsys.readouterr()

    assert captured.out == "\nTime recorded: Thu, 20 Apr 2023 08:45:20" \
                           "\nRecording location: Milky Way, Sol, Earth, " \
                           "British Isles, England, London" \
                           "\nScribe: Rory" \
                           "\nMissive: Hello there\n"


