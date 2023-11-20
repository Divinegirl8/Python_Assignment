geo_political_zones = {
    "north_central": ["Benue", "FCT", "Kogi", "Kwara", "Nasarawa", "Niger", "Plateau"],
    "north_east": ["Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe"],
    "north_west": ["Kaduna", "Katsina", "Kano", "Kebbi", "Sokoto", "Jigawa", "Zamfara"],
    "south_east": ["Abia", "Anambra", "Ebonyi", "Enugu", "Imo"],
    "south_south": ["Akwa Ibom", "Bayelsa", "Cross River", "Delta", "Edo", "Rivers"],
    "south_west": ["Ekiti", "Lagos", "Osun", "Ondo", "Ogun", "Oyo"]

}


def get_geo_political_zones(value):
    for key, values in geo_political_zones.items():
        if value.lower() in map(str.lower, values):
            return key


print(get_geo_political_zones("oyo"))
