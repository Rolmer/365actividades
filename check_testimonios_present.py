with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

terms = [
    "Experiencias y opiniones",
    "Únete a personas de todo el mundo",
    "Y obtén 365 Actividades para transformar",
    "testimonios",
    "Reemplazar por testimonio real"
]

for t in terms:
    print(f"Term '{t}': {t in content}")
