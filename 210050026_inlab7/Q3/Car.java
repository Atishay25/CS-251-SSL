package Q3 ;

/*
 * Create class Car along with proper methods and inheritance as required
 */

public class Car extends Vehicle {

    // Constructor
    Car (String regNo, String manufacturer, String owner){
        super(regNo, manufacturer, owner);
        this.CO2 = -1;
        this.CO = -1;
        this.HC = -1;
    }

    // Function to check pollution status of a Car
    String checkPollutionStatus(){
        if(CO2 == -1 && CO == -1 && HC == -1){
            pollutionStatus = "PENDING";
        }
        if(CO2 >= 0){
            if(CO2 <= 15 && CO <= 0.5 && HC <= 750){
                pollutionStatus = "PASS";
            }
            else{
                pollutionStatus = "FAIL";
            }
        }

        return pollutionStatus;
    }
}