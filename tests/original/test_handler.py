import pytest


@pytest.fixture()
def mocked_env(mocker):
    m_connection = mocker.patch("src.connection.MyConnection")
    m_write_client = mocker.patch("src.handler.write_client")

    return m_connection, m_write_client


def test_handler_one(mocked_env):
    m_connection, m_write_client = mocked_env
    print(m_connection)
    from src.handler import handler

    handler("Input One")

    m_write_client.assert_called_with(m_connection().conn_client(), "Input One")


def test_handler_two(mocked_env):
    m_connection, m_write_client = mocked_env
    print(m_connection)
    from src.handler import handler

    handler("Input Two")

    m_write_client.assert_called_with(m_connection().conn_client(), "Input Two")
