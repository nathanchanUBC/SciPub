SKYLIGHT = [
    "Stewart, J",
    "Birol, G",
    "Code, W",
    "Davy, E",
    "Elouazizi, N",
    "Goedhart, C",
    "Jeffery, E",
    "Koenig, S",
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
    "Kremen, C",
    "Oberg, G"
]
MSLAB = [
    "Blakney, A",
    "Leslie, S",
    "Miller, F",
    "Todesco, M",
    "Fox, J"
]
EOAS = [
    "Gilley, B",
    "Harris, S",
    "Ivannochko, T",
    "d'Arcy, M",
    "Lukes, L",
    "Pete, S",
    "White, R"
]
STAT = [
    "Dunham, B",
    "Timbers, T",
    "Yu, E",
    "Heckman, N",
    "Lee, M",
    "Ostblom, J",
    "Pleiss, G"
]
MATH = [
    "Leung, F",
    "Liu, K",
    "MacLean, M",
    "Piccolo, C",
    "Yeager, E",
    "Cytrynbaum, E",
    "Loewen, P",
    "Williams, T"
]
CPSC = [
    "Acton, D",
    "Allen, M",
    "Belleville, P",
    "Knorr, E",
    "Wolfman, S", 
    "Conati, C",
    "Leyton-Brown, K",
    "MacLean, K",
    "McGrenere, J",
    "Ng, R",
    "Poole, D",
    "Pottinger, R",
    "Baniassad, E",
    "Bowman, W",
    "Heeren, C",
    "Oluwakemi, O",
    "Margo, S",
    "Toti, G",
    "Yoon, D"
]
ZOOL = [
    "Kalas, P",
    "Aviles, L",
    "Pennell, M",
    "Ramer, M",
    "Redfield, R",
    "Schulte, P",
    "Srivastava, D",
    "Steinwand, B"
]
PHAS = [
    "Bates, S",
    "Charbonneau, A",
    "Ives, J",
    "Rieger, G",
    "Milner, V",
    "Reinsberg, S",
    "Stamp, P",
    "Man, Allison",
    "McIver, J"
]
MICB = [
    "Oliver, D",
    "Hallam, S"
]
CHEM = [
    "Addison, C",
    "Bussiere, G",
    "Monga, V",
    "Rodriguez-Nunez, J",
    "Stoodley, R",
    "Wickenden, J",
    "Dake, G",
    "Hein, J",
    "Borduas-Dedekind, N"
]
BOTA = [
    "Chowrira, G",
    "Zeiler, K",
    "Tseng, M",
    "Clarkston, B",
    "Michaletz, S"
]

def isUBC(name):
    return (name in SKYLIGHT or name in IRES or name in MSLAB or name in EOAS or name in STAT or name in MATH or name in ZOOL or name in PHAS or name in MICB or name in CHEM or name in BOTA)

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
    if name in ZOOL:
        return 'Zoology'
    if name in PHAS:
        return 'Physics and Astronomy'
    if name in MICB:
        return 'Microbiology'
    if name in CHEM:
        return 'Chemistry'
    if name in BOTA:
        return 'Botany'
    else:
        return 'Other/Non-UBC'
    
def standard_name(fullname):
    i = fullname.find(' ')
    if i == -1:
        return fullname
    else:
        return fullname[:i+2]