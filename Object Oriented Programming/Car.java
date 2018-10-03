// Child class of automobile

public class Car extends Automobile{

    // Some car specific properties
    private String color;
    private String model;

    public Car(){
        super();
    }

    public Car(String _name, String _model, String _color){
        super(_name, 4);
        this.model = _model;
        this.color = _color;
    }


    // some getter functions
    public String getColor(){
        return this.color;
    } 
    public String getModel(){
        return this.model;
    }

    // overwrites the normal drive function from automobile
    public void drive(){
        System.out.println("The car drives normally down the road");
    }

    public String toString(){
        return "A car is a type of automobile!";
    }


}