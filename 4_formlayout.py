import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QLabel, QLineEdit, QHBoxLayout, QComboBox

# สร้างคลาส Window ซึ่งสืบทอดมาจาก QWidget
class Window(QWidget):
    def __init__(self):
        # เรียกใช้งาน constructor ของ QWidget
        super().__init__()
        # กำหนดชื่อหน้าต่าง
        self.setWindowTitle("Form Layout")
        # กำหนดตำแหน่งและขนาดของหน้าต่าง (x, y, width, height)
        self.setGeometry(350, 150, 400, 400)
        # เรียกใช้ฟังก์ชัน UI เพื่อตั้งค่า UI
        self.UI()

    def UI(self):
        # สร้าง Layout แบบฟอร์ม (Form Layout)
        formLayout = QFormLayout()

        # สร้างช่องกรอกข้อมูลสำหรับ "Name"
        name_txt = QLabel("Name : ")       # ป้ายกำกับข้อความ "Name"
        name_input = QLineEdit()           # ช่องกรอกข้อความสำหรับชื่อ

        # สร้างช่องกรอกข้อมูลสำหรับ "Surname"
        surname_txt = QLabel("Surname : ") # ป้ายกำกับข้อความ "Surname"
        surname_input = QLineEdit()        # ช่องกรอกข้อความสำหรับนามสกุล

        # สร้าง ComboBox สำหรับเลือกประเทศ
        combo = QComboBox()
        combo.addItems(["Thai", "USA", "China"])  # เพิ่มรายการประเทศใน ComboBox

        # สร้าง Layout แนวนอน (Horizontal Layout) สำหรับปุ่ม
        hbox = QHBoxLayout()
        hbox.addStretch()                           # เพิ่มพื้นที่ว่างแบบขยายได้ด้านซ้าย
        hbox.addWidget(QPushButton("Enter"))        # ปุ่ม "Enter"
        hbox.addWidget(QPushButton("Exit"))         # ปุ่ม "Exit"

        # เพิ่มแต่ละแถวลงใน Form Layout
        formLayout.addRow(name_txt, name_input)     # แถวสำหรับชื่อ
        formLayout.addRow(surname_txt, surname_input) # แถวสำหรับนามสกุล
        formLayout.addRow(QLabel("Country : "), combo) # แถวสำหรับประเทศ
        formLayout.addRow(hbox)                     # แถวสำหรับปุ่ม

        # กำหนด Layout ให้กับหน้าต่าง
        self.setLayout(formLayout)
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
