
# proxy -> filter traffic, rate limiting
# client -> proxy/middleware  -> server
# bot -> proxy if banned <-, norm user  -> server


class Server:
    def fetch_data(self):
        print("fetching users from db")
    

class RateLimitProxy:
    def __init__(self):
        self.server = Server()
        self.calls = 0
    
    def fetch_data(self):
        if self.calls < 5:
            self.server.fetch_data()
            self.calls += 1
        else:
            print("Too many requests today")


proxy = RateLimitProxy()
for _ in range(10):
    proxy.fetch_data()
