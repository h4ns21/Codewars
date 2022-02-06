# First method

def are_you_playing_banjo(name):
    return name + ' plays banjo' if name[0] == 'R' or name[0] == 'r' else name + ' does not play banjo'  

# Second method

def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";
