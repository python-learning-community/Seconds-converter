##this program coverts a given seconds to hour(s),minute(s)

def from_secs():
    the_secs = int(input('Enter the total seconds :'))
    
    to_hour = int(the_secs/3600)
    
    the_mins = the_secs - (to_hour*3600)
    to_mins = int(the_mins/60)
    
    to_secs = the_secs - (to_hour*3600) - (to_mins*60)
    
    print('The total hour is ',to_hour)
    print('The total minutes is ',to_mins)
    print('The total seconds is ',to_secs)
from_secs()
input('Press the <ENTER> key to exit')
