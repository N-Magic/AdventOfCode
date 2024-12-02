import sys
def isSafeReport(report):
    increasing = None
    for i in range(1, len(report)):
        diff = report[i] - report[i-1]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if increasing is None:
            if diff > 0:
                increasing = True
            elif diff < 0:
                increasing = False
        elif increasing and diff < 0:
            return False
        elif not increasing and diff > 0:
            return False
    return True
def countSafeReports(file_path):
    with open(file_path, 'r') as f:
        data = f.read().strip()
    reports = [list(map(int, line.split())) for line in data.splitlines()]
    safe_count = 0
    for report in reports:
        if isSafeReport(report):
            safe_count += 1
    return safe_count
file_path = sys.argv[1]
safe_reports = countSafeReports(file_path)
print(safe_reports)
