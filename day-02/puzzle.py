"""
This function can replace two functions below and solve this the smarter way

def is_safe_report(levels):
    is_increasing = all(levels[i] < levels[i+1] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i+1] for i in range(len(levels) - 1))

    valid_differences = all(1 <= abs(levels[i+1] - levels[i]) <= 3 for i in range(len(levels) - 1))

    return (is_increasing or is_decreasing) and valid_differences
"""

def check_inc_dec(numbers):
    if (numbers == sorted(numbers, reverse=False) or
        numbers == sorted(numbers, reverse=True)):
        return True
    else:
        return False

def is_report_safe(numbers):
    unsafe_count = 0
    if check_inc_dec(numbers):
        for i in range(len(numbers) - 1):
            if (abs(numbers[i] - numbers[i + 1]) < 1 or
                abs(numbers[i] - numbers[i + 1]) > 3):
                unsafe_count += 1
        return True if unsafe_count == 0 else False
"""
This function can be improved like this, according to previous changes

def is_safe_with_dampener(levels):
    if is_safe_report(levels):
        return True
    
    for i in range(len(levels)):
        modified_report = levels[:i] + levels[i+1:]  # Remove the level at index i
        if is_safe_report(modified_report):
            return True
            
    return False
"""
def is_report_safe_if_tolerate_bad_level(numbers):
    safe_if_tolerate_count = 0
    for i in range(len(numbers)):
        removed_numbers = numbers.copy()
        rm_num = removed_numbers.pop(i)
        if is_report_safe(removed_numbers):
            safe_if_tolerate_count += 1
    return True if safe_if_tolerate_count > 0 else False


if __name__ == '__main__':
    with open("input.txt") as file:
        safe_count = 0
        tolerate_safe_count = 0
        for report in file:
            levels = list(map(int, report.split()))
            # First part
            if is_report_safe(levels):
                safe_count += 1
            # Second part
            elif is_report_safe_if_tolerate_bad_level(levels):
                tolerate_safe_count += 1
    """
    safe_reports_count = sum(is_safe_report(report) for report in reports)
    print(f"Number of safe reports: {safe_reports_count}")
    safe_reports_count = sum(is_safe_with_dampener(report) for report in reports)
    print(f"Number of safe reports with the Problem Dampener: {safe_reports_count}")
    """
    print(safe_count)
    print(tolerate_safe_count+safe_count)