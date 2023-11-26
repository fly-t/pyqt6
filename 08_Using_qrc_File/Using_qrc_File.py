from ui.icons_rc  import *
from PySide6.QtCore import Qt, QUrl, Slot
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QMainWindow, QToolBar, QApplication, QFileDialog, QSlider
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
        playIcon = QIcon(QPixmap(":/icons/play.png"))

        fileMenu = self.menuBar().addMenu("&File")  # why &File not File， 有&可以快捷键alt+首字母打开
        openAction = QAction(QIcon.fromTheme("document-open", playIcon), # 如果没有找到系统图标， 使用设置的图标
                             "&Open...", self, shortcut=QKeySequence("Ctrl+1"),
                             triggered=self.open)  # triggered=self.open触发后调用的slot函数
        fileMenu.addAction(openAction)

        exitAction = QAction(QIcon.fromTheme("application-exit"), "E&xit",
                             self, shortcut="Ctrl+Q", triggered=self.close)
        fileMenu.addAction(exitAction)

        playMenu = self.menuBar().addMenu("&Play")

        playIcon = QIcon(QPixmap(":/icons/play.png"))
        self.playAction = toolBar.addAction(playIcon, "Play")
        self.playAction.triggered.connect(self.play)
        playMenu.addAction(self.playAction)
        
        # 使用 : 作为资源路径的前缀是 Qt 框架的一种规范，使得在处理资源时更加清晰和一致
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

        # self._volume_slider = QSlider()
        # self._volume_slider.setOrientation(Qt.Horizontal)
        # self._volume_slider.setMinimum(0)
        # self._volume_slider.setMaximum(100)
        # available_width = self.screen().availableGeometry().width()
        # self._volume_slider.setFixedWidth(available_width / 10)
        # self._volume_slider.setValue(self.audioOutput.volume())
        # self._volume_slider.setTickInterval(10)
        # self._volume_slider.setTickPosition(QSlider.TicksBelow)
        # self._volume_slider.setToolTip("Volume")
        # # self._volume_slider.valueChanged.connect(self._audio_output.setVolume)
        # toolBar.addWidget(self._volume_slider)
    
    @Slot()
    def open(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self, "Open Media Files", "", "Media Files (*.mp3 *.ogg *.wav);;All Files (*)")

        if file_paths:
            self.playlist = file_paths
            self.current_index = 0
            self.play()
    
    @Slot()
    def play(self):
        if self.playlist:
            self.player.setAudioOutput(self.audioOutput)
            media_content = QUrl.fromLocalFile(self.playlist[self.current_index])
            self.player.setSource(media_content)
            self.audioOutput.setVolume(50)
            self.player.play()

    @Slot()
    def previous(self):
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.play()

    @Slot()
    def next(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play()


if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
