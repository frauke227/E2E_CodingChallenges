# Wash your hands!

#import humanfriendly
import math


def wash_hands(N, nM):
    # N = number of times a person washes their hands per day
    # nM = number of month they follow this routine
    # It takes 21 seconds to wash your hands. A month is considered to have 30 days.
    totalSeconds = N * 21 * nM * 30
    minutes = math.floor(totalSeconds/60)
    seconds = totalSeconds - minutes * 60
    return(f'{minutes} minutes and {seconds} seconds')


print(wash_hands(7, 9))
