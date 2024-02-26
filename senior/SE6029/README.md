# [SE6029] Object Oriented Programming Writeups


> 2024-Spring-OOAD  
>
> *NO OFFENSE MEANS I AM ABOUT TO INSULT YOU, BUT DONT GET MAD*


### [`C++` Project Templates Structure](./templates/)

```
PROJECT_ROOT
├── bin/
│   └── main.out
├── include/
│   └── *.h
├── src/
│   └── *.cpp
├── test/
│   └──   :
└──  build.sh
```

#### How to **compile and execute** the `MAIN PROGRAM` with this templates?
```sh
g++ -Iinclude -o src/*.cpp -o bin/main.out && ./bin/main.out
```

### Genuine Understanding V.S. Superficial Knowledge.

```cpp
class EmployeeCensus: public Listcontainer {

public:
    ...
    // public routines
    void AddEmployee ( Employee employee ); 
    void RemoveEmployee ( Employee employee );
    Employee NextItemInList();
    Employee FirstItem;
    Employee LastItem;
    ...
private:
    ...
}
```

- 搞笑題目 (例如，前10名搶答者有分)
- 名詞解釋 (前30%滿分，中間30%60分，尾巴40% 30分)
- 嚴重思考題 (對比較重要，不搶答，給你滿滿的時間)
喔! 你抄襲就0分，你給別人抄襲你就變成50%分數


每一題公告之前會告知哪一種類型


### Materials

| Week | Topic  | Code |
| ---- | ------ | ---- |
| 1    | [Software Engineering Basics](./00_software_engineering_basics/), [Classes and Object]((./01_classes_and_object/README.md)) | [`Point`](./01_classes_and_object/01_Point/), [`Dog`](./01_classes_and_object/02_Dog/), [`Dog` in `C`](./01_classes_and_object/03_DogC/), [`Constructor` and `Deconstructor`](./01_classes_and_object/04_ConstructorDeconstructor/), [`Car`](./01_classes_and_object/05_CarStack/), [`Car` in `Heap`](./01_classes_and_object/06_CarHeap/) |

