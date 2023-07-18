import pytest

from app.missive import Missive
from app.db_controller import DatabaseController
from app.missive_gateway import MissiveGateway


missive_gateway = MissiveGateway(DatabaseController, "../missives_test.db")


@pytest.fixture(autouse=True)
def teardown():
    yield
    missive_gateway.delete_all_missives()


def test_write_to_and_read_from_db():
    written_missive = Missive(name="Rory", message="Hello there")
    missive_gateway.insert_missive(written_missive)

    record = missive_gateway.select_missive_by_name(written_missive.name)
    read_missive = Missive.init_from_record(record)

    assert written_missive.name == read_missive.name
    assert written_missive.message == read_missive.message
    assert written_missive.creation_time == read_missive.creation_time
    assert written_missive.location == read_missive.location
    assert written_missive.gathering == read_missive.gathering
