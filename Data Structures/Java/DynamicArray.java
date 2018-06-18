public class DynamicArray {

    private int[] arr; 

    public DynamicArray(int size) {
        this.arr = new int[size];
    }

    public void insert(int i, int value){
        if (i >= this.arr.length) {
            this.increase();
        }
        this.arr[i] = value;
    }
    
    public int getValue(int i){
        return this.arr[i];
    }

    private void increase(){
        int[] temp = this.arr;
        this.arr = new int[temp.length*2];
        for (int i = 0; i < temp.length; i++){
            this.arr[i] = temp[i];
        }
    }

}

