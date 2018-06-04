/* 

ES6, or EMCAScript6, is a (somewhat recent) huge update on the Javascript language. 
This new standard provides plenty of powerful and useful features, but also depricates some old ones.
Proficiency in the new ES6 features is a must for any JS developers, whether it be for front end or back end.
Below are some of the more important ES6 features, along with examples.
For a full list on all the changes, visit this page: http://es6-features.org/#Constants

*/


/*

Arrow Functions:

General syntax: function_name = (function parameters) => {};
Is basically a shorthand form for normal function notation, but binds 'this' differently.

*/

let generic_arrow_func = (a, b) => { return a+b };

let simple_arrow_func = a => a + 2;

let num = 4;

console.log(simple_arrow_func(4));


/*

Class:

Javascript now has "classes" - hooray! 
Javascript is still not a lanugage with an object oriented programming model, but now it has syntactic sugar that makes it look like one.
This topic is a rather lengthy one, so for everything you need to know about "class" in JS, visit https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes  

*/

class Snack {

    constructor(name, brand) {
        this.name = name;
        this.brand = brand;
    }

    static definition(){
        console.log("Snacks are fun to eat!");
    }

    eat() {
        console.log(this.name + ' by ' + this.brand + ' is fun to eat!');
    }

}

class Chocolate extends Snack {

    constructor(name, brand) {
        super(name, brand);
    }

    static definition(){
        console.log("Chocolates are sweet!");
    }

    eat() {
        console.log(this.name + ' by ' + this.brand + ' is awesome chocolate');
    }

}

let kitkat = new Chocolate('Kitkat', 'Nestle');

kitkat.eat();
Chocolate.definition();


/*

String Interpolation:

Ever struggled with multiline strings? Or including javascript inside strings?
Say no more.

*/

let some_string = 'And can have embedded JS!'

let this_is_awesome = `This string

    is multi

    lined!

    ${some_string}

    How awesome is that?
`;

console.log(this_is_awesome);


/*

Default:

Default function parameter values. Why didn't JS have this before?

*/

let get_area = (height, width=10) => {return height*width};


/*

*/