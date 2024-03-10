// In C, 當你使用 struct 時，你只有定義了資料
// 有時候你還得自己動手做一些初始化的動作
// 例如

typedef struct dog_body {
    int age;
    int weight;
    char *name;
} Dog;

//  假設你事先不能知道 name 的長度。你必須自己想辦法配置空間與初始化
Dog myDog;
// ...
// somehow, you got a dog name from input, it is stored in dname
myDog.name = malloc(strlen(dname));
strcpy(myDog.name, dname);

// ...
