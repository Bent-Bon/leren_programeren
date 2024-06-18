import sys, os
from test_lib import test, report
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import data

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from data import JOURNEY_IN_DAYS

if JOURNEY_IN_DAYS == 11:
    print("correct")


if __name__ == "__main__":
    report()