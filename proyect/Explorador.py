import sys
from os import getcwd, listdir, stat
from os.path import dirname, isdir, isfile, join
from time import localtime, strftime
try:
    # Windows.
    from os import startfile
except ImportError:
    # Otras plataformas.
    from webbrowser import open as startfile
from hurry.filesize import size
from PyQt4.QtCore import QStringList
from PyQt4.QtGui import (QApplication, QHBoxLayout, QIcon, QMainWindow,
                         QLineEdit, QPushButton, QTreeWidget,
                         QTreeWidgetItem, QVBoxLayout, QWidget)
class Window(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Explorador de archivos y carpetas")
        
        self.back_history = []
        self.forward_history = []
        
        self.back_button = QPushButton(self)
        self.back_button.setIcon(QIcon("images/back.png"))
        self.back_button.clicked.connect(self.back_clicked)
        self.back_button.setEnabled(False)
        
        self.forward_button = QPushButton(self)
        self.forward_button.setIcon(QIcon("images/forward.png"))
        self.forward_button.clicked.connect(self.forward_clicked)
        self.forward_button.setEnabled(False)
        
        self.up_button = QPushButton(self)
        self.up_button.setIcon(QIcon("images/up.png"))
        self.up_button.clicked.connect(self.up_button_clicked)
        
        self.address_edit = QLineEdit(self)
        
        self.refresh_button = QPushButton(self)
        self.refresh_button.setIcon(QIcon("images/update.png"))
        self.refresh_button.clicked.connect(self.refresh_button_clicked)
        
        self.toplayout = QHBoxLayout()
        self.toplayout.addWidget(self.back_button)
        self.toplayout.addWidget(self.forward_button)
        self.toplayout.addWidget(self.up_button)
        self.toplayout.addWidget(self.address_edit)
        self.toplayout.addWidget(self.refresh_button)
        
        self.main_tree = QTreeWidget(self)
        self.main_tree.setRootIsDecorated(False)
        self.main_tree.setHeaderLabels(
            ("Nombre", u"Fecha de modificación", u"Tamaño"))
        self.main_tree.itemDoubleClicked.connect(self.item_double_clicked)
        
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.toplayout)
        self.layout.addWidget(self.main_tree)
        
        self.central_widget = QWidget(self)
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        
        self.resize(800, 600)
        # Iniciar en el directorio actual.
        self.load_path(getcwd())
    
    def back_clicked(self, checked):
        if self.back_history and len(self.back_history) > 1:
            # Obtener el último elemento.
            path = self.back_history[-2]
            self.forward_history.append(self.back_history[-1])
            # Remover el directorio actual.
            del self.back_history[-1]
            self.load_path(path, False)
    
    def forward_clicked(self, checked):
        if self.forward_history:
            path = self.forward_history[-1]
            self.back_history.append(path)
            del self.forward_history[-1]
            self.load_path(path, False)
    
    def item_double_clicked(self, item, column):
        filepath = join(self.current_path, unicode(item.text(0)))
        if isdir(filepath):
            self.load_path(filepath)
        else:
            # Iniciar archivo con el programa predeterminado.
            startfile(filepath)
    
    def up_button_clicked(self, checked):
        parent = dirname(self.current_path)
        if parent != self.current_path:
            self.load_path(parent)
    
    def load_path(self, path, use_history=True):
        # Obtener archivos y carpetas.
        items = listdir(unicode(path))
        # Eliminar el contenido anterior.
        self.main_tree.clear()
        
        for i in items:
            # Omitir archivos ocultos.
            if i.startswith("."):
                continue
            filepath = join(path, i)
            # Obtener informacion del archivo.
            stats = stat(filepath)
            # Crear el control ítem.
            item_widget = QTreeWidgetItem(
                (i, strftime("%c", localtime(stats.st_mtime)).decode("utf-8"),
                 size(stats.st_size) if isfile(filepath) else "")
            )
            # Establecer el ícono correspondiente.
            item_widget.setIcon(0, QIcon("images/%s.png" %
                ("file" if isfile(filepath) else "folder")))
            # Añadir elemento.
            self.main_tree.addTopLevelItem(item_widget)
        
        # Ajustar el tamaño de las columnas.
        for i in range(3):
            self.main_tree.resizeColumnToContents(i)
        
        self.current_path = path
        self.address_edit.setText(self.current_path)
        
        # Añadir al historial.
        if use_history:
            self.back_history.append(self.current_path)
        
        # Habilitar / dehabilitar botones del historial.
        if self.back_history and len(self.back_history) > 1:
            if not self.back_button.isEnabled():
                self.back_button.setEnabled(True)
        else:
            if self.back_button.isEnabled():
                self.forward_history = []
                self.back_button.setEnabled(False)
        
        if self.forward_history:
            if not self.forward_button.isEnabled():
                self.forward_button.setEnabled(True)
        else:
            if self.forward_button.isEnabled():
                self.forward_button.setEnabled(False)
    
    def refresh_button_clicked(self, checked):
        self.load_path(self.current_path)
if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())