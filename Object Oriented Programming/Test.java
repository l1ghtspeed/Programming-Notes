public class Test {
    public static void main(String args[]){
        Automobile randomAuto = new Automobile();
        Car civic = new Car("Honda Civic 2010", "Sedan", "blue");
        System.out.println(randomAuto);
        System.out.println(civic.getColor());
    }
}