#include "Compare.h"

#include <string>
using namespace std;

static string layTen(const string& hoTen) {
    size_t pos = hoTen.find_last_of(' ');
    if (pos == string::npos) return hoTen;
    return hoTen.substr(pos + 1);
}

bool soSanhTheoMa(const KhachHang &a, const KhachHang &b) {
    return a.getMaKH() < b.getMaKH();
}

bool soSanhTheoTen(const KhachHang &a, const KhachHang &b) {
    string tenA = layTen(a.getHoTen());
    string tenB = layTen(b.getHoTen());
    if (tenA != tenB) return tenA < tenB;
    return a.getHoTen() < b.getHoTen();
}