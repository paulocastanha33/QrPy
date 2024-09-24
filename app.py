from PyQt5 import QtWidgets, uic, QtGui
import pyqrcode
from PyQt5.QtCore import Qt, QTimer
import sys
from PIL import Image

class QRCodeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(QRCodeApp, self).__init__()
        uic.loadUi('interface.ui', self)

        # Remove as bordas da janela
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        # Define a transparência da janela (sem fundo sólido)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Define a opacidade da janela (ajuste conforme necessário)
        self.setWindowOpacity(0.9)

        # Conectar botão de gerar QR code à função
        self.generate_button.clicked.connect(self.create_qrcode)
        
        # Conectar botão de limpar à função
        self.clear_button.clicked.connect(self.clear_fields)
        
        # Conectar botão de sair à função
        self.exit_button.clicked.connect(self.exit_app)

    def create_qrcode(self):
        # Obter texto do campo de entrada
        text = self.text_input.text()

        if text:
            # Criar QR Code
            qr = pyqrcode.create(text)
            qr_file = 'myqr.png'
            qr.png(qr_file, scale=6)

            # Exibir mensagem de sucesso dentro do QLabel
            self.msg_label.setText("QR Code criado e salvo com sucesso!")

            # Carregar a imagem do QR code e exibir no QLabel
            self.show_qrcode(qr_file)
        else:
            # Exibir mensagem de erro dentro do QLabel
            self.msg_label.setText("Por favor, insira um texto válido.")

    def show_qrcode(self, qr_file):
        # Abrir a imagem do QR code gerada
        image = Image.open(qr_file)
        image = image.resize((200, 200))  # Redimensionar se necessário
        image.save('myqr_resized.png')  # Salvar a imagem redimensionada para exibição

        # Converter a imagem em QPixmap e definir no QLabel
        pixmap = QtGui.QPixmap('myqr_resized.png')
        self.qr_label.setPixmap(pixmap)  # 'qr_label' é o QLabel onde a imagem será exibida
        self.qr_label.setScaledContents(True)  # Ajustar para que a imagem se encaixe no QLabel

    def clear_fields(self):
        # Limpar todos os campos
        self.text_input.clear()  # Limpa o campo de texto
        self.qr_label.clear()  # Limpa o QLabel de imagem
        self.msg_label.clear()  # Limpa o QLabel de mensagens

    def exit_app(self):
        # Fechar a aplicação
        sys.exit()

# Inicializar o aplicativo
app = QtWidgets.QApplication(sys.argv)
window = QRCodeApp()
window.show()
sys.exit(app.exec_())