package Q3;

/*
 * Create class Vehicle along with given attributes and methods 
 */

public class Vehicle {

    protected String regNo;             // Registration ID
    protected String manufacturer;      // Manufacturer
    protected String owner;             // Owner of vehicle
    protected double CO2;               // Content of CO2 emitted
    protected double CO;                // Content of CO emitted
    protected double HC;                // Content of HC emitted
    protected String pollutionStatus;   // Pollution status of vehicle

    // Constructor
    Vehicle (String regNo, String manufacturer, String owner){
        this.regNo = regNo;
        this.manufacturer = manufacturer;
        this.owner = owner;
        pollutionStatus = "PENDING";
    }
    
    // Function to check pollution status of a Vehicle
    String checkPollutionStatus(){
        return pollutionStatus;
    }

    // Update the pollution parameters of a Vehicle
    void updatePollution(double CO2, double CO, double HC){
        this.CO2 = CO2;
        this.CO = CO;
        this.HC = HC;
    }

    // get Registration ID of a vehicle
    String getRegNo(){
        return regNo;
    }

    public String toString(){
        String str;
        String Manufac = "Manufacturer: " + manufacturer + '\n';
        String Reg = "Reg No: " + regNo + '\n';
        String Own = "Owner: " + owner + '\n';
        String PollStatus = "Pollution Status: " + pollutionStatus;
        str = Reg + Manufac + Own + PollStatus;
        return str;
    }

}