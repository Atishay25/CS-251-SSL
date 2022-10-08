package Q1;

import java.util.Map.Entry;
import java.util.*; 
import java.util.regex.*;

public class Graph {

    // Assume maximum path length to be less than INF
    private static Integer INF = 1000*1000*1000 ;
    private Map<String, Node> nodeMap = new HashMap<>() ;
    
    public void addNode(String name) {
        /*
         * Implement this method
         */
        Node newNode = new Node(name);
        nodeMap.put(name, newNode);
    }

    public void addDirectedEdge(String nameA, String nameB, Integer distance) {
        /*
         * Implement this method
         * Check if nodes with nameA and nameB exist.
         */
        Boolean A_exists = false;
        Boolean B_exists = false;
        for(Map.Entry<String, Node> entry : nodeMap.entrySet()){        // Checking if nameA and nameB Nodes exist
            if(A_exists && B_exists) break;
            if(entry.getKey().equals(nameA)) A_exists = true;
            else if(entry.getKey().equals(nameB)) B_exists = true; 
        }
        if(!(A_exists && B_exists)) return;            
        nodeMap.get(nameA).addNeighbour(nodeMap.get(nameB), distance);
    }

    public Map<String, Integer> dijkstraAlgorithm(String source) {
        /*
         * Implement this method
         * Return a map of name of all the nodes
         * with the minimum distance from source node
         */
        Map<String, Integer> dist = new HashMap<>();        // Map to store shortest distances
        Map<String, Boolean> visited = new HashMap<>();     // Map to store visiting status of a Node

        for(Map.Entry<String, Node> entry : nodeMap.entrySet()){
            if(entry.getKey().equals(source)){
                dist.put(source, 0);            // shortest distance from a node to itself i zero 
            }
            else dist.put(entry.getKey(), INF);
            visited.put(entry.getKey(), false);
        }

        PriorityQueue<String> pQueue = new PriorityQueue<String>();     // Using predefined Pririty queue
        pQueue.add(nodeMap.get(source).getName());                                                     

        while(pQueue.size() != 0){
            String next = pQueue.remove();
            visited.put(next, true);
            for(Map.Entry<Node, Integer> entry : nodeMap.get(next).adjacentNodes.entrySet()){
                if(dist.get(entry.getKey().getName()) > dist.get(next) + entry.getValue()){     
                    dist.put(entry.getKey().getName(), dist.get(next) + entry.getValue());  
                    pQueue.add(entry.getKey().getName());
                }
            }
        }
        return dist;
    }
}