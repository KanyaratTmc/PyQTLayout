import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

# สร้างคลาส Window ที่สืบทอดจาก QWidget
class Window(QWidget):
    def __init__(self):
        # เรียกใช้งาน constructor ของ QWidget
        super().__init__()
        # กำหนดชื่อหน้าต่าง
        self.setWindowTitle("Horizontal Box Layout")
        # กำหนดขนาดและตำแหน่งของหน้าต่าง (x, y, width, height)
        self.setGeometry(350, 150, 400, 400)
        # เรียกใช้ฟังก์ชัน UI เพื่อตั้งค่า UI
        self.UI()

    def UI(self):
        # สร้าง Horizontal Box Layout
        hbox = QHBoxLayout()

        # สร้างปุ่ม 3 ปุ่ม
        button1 = QPushButton("Button1", self)  # ปุ่มแรก
        button2 = QPushButton("Button2", self)  # ปุ่มที่สอง
        button3 = QPushButton("Button3", self)  # ปุ่มที่สาม

        # เพิ่มช่องว่างที่ขยายได้ทั้งสองด้านของปุ่ม (เพื่อจัดตำแหน่งให้อยู่ตรงกลาง)
        hbox.addStretch()
        # เพิ่มปุ่มเข้าไปใน Layout
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        hbox.addWidget(button3)
        # เพิ่มช่องว่างที่ขยายได้อีกครั้งทางด้านขวาของปุ่ม
        hbox.addStretch()

        # ตั้งค่า Layout ให้กับหน้าต่าง
        self.setLayout(hbox)
        # แสดงหน้าต่าง
        self.show()

# ฟังก์ชันหลักสำหรับรันแอปพลิเคชัน
def main():
    # สร้าง QApplication สำหรับจัดการอีเวนต์
    app = QApplication(sys.argv)
    # สร้างวัตถุหน้าต่าง
    window = Window()
    # ออกจากโปรแกรมเมื่อปิดหน้าต่าง
    sys.exit(app.exec())

# จุดเริ่มต้นของโปรแกรม
if __name__ == '__main__':
    main()
