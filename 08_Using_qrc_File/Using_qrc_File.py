from ui.icons_rc  import *
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QMainWindow, QToolBar, QMenu, QApplication, QFileDialog
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtGui import QIcon, QKeySequence, QPixmap, QAction



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.playlist = []
        self.current_index = 0  # 用于跟踪当前播放的索引

        toolBar = QToolBar()
        self.addToolBar(toolBar)

        fileMenu = self.menuBar().addMenu("&File")
        openAction = QAction(QIcon.fromTheme("document-open"),
                             "&Open...", self, shortcut=QKeySequence.Open,
                             triggered=self.open)
        fileMenu.addAction(openAction)

        exitAction = QAction(QIcon.fromTheme("application-exit"), "E&xit",
                             self, shortcut="Ctrl+Q", triggered=self.close)
        fileMenu.addAction(exitAction)

        playMenu = self.menuBar().addMenu("&Play")

        playIcon = QIcon(QPixmap(":/icons/play.png"))
        self.playAction = toolBar.addAction(playIcon, "Play")
        self.playAction.triggered.connect(self.play)
        playMenu.addAction(self.playAction)

        previousIcon = QIcon(QPixmap(":/icons/previous.png"))
        self.previousAction = toolBar.addAction(previousIcon, "Previous")
        self.previousAction.triggered.connect(self.previous)
        playMenu.addAction(self.previousAction)

        pauseIcon = QIcon(QPixmap(":/icons/pause.png"))
        self.pauseAction = toolBar.addAction(pauseIcon, "Pause")
        self.pauseAction.triggered.connect(self.player.pause)
        playMenu.addAction(self.pauseAction)

        nextIcon = QIcon(QPixmap(":/icons/forward.png"))
        self.nextAction = toolBar.addAction(nextIcon, "Next")
        self.nextAction.triggered.connect(self.next)
        playMenu.addAction(self.nextAction)

    def open(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self, "Open Media Files", "", "Media Files (*.mp3 *.ogg *.wav);;All Files (*)")

        if file_paths:
            self.playlist = file_paths
            self.current_index = 0
            self.play()

    def play(self):
        if self.playlist:
            self.player.setAudioOutput(self.audioOutput)
            media_content = QUrl.fromLocalFile(self.playlist[self.current_index])
            self.player.setSource(media_content)
            self.audioOutput.setVolume(50)
            self.player.play()

    def previous(self):
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.play()

    def next(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play()


if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
