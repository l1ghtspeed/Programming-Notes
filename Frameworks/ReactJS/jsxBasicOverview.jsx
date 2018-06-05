/* 

JSX is a pivotal part of React. It is a syntax extension - meaning it is not actual Javascript, but it can get compiled down to Javascript. 

It looks very similar to HTML, so when you see HTML-like elements in a React project, you'll know its JSX. Take a look at the code below.  

The 'const header' and ';' is normal JS but everything between the header tags is JSX. 
One complete JSX statement (including the tags) is known as a JSX element. 

*/

const header = <h1>This h1 element is JSX!</h1>;

/* 

JSX elements can be used in any way other Javascript data types can be used. 
E.g. Passed to a function, be part of an array.

*/

let list_Of_Superheros = [
    <li>Ironman</li>, 
    <li>Captain America</li>, 
    <li>Hulk</li>,
    <li>Thor</li>
];


/*

JSX elements, just like HTML, can have attributes. 
The attribute for 'class' in HTML is 'className' in JSX. 
This is because 'class' is already a reserved keyword in Javascript!

*/

var list_Of_Villains = [
    <li className="Marvel">Thanos</li>, 
    <li className="Marvel">Ultron</li>, 
    <li className="DC">Joker</li>,
    <li className="DC">Darkseid</li>
];


/*

Also like HTML elements, JSX elements can be nested. 
However, unless you write everything on one line, you must use brackets around them.
Another thing - there can only be one highest layer JSX element. 
It's an easy problem to avoid, just wrap the multiple highest layer elements in a div.

E.g. This won't compile properly:

let foo = (
    <h1>bar</h1>
    <h1>bar</h1>
);

The example below will work though, since both <a> elements are wrapped inside a parent div

*/

let image_links = (
    <div>
        <a href="http://zigao.io">
            <img src="./zigao_logo.png"/>
        </a>
        <a href="http://github.com">
            <img src="./github_logo.png"/>
        </a>
    </div>
);


/* 

You can insert normal Javascript into JSX, but it must be done within a set of curly brackets {}.
They are commonly used to modify the content of a JSX element or an attribute of a JSX element.

*/

let favourite_movie = {
    name: 'Avengers Infinity War',
    link: 'https://www.imdb.com/title/tt4154756/'
}

let movie_and_review = <a href={favourite_movie.link}>My favourite movie is: {favourite_movie.name}</a>;



/* 

Event listeners can be added as attributes to JSX elements.
For a full list of supported events visit this link: https://reactjs.org/docs/events.html#supported-events

*/

var hero_image_path = '../src/ironman.png';
var changePicture = () => {hero_image_path = '../src/batman.png'};

let super_hero_image = <img 

    onClick={changePicture()}
    src={hero_image_path}

/>;



/*

We can use conditionals along with JSX, but we cannot inject 'if/else' statements directly into the JSX elements.
You can either use the ternary and '&&' statements inside the JSX element, or resort to putting the if/else statement outside.

*/

let today_is_monday = false;
let have_coffee = true;

let day;

if (today_is_monday){
    day = 'today is a horrible day';
} else {
    day = 'today is a great day';
}

let good_or_bad_day = <p>

    {day}, {have_coffee ? 'but I will be productive' : 'and I will not be productive'}
    
</p>;




/*

JSX gets rendered to a webpage via the 'render()' method from the ReactDOM library. 
Remember to install the correct dependencies using npm install.

The render() method takes in two parameters - the JSX element, and an actual HTML element from the html file you are serving.

The render() is one reason that makes React so special - it only updates the DOM elements that are changed, instead of the whole page.
This makes the process a lot faster. I encourage you to read through this article https://www.codecademy.com/articles/react-virtual-dom 

*/

import React from 'react';
import ReactDOM from 'react-dom';

ReactDOM.render(<h1>Some Heros and Villains</h1>, document.getElementById("header"));
ReactDOM.render(<h3>Heros: {list_Of_Superheros}</h3>, document.getElementById("hero-container"));
ReactDOM.render(<h3>Villains: {list_Of_Villains}</h3>, document.getElementById("villain-container"));
ReactDOM.render(super_hero_image, document.getElementById("links"));






