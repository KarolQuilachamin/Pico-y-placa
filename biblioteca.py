#biblioteca

import datetime

def day(dt):
    day, month, year = (int(x) for x in dt.split('/'))
    ans = datetime.date(year, month, day)
    return ans.strftime("%A") 

def time(t):
    hour, minute = (int(x) for x in t.split(':'))
    h=hour+minute/60
    if (h>=7 and h<9.5)or(h>=16 and h<19.5):
        return True
    else:
        return False
    
def plate(p):
    p=list(p)
    return int(p[len(p)-1])
    
