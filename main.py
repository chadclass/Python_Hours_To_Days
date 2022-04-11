calculation_to_hours = 24
measurement_of_time = "Hours"


def days_to_hours(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_hours} {measurement_of_time}")
    print(custom_message)


def scope_check():
    print(measurement_of_time)
    print(num_of_days)


scope_check()


days_to_hours(20, "Good Work!")


