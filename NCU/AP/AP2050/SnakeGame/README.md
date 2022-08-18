# Snake Gmae

This is the project that build a little python game -> "Snake Game" through the package "pygame". 

However, when we want to do this project, we will face a lot of problems when we build the python enviroment. Therefore, we have tested a lot of times, then we choose "anaconda" to build. So, here is the steps.

## Create enviroment

Build the enviroment through anaconda (Actually, I use miniconda in my mac, but it's still the same steps.)

my Conda --version: conda 4.12.0

* ### First steps: 

    Build a virtual enviroment which called pygameand install python 3.6.13 version. Then activate it...
<br>

    ```vim
    $ conda create --name pygame python=3.6.13
    $ conda activate pygame
    ```

* ### Second steps: Install pygame

    ```vim
    $ python3 -m pip install -U pygame --user
    ```

    If omitting `--user`. The package gets installed into the conda environment.

* ### Third steps: Test pygame
    ```vim
    $ python3 -m pygame.examples.aliens
    ```

* ### Well done.


## Run Snake Game

```vim
$ python main.py
```