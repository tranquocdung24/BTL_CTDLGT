#include "App.h"
#include<iostream>
using namespace std;

void App::run() {
    do {
        cout << "\n========== MENU QUAN LY KHACH HANG ==========\n";
        cout << "1. Nhap them khach hang\n";
        cout << "2. Xoa mot khach hang\n";
        cout << "3. Sua thong tin cua khach hang\n";
        cout << "4. Sap xep danh sach theo Ma KH\n";
        cout << "5. Sap xep danh sach theo Ho ten\n";
        cout << "6. Hien thi toan bo danh sach khach hang\n";
        cout << "0. Thoat chuong trinh\n";
        cout << "======================================================\n";
        cout << "Nhap lua chon cua ban: ";
        cin >> choice;

        switch (choice) {
            case 1:
                ql.themKhachHang();
                break;
            case 2:
                ql.xoaKhachHang();
                break;
            case 3:
                ql.suaThongTin();
                break;
            case 4:
                ql.sapXepTheoMa();
                break;
            case 5:
                ql.sapXepTheoTen();
                break;
            case 6:
                ql.hienThi();
                break;
            case 0:
                cout << "Da thoat chuong trinh!\n";
                break;
            default:
                cout << "Lua chon khong hop le! Vui long chon lai.\n";
                cin.clear();
                cin.ignore(1000, '\n');
                break;
        }
    }
    while (choice != 0);
}
