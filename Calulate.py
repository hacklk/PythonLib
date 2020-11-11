def population_density(population, land_area):
    """Calculate the population density of an area.

    population: int. The population of the area
    land_area: int or float. This function is unit-agnostic, if you pass
               in values in terms of square km or square miles the
               function will return a density in those units.
    """
    return population / land_area

 
def print_testcase(expected_value, actual_value):
    print("expected value: {}, actual value: {}".format(expected_value, actual_value))
    return_value = print_testcase(42, 42)
    
