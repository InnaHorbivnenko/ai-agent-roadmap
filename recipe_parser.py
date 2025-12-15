#szuka liczby, szuka produkty, zapisuje wyniki

KNOWN_PRODUCTS = {
    "jajk": {
        "name": "jajka",
        "unit": "szt"
    },
    "mąk": {
        "name": "mąka",
        "unit": "g"
    },
    "mlek": {
        "name": "mleko",
        "unit": "l"
    },
    "cukr": {
        "name": "cukier",
        "unit": "g"
    },
    "masł": {
        "name": "masło",
        "unit": "g"
    }
}

recipe_text = """
Potrzebujemy 3 jajka, 200 g mąki oraz 0.5 l mleka.
Na koniec dodajemy 50 g cukru.
"""
import re

shopping_list = []

for root, data in KNOWN_PRODUCTS.items():

    #{product}\w* - szuka produktu z dowolnymi końcówkami, zaczynajacego sie od tego rdzenia
    pattern = rf"(\d+(\.\d+)?)\s*(g|l|szt)?\s*{root}\w*"
    match = re.search(pattern, recipe_text, re.IGNORECASE)

    if match:
        quantity = float(match.group(1))
        shopping_list.append({
            "name": data["name"],
            "quantity": quantity,
            "unit": data["unit"]
})

print("LISTA ZAKUPÓW:")
for item in shopping_list:
    print(f"- {item['name']}: {item['quantity']} {item['unit']}")

