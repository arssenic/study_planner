def calculate_phase_ranges(days):
    foundation_end = max(2, days // 3)
    deep_dive_end = (2 * days) // 3

    return {
        "foundation_start": 1,
        "foundation_end": foundation_end,
        "deep_dive_start": foundation_end + 1,
        "deep_dive_end": deep_dive_end,
        "practice_start": deep_dive_end + 1,
        "practice_end": days
    }


def calculate_total_hours(days, hours_per_day):
    return days * hours_per_day