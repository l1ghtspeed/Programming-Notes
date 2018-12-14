/*
Problem Description:

Write an algorithm to generate all possible permutations of a given string with the following traits:

Any letter 'i' can change to '1', any letter 'e' can change to '3' and any 'a' can change to '@'.

Also, if the first character of the string is a character and is lowercase, you can capitalize it.

Problem is part of a CSI (Data Structures and Algorithms) assignment for a password cracker.

*/

// A helper function to generate all the possible permutations based on the rulings
public static ArrayList<String> generatePermutations(String initial){
    ArrayList<String> set = new ArrayList<>();
    Queue<String[]> que = new LinkedList<String[]>();
    set.add(initial);

    // Que initial population
    que.add(new String[]{initial, "0"});
    if (Character.isLetter(initial.charAt(0)) && !Character.isUpperCase(initial.charAt(0))){
        que.add(new String[]{Character.toUpperCase(initial.charAt(0))+initial.substring(1), "1"});
        set.add(Character.toUpperCase(initial.charAt(0))+initial.substring(1));
    }

    // Follows breadth first search algorithm structure
    while(!que.isEmpty()){
        String[] node = que.poll();
        int pos = Integer.parseInt(node[1]);
        if (pos < node[0].length()){ 
            char currentChar = node[0].charAt(pos);
            if (currentChar == 'a' || currentChar == 'A'){
                que.add(new String[]{node[0].substring(0, pos) + "@" + node[0].substring(pos+1), Integer.toString(pos+1)});
                set.add(node[0].substring(0, pos) + "@" + node[0].substring(pos+1));
            } else if (currentChar == 'e' || currentChar == 'E'){
                que.add(new String[]{node[0].substring(0, pos) + "3" + node[0].substring(pos+1), Integer.toString(pos+1)});
                set.add(node[0].substring(0, pos) + "3" + node[0].substring(pos+1));
            } else if (currentChar == 'i' || currentChar == 'I'){
                que.add(new String[]{node[0].substring(0, pos) + "1" + node[0].substring(pos+1), Integer.toString(pos+1)});
                set.add(node[0].substring(0, pos) + "1" + node[0].substring(pos+1));
            }
            que.add(new String[]{node[0], Integer.toString(pos+1)});
        }
    }
    return set;
}
    