dagen = {
    'maandag': 'werkdagen',
    'dinsdag': 'werkdagen',
    'woensdag': 'werkdagen',
    'donderdag': 'werkdagen',
    'vrijdag': 'werkdagen',
    'zaterdag': 'weekend',
    'zondag': 'weekend'
}

print("de hele week:")
print("")
for dag in dagen.items():
    print(f"{dag}")

print("")
#dag_type zijn de werkdagen of de weekend delen
print("alle werkdagen:")
print("")
for dag, dag_type in dagen.items():
    if dag_type == 'werkdagen':
        print(f"werkdag: {dag}")

print("")

print("alle weekend delen:")
print("")
for dag, dag_type in dagen.items():
    if dag_type == 'weekend':
        print(f"weekend: {dag}")

print("")

#reversed draai het om
print("werkdagen omgekeerd:")
print("")
for dag, dag_type in reversed(dagen.items()):
    if dag_type == 'werkdagen':
        print(f"werkdag: {dag}")

print("")

print("weekend omgekeerd:")
print("")
for dag, dag_type in reversed(dagen.items()):
    if dag_type == 'weekend':
        print(f"weekend: {dag}")

print("")

print("de hele week omgekeerd:")
print("")
for dag in reversed(dagen.items()):
    print(f"{dag}")