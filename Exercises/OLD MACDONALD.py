# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    new_string = ""
    i=0
    for letter in name:
        if i == 0 or i == 3:
            new_string += letter.capitalize()
        else:
            new_string += letter
        i +=1
    return new_string

# Check
print(old_macdonald('macdonald'))