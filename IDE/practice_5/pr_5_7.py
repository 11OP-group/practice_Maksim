compartment = (seat_number - 1) // 4
SEATS_PER_COMPARTMENT = 4


def get_compartment_number(seat_number):
    if seat_number < 1:
        raise ValueError("Номер места должен быть больше 0")
    return (seat_number - 1) // SEATS_PER_COMPARTMENT + 1


seat = int(input("Введите номер места в вагоне: "))
compartment = get_compartment_number(seat)

print(f"Место №{seat} находится в купе №{compartment}")
