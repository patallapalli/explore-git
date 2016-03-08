#Liquid For Devs!

We don't need to add functionality in `src/`, that is the participants' job *(See the wiki* **"Liquid: How to"** *page)*.
**The main file is `liquid.cpp`.**

This is the directory structure:
```
└── liquid
    ├── liquid.cpp
    ├── testing.cpp
    ├── shunting-yard.cpp
    ├── shunting-yard.h
    ├── Makefile
    └── src
        ├── math-lib.h
        ├── ml_add.cpp
        ├── ml_div.cpp
        ├── ml_mul.cpp
        ├── ml_sub.cpp
        ├── .
        ├── .
        ├── .
        └── ml_*****.cpp
```

##How to `build` and `run`

On your terminal,
```sh
$ cd <path to "liquid">
$ make liquid
$ make test <or> ./liquid
```
In case you get errors in building, try
```sh
$ make again
```

`make liquid`compiles all the `src/ml_ * .cpp` files and links them to th `liquid.o` to make the executeable `liquid`.

##What needs to be done?
Currently, `liquid.cpp` is has a non-intuitive way of interaction. Since we are making a math expression solver, we should be able to input `infix` expressions.
@bamos built a nice implementation of the [Shunting-Yard Algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm) [here](/bamos/https://github.com/bamos/cpp-expression-parser/)
We need to change our `liquid.cpp` to utilise the power of `shunting-yard.cpp`.

* Get user expression from `stdin`.
* Compile the expression (using `calculator::compile()`)
* Evaluate the expression
    - by over-riding / modifying the `calculator::calculate(TokenQueue_t)` method.
    - the functions implemented by `src/ml_ * .cpp` would be invoked.
* Show output, wait for more expressions.

**That's not all!**
Checkout the [issues](/arrow-/explore-git/issues) for details on adding function calls, exotic operators.

***
***Comment on the issue to let everyone know you are working on this. Why should 14 people develop just 1 feature which can be developed by a far less number of people and there are numerous other things to work on.***
***
To work on this, you must understand the "Shuning Yard Algorithm" pretty well. The [wikipedia page has a lot of references](https://en.wikipedia.org/wiki/Shunting-yard_algorithm#External_links).
