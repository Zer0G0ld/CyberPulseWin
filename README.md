# CyberPulse

Este projeto é uma aplicação Python que coleta informações sobre o sistema (armazenamento, RAM, CPU e modelo) e as exibe em uma página HTML, além de enviar notificações a cada minuto.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas:
  - psutil
  - plyer

## Instalação

### 1. Clone o repositório
Clone este repositório em sua máquina:

```bash
git clone https://github.com/Zer0G0ld/CyberPulseWin
cd CyberPulseWin
````

### 2. Crie um ambiente virtual (opcional, mas recomendado)
Crie e ative um ambiente virtual para gerenciar as dependências do projeto:

```bash
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências
Instale as bibliotecas necessárias:

```bash
pip install psutil plyer
```

### Execução
Para executar a aplicação, use o seguinte comando:

```bash
python main.py
```

A aplicação iniciará um servidor HTTP na porta 8080 e enviará notificações a cada minuto com as informações coletadas do sistema.

### Acessando a página
Você pode acessar a página HTML com as informações do dispositivo abrindo o seguinte endereço em seu navegador:

```arduino
http://localhost:8080
```

### Considerações
As notificações dependem do suporte da biblioteca `plyer` para o seu sistema operacional. Certifique-se de que você tenha as configurações corretas para recebê-las.
Se você estiver usando Windows, o `os.uname()` não está disponível, então usamos `platform.system()` e `platform.release()` para obter informações sobre o sistema.

### Contribuições
Sinta-se à vontade para contribuir com este projeto, criando um fork e enviando pull requests com melhorias ou correções.

### Licença
Este projeto está licenciado sob a GNU General Public License v3.0 - veja o arquivo [LICENSE](https://github.com/Zer0G0ld/CyberPulseWin/blob/main/LICENSE) para mais detalhes.
