package Q2 ;

import java.net.*;
import java.util.Scanner;
import java.io.*;

public class Client {  

    private ServerSocket server = null;
    private Socket socket1 = null; 
    private Socket socket2 = null;
    //private BufferedReader in = null;
    //private PrintWriter out = null;
    private DataInputStream in = null;
    private DataOutputStream out = null;
    private Integer ID = null;
    private Board board = null ;
    private Scanner sc = new Scanner(System.in);


    /*
     * server socket allows this player to accept connection from other player
     * socket1 is the accepted connection from server socket
     * socket2 is the socket that connects to the server of the other player
     * NOTE: Socket(HOST, port) throws ConnectException if no server is listening on port
     *       handle this while creating socket2
     *       Since server.accept is blocking, so order in which sockets are initialised must be considered appropriately.
     */


    /*
     * Add any variables you need
     */

    private void printResult(int winner, int ID) {
        /*
         * Don't change this function
         */
        if(winner == 0) {
            System.out.println("DRAW") ;
        } 
        else if(winner == ID) {
            System.out.println("YOU WON") ;
        }
        else System.out.println("YOU LOSE") ;
    }

    private Integer[] takeInput(){
        /*
         * Take input from the user from STDIN and return the position as an array
         * 
         */
        System.out.print("Enter the position: ");

        /* take x and y as space separated integer*/
        int x = sc.nextInt();
        int y = sc.nextInt();
        if(!board.available(x, y)){
            System.out.println("INVALID INPUT! Enter again");
            return takeInput();
        }
        else {
            Integer[] pos = new Integer[2];
            pos[0] = x;
            pos[1] = y;
            return pos;
        }

        /* check if the x and y position is valid and available on the board [x,y in {0,1,2}X{0,1,2}]
         * if not valid or not available, print "INVALID INPUT! Enter again" (without quotes) and ask for input again
        */
        
    }
    private void sendMove(Integer[] pos){
        /*
         * Send the move to other player by writing to the appropriate socket
         * sent string format: "x y" (space separated)
         */
        String move = Integer.toString(pos[0]) + " " + Integer.toString(pos[1]);
        try {
            out.writeUTF(move);  
        } catch (IOException e) {
            // handle exception
            e.printStackTrace();
        }       
    }

    private Integer[] recieveMove(){
        /*
         * Recieve the move from the server by reading from the appropriate socket
         * return the move as an array of two integers
         * recieve format: "x y" (space separated)
         */
        Integer[] received = new Integer[2];
        try{
            String str = in.readUTF();
            String[] s = str.split(" ");
            received[0] = Integer.valueOf(s[0]);
            received[1] = Integer.valueOf(s[1]);
            return received;
        }
        catch(IOException e){
            e.printStackTrace();
        }
        return received;

    }
    public Client(Integer ID, Integer port1, Integer port2){
        /*
        * port1 is the port on which server is running and 
        * this player will accept connection from other player
        * 
        * port2 is the port on which the server of the other player is running
        */     

        /*
        * Initialize ID
        * Also initialize the board
        */
        this.ID = ID;
        this.board = new Board();
        try{
            /*
            * INITIALIZE THE ServerSocket 
            */
            server = new ServerSocket(port1);
            System.out.println("Server started");
            System.out.println("Waiting for a client ...");
            /* Don't chnage above print statements */
            while(true){
                try{
                    socket2 = new Socket("localhost",port2);
                    socket1 = server.accept();
                    break;
                }
                catch(IOException e){
                    continue;
                }
            }
            in = new DataInputStream(socket1.getInputStream());
            out = new DataOutputStream(socket2.getOutputStream());
            /*
            * INITIALIZE both socket variables, one that connects to other player and other accepting connection on server socket
            * NOTE: Socket(HOST, port) throws java.net.ConnectException if no server is listening on port
            * this happens when the other player is not yet ready to play i.e. has not started the server

            * handle this by trying to create the socket conneting to other player again and again in a loop until it is created
            * incase of exception just continue the loop
            *
            /*
             * initialize the input and output streams appropriately
             */

        }
        catch(IOException e){
            e.printStackTrace();
        }
    }

    public void runClient () {
        Boolean myturn = ID==1;
        int result;
        board.printBoard();
        while(true) {
                /*
                * Here we would have the game logic
                * You can use the functions defined above
                * NOTE: for player with ID 1, it is your turn initially
                *       for player with ID 2, it is the other player's turn initially
                * We have implemented the game using a logic which utilizes myturn bool. You are welcome to try any other logic.
                */

            if(myturn) {
                /* your turn */
                Integer[] input = takeInput();
                board.updateBoard(input, ID);
                sendMove(input);

            }
            else {
                /* other player's turn */
                Integer[] receive = recieveMove();
                if(ID == 1) board.updateBoard(receive, 2);
                else board.updateBoard(receive, 1);

            }
            myturn = !myturn;

            result = board.checkBoard();
            if(result != -1) break;

        }
        printResult(result, ID);
    }

    public static void main(String args[]) {
        /*
         * Don't change this function
         */
        Integer ID = Integer.parseInt(args[0]) ;
        System.out.println(ID);
        if(ID != 1 && ID != 2) {
            System.out.println("Incorrect Player ID\n");
            return ;
        }
        Integer port1 = Integer.parseInt(args[1]) ;
        Integer port2 = Integer.parseInt(args[2]) ;
        try {
            Client client = new Client(ID, port1, port2) ;
            client.runClient() ;
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
