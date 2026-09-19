public class Lasagna {
    private static final int EXPECTED_MIN=40;
    private static final int MIN_PER_LAYERS=2;
    
    public int expectedMinutesInOven(){
        return EXPECTED_MIN;
    }
    public int remainingMinutesInOven(int minutes){
        return expectedMinutesInOven()-minutes;
    }
    public int preparationTimeInMinutes(int numberOfLayers){
        return MIN_PER_LAYERS* numberOfLayers;
    }
    public int totalTimeInMinutes(int nbLayers,int minOven){
        return preparationTimeInMinutes(nbLayers)+minOven;
    }
}
