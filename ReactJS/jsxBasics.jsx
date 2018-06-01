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

*/

var list_Of_Villains = [
    <li class="Marvel">Thanos</li>, 
    <li class="Marvel">Ultron</li>, 
    <li class="DC">Joker</li>,
    <li class="DC">Darkseid</li>
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

JSX gets rendered to a webpage via the 'render()' method from the ReactDOM library. 
Remember to install the correct dependencies using npm install.

The render() method takes in two parameters - the JSX element, and an actual HTML element from the html file you are serving.

The render() is one reason that makes React so special - it only updates the DOM elements that are changed, instead of the whole page.
This makes the process a lot faster. I encourage you to read through this article https://www.codecademy.com/articles/react-virtual-dom 

*/

import React from 'react';
import ReactDOM from 'react-dom';

ReactDOM.render(<h1>Some Heros and Villains</h1>, document.getElementById("header"));
ReactDOM.render(list_Of_Superheros[0], document.getElementById("hero-container"));
ReactDOM.render(list_Of_Superheros[1], document.getElementById("hero-container"));
ReactDOM.render(list_Of_Villains[0], document.getElementById("villain-container"));
ReactDOM.render(image_links, document.getElementById("links"));




