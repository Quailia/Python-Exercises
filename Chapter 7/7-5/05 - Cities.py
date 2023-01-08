#Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value.

def describe_city(city_name, country = "Japan"):
    print(f"The city of {city_name} is in {country}.")

#Call your function for three different cities, at least one of which is not in the default country.
describe_city("Tokyo")
describe_city("Kyoto")
describe_city("Vancouver", "Canada")