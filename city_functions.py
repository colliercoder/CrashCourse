def city_description(city,country,population = ''):
    if population:
        city_descrip = city + ', ' + country + ' - population ' + str(population)
    else:
        city_descrip = city + ', ' + country
    return city_descrip.title()

