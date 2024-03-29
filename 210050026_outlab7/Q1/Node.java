package Q1;

import java.util.HashMap;
import java.util.Map;

public class Node {
    private String name;
    
    public Map<Node, Integer> adjacentNodes = new HashMap<>();
 
    public Node(String name) {
        /*
         * Implement this constructor
         */
        this.name = name;
    }

    public String getName() {
        /*
         * Implement this method
         * Return name of the node
         */
        return name;
    }

    public void addNeighbour(Node node, int distance) {
        /*
         * Implement this method
         */
        adjacentNodes.put(node, distance);
    }
}
