import sys
import random
import string
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QCheckBox

# Definição da classe principal da aplicação
class GeradorSenhas(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuração da janela principal
        self.setWindowTitle("Gerador de Senhas Seguras")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Elementos da interface gráfica

        # Rótulo e campo de entrada para o comprimento da senha
        self.comprimento_label = QLabel("Comprimento da Senha:")
        self.comprimento_input = QLineEdit(self)
        self.comprimento_input.setPlaceholderText("Digite o comprimento da senha")

        # Caixas de seleção para incluir tipos de caracteres
        self.letras_checkbox = QCheckBox("Incluir Letras (A-Z, a-z)")
        self.numeros_checkbox = QCheckBox("Incluir Números (0-9)")
        self.caracteres_especiais_checkbox = QCheckBox("Incluir Caracteres Especiais (!@#$%^&*)")

        # Botão para gerar senha
        self.gerar_button = QPushButton("Gerar Senha", self)
        self.gerar_button.clicked.connect(self.gerar_senha)

        # Rótulo e campo de saída para a senha gerada
        self.senha_label = QLabel("Senha Gerada:")
        self.senha_output = QLineEdit(self)
        self.senha_output.setReadOnly(True)

        # Adicionar elementos à interface gráfica
        layout.addWidget(self.comprimento_label)
        layout.addWidget(self.comprimento_input)
        layout.addWidget(self.letras_checkbox)
        layout.addWidget(self.numeros_checkbox)
        layout.addWidget(self.caracteres_especiais_checkbox)
        layout.addWidget(self.gerar_button)
        layout.addWidget(self.senha_label)
        layout.addWidget(self.senha_output)

    # Método para gerar a senha com base nos critérios selecionados pelo usuário
    def gerar_senha(self):
        # Obter o comprimento da senha a partir do campo de entrada
        comprimento = int(self.comprimento_input.text()) if self.comprimento_input.text().isdigit() else 12

        # Verificar quais tipos de caracteres devem ser incluídos com base nas caixas de seleção
        incluir_letras = self.letras_checkbox.isChecked()
        incluir_numeros = self.numeros_checkbox.isChecked()
        incluir_caracteres_especiais = self.caracteres_especiais_checkbox.isChecked()

        # Definir os caracteres possíveis com base nas escolhas do usuário
        caracteres = ""
        if incluir_letras:
            caracteres += string.ascii_letters
        if incluir_numeros:
            caracteres += string.digits
        if incluir_caracteres_especiais:
            caracteres += "!@#$%^&*()_+=-[]{}|;:,.<>?"

        # Verificar se pelo menos um tipo de caractere foi selecionado
        if not caracteres:
            self.senha_output.setText("Selecione pelo menos um tipo de caractere.")
            return

        # Gerar a senha aleatória com base nos critérios e exibi-la na interface
        senha = "".join(random.choice(caracteres) for _ in range(comprimento))
        self.senha_output.setText(senha)

# Ponto de entrada da aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gerador_senhas = GeradorSenhas()
    gerador_senhas.show()
    sys.exit(app.exec())
