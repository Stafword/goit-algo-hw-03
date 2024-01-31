import re


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


def normalize_phone(phone_number):
    cleaned_number = re.sub(r"\D", "", phone_number)

    if cleaned_number.startswith("+"):
        if len(cleaned_number) == 12 and cleaned_number[1:4] != "38":
            cleaned_number = "+38" + cleaned_number[1:]
    else:
        cleaned_number = "+38" + cleaned_number
    return cleaned_number


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормализовані номери телефонів для SMS-розсилки:", sanitized_numbers)
