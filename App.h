#ifndef BTL_CTDLGT_APP_H
#define BTL_CTDLGT_APP_H

#include "QuanLyKhachHang.h"
#include <iostream>
using namespace std;

class App {
    private:
        int choice;
        QuanLyKhachHang ql;
    public:
        void run();
};
#endif //BTL_CTDLGT_APP_H
