import re
def normalize_phone(phone_number):
    # видаляємо все, окрім цифр і +
    normalized_number = re.sub(r'\D', '', phone_number)
    # якщо номер без міжнародного коду, - додаємо його
    if not normalized_number.startswith("+"):
        if normalized_number.startswith("380"):
            normalized_number = "+" + normalized_number
        else:
            normalized_number = "+38" + normalized_number
    return normalized_number

# приклад

phone1 = "    +38(050)123-32-34"
phone2 = "     0503451234"
phone3 = "(050)8889900"
phone4 = "38050-111-22-22"
phone5 = "38050 111 22 11   "

print(normalize_phone(phone1)) 
print(normalize_phone(phone2))
print(normalize_phone(phone3))
print(normalize_phone(phone4))
print(normalize_phone(phone5))

