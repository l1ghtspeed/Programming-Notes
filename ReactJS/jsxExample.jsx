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

