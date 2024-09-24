import time
import os
import psutil  # Para coletar informações do sistema
import platform  # Para obter informações sobre o sistema operacional
from http.server import SimpleHTTPRequestHandler, HTTPServer
from plyer import notification  # Para notificações

# Função para coletar informações do dispositivo
def get_info():
    storage = psutil.disk_usage('/').percent  # Porcentagem de uso do disco
    ram = psutil.virtual_memory().percent  # Porcentagem de uso da RAM
    cpu = psutil.cpu_percent(interval=1)  # Porcentagem de uso da CPU
    model = f"{platform.system()} {platform.release()}"  # Nome do modelo
    return storage, ram, cpu, model

# Função para enviar notificações
def send_notifications(titulo, mensagem):
    notification.notify(
        title=titulo,
        message=mensagem,
        app_name="Informações do Dispositivo",
        timeout=10
    )

# Handler HTTP
class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        storage, ram, cpu, model = get_info()  # Chame a função correta
        html_content = f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Informações do Dispositivo</title>
        </head>
        <body>
            <h1>Informações do Dispositivo</h1>
            <p>Armazenamento: {storage}% usado</p>
            <p>RAM: {ram}% usada</p>
            <p>CPU: {cpu}% em uso</p>
            <p>Modelo: {model}</p>
        </body>
        </html>"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode())

# Inicializando o servidor
def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8080)  # O servidor escuta na porta 8080
    httpd = server_class(server_address, handler_class)
    print('Iniciando o servidor...')
    httpd.serve_forever()

if __name__ == "__main__":
    # Inicie o servidor em uma thread separada
    import threading
    server_thread = threading.Thread(target=run)
    server_thread.daemon = True
    server_thread.start()

    while True:
        storage, ram, cpu, model = get_info()  # Coleta as informações
        mensagem = f"Armazenamento: {storage}% usado\nRAM: {ram}% usada\nCPU: {cpu}% em uso\nModelo: {model}"
        send_notifications("Informações do Dispositivo", mensagem)
        time.sleep(60)  # Aguarda 1 minuto antes da próxima coleta
