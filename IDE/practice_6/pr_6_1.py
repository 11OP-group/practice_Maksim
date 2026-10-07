TEMP_MIN, TEMP_MAX = 36, 37
PRESSURE_MIN, PRESSURE_MAX = 110, 130
PULSE_MIN, PULSE_MAX = 60, 100

TEMP_LOW, TEMP_HIGH = 35, 38
PRESSURE_LOW, PRESSURE_HIGH = 105, 140
PULSE_LOW, PULSE_HIGH = 55, 110

CRITICAL_TEMP_LOW, CRITICAL_TEMP_HIGH = 35, 38
CRITICAL_PRESSURE_LOW, CRITICAL_PRESSURE_HIGH = 105, 140
CRITICAL_PULSE_LOW, CRITICAL_PULSE_HIGH = 55, 110

temperature = float(input("Температура (°C): "))
pressure = int(input("Давление (верхнее): "))
pulse = int(input("Пульс (уд/мин): "))

is_critical = (
    temperature < CRITICAL_TEMP_LOW or temperature > CRITICAL_TEMP_HIGH
    or pressure < CRITICAL_PRESSURE_LOW or pressure > CRITICAL_PRESSURE_HIGH
    or pulse < CRITICAL_PULSE_LOW or pulse > CRITICAL_PULSE_HIGH
)

is_normal = (
    TEMP_MIN <= temperature <= TEMP_MAX
    and PRESSURE_MIN <= pressure <= PRESSURE_MAX
    and PULSE_MIN <= pulse <= PULSE_MAX
)
if is_critical:
    print("Состояние: требуется врач")
elif is_normal:
    print("Состояние: норма")
else:
    print("Состояние: лёгкое недомогание")
