/*

OK Now we get to some meatier and more meaningful features of React
What's required: decent understanding of JSX, Javascript, ES6, HTML, CSS 

*/


/*

Components:

A React component is essentially a chunk of reuseable code. 
Think of the views you would have to build for a social media app - many different screens will require the same menu bar at the bottom.
It would be much more convenient to just slide the same component in, instead of copy pasting it again.

Components are also super nice because they allow you to easily insert JS logic into them.
No longer will you have to have annoying script tags or have switch back between the script.js.

*/

import React from 'react';
import ReactDOM from 'react-dom';

class Automobile extends React.Component{
    changePerson(person){
        person='Steve';
    }

    render(){
        let person = 'Bob';
        const car = {
            name: person=='Bob' ? 'BMW M4' : 'Mercedes E class',
            type: person=='Bob' ? 'Coupe' : 'Sedan',
            url: person=='Bob' ? '../src/bmw.png' : '../src/mercedes.png'
        }
        return (
            <div>
                <h1>
                    I have the {car.name} {car.type} as my car.
                </h1>
                <img onClick={this.changePerson(person)} src={car.url} alt={car.name}/>
            </div>
        );
    }
}

ReactDOM.render(<Automobile/>, document.getElementById('app'));