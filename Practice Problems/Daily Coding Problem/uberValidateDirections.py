'''

Problem:

This problem was asked by Uber.

A rule looks like this:

A NE B

This means this means point A is located northeast of point B.

A SW C

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.

A NW B
A N B
is considered valid.

'''

'''

My Approach:

My approach is to create a grid type system using a dictionary where everytime a new node is called it's coordinates are either updated or checked for validity.

E.G.

A NE B

Then the dictionary will look like:

{
    A: (0, 0),
    B: (1, 1)
}

If two nodes that are called already exist, we can use math to figure out if it is correctly in position. 

''' 

# Solution is given in Java, copied out from online 
class Solution {
  public static void main(String[] args) {
    test1();
    test2();
    test3();
  }

  private static void test1() {
    String[] rules = {"A N B",
                      "C SE B",
                      "C N A"};
    System.out.println(validate(rules));
  }

  private static void test2() {
    String[] rules = {"A NW B",
                      "A N B"};
    System.out.println(validate(rules));
  }

  private static void test3() {
    String[] rules = {"A N B",
                      "C N B"};
    System.out.println(validate(rules));
  }

  static class Node {
    List<Set<Node>> edges = new ArrayList<>();
    char val;
    public Node(char val) {
      this.val = val;
      for (int i = 0; i < 4; i++)
        edges.add(new HashSet<>());
    }
  }

  public static final int N = 0;
  public static final int E = 1;
  public static final int S = 2;
  public static final int W = 3;
  public static final int[] DIRS = {N, E, S, W};
  public static final Map<Character, Integer> charToDir = new HashMap<>();;
  static {
    charToDir.put('N', N);
    charToDir.put('E', E);
    charToDir.put('S', S);
    charToDir.put('W', W);
  }

  public static boolean validate(String[] rules) {
    Map<Character, Node> map = new HashMap<>();

    for (String line : rules) {
      String[] rule = line.split(" ");
      System.out.println("Rule " + rule[0] + " " + rule[1] + " " + rule[2]);
      char fromVal = rule[2].charAt(0);
      char toVal = rule[0].charAt(0);

      if (!map.containsKey(fromVal)) {
        Node n = new Node(fromVal);
        map.put(fromVal, n);
      }

      if (!map.containsKey(toVal)) {
        Node n = new Node(toVal);
        map.put(toVal, n);
      }

      Node from = map.get(fromVal);
      Node to = map.get(toVal);

      /* Decompose diagonal (two-char) directions to single directions */
      for (char dirChar : rule[1].toCharArray()) {
        int dir = charToDir.get(dirChar);
        if (!isValid(map, from, to, dir))
          return false;
        addEdges(map, from, to, dir);
        System.out.println(from.edges.get(dir));
         System.out.println(to.edges.get(opposite(dir)));
      }

    }

    return true;
  }

  private static int opposite(int dir) {
    return (dir + 2) % 4;
  }

  private static boolean isValid(Map<Character, Node> map,
                                 Node from,
                                 Node to,
                                 int newDir) {
    int oppositeDir = opposite(newDir);
    if (from.edges.get(oppositeDir).contains(to))
          return false;

    return true;
  }

  private static void addEdges(Map<Character, Node> map,
                                  Node from,
                                  Node to,
                                  int newDir) {
    /* Get the direct opposite direction, e.g. S from N */
    int oppositeDir = opposite(newDir);

    /* Add the immediate edge between the nodes, using bi-directional edges. */
    from.edges.get(newDir).add(to);
    to.edges.get(oppositeDir).add(from);

    for (int dir : DIRS) {
      /* Relationships in the same direction are ambiguous.
         For example, if A is north of B, and we are adding 
         C north of B, we cannot say C is north of A. */
      if (dir == newDir)
        continue;

      for (Node neighbor : from.edges.get(dir)) {
        /* No need to add self-edges */
        if (neighbor == to)
          continue;
        /* Add bi-directional edges */
        neighbor.edges.get(newDir).add(to);
        to.edges.get(oppositeDir).add(neighbor);
      }
    }
  }
}