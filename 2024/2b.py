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
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if isSafeReport(modified_report):
                safe_count += 1
                break
    return safe_count
file_path = "2.in"
safe_reports = countSafeReports(file_path)
print(safe_reports)
