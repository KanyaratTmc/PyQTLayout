import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox, QRadioButton, QComboBox

# สร้างคลาส Window ซึ่งสืบทอดมาจาก QWidget
class Window(QWidget):
    def __init__(self):
        # เรียกใช้งาน constructor ของ QWidget
        super().__init__()
        # กำหนดชื่อหน้าต่าง
        self.setWindowTitle("Vertical Box Layout")
        # กำหนดตำแหน่งและขนาดของหน้าต่าง (x, y, width, height)
        self.setGeometry(350, 150, 400, 400)
        # เรียกใช้ฟังก์ชัน UI เพื่อตั้งค่า UI
        self.UI()

    def UI(self):
        # สร้าง Layout หลักเป็น QVBoxLayout
        mainLayout = QVBoxLayout()
        # สร้าง Layout ย่อย 2 ชุด: topLayout และ bottomLayout (แนวนอน)
        topLayout = QHBoxLayout()
        bottomLayout = QHBoxLayout()
        # เพิ่ม Layout ย่อยเข้าไปใน Layout หลัก
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bottomLayout)

        # สร้าง Widget แต่ละตัว
        cbox = QCheckBox()       # กล่องเช็ค (CheckBox)
        rbtn = QRadioButton()    # ปุ่มตัวเลือก (RadioButton)
        combo = QComboBox()      # กล่องเลือกตัวเลือกแบบเลื่อนลง (ComboBox)

        # สร้างปุ่มแบบ ComboBox (ชื่อ btn1, btn2)
        btn1 = QComboBox()       # ปุ่ม ComboBox ตัวที่ 1
        btn2 = QComboBox()       # ปุ่ม ComboBox ตัวที่ 2

        # เพิ่ม Widget เข้าไปใน topLayout
        topLayout.addWidget(cbox)   # เพิ่ม CheckBox
        topLayout.addWidget(rbtn)   # เพิ่ม RadioButton
        topLayout.addWidget(combo)  # เพิ่ม ComboBox

        # เพิ่ม Widget เข้าไปใน bottomLayout
        bottomLayout.addWidget(btn1)  # เพิ่ม ComboBox (btn1)
        bottomLayout.addWidget(btn2)  # เพิ่ม ComboBox (btn2)

        # ตั้งค่า Layout หลักให้กับหน้าต่าง
        self.setLayout(mainLayout)
        # แสดงหน้าต่าง
        self.show()

# ฟังก์ชันหลักของโปรแกรม
def main():
    # สร้าง QApplication เพื่อจัดการอีเวนต์
    app = QApplication(sys.argv)
    # สร้างวัตถุหน้าต่าง
    window = Window()
    # ออกจากโปรแกรมเมื่อหน้าต่างปิด
    sys.exit(app.exec())

# จุดเริ่มต้นของโปรแกรม
if __name__ == '__main__':
    main()
