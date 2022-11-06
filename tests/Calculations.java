import java.util.*;

public class Calculations {

    /** Risk value */
    public static int riskValue;

    /** Seizures had while consumed alcohol average during week */
    public static int averageConsumed;

    /** Seizures had while sleeping poorly average during week */
    public static int averageAmountProject;

    /** Seizures had while stress average during week */
    public static int averageStress;

    /** Seizures had while not medicated average during week */
    public static int averageMedication;

    /** Seizures had while men cycle average during week */
    public static int averageCurrent;

    /** Seizures had while during week */
    public static boolean Seizures;

    public static void main(String[] args) {
        
    }
    public static void sleep(int amount){
        if (amount > 3) {
            riskValue = riskValue + 1;
        }
    }
    public static void alchohol(int amount){
        if (amount > 3) {
            riskValue = riskValue + 1;
        }
    }

    public static void stress(int level){
        if (level > 3) {
            riskValue = riskValue + 1;
        }
    }

    public static void medication(boolean val) {
        if (val == false) {
            riskValue = riskValue + 1;
        }
    }

    public static void men(boolean current){
        if (current  == true) {
            riskValue = riskValue + 1;
        }
    }

}