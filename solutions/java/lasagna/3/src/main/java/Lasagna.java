public class Lasagna {
    private static final int EXPECTED_MIN=40;
    private static final int MIN_PER_LAYERS=2;
    
    // TODO: define the 'expectedMinutesInOven()' method
    public int expectedMinutesInOven(){
        return EXPECTED_MIN;
    }
    // TODO: define the 'remainingMinutesInOven()' method
    public int remainingMinutesInOven(int minutes){
        return expectedMinutesInOven()-minutes;
    }
    // TODO: define the 'preparationTimeInMinutes()' method
    public int preparationTimeInMinutes(int numberOfLayers){
        return MIN_PER_LAYERS* numberOfLayers;
    }
    // TODO: define the 'totalTimeInMinutes()' method
    public int totalTimeInMinutes(int nbLayers,int minOven){
        return preparationTimeInMinutes(nbLayers)+minOven;
    }
}
