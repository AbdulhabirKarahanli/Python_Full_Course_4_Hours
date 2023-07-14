print("Hello Habir, keep it up!")

# We have keys that associated with certain values. When we call keys, Python gives the values.
Month_Conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(Month_Conversions["Nov"])
print(Month_Conversions["Jan"])

print(Month_Conversions.get("Dec"))

print(Month_Conversions.get("Luv"))  # None
print(Month_Conversions.get("Luv", "Not a valid key"))

# Example

my_mac = {
    "brand": "Apple",
    "model": "Macbook Pro",
    "year": "2020",
    "ram": "16",
    "SSD": "512 GB",
    "sec_size": "13 inch",
    "keyboard": "magic keyboard",
    "processor": "intel i5"
}

print(my_mac.get("year"))