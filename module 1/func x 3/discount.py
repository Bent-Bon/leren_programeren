list = [
    {"brand": "yamaha", "price": 2100, "month_discount_brands": 10},
    {"brand": "kymco", "price": 2300, "month_discount_brands": 10},
    {"brand": "vespa", "price": 1900, "month_discount_brands": 10},
    {"brand": "aprillia", "price": 2500, "month_discount_brands": 0},
    {"brand": "kawasaki", "price": 3100, "month_discount_brands": 0},
    {"brand": "suzuki", "price": 2700, "month_discount_brands": 0}
]

def calc_discount(brand):
    for item in list:
        if item["brand"] == brand and item["month_discount_brands"] == 10:
            prijs_korting = item["price"] / 100 * item["month_discount_brands"]
            return f"{brand} heeft een maand korting van €{prijs_korting}"
        elif item["brand"] == brand and item["month_discount_brands"] == 0:
            return "dit merk heeft geen maand korting"

    return "dit merk verkopen wij niet"

print(calc_discount("yamaha"))
print(calc_discount("aprillia"))
print(calc_discount("truimph"))