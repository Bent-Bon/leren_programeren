import random

def get_random_compliment(naam: str) -> str:
    
    comps = ("je bent super ", "je doet geweldig ", "niemand is zoals jij ")
    return(random.choice(comps) + naam)

print(get_random_compliment ("harm"))