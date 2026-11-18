cmake_minimum_required(VERSION 4.4)
project(BTL_CTDLGT)

set(CMAKE_CXX_STANDARD 17)

add_executable(BTL_CTDLGT main.cpp
        KhachHang.h
        KhachHang.cpp
        List.h
        Compare.h
        Compare.cpp
        QuanLyKhachHang.h
        QuanLyKhachHang.cpp
        App.h
        App.cpp
)
