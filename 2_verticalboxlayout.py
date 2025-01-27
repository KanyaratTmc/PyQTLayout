import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

# สร้างคลาส Window ซึ่งสืบทอดมาจาก QWidget
class Window(QWidget):
    def __init__(self):
        # เรียกใช้งาน constructor ของ QWidget
        super().__init__()
        # กำหนดชื่อหน้าต่าง
        self.setWindowTitle("Vertical Box Layout")
        # กำหนดขนาดและตำแหน่งของหน้าต่าง (x, y, width, height)
        self.setGeometry(350, 150, 400, 400)
        # เรียกใช้ฟังก์ชัน UI เพื่อตั้งค่า UI
        self.UI()

    def UI(self):
        # สร้าง Vertical Box Layout
        vbox = QVBoxLayout()

        # สร้างปุ่ม 3 ปุ่ม
        button1 = QPushButton("Save", self)   # ปุ่ม Save
        button2 = QPushButton("Exit", self)   # ปุ่ม Exit
        button3 = QPushButton("Hello", self)  # ปุ่ม Hello

        # เพิ่มช่องว่างที่ขยายได้ด้านบน
        vbox.addStretch()
        # เพิ่มปุ่มลงใน Layout
        vbox.addWidget(button1)  # เพิ่มปุ่ม Save
        vbox.addWidget(button2)  # เพิ่มปุ่ม Exit
        vbox.addWidget(button3)  # เพิ่มปุ่ม Hello
        # เพิ่มช่องว่างที่ขยายได้ด้านล่าง
        vbox.addStretch()

        # ตั้งค่า Layout ให้กับหน้าต่าง
        self.setLayout(vbox)
        # แสดงหน้าต่าง
        self.show()

# ฟังก์ชันหลักของโปรแกรม
def main():
    # สร้าง QApplication สำหรับจัดการอีเวนต์
    app = QApplication(sys.argv)
    # สร้างวัตถุหน้าต่าง
    window = Window()
    # ออกจากโปรแกรมเมื่อหน้าต่างปิด
    sys.exit(app.exec())

# จุดเริ่มต้นของโปรแกรม
if __name__ == '__main__':
    main()
