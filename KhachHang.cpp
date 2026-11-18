
#include "KhachHang.h"
#include <iostream>
#include <iomanip>
using namespace std;

KhachHang::KhachHang() : maKH(0), hoTen(""), sdt("") {}

KhachHang::KhachHang(int ma, string ten, string sdt): maKH(ma), hoTen(ten), sdt(sdt) {}

int KhachHang::getMaKH() const {
    return maKH;
}

string KhachHang::getHoTen() const {
    return hoTen;
}

string KhachHang::getSdt() const {
    return sdt;
}

void KhachHang::setMaKH(int ma) {
    maKH = ma;
}

void KhachHang::setHoTen(string ten) {
    hoTen = ten;
}

void KhachHang::setSdt(string s) {
    sdt = s;
}

void KhachHang::nhap() {
    cout << "Nhap Ma KH: ";
    while (!(cin >> maKH)) {
        cout << "Ma KH phai la so! Vui long nhap lai!";
        cin.clear();
        cin.ignore(1000,'\n');
    }
    cin.ignore(1000,'\n');
    cout << "Nhap Ho Ten: ";
    getline(cin, hoTen);
    cout << "Nhap SDT: ";
    getline(cin, sdt);
}

void KhachHang::xuat() const {
    cout << left << setw(12) << maKH
         << setw(28) << hoTen
         << setw(15) << sdt << endl;
}