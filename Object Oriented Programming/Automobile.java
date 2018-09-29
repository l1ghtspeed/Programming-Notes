// This is the super class - automobile

public class Automobile {

    // public static and final means no instance is required to use or access, and subclass cannot override these values, accessible anywhere
    public static final Boolean hasWheels = true;
    public static final Boolean hasEngine = true;

    // private is automobile class only
    private int numberOfChildClasses = 2;

    // protected is automobile and any of its child classes
    protected String name;
    protected int numWheels;

    // complex overloaded constructor
    public Automobile(String _name, int _numWheels){
        this.name = _name;
        this.numWheels = _numWheels;
    }

    // simple constructor
    public Automobile(){
        this.name = "no name given";
        this.numWheels = 0;
    }


    // To String function, overwriting the base Object toString method from Java. 
    public String toString() {
        return "An automobile is the parent class of many different child classes!";
    }


    // final function, child class cannot overwrite
    public final String getName(){
        return this.name;
    }


    // Static functions to be overwritten
    public static String about(){
        return "Automobiles were first invented in the year (some year)";
    }


    // Static function not to be overwritten
    public static final String defineEngine(){
        return "Engine is something that makes the automobile move";
    }


    // A general drive function, to be overwritten by child classes
    public void drive(){
        System.out.println("The automobile drives down the road");
    }

    public int getNumberOfChildClasses(){
        return this.numberOfChildClasses;
    }
}


