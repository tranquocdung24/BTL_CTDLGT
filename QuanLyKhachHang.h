#ifndef BTL_CTDLGT_QUANLYKHACHHANG_H
#define BTL_CTDLGT_QUANLYKHACHHANG_H
#include "List.h"
#include "KhachHang.h"

class QuanLyKhachHang {
private:
    List<KhachHang> ds;
    int TimTheoMa(int ma) const;

public:
    void themKhachHang();
    void xoaKhachHang();
    void suaThongTin();
    void sapXepTheoMa();
    void sapXepTheoTen();
    void hienThi() const;
};
#endif //BTL_CTDLGT_QUANLYKHACHHANG_H
