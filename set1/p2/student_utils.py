# Name: Mark Neilson Tol
# Section: IV-BSIT C
# Activity: P2 - Custom Module
# Date: November 16, 2026

def compute_average(grades):
    return sum(grades) / len(grades)


def get_status(average):
    if average >= 75:
        return "PASSED"
    return "FAILED"


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)