#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    n = len(predictions)

    errors = abs(net_worths - predictions)
    error_limit = sorted(errors, reverse=True)[n/10 - 1]

    for i in range(n):
        if errors[i] < error_limit:
            cleaned_data.append((ages[i], net_worths[i], errors[i]))

    return cleaned_data

