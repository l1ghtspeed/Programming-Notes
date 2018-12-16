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

Async, Await, Promises:

Promises are a huge upgrade/update to Javascript callbacks.
As you know, Javascript is asynchronous and non-blocking, meaning there is one main thread of execution, 
and it never stops to wait for some action to complete. 

*/


// Old callback way of handling things (with jQuery and AJAX as example)
let print_content = (data) => {
    //Put code in here that you want to execute after the request
    console.log(data);
};

let get_README_md = (callback) => {
    $.ajax({
        url: "https://raw.githubusercontent.com/ZGao28/Programming-Notes/master/README.md",
        success: callback(data)
    });
};

// New promises + async await way of handling things

const https = require('https');

let add_some_numbers = async (url) => {
    //await is used to wait for the get request to go through and come back
    let bounds = await get_nums(url);
    let sum = 0;
    for (let i = (bounds[0] < bounds[1] ? bounds[0] : bounds[1]); i < (bounds[0] < bounds[1] ? bounds[1] : bounds[0]); i++){
        sum+=i;
    }
    return sum;
}

let get_nums = (url) => {
    //A promise is an object.
    //After it gets resolved via the resolve function passed in, the promise gets returned to the await.
    return new Promise ((resolve, reject) =>
    { 
        https.get(url, (resp) => {
            let data = '';

            resp.on('data', (chunk) => {
                data += chunk;
            });
    
            resp.on('end', () => {
                resolve(data);
            });   
 
        }).on("error", (err) => {
            console.log("Error: " + err.message);
        });
    });
}



/* 

let and const:

let and const should be used in place of var!

const: can be declared and set once, and then cannot be changed again!
Any variable that you know will not be changed should be declared with const -> it's good practice because if you do accidentally change it then the app will crash

let can be reassigned but cannot be redeclared -> e.g. 

DOES NOT WORK
let apple = 5;
let apple = 5;

DOES WORK
let apple = 5;
apple = 6;

var would work in both examples.

let and const are function scoped like var, but they are both also BLOCK SCOPED -> 
meaning if you declare it inside a for loop or if statement, it will not be visible to the outside!



*/


let globalLet = 2; //This is global
var globalVar = 2; //This is also global

if (abc == 2){
    let ifStatementOnlyLet = 3; //This is only visible inside this if statement
    var stillGlobalVar = 4; //This is visible globally still! 
}

// this would work
console.log(stillGlobalVar);

// this would crash
console.log(ifStatementOnlyLet);



/* 

Destructuring:

Another neat trick offered by ES6, the last that we'll cover in this brief overview.
There are a lot of different ways you can use destructuring, I'll only be showing a couple.
For the full list, visit: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment

*/

let [coffee_crisp, aero, snickers, ...other_chocolates] = ["coffee crisp", "aero", "snickers bar", "kit kat", "Mr. Big", "Mars bar"];

console.log(other_chocolates); //Should print out array of last three chocolates

const pet = {

    type: 'dog',
    breed: 'husky',
    age: 2,
    name: 'Rufus'

}

//name and age values of pet are passed in as new variables!
//Constructor below is same as {name, age} = {pet.name, pet.age}
let print_pet_name = ({name, age} = pet) => {
    console.log(`${name} is ${age} years old!` );
}

