# deklarasi variable cars dengan nilai 100
cars = 100

# deklarasi variable space_in_a_car dengan nilai float 4.0
space_in_a_car = 4.0

# deklarasi variable drivers dengan nilai 30
drivers = 30

# deklarasi variable passengers dengan nilai 90
passengers = 90

# deklarasi variable cars_not_driven
# dengan hasil operasi pengurangan jumlah mobil dengan jumlah pengemudi
cars_not_driven = cars - drivers

# deklarasi variable cars_driven
# dengan nilai jumlah pengemudi
cars_driven = drivers

# deklarasi carpool_capacity
# dengan nilai perkalian jumlah mobil yang dikendarai dengan kapasitas mobil
carpool_capacity = cars_driven * space_in_a_car

# deklarasi variable average_passengers_per_car
# dengan nilai passengers
average_passengers_per_car = passengers

print("There are", cars, "cars available.")
print("There are only", drivers,"drivers available.")
print("There will be", cars_not_driven,"empty cars today.")
print("We can transport", carpool_capacity,"people today.")
print("We have", passengers,"to carpool today.")
print("we need to put about", average_passengers_per_car,"in each car.")
