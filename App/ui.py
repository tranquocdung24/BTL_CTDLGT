import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                             QPushButton, QApplication, QMainWindow, QGroupBox, QLineEdit,
                             QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView)
from PyQt5.QtCore import Qt


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản Lý Khách Hàng")
        self.resize(1000, 540)
        self.setupUi()
    def setupUi(self):
        root = QWidget()
        self.setCentralWidget(root)
        main = QVBoxLayout()
        root.setLayout(main)
        title = QLabel("QUẢN LÝ KHÁCH HÀNG")
        title.setAlignment(Qt.AlignCenter)
        title.setObjectName("title")
        main.addWidget(title)

        content = QHBoxLayout()
        main.addLayout(content)

        left = QVBoxLayout()
        content.addLayout(left,3)
        gb_ttin_kh = QGroupBox("Nhập thông tin khách hàng")
        ttin_kh = QVBoxLayout()
        gb_ttin_kh.setLayout(ttin_kh)
        ma_khach_hang = QHBoxLayout()
        self.maKH = QLabel("Mã KH: ")
        self.in_maKH = QLineEdit()
        ma_khach_hang.addWidget(self.maKH)
        ma_khach_hang.addWidget(self.in_maKH)
        ho_ten = QHBoxLayout()
        self.hoTen = QLabel("Họ tên: ")
        self.in_hoTen = QLineEdit()
        ho_ten.addWidget(self.hoTen)
        ho_ten.addWidget(self.in_hoTen)
        SDT = QHBoxLayout()
        self.sdt = QLabel("SĐT: ")
        self.in_sdt = QLineEdit()
        SDT.addWidget(self.sdt)
        SDT.addWidget(self.in_sdt)
        ttin_kh.addLayout(ma_khach_hang)
        ttin_kh.addLayout(ho_ten)
        ttin_kh.addLayout(SDT)
        left.addWidget(gb_ttin_kh)
        gb_chuc_nang = QGroupBox("Chức năng")
        chuc_nang = QVBoxLayout()
        gb_chuc_nang.setLayout(chuc_nang)
        self.btn_them = QPushButton("Thêm Khách Hàng")
        self.btn_them.setObjectName("btn_them")
        self.btn_them.setCursor(Qt.PointingHandCursor)
        self.btn_sua = QPushButton("Sửa Thông Tin ")
        self.btn_sua.setObjectName("btn_sua")
        self.btn_sua.setCursor(Qt.PointingHandCursor)
        self.btn_xoa = QPushButton("Xóa Khách Hàng")
        self.btn_xoa.setObjectName("btn_xoa")
        self.btn_xoa.setCursor(Qt.PointingHandCursor)
        self.btn_moi = QPushButton("Làm mới form")
        self.btn_moi.setObjectName("btn_moi")
        self.btn_moi.setCursor(Qt.PointingHandCursor)
        chuc_nang.addWidget(self.btn_them)
        chuc_nang.addWidget(self.btn_sua)
        chuc_nang.addWidget(self.btn_xoa)
        chuc_nang.addWidget(self.btn_moi)
        left.addWidget(gb_chuc_nang)
        gb_sort = QGroupBox("Sắp xếp")
        srt = QVBoxLayout()
        gb_sort.setLayout(srt)
        self.btn_sort_ma = QPushButton("Theo Mã KH")
        self.btn_sort_ma.setObjectName("btn_sort")
        self.btn_sort_ma.setCursor(Qt.PointingHandCursor)
        self.btn_sort_ten = QPushButton("Theo Họ tên")
        self.btn_sort_ten.setObjectName("btn_sort")
        self.btn_sort_ten.setCursor(Qt.PointingHandCursor)
        srt.addWidget(self.btn_sort_ma)
        srt.addWidget(self.btn_sort_ten)
        left.addWidget(gb_sort)
        left.addStretch(1)

        right = QVBoxLayout()
        content.addLayout(right,7)
        Search_maKH = QHBoxLayout();
        self.in_search_maKH = QLineEdit()
        self.in_search_maKH.setPlaceholderText("  Nhập mã khách hàng cần tìm kiếm")
        self.btn_search = QPushButton("Search")
        self.btn_search.setObjectName("btn_search")
        self.btn_search.setCursor(Qt.PointingHandCursor)
        Search_maKH.addWidget(self.in_search_maKH)
        Search_maKH.addWidget(self.btn_search)
        right.addLayout(Search_maKH)
        self.table = QTableWidget(0, 3)
        self.table.verticalHeader().setVisible(False)
        hh = self.table.horizontalHeader()
        hh.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        hh.setSectionResizeMode(1, QHeaderView.Stretch)
        hh.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.table.setHorizontalHeaderLabels(["Mã Khách Hàng", "Họ và tên", "Số điện thoại"])
        right.addWidget(self.table, 1)
        self.count = QLabel("Tổng số khách hàng: 0")
        self.count.setAlignment( Qt.AlignLeft)
        self.count.setObjectName("count")
        right.addWidget(self.count)


        self.setStyleSheet("""
                            QMainWindow {
                                background-color: #f4f6f9;
                            }
                            #title {
                                font-size:40px;
                                padding: 10px;
                                font-family: Arial;
                                 color: #1F3A68;
                                font-weight: bold;
                            }
                            QGroupBox {
                                font-family: Arial;
                                color: #1F3A68;
                                font-weight: bold;
                                font-size: 17px;
                            }
                            QLineEdit {
                                padding: 10px;
                                border-radius: 10px;
                                font-size: 15px;
                            }
                            QPushButton {
                                padding: 10px;
                                border-radius: 10px;
                                color: white;
                                font-weight: bold;
                                font-size: 17px;
                            }
                            #btn_them {
                                background-color: green;
                            }
                            #btn_sua {
                                background-color: orange;
                            }
                            #btn_xoa {
                                background-color: red;
                            }
                            #btn_moi {
                                background-color: gray;
                            }
                            #btn_sort, #btn_search {
                                background-color: blue;
                            }
                            QLineEdit:focus {
                                border: 1px solid blue;
                            }
                            QHeaderView::section {
                                background-color: #34495e;
                                color: #ffffff;
                                padding: 8px;
                                font-weight: bold;
                                border: none;
                            }
                            QLabel {
                                font-size: 15px;
                            }
                            #count {
                                font-size:20px;
                                color: #34495e;
                            }
                            """)

def run():
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()

