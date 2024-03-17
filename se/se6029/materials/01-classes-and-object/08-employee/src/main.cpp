#include <iostream>
#include "Employee.h"

int main() {
    Employee programmer("John", 22);
    std::cout << programmer.getName() << std::endl;

    // Lots of code here

    // 當我們用這個程式想對 Jogn 做升遷時
    Employee manager = programmer;

    // This program has the runtime error
    // because the programmer object is deleted
    // effect dangling pointer in manager object
    // 原先 programmer 被建立時，會有個指向 John 的指標
    // 當複製 programmer 到 manager 也有指向 John 的指標
    // 不過當 programmer 被刪除後，programmer 原先建構的
    // Employee Construct 也會被刪除，連帶指向 John 的區段也被刪除
    // 導致新複製的 manager 不知道要指去哪裡找 John
    // 造成 dangling pointer

    delete &programmer;
    return 0;
}
