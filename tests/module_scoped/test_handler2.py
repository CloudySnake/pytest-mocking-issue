import pytest
from unittest import mock


@pytest.fixture()
def mocked_env(mocker):
    m_write_client = mocker.patch("src.handler.write_client")

    return m_write_client


@pytest.fixture(scope="module")
def mocked_conn():
    with mock.patch("src.connection.MyConnection") as m_connection:
        yield m_connection


def test_handler_one(mocked_conn, mocked_env):
    m_connection = mocked_conn
    m_write_client = mocked_env

    print(m_connection().conn_client())

    from src.handler import handler

    handler("Input One")

    m_write_client.assert_called_with(m_connection().conn_client(), "Input One")


def test_handler_two(mocked_conn, mocked_env):
    m_connection = mocked_conn
    m_write_client = mocked_env

    print(m_connection().conn_client())
    
    from src.handler import handler

    handler("Input Two")

    m_write_client.assert_called_with(m_connection().conn_client(), "Input Two")
