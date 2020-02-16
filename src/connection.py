class MyConnection:
    def __init__(self):
        raise NotImplementedError

    def conn_client(self):
        return {"Connection": "Active"}

    def push(self, input):
        pass