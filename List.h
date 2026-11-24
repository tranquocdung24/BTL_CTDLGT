#ifndef BTL_CTDLGT_LIST_H
#define BTL_CTDLGT_LIST_H

#include<iostream>
#include<algorithm>
using namespace std;

template<class T>
class List {
private:
    T *data;
    int size;
    int capacity;

    void autoResize();
    int partition(int l, int r, bool (*cmp)(const T &a, const T &b));
    void QuickSort1(int l, int r, bool (*cmp)(const T &a, const T &b));
public:
    List();
    ~List();

    void push_back(T &new_data);
    void remove(int idx);
    int getSize() const;
    bool isEmpty() const;
    const T& operator[](int idx) const;
    T& operator[](int idx);
    void QuickSort(bool (*cmp)(const T &a, const T &b));
};

template<class T>
void List<T>::autoResize() {
    if (capacity == size) {
        capacity *=2;
        T* temp = new T[capacity];
        for (int i = 0; i < size; i++) {
            temp[i] = data[i];
        }
        delete [] data;
        data = temp;
    }
}

template<class T>
int List<T>::partition(int l, int r, bool (*cmp)(const T &a, const T &b)) {
    T pivot = data[r];
    int i = l-1;
    for (int j = l; j < r; j++) {
        if (cmp(data[j], pivot)) {
            i++;
            swap(data[i], data[j]);
        }
    }
    swap(data[i+1], data[r]);
    return i+1;
}

template<class T>
void List<T>::QuickSort1(int l, int r, bool (*cmp)(const T &a, const T &b)) {
    if (l>=r) return;
    int pos = partition(l, r, cmp);
    QuickSort1(l, pos - 1, cmp);
    QuickSort1(pos + 1, r, cmp);
}

template<class T>
List<T>::List() {
    capacity = 1;
    data = new T[capacity];
    size = 0;
}

template<class T>
List<T>::~List() {
    delete [] data;
}

template<class T>
bool List<T>::isEmpty() const {
    return size == 0;
}

template<class T>
void List<T>::push_back(T &new_data) {
    autoResize();
    data[size] = new_data;
    size++;
}

template<class T>
void List<T>::remove(int idx) {
    if (!isEmpty() && idx >= 0 && idx < size) {
        for (int i = idx; i < size-1; i++) {
            data[i] = data[i+1];
        }
        size--;
    }
}

template<class T>
int List<T>::getSize() const {
    return size;
}

template<class T>
const T& List<T>::operator[](int idx) const {
    return data[idx];
}

template<class T>
T& List<T>::operator[](int idx) {
    return data[idx];
}

template<class T>
void List<T>::QuickSort(bool (*cmp)(const T &a, const T &b)) {
    if (size > 1) {
        QuickSort1(0, size - 1, cmp);
    }
}
#endif //BTL_CTDLGT_LIST_H
