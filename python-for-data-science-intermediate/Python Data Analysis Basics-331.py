## 1. Reading the MoMA Dataset ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below

for row in moma:
    
    date = row[6]
    
    if date != "":
        date = int(date)
        row[6] = date
        

## 2. Calculating Artist Ages ##

ages = []

for row in moma:
    
    date = row[6]
    birth = row[3]
    
    if type(birth) == int:
        age = date - birth
    else:
        age = 0
        
    ages.append(age)
    
#print(ages)
    
final_ages = []

for age in ages:
    
    if age >= 20:
        final_ages.append(age)
    else:
        final_ages.append('Unknown')

#print(final_ages)

## 3. Converting Ages to Decades ##

# The final_ages variable is available
# from the previous screen

decades = []

for age in final_ages:
    
    if type(age) == int:
        decade = str(age)
        decades.append(decade[:-1] + '0s')
    else:
        decades.append(age)

        
print(decades)

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen

decade_frequency = {}

for age in decades:
    
    if age not in decade_frequency:
        decade_frequency[age] = 1
    else:
        decade_frequency[age] += 1

## 5. Inserting Variables into Strings ##

artist = "Pablo Picasso"
birth_year = 1881



template = "{artist}'s birth year is {birth_year}"
output = template.format(artist=artist, birth_year=birth_year)
print(output)

## 6. Creating an Artist Frequency Table ##

artist_freq = {}

for row in moma:
    
    artist = row[1]
    
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else:
        artist_freq[artist] += 1

## 7. Creating an Artist Summary Function ##

def artist_summary(artist_name: str):
    
    num_artworks = artist_freq[artist_name]
    
    template = "There are {num_artworks} artworks by {artist_name} in the dataset"
    print(template.format(num_artworks=num_artworks, artist_name=artist_name))
    
artist_summary("Henri Matisse")

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

template = 'The population of {country} is {pop:,.2f} million'

for country in pop_millions:
    print(template.format(country = country[0], pop = country[1]))
    

## 9. Challenge: Summarizing Artwork Gender Data ##

freq_table = {}

for row in moma:
    Gender = row[5]
    
    if Gender not in freq_table:
        freq_table[Gender] = 1
    else:
        freq_table[Gender] += 1
        
for gender, count in freq_table.items():
    template = 'There are {num:,} artworks by {sex} artists'
    print(template.format(num = count, sex = gender))