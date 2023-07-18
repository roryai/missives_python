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

    assert written_missive == read_missive


def test_selects_random_missive():
    missive = Missive(name="Rory", message="Hello there")
    missive_gateway.insert_missive(missive)
    selected_record = missive_gateway.select_one_random_missive()
    selected_missive = Missive.init_from_record(selected_record)

    assert selected_missive == missive


def test_returns_none_if_no_record_found():
    selected_record = missive_gateway.select_one_random_missive()

    assert selected_record is None
