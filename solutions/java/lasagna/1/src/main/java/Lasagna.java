public class Lasagna {
    // TODO: define the 'expectedMinutesInOven()' method
    public int expectedMinutesInOven(){
        return 40;
    }
    // TODO: define the 'remainingMinutesInOven()' method
    public int remainingMinutesInOven(int minutes){
        return expectedMinutesInOven()-minutes;
    }
    // TODO: define the 'preparationTimeInMinutes()' method
    public int preparationTimeInMinutes(int numberOfLayers){
        return 2* numberOfLayers;
    }
    // TODO: define the 'totalTimeInMinutes()' method
    public int totalTimeInMinutes(int nbLayers,int minOven){
        return preparationTimeInMinutes(nbLayers)+minOven;
    }
}
