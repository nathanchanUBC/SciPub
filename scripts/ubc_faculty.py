from unidecode import unidecode
SKYLIGHT = [
    "Stewart, J",
    "Birol, G",
    "Code, W",
    "Davy, E",
    "Elouazizi, N",
    "Goedhart, C",
    "Jandciu, E",
    "Jeffery, E",
    "Koenig, S",
    "Milner-Bolotin, M",
    "Zohreh, M",
    "Paton, K",
    "Ruosi, A",
    "Schroeder, A",
    "Sherman, S",
    "Welsh, A",
    "Wong, J"
]
IRES = [
    "Boyd, D",
    "Gantois, J",
    "Giang, A",
    "Johnson, M",
    "Kremen, C",
    "Oberg, G",
    "Öberg, G",
    "Reid, A",
    "Zhao, J"
]
MSLAB = [
    "Blakney, A",
    "Leslie, S",
    "Miller, F",
    "Todesco, M",
    "Fox, J"
]
EOAS = [
    "Groat, L",
    "Gilley, B",
    "Harris, S",
    "Heagy, L",
    "Ivannochko, T",
    "d'Arcy, M",
    "Lukes, L",
    "Pete, S",
    "Schoof, C",
    "Sutherland, S",
    "White, R",
    "Caruthers, A",
    "Gilley, B",
    "Johnson, C",
    "Schoof, C",
    "Oldenburg, D",
    "Steyn, D",
    "Turner, D",
    "Eberhardt, E",
    "Olsen, E",
    "Pakhomov, E",
    "Andrews, G",
    "Dipple, G",
    "Finnis, J",
    "Mortensen, J",
    "Scoates, J",
    "Chan, K",
    "Hickey, K",
    "Orians, K",
    "Russell, K",
    "Kennedy, L",
    "Bevier, M",
    "Bevier, M",
    "Bostock, M",
    "Jellinek, M",
    "Johnson, M",
    "Kopylova, M",
    "Lipsen, M",
    "Maldonado, M",
    "Maldonado, M",
    "Smit, M",
    "Austin, P",
    "Smith, P",
    "Beckie, R",
    "Francois, R",
    "Pawlowicz, R",
    "Stull, R",
    "Allen, S",
    "Harris, S",
    "Hollingshead, S",
    "McDougall, S",
    "Mills, S",
    "Sutherland, S",
    "Dzikowski, T",
    "Ivanochko, T",
    "Mayer, U",
    "Burt, W",
    "Hsieh, W",
    "Holland, T",
    "Sherman, S",
    "Kennedy, B",
    "Lane, E",
    "Jones, F",
    "Caulkins, J"
]
STAT = [
    "Dunham, B",
    "Timbers, T",
    "Yu, E",
    "Heckman, N",
    "Lee, M",
    "Ostblom, J",
    "Pleiss, G",
    "Chang, B",
    "Dunham, B",
    "Yu, E",
    "Nolde, N",
    "Lim, Y",
    "Yapa, G"
]
MATH = [
    "Leung, F",
    "Liu, K",
    "MacLean, M",
    "Piccolo, C",
    "Yeager, E",
    "Cytrynbaum, E",
    "Loewen, P",
    "Williams, T",
    "Merchant, S",
    "Rechnitzer, A",
    "Walls, P",
    "Liang, R",
    "Lindsay, A",
    "Raghoonundun, A",
    "Zaman, A",
    "de Oliveira, G",
    "Karimfazli, I",
    "Robson, L",
    "Raggi, M",
    "Willoughby, M",
    "Bell, P",
    "Schwarz, R",
    "Kapoor, V",
    "Thompson, W",
    "Chau, A",
    "Peirce, A",
    "Rechnitzer, A",
    "Homsy, B",
    "Marcus, B",
    "Wetton, B",
    "Piccolo, C",
    "Schoetzau, D",
    "Cytrynbaum, E",
    "S. Leung, F",
    "Slade, G",
    "Bryan, J",
    "Gordon, J",
    "MacDonald, J",
    "Doebeli, M",
    "MacLean, M",
    "Ward, M",
    "Yilmaz, O",
    "Loewen, P",
    "Anstee, R",
    "Froese, R",
    "Gupta, R",
    "Gustafson, S",
    "Ramdorai, S",
    "van Willigenburg, S",
    "Kim, Y",
    "Reichstein, Z",
    "Lo, J",
    "Garaschuk, K",
    "Yurasovskaya, K",
    "Ottaway, P",
    "Merchant, S"
]
CPSC = [
    "Acton, D",
    "Allen, M",
    "Belleville, P",
    "Knorr, E",
    "Wolfman, S", 
    "Conati, C",
    "Holmes, R",
    "Kiczales, G",
    "Leyton-Brown, K",
    "MacLean, K",
    "McGrenere, J",
    "Mochetti, K",
    "Ng, R",
    "Poole, D",
    "Pottinger, R",
    "Seltzer, M",
    "Baniassad, E",
    "Bowman, W",
    "Heeren, C",
    "Ola, O",
    "Margo, S",
    "Toti, G",
    "Yoon, D",
    "Hutter, F",
    "K. Pong, T",
    "Knoll, B",
    "Schneider, O",
    "Southey, T",
    "Condon, A",
    "Conati, C",
    "Acton, D",
    "Lowe, D",
    "Knorr, E",
    "Wohlstadter, E",
    "Carenini, G",
    "Kiczales, G",
    "Murphy, G",
    "Tsiknis, G",
    "Hoos, H",
    "Mitchell, I",
    "Little, J",
    "McGrenere, J",
    "Leyton-Brown, K",
    "Maclean, K",
    "Voll, K",
    "Allen, M",
    "Friedlander, M",
    "Hutchinson, N",
    "Carter, P",
    "Ng, R",
    "Pottinger, R",
    "Woodham, R",
    "Wolfman, S",
    "Tew, A",
    "Yu, B",
    "Dawson, J",
    "Golbeck, R",
    "Lister, R"
]
BIOL = [
    "Berger, J",
    "Kalas, P",
    "Aviles, L",
    "Pennell, M",
    "Ramer, M",
    "Redfield, R",
    "Schulte, P",
    "Srivastava, D",
    "Steinwand, B",
    "Chowrira, G",
    "Klenz, J",
    "Zeiler, K",
    "Tseng, M",
    "Clarkston, B",
    "Michaletz, S",
    "Lacombe, A",
    "O’Neill, A",
    "Milsom, B",
    "Berezowsky, C",
    "Altshuler, D",
    "Moerman, D",
    "Srivastava, D",
    "Hammill, E",
    "Bole, G",
    "Bradfield, G",
    "Haughn, G",
    "Spiegelman, G",
    "Klenz, J",
    "Richards, J",
    "Whitton, J",
    "Lee, J",
    "Nomme, K",
    "Berbee, M",
    "Hawkes, M",
    "O’Connor, M",
    "Kalas, P",
    "Matthews, P",
    "Schulte, P",
    "Jetter, R",
    "Maurus, R",
    "Turkington, R",
    "Young, R",
    "Chowrira, S",
    "Ellis, S",
    "Graham, S",
    "Beatty, T",
    "Auld, V",
    "Goodey, W",
    "Tetzlaff, W",
    "Zhang, Y",
    "Clarkston, B",
    "Taylor, J",
    "McDonnell, L",
    "Weir, L",
    "Banet, M",
    "Barker, M",
    "Hansen, M",
    "Schimpf, N",
    "Smith, K",
    "Hallam, S"
]
MICB = [
    "Bingle, W",
    "Graves, M",
    "Kion, T",
    "Oliver, D",
    "Gaynor, E",
    "Hallam, S",
    "Harder, K",
    "Johnson, P",
    "Mohn, W",
]
PHAS = [
    "Bates, S",
    "Bonn, D",
    "Charbonneau, A",
    "Ives, J",
    "Rieger, G",
    "Haber, E",
    "Milner, V",
    "Reinsberg, S",
    "Stamp, P",
    "Man, A",
    "McIver, J",
    "Wieman, C",
    "Gendre, M",
    "Holmes, N",
    "Vernstrom, T",
    "Boley, A",
    "Kotlicki, A",
    "Mackay, A",
    "McCutcheon, B",
    "Heiner, C",
    "Wieman, C",
    "Bonn, D",
    "Bryman, D",
    "Jones, D",
    "Witt, D",
    "Koster, E",
    "Bates, F",
    "Rieger, G",
    "Affleck, I",
    "Stairs, I",
    "Charbonneau, J",
    "Folk, J",
    "Heyl, J",
    "Iqbal, J",
    "Ives, J",
    "Karczmarek, J",
    "McKenna, J",
    "Roettler, J",
    "Young, J",
    "Zibin, J",
    "Madison, K",
    "Schleich, K",
    "Deslauriers, L",
    "Van Waerbeke, L",
    "Hasinoff, M",
    "Tovar, M",
    "Van Raamsdonk, M",
    "Burke, S",
    "Matticon, T",
    "Hinkov, V",
    "Sossi, V",
    "Stang, J",
    "Strubbe, L",
    "Heiner, C",
    "Roll, I",
    "Carolan, J",
    "Day, J",
    "Deslauriers, L",
    "Newbury, P"
]
CHEM = [
    "Addison, C",
    "Algar, W",
    "Bussiere, G",
    "Monga, V",
    "Rodriguez-Nunez, J",
    "Stoodley, R",
    "Wickenden, J",
    "Dake, G",
    "Hein, J",
    "Borduas-Dedekind, N",
    "Lekhi, A",
    "Rogers, C",
    "Bizzotto, D",
    "Bussiere, G",
    "Dake, G",
    "Bates, J",
    "Love, J",
    "Rodriguez Nunez, J",
    "Stewart, J",
    "Schafer, L",
    "Algar, R",
    "Stoodley, R",
    "Nussbaum, S",
    "Kunz, T",
    "Monga, V",
    "Duis, J",
    "Maxwell, E",
    "Knox, K"
]

