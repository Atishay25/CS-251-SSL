package Q3;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.*;  

public class PollutionCheck {
    public static void main(String [] args) throws Exception {

        // Text files for vehicles, pollution, query data
        File v = new File(args[0]);
        File p = new File(args[1]);
        File q = new File(args[2]);

        // Vector of Car and Truck Objects
        Vector<Car> cars = new Vector<Car>();
        Vector<Truck> trucks = new Vector<Truck>();

        // Reading data from Files using BufferedReader
        BufferedReader vehicles = new BufferedReader(new FileReader(v));
        BufferedReader pollution = new BufferedReader(new FileReader(p));
        BufferedReader queries = new BufferedReader(new FileReader(q));

        String v_str, q_str, p_str;     // String to process text files

        // Creating Car and Truck objects if they are found in vehicles list
        while ((v_str = vehicles.readLine()) != null){
            String[] vehicleData = v_str.split(", ");
            if(vehicleData[3].equals("Car")){
                Car newCar = new Car(vehicleData[0],vehicleData[1],vehicleData[2]);
                cars.addElement(newCar);
            }
            else if(vehicleData[3].equals("Truck")){
                Truck newtruck = new Truck(vehicleData[0],vehicleData[1],vehicleData[2]);
                trucks.addElement(newtruck);
            }
        }
        
        // Update Pollution Parameters of Cars and Trucks
        // if they are present in pollution list
        while ((p_str = pollution.readLine()) != null){
            String[] pollutionData = p_str.split(", ");
            for(int i = 0; i < cars.size(); i++){
                if(pollutionData[0].equals(cars.elementAt(i).getRegNo())){
                    double CO2 =  Double.valueOf(pollutionData[1]);
                    double CO =  Double.valueOf(pollutionData[2]);
                    double HC =  Double.valueOf(pollutionData[3]);
                    cars.elementAt(i).updatePollution(CO2, CO, HC);
                }
            }
            for(int i = 0; i < trucks.size(); i++){
                if(pollutionData[0].equals(trucks.elementAt(i).getRegNo())){
                    double CO2 =  Double.valueOf(pollutionData[1]);
                    double CO =  Double.valueOf(pollutionData[2]);
                    double HC =  Double.valueOf(pollutionData[3]);
                    trucks.elementAt(i).updatePollution(CO2, CO, HC);
                }
            }
        }
        
        // Process Queries from queries file
        while ((q_str = queries.readLine()) != null){
            String query;
            query = q_str;
            boolean registered = false;    // Variable to check registration of a Vehicle
            for(int i = 0; i < cars.size(); i++){
                if(cars.elementAt(i).getRegNo().equals(query)){
                    registered = true;
                    System.out.println(cars.elementAt(i).checkPollutionStatus());
                }
            }
            for(int i = 0; i < trucks.size(); i++){
                if(trucks.elementAt(i).getRegNo().equals(query)){
                    registered = true;
                    System.out.println(trucks.elementAt(i).checkPollutionStatus());
                }
            }
            if(!registered){
                System.out.println("NOT REGISTERED");
            }
        }

        vehicles.close();
        queries.close();
        pollution.close();

    }
}