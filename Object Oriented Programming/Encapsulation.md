# Encapsulation

Encapsulation is the first fundamental concepts of OOP we will be covering. Encapsulation is just the bundling of any number of methods (functions), and any amount of data. Bundled data and functions can be then declared to be visible to only within the bundle - this is also called **information hiding**.

It can sound kind of confusing with pure explaination, so let me give an example, with some sample Java code. 

Let's say we want to bundle together an object called a car. A car can do many things, and has many properties. For example, cars are able to drive. Cars are also able to roll up their windows. Cars also have many properties - we can consider this as the data we bundle.  


``` 

public class Car {

    //some bundled variables (data)
    private int number_of_wheels = 4;
    private int number_of_doors = 4;
    private boolean isElectric = false;
    private String color = "red";

    //constructor
    public Car(){

    }

    //this is a bundled method!
    public void drive(String direction){
        //some code here to move the car
    }


    //another bundled method
    private void roll_up_windows(){
        //some other code here
    }


}

```

If we bundled all that stuff together, we get something known in Object Oriented Programming as a **class**. In the example, the class is Car. You can think of classes as a mold, that creates an object with a defined set of properties and functions.

Ok so you may have noticed that in the sample code before all the functions and type declarations there is a 'private', or 'public' keyword. That's the scope declarator that basically states whether or not that function or variable can be accessed outside of the class. I won't go too in depth about it since it varies based on language.

Well that's encapsulation in a nutshell. It is basically just the bundling together of many different components into one thing. The full nuances of encapsulation go far beyond what I explained here but this is just a general definition.