"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """

    list =[number,number+1,number+2]

    return list


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    new_list=[]

    for i in rounds_1:
        new_list.append(i)
    for i in rounds_2:
        new_list.append(i)
        

    return new_list


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    for i in rounds:
        if i==number:
            return True
    return False
    


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """

    total=0
    for i in hand:
        total+=i

    average=total/len(hand)
    return average


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """
    first=hand[0]
    last=hand[len(hand)-1]
    
    mid = hand[int((len(hand) / 2 + 0.5) - 1)]
    approx=(first+last)/2

    if card_average(hand) == approx or card_average(hand)==mid:
        return True
    else:
        return False

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """
    sum_even=0
    sum_odd=0
    odd_count=0
    even_count=0
    
    for i in range(len(hand)):
        if i%2==0:
            sum_even+=hand[i]
            even_count+=1
            
        else:
            sum_odd+=hand[i]
            odd_count+=1
            
    average_even=sum_even/even_count
    average_odd=sum_odd/odd_count
    
    if average_even==average_odd:
        return True
    else:
        return False
 
           


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """
    last=len(hand)-1
    if hand[last]==11:
        hand[last]=22
    
    return hand
