months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date_input = input("Date: ").strip()

        if "/" in date_input:
            parts = date_input.split("/")
            if len(parts) == 3:
                month, day, year = parts
                try:
                    month = int(month)
                except:
                    continue
                day = int(day)
                year = int(year)
                if 0 <= year <= 10000 and 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
        elif "," in date_input:
            month_day, year = date_input.split(",")
            year = int(year.strip())
            month_name, day = month_day.strip().rsplit(" ", 1)
            try:
                day = int(day)
            except:
                continue
            month_name = month_name.lower().title()
            if month_name in months and 1 <= day <= 31:
                month = months.index(month_name) + 1
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break

    except (ValueError, EOFError, KeyboardInterrupt):
        break