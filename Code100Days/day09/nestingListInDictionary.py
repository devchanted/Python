# Nesting Dictionary in a Dictionary


travel_log = {
    "USA" : ["San Francisco", "Las Vegas", "Los Angeles"],
    "UAE" : ["Dubai", "Qatar", "Abudhabi"]
}

print(travel_log)
print(travel_log["USA"])

#nested list

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

#Nested Dictionary 

travel_blog = {

    "USA" : {
        "total_visits": 4,
        "cities_visited": ["San Francisco", "Las Vegas", "Los Angeles"]
    },

    "UAE" : {
        
        "cities_visited": ["Dubai", "Qatar", "Abudhabi"],
        "total_visits" : 1
    },
}

print(travel_blog["UAE"]["cities_visited"][2])