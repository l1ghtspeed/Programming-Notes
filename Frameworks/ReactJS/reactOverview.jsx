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

/*

Components can render other components! Even components from a different source file.
As long as the variables you want to use are exported from the other source file, you can import them over.

*/

import { HeaderBar } from '../../Examples/reactapp/HeaderFile.jsx';
//imports footerbar class and pageNumber variable to use
import { FooterBar, pageNumber } from '../../Examples/reactapp/FooterFile.jsx';

class MainSite extends React.Component {
    render(){
        return (
            <div>
                <HeaderBar />
                <FooterBar />
            </div>
        )
    }
}

ReactDOM.render(<MainSite />, document.getElementById('app'));

/*

Props:

We've now goten to the second thing that makes React special. 
'props' is an object used to pass information between components.
'this.props' contains a bunch of information about the component.

Props can be used in many ways - you can pass functions through props such as event handlers.
You can view all the child elements of a component instance.
You can set default props if nothing else if passed in (useful for user inputs).

Pretend Button.js exists

import React from 'react';

class Button extends React.Component{
    render(){
        return <button onClick={this.props.onClick}>Sign Up</button>
    }
}

Pretend Form.js exists

import React from 'react';
import { Button } from './Button.js'

class Form extends React.Component
*/

class Login extends React.Component {
    render(){
        return <h1>My name is {this.props.info.name}, and my passcode is {this.props.info.passcode}</h1>
    }
}

ReactDOM.render(
    <Login info={{name: 'Bob Joe', passcode: 'bobIsAwesome123'}}/>, 
    document.getElementById('app')
);


class Button extends React.component {



}