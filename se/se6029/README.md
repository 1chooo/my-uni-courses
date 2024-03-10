# Object Oriented Analysis and Design Writeups

> 2024-Spring-OOAD  
>
> *NO OFFENSE MEANS I AM ABOUT TO INSULT YOU, BUT DONT GET MAD*


## [`C++` Project Templates Structure](./templates/)

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

### How to **compile and execute** the `MAIN PROGRAM` with this templates?
```sh
g++ -Iinclude -o src/*.cpp -o bin/main.out && ./bin/main.out
```

## Genuine Understanding V.S. Superficial Knowledge.

```cpp
class EmployeeCensus: public ListContainer {

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

- 搞笑題目 (例如，前 10 名搶答者有分)
- 名詞解釋 (前 30% 滿分，中間 30% 60 分，尾巴 40% 30 分)
- 嚴重思考題 (對比較重要，不搶答，給你滿滿的時間)

> [!WARNING]
> 喔！你抄襲就 0 分，你給別人抄襲你就變成 50% 分數


每一題公告之前會告知哪一種類型


## Materials

| Week | Topic  | Code | Homework |
| ---- | ------ | ---- | -------- |
| 1    | [Software Engineering Basics](./materials/00_software_engineering_basics/), [Classes and Object]((./materials/01_classes_and_object/README.md)) | [`Point`](./materials/01_classes_and_object/01_Point/), [`Dog`](./materials/01_classes_and_object/02_Dog/), [`Dog in C`](./materials/01_classes_and_object/03_DogC/), [`Constructor and Deconstructor`](./materials/01_classes_and_object/04_ConstructorDeconstructor/), [`Car`](./materials/01_classes_and_object/05_CarStack/), [`Car in Heap`](./materials/01_classes_and_object/06_CarHeap/), [`Cat`](./materials/01_classes_and_object/07_Cat/), [`Employee`](./materials/01_classes_and_object/08_Employee/), [`Table`](./materials/01_classes_and_object/09_Table/) |  |
<!-- |     |  |  |  |
|     |  |  |  | -->

## Collaboration Guidelines
### Forking this Repository:

Fork the [`object-oriented-analysis-and-design-writeups`](https://github.com/1chooo/object-oriented-analysis-and-design-writeups) repository into your own workspace.

### Cloning the Repository to Your Workspace:

```shell
$ git clone git@github.com:<your_workspace_name>/object-oriented-analysis-and-design-writeups.git
```

### Setting Upstream Remote:
```shell
$ git remote add upstream git@github.com:1chooo/object-oriented-analysis-and-design-writeups.git

$ git remote -v
origin  git@github.com:<your_user_name>/object-oriented-analysis-and-design-writeups.git (fetch)
origin  git@github.com:<your_user_name>/object-oriented-analysis-and-design-writeups.git (push)
upstream        git@github.com:1chooo/object-oriented-analysis-and-design-writeups.git (fetch)
upstream        git@github.com:1chooo/object-oriented-analysis-and-design-writeups.git (push)
```
### Pull Requests:
If you have any valuable ideas to contribute, please create a pull request and provide details about the outstanding work you've done.

### Issue Reporting:
If you encounter any problems while contributing to this project, please report the issues in the [object-oriented-analysis-and-design-writeups/issues](https://github.com/1chooo/object-oriented-analysis-and-design-writeups/issues) section.


### Important Notes:
> [!IMPORTANT]  
> #### Make sure to synchronize and update your repository before initiating a pull request:
> 1. Run `git stash save` to temporarily stash your local changes.
> 2. Run `git fetch upstream` to sync the source project with your local copy.
> 3. Run `git checkout main` to switch to the main branch.
> 4. Run `git merge upstream/main` to merge the updated remote version into your local copy. If there are no conflicts, the update process is complete.
> 5. Run `git stash pop` to apply your temporarily stashed changes back to your working directory. Resolve any conflicts if necessary.


## CONTACT INFO.

> eCloudValley Cloud Developer Intern </br>
> **Hugo ChunHo Lin**
> 
> <aside>
>   📩 E-mail: <a href="mailto:hugo970217@gmail.com">hugo970217@gmail.com</a>
> <br>
>   🧳 Linkedin: <a href="https://www.linkedin.com/in/1chooo/">Hugo ChunHo Lin</a>
> <br>
>   👨🏻‍💻 GitHub: <a href="https://github.com/1chooo">1chooo</a>
>    
> </aside>


## License
Released under [MIT](./LICENSE) by [Hugo ChunHo Lin](https://github.com/1chooo).

This software can be modified and reused without restriction.
The original license must be included with any copies of this software.
If a significant portion of the source code is used, please provide a link back to this repository.
