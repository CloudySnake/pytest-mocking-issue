from src.connection import MyConnection

"""
This connection is being instantiated outside of the handler so that it persists for
the life of the Lambda instance not per invocation
"""
connection = MyConnection()
client = connection.conn_client()


def handler(input):
    write_client(client, input)


def write_client(client, input):
    client["Writing"] = input


if __name__ == "__main__":
    handler("in")
