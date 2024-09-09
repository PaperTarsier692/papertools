import http.server
from .File import File
from typing import Callable, Any, Union


class WebServify:
    '''Simple class for providing a HTTP server'''

    def __init__(self) -> None:
        global get, post, file
        get = self._Get()
        post = self._Post()
        file = self._File()
        self.get = get
        self.post = post
        self.file = file

    def start(self, port: int = 8080, ip: str = '127.0.0.1') -> None:
        '''Starts the Server'''
        http.server.HTTPServer((ip, port), self._Handler).serve_forever()

    class _Get:
        def __init__(self) -> None:
            self.gets: dict[str, Callable] = {}

        def serve(self, path: str) -> Any:
            '''Decorator for turning a function into an GET API endpoint'''
            def decorator(func: Callable) -> Callable:
                self.gets[path] = func
                return func
            return decorator

    class _Post:
        def __init__(self) -> None:
            self.posts: dict[str, Callable] = {}

        def serve(self, path: str) -> Any:
            '''Decorator for turning a function into an POST API endpoint'''
            def decorator(func: Callable) -> Callable:
                self.posts[path] = func
                return func
            return decorator

    class _File:
        def __init__(self) -> None:
            self.files: dict[str, Union[str, File]] = {}

        def file(self, filepath: str, webpath: Union[str, None] = None, load_into_ram: bool = True) -> None:
            '''Hosts the given file at the given webpath (default is filename). load_into_ram specifies wether the file should be reloaded everytime a requests gets made, or be loaded once into the RAM.'''
            if webpath == None:
                webpath = filepath
            if load_into_ram:
                self.files[webpath] = File(filepath).read()
            else:
                self.files[webpath] = File(filepath)

    class _Handler(http.server.BaseHTTPRequestHandler):
        '''The handler for requests'''

        def do_GET(self) -> None:
            if self.path.split('?')[0] not in get.gets:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                return

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            args: dict[str, str] = {}
            if '?' in self.path:
                for arg in self.path.split('?')[1].split('&'):
                    args[arg.split('=')[0]] = arg.split('=')[1]
            out: function = get.gets[self.path.split('?')[0]]
            result: Any = out(**args)
            self.wfile.write(result.encode())

        def do_POST(self) -> None:
            if self.path.split('?')[0] not in post.posts:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                return

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            args: dict[str, str] = {}
            if '?' in self.path:
                for arg in self.path.split('?')[1].split('&'):
                    args[arg.split('=')[0]] = arg.split('=')[1]
            out: function = post.posts[self.path.split('?')[0]]
            result: Any = out(**args)
            self.wfile.write(result.encode())
