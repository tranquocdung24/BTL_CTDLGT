#ifndef BTL_CTDLGT_KHACHHANG_H
#define BTL_CTDLGT_KHACHHANG_H

#include <string>
using namespace std;

class KhachHang {
private:
    int maKH;
    string hoTen;
    string sdt;

public:
    KhachHang();
    KhachHang(int ma, string ten, string sdt);

    int getMaKH() const;
    string getHoTen() const;
    string getSdt() const;

    void setMaKH(int ma);
    void setHoTen(string ten);
    void setSdt(string sdt);

    void nhap();
    void xuat() const;
};

#endif //BTL_CTDLGT_KHACHHANG_H
