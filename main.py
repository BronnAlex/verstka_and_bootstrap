# import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8000


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        """Метод для обработки входящих гет запросов"""
        self.send_response(200)  # отправка кода ответа
        # Вызов self.send_header("Content-type", "text/html")
        # в контексте HTTP-сервера на Python используется для установки типа содержимого ответа.
        # В данном случае устанавливается значение «text/html», что означает, что весь текст,
        # выведенный сервером, будет интерпретирован клиентом как HTML-разметка.
        self.send_header("Content-type", "text/html")
        #  завершение заголовка ответа.
        self.end_headers()
        # читаем файл html, который возвращает разметку html
        r = read_html("src/contacts.html")
        print(r)
        # записываем строку переведенную в байты методом wfile.write для ...
        self.wfile.write(r.encode("utf-8"))

    def do_POST(self):
        """Метод для обработки входящих post запросов"""
        content_length = int(self.headers["Content-length"])
        body = self.rfile.read(content_length)
        print(body)
        self.send_response(200)
        self.end_headers()


def read_html(current_file):
    """Функция чтения шаблона html"""
    with open(current_file, "r", encoding="UTF-8") as file_html:
        result = file_html.read()
        # print(result)
    return result


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Сервер запущен http://%s%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Сервер остановлен")

    # file_name = 'src/contacts.html'
    # read_html(file_name)
