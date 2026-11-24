#include "QuanLyKhachHang.h"
#include "Compare.h"
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int QuanLyKhachHang::TimTheoMa(int ma) const {
    for (int i = 0; i < ds.getSize(); i++)
        if (ds[i].getMaKH() == ma)
            return i;
    return -1;
}

void QuanLyKhachHang::themKhachHang() {
    char tiepTuc;
    do {
        cout << "\n--- NHAP THONG TIN KHACH HANG ---\n";
        KhachHang kh;
        kh.nhap();
        while (TimTheoMa(kh.getMaKH()) != -1) {
            cout << "Loi! Ma KH " << kh.getMaKH() << " da ton tai! Vui long nhap lai.\n";
            kh.nhap();
        }
        ds.push_back(kh);
        cout << "Ban co tiep tuc them khach hang nua khong (y/n)? ";
        cin >> tiepTuc;
        cin.ignore();
    }
    while (tiepTuc == 'y' || tiepTuc == 'Y');
}

void QuanLyKhachHang::xoaKhachHang() {
    if (ds.isEmpty()) {
        cout << "Danh sach dang trong!\n";
        return;
    }
    int ma;
    cout << "Nhap Ma KH can xoa: ";
    cin >> ma;
    int target = TimTheoMa(ma);
    if (target != -1) {
        ds.remove(target);
        cout << "Da xoa khach hang co ma " << ma << " thanh cong!\n";
    }
    else {
        cout << "Khong tim thay khach hang co ma " << ma << "!\n";
    }
}

void QuanLyKhachHang::suaThongTin() {
    if (ds.isEmpty()) {
        cout << "Danh sach dang trong!\n";
        return;
    }
    int ma;
    cout << "Nhap Ma KH can sua thong tin: ";
    cin >> ma;
    cin.ignore();
    int target = TimTheoMa(ma);
    if (target != -1) {
        string tenMoi, sdtMoi;
        cout << "Thong tin hien tai: \n" << "Ho va ten: " << ds[target].getHoTen() << endl
             << "SDT: " << ds[target].getSdt() << endl;

        cout << "Nhap ho ten moi: ";
        getline(cin,tenMoi);
        cout << "Nhap SDT moi: ";
        getline(cin,sdtMoi);

        ds[target].setHoTen(tenMoi);
        ds[target].setSdt(sdtMoi);
        cout << "Cap nhat thong tin thanh cong!\n";
    }
    else {
        cout << "Khong tim thay khach hang co ma " << ma << "!\n";
    }
}

void QuanLyKhachHang::sapXepTheoMa() {
    ds.QuickSort(soSanhTheoMa);
    cout << "Da sap xep theo Ma KH.\n";
    hienThi();
}

void QuanLyKhachHang::sapXepTheoTen() {
    ds.QuickSort(soSanhTheoTen);
    cout << "Da sap xep theo ho ten.\n";
    hienThi();
}

void QuanLyKhachHang::hienThi() const {
    if (ds.isEmpty()) {
        cout << "Danh sach dang trong!\n";
        return;
    }
    cout << "\n================ DANH SACH KHACH HANG ================\n";
    cout << left << setw(12) << "Ma KH"
         << setw(28) << "Ho va Ten"
         << setw(15) << "So Dien Thoai" << endl;
    cout << "------------------------------------------------------\n";
    for (int i = 0; i < ds.getSize(); i++)
        ds[i].xuat();
    cout << "======================================================\n";
}
