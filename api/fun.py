from http.server import BaseHTTPRequestHandler
from urllib import parse
import random

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        query = dict(query_string_list)

        name = query.get("name")
        greetings = ['Hello ', "What's up ", 'Thanks for stopping by ', "Welcome to the internet "]
        punc = ['?', '!', '!!!', '.', '...']

        if name:
            message = f"{random.choice(greetings)}{name}{random.choice(punc)}"
        else:
            message = "Hi stranger. Throw your name in the query, if you're feeling frisky"


        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        self.wfile.write(message.encode())