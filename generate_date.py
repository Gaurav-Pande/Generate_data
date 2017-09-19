import random 
from datetime import datetime, timedelta
import csv

def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())),)

if __name__ == '__main__':
	print random_date(datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p'), datetime.strptime('Jun 30 2005  1:33PM', '%b %d %Y %I:%M%p'))
