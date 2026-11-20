import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import Qt
from List import List
from Compare import soSanhTheoMa, soSanhTheoTen
from ui import Ui_MainWindow
from KhachHang import KhachHang

class App(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ds = List()

        self.btn_them.clicked.connect(self.themKhachHang)
        self.btn_sua.clicked.connect(self.suaThongTin)
        self.btn_xoa.clicked.connect(self.xoaKhachHang)
        self.btn_moi.clicked.connect(self.lamMoi)
        self.btn_sort_ma.clicked.connect(self.sortTheoMa)
        self.btn_sort_ten.clicked.connect(self.sortTheoTen)
        self.btn_search.clicked.connect(self.TimKhachHang)

    def TimTheoMa(self, ma):
        for i in range(len(self.ds)):
            if int(self.ds[i].maKH) == int(ma):
                return i
        return -1

    def TimKhachHang(self):
        ma_text = self.in_search_maKH.text().strip()
        if not ma_text:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập mã khách hàng để tìm kiếm")
            return
        elif not ma_text.isdigit():
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập mã khách hàng là số nguyên để tìm kiếm")
            return
        idx = self.TimTheoMa(ma_text)
        if(idx != -1):
            self.in_maKH.setText(str(self.ds[idx].maKH))
            self.in_maKH.setEnabled(False)
            self.in_hoTen.setText(self.ds[idx].hoTen)
            self.in_sdt.setText(self.ds[idx].sdt)
            self.table.selectRow(idx)
        else:
            QMessageBox.warning(self, "Lỗi", f"Không tìm thấy khách hàng có mã {ma_text}")

    def hienThi(self):
        self.table.setRowCount(len(self.ds))
        for i in range(len(self.ds)):
            kh = self.ds[i]
            for c, text in enumerate((str(kh.maKH), f"   {kh.hoTen}", kh.sdt)):
                item = QTableWidgetItem(text)
                if c!=1:
                    item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(i, c, item)
        self.count.setText(f"Tổng số khách hàng: {len(self.ds)}")

    def lamMoi(self):
        self.in_maKH.clear()
        self.in_maKH.setEnabled(True)
        self.in_sdt.clear()
        self.in_hoTen.clear()
        self.in_search_maKH.clear()

    def themKhachHang(self):
        Makh = self.in_maKH.text().strip()
        ten = self.in_hoTen.text().strip()
        so_dien_thoai = self.in_sdt.text().strip()
        if not Makh:
            QMessageBox.warning(self, "Lỗi","Mã KH không được để trống")
            return
        if not Makh.isdigit():
            QMessageBox.warning(self, "Lỗi","Mã KH phải là số nguyên")
            return
        if not ten:
            QMessageBox.warning(self, "Lỗi","Họ tên không được để trống")
            return
        if not all(c.isalpha() or c.isspace() for c in ten):
            QMessageBox.warning(self, "Lỗi", "Họ tên phải là chữ")
            return
        if not so_dien_thoai:
            QMessageBox.warning(self, "Lỗi","Số điện thoại không được để trống")
            return
        if not so_dien_thoai.isdigit():
            QMessageBox.warning(self, "Lỗi", "Số điện thoại phải là số")
            return
        if self.TimTheoMa(int(Makh)) != -1:
            QMessageBox.warning(self, "Lỗi",f"Mã KH {Makh} đã tồn tại.")
            return
        self.ds.push_back(KhachHang(int(Makh), ten, so_dien_thoai))
        self.hienThi()
        self.lamMoi()

    def suaThongTin(self):
        ma_text = self.in_maKH.text().strip()
        ten = self.in_hoTen.text().strip()
        sdt = self.in_sdt.text().strip()
        if not ma_text or not ma_text.isdigit():
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập khách hàng cần sửa")
            return
        if not ten or not sdt:
            QMessageBox.warning(self, "Lỗi", "Họ tên và SĐT không được để trống")
            return
        idx = self.TimTheoMa(self.in_maKH.text().strip())
        if idx == -1:
            QMessageBox.warning(self, "Lỗi", f"Không tìm thấy khách hàng có mã {ma_text}!")
            return
        self.ds[idx].hoTen = ten
        self.ds[idx].sdt = sdt
        self.hienThi()
        self.lamMoi()
        QMessageBox.information(self, "Thông báo", "Đã cập nhật khách hàng thành công")


    def xoaKhachHang(self):
        ma_text = self.in_maKH.text().strip()
        if not ma_text or not ma_text.isdigit():
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập khách hàng cần xóa")
            return
        idx = self.TimTheoMa(int(ma_text))
        if idx == -1:
            QMessageBox.warning(self, "Lỗi", f"Không tìm thấy khách hàng có mã {ma_text}")
            return
        self.ds.remove(idx)
        self.hienThi()
        self.lamMoi()
        QMessageBox.information(self, "Thông báo", "Đã xóa khách hàng thành công")

    def sortTheoMa(self):
        self.ds.QuickSort(soSanhTheoMa)
        self.hienThi()

    def sortTheoTen(self):
        self.ds.QuickSort(soSanhTheoTen)
        self.hienThi()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())