def isUBC(name):
    return (name in SKYLIGHT 
            or name in IRES
            or name in MSLAB 
            or name in EOAS 
            or name in STAT 
            or name in MATH 
            or name in CPSC 
            or name in BIOL
            or name in MICB
            or name in PHAS 
            or name in CHEM) 

def get_faculty(name):
    if name in SKYLIGHT:
        return 'Skylight'
    if name in IRES:
        return 'Institute for Resources, Environment, and Sustainability'
    if name in MSLAB:
        return 'Michael Smith Labs'
    if name in EOAS:
        return 'Earth, Ocean and Atmospheric Sciences'
    if name in STAT:
        return 'Statistics'
    if name in MATH:
        return 'Mathematics'
    if name in CPSC:
        return 'Computer Science'
    if name in BIOL:
        return 'Biology'
    if name in MICB:
        return 'Microbiology and Immunology'
    if name in PHAS:
        return 'Physics and Astronomy'
    if name in CHEM:
        return 'Chemistry'
    else:
        return 'Other/Non-UBC'
    
def standard_name(fullname):
    fullname = removeAccents(fullname)
    i = fullname.find(' ')
    if i == -1:
        return fullname
    else:
        return standardize(fullname[:i+2])
    
standardizedNames = {
    "Rodriguez N": "Rodriguez Nunez, J",
    "De B": "De Bruijn, R",
    "El K": "El Khoury, E",
    "Del C": "Del Campo, M",
    "Le Magueres, P": "Le Magueres, P",
    "von O": "von Oppen, J",
    "De A": "De Andrade, E",
    "St J": "St John, K",
    "Ururay F": "Ururay Fragoso Araujo, T",
    "Domingos C": "Domingos Correia Santos, C",
    "van d": "van der Hoeven Kraft, K",
    "De C": "De Croon, R",
    "De L": "De Laet, T",
}

def standardize(name):
    if name in standardizedNames.keys():
        return standardizedNames[name]
    else: return name

def removeAccents(names):
    return unidecode(names)

def groupOther(dict):
    other_count = 0
    for title, count in dict.items():
        if count == 1:
            other_count+=1
    dict["Other"] = other_count
    new_dict = {}
    for title, count in (dict.items()):  
        if count != 1 or title == "Other":
            new_dict[title] = count
    return new_dict

def otherDict(dict):
    new_dict = {}
    for title, count in dict.items():
        if count == 1:
            new_dict[title] = count
    return new_dict