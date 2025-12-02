import string 
strip = string.whitespace
harmful_ingredients= [
    "Talc with asbestos risk",
    " Lead ",
    " Mercury",
    "Arsenic ",
    " 1 4 Dioxane ",
    "Toluene ",
    " Formaldehyde",
    "Dibutyl phthalate ",
    "Synthetic fragrances ",
    " Triclosan",
    " Phthalates ",
    "Sodium lauryl sulfate ",
    " Sodium laureth sulfate ",
    "DMDM hydantoin ",
    "Quaternium 15 ",
    " Ammonia",
    " Resorcinol",
    " Parabens  ",
    "Mineral oil ",
    "Hydroquinone ",
    "Denatured alcohol ",
    " Isopropyl alcohol",
    " Oxybenzone",
    " Octinoxate ",
    "BHT ",
    "BHA ",
    "Carbon black ",
    " Siloxanes ",
    "PEG compounds ",
    "Petrolatum "
]
alch=string.ascii_lowercase +string.digits

lst = []

for i in harmful_ingredients:
    i=i.strip().lower()
    chem=''.join([char for char in i if char in alch])
    lst.append(chem)
print(lst)



    