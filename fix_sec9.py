with open('build_landing.py', 'r', encoding='utf-8') as f:
    code = f.read()

target = "Es un pago único de tan solo $7 USD sin cobros recurrentes ni membresías. Tras el pago, recibes tus accesos al correo al instante."
replacement = "El pago se realiza mediante Hotmart, la plataforma líder de productos digitales, con cifrado SSL de 256 bits. Se procesa como pago único (sin suscripciones ni cobros recurrentes) y el acceso a los materiales queda habilitado de forma inmediata y de por vida tras completar la compra."

if target in code:
    code = code.replace(target, replacement)
    with open('build_landing.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Replaced in build_landing.py successfully!")
else:
    print("Target string not found in build_landing.py")
