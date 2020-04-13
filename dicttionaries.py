#Dictionaries are special structure in python that allows to store information which are called as key value pairs
month_conversion = {
    "Jan" : "January", #Jan is the key and January is the value - Key has to be unique
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"

}
print(month_conversion["Dec"])
print(month_conversion.get("Mak", "Invalid Entry"))