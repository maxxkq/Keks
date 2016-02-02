from socket import socket as sock


class Start:
    """Class for Response page"""

    def __init__(self, name=None, listen_count=0):
        self.socket = sock()
        self.host = '0.0.0.0'
        self.port = 5000
        self.filename = name
        self.session = []
        self.method = None
        self.listen_count = listen_count
        self.url = ''
        self.dict_of_urls = {}
        self.connection = None

    def start_framework(self, request):
        self.start_session(request)
        try:
            if self.url.startswith('/') and '.ico' not in self.url:
                send_ = self.dict_of_urls[self.url]()
                self.render(send_)
            else:
                raise NameError
        except NameError:
            print(self.url + ' Error')
        except KeyError:
            print("This url | " + self.url + " | don't register")

    def start_session(self, request):
        self.session = request.recv(1024).decode('utf-8').split()
        self.method = self.session[0]
        self.url = self.session[1]
        print('URL : ' + self.url)

    def add_url_rule(self, url, func):
        self.dict_of_urls[url] = func

    def run(self, host=None, port=None):
        if host:
            self.host = host
        if port:
            self.port = port

        while True:
            try:
                self.socket.bind((self.host, self.port))
                print(self.port)
                break
            except OSError:
                self.port += 1

        self.socket.listen(self.listen_count)

        while True:
            connection, address = self.socket.accept()
            self.connection = connection
            self.start_framework(connection)

    def render(self, mess):
        print(mess)
        return self.connection.sendall(mess.encode('utf-8'))

    def route(self, rule):
        def decorator(f):
            self.add_url_rule(rule, f)
            return f
        return decorator
