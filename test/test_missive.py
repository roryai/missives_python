import pytest
from app.missive import Missive
from app.db_controller import DatabaseController
from app.missive_gateway import MissiveGateway
from datetime import datetime


missive_gateway = MissiveGateway(DatabaseController, "../missives_test.db")
default_missive = Missive(name="Rory", message="Hello there",
                          creation_time=str(datetime(2023, 4, 20, 8, 45, 20)))
default_missive_output = "\n\nTime recorded:      Thu, 20 Apr 2023 08:45" \
                 "\nRecording location: Milky Way, Sol, Earth, British Isles, England, Devon" \
                 "\nGathering:          Burning Nest '23" \
                 "\n\nScribe:  Rory" \
                 "\nMissive: Hello there\n"


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    missive_gateway.delete_all_missives()
    yield


def test_missive_output_format(capsys):
    default_missive.display_missive()
    captured = capsys.readouterr()

    assert captured.out == default_missive_output


def test_read_and_write_to_database(capsys):
    missive_gateway.insert_missive(default_missive)

    # select missive and map db data to Missive
    record = missive_gateway.select_missive_by_name(default_missive.name)
    missive = Missive.init_from_record(record)
    missive.display_missive()
    captured = capsys.readouterr()

    assert captured.out == default_missive_output


def test_attributes_successfully_read_from_record():
    written_missive = Missive(name="Rory", message="Hello there")
    missive_gateway.insert_missive(written_missive)

    record = missive_gateway.select_missive_by_name(default_missive.name)
    read_missive = Missive.init_from_record(record)

    assert written_missive.name == read_missive.name
    assert written_missive.message == read_missive.message
    assert written_missive.creation_time == read_missive.creation_time
    assert written_missive.location == read_missive.location
    assert written_missive.gathering == read_missive.gathering
