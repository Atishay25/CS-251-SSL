package Q3 ;

/*
 * Create class Truck along with proper methods and inheritance as required
 */

public class Truck extends Vehicle {
    
    // Constructor
    Truck (String regNo, String manufacturer, String owner){
        super(regNo, manufacturer, owner);
        this.CO2 = -1;
        this.CO = -1;
        this.HC = -1;
    }

    // Function to check pollution status of a Truck
    String checkPollutionStatus(){
        if(CO2 == -1 && CO == -1 && HC == -1){
            pollutionStatus = "PENDING";
        }
        if(CO2 >= 0){
            if(CO2 <= 25 && CO <= 0.8 && HC <= 1000){
                pollutionStatus = "PASS";
            }
            else{
                pollutionStatus = "FAIL";
            }
        }

        return pollutionStatus;
    }
}