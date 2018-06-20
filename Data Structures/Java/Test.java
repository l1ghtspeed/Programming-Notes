public class Test {

    public static void main (String[] args){
        int dsetsize = 10;
        DisjointSet dset = new DisjointSet(dsetsize);
        for (int i = 0; i < dsetsize; i++){
            dset.MakeSet(i);
        }
        System.out.println(dset);
        dset.Union(2, 3);
        System.out.println(dset);
        dset.Union(2, 9);
        System.out.println(dset);
        dset.Union(5, 1);
        System.out.println(dset);
        dset.Union(5, 3);
        System.out.println(dset);
        System.out.println(dset.Find(5));
        System.out.println(dset);

    }
}