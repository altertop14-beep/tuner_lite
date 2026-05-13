
import sys
import numpy as np
from PyQt6.QtWidgets import *
import pyqtgraph as pg

def engine_model(boost, fuel):
    air = boost * 0.85
    return min(fuel * 1.6, air * 2.0)

def detect_maps(data):
    maps = []
    for i in range(0, len(data)-64, 16):
        block = data[i:i+64]
        if np.var(block) > 80 and np.ptp(block) > 50:
            maps.append(block)
    return maps

def hex_dump(data):
    return "\n".join(
        f"{i:06X}: " + " ".join(f"{b:02X}" for b in data[i:i+16])
        for i in range(0, len(data), 16)
    )

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ECU AI Tuner vNext")
        self.resize(1200, 700)

        self.data = np.random.randint(0, 255, 2048)
        self.maps = detect_maps(self.data)

        layout = QHBoxLayout()

        self.list = QListWidget()
        self.view = pg.ImageView()

        self.hex = QTextEdit()
        self.hex.setText(hex_dump(self.data))

        self.sim = QLabel("Simulation idle")

        btn = QPushButton("Run Simulation")
        btn.clicked.connect(self.simulate)

        right = QVBoxLayout()
        right.addWidget(self.hex)
        right.addWidget(self.sim)
        right.addWidget(btn)

        container = QWidget()

        layout.addWidget(self.list, 2)
        layout.addWidget(self.view, 5)
        layout.addWidget(QWidget().setLayout(right), 3)

        container.setLayout(layout)
        self.setCentralWidget(container)

    def simulate(self):
        stock = engine_model(1800, np.mean(self.data))
        tuned = engine_model(2000, np.mean(self.data)*1.1)
        self.sim.setText(f"Stock: {stock:.1f} | Tuned: {tuned:.1f}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = App()
    w.show()
    sys.exit(app.exec())
