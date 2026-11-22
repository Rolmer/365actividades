import json
import re

with open('clean_months.json', 'r', encoding='utf-8') as f:
    months_data = json.load(f)
for m in months_data:
    if m.get('image') and m['image'].startswith('/'):
        m['image'] = '.' + m['image']

with open('section_1.html', 'r', encoding='utf-8') as f:
    sec1 = f.read()

with open('section_2.html', 'r', encoding='utf-8') as f:
    sec2 = f.read()

with open('section_3.html', 'r', encoding='utf-8') as f:
    sec3 = f.read()

with open('section_4.html', 'r', encoding='utf-8') as f:
    sec4 = f.read()

with open('section_5.html', 'r', encoding='utf-8') as f:
    sec5 = f.read()

sec1 = sec1.replace('/__l5e/', './__l5e/').replace('/assets/', './assets/')
sec2 = sec2.replace('/__l5e/', './__l5e/').replace('/assets/', './assets/')
sec3 = sec3.replace('/__l5e/', './__l5e/').replace('/assets/', './assets/')
sec4 = sec4.replace('/__l5e/', './__l5e/').replace('/assets/', './assets/')
sec5 = sec5.replace('/__l5e/', './__l5e/').replace('/assets/', './assets/')

# Update sec1:
# 1) Top bar: "5 bonos de regalo" -> "4 bonos de regalo"
sec1 = sec1.replace('5 bonos de regalo', '4 bonos de regalo')
# 2) Mockup badge: "+5 bonos" -> "+4 bonos"
sec1 = sec1.replace('+5 bonos', '+4 bonos')

# 3) Replace button and price in Hero with indicator "Descubre todo lo que incluye"
hero_cta_pattern = r'<div class="mt-10 flex flex-col items-center gap-4 lg:items-start">.*?</ul></div>'
hero_replacement = '''<div class="mt-10 flex flex-col items-center gap-4 lg:items-start">
  <a href="#que-vas-a-obtener" class="inline-flex items-center justify-center gap-2.5 whitespace-nowrap rounded-full bg-primary/10 border-2 border-primary/30 font-display font-bold text-primary shadow-sticker transition-transform hover:-translate-y-0.5 hover:bg-primary/20 active:translate-y-0.5 h-14 px-8 text-lg sm:h-16 sm:px-10 sm:text-xl w-full max-w-md cursor-pointer">
    <span>Descubre todo lo que incluye</span>
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-arrow-down size-5 animate-bounce"><path d="M12 5v14"/><path d="m19 12-7 7-7-7"/></svg>
  </a>
  <ul class="flex flex-wrap justify-center gap-x-5 gap-y-2 text-sm font-bold text-muted-foreground lg:justify-start">
    <li class="flex items-center gap-1.5"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-download size-4 text-teal" aria-hidden="true"><path d="M12 15V3"></path><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><path d="m7 10 5 5 5-5"></path></svg> Acceso inmediato</li>
    <li class="flex items-center gap-1.5"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-printer size-4 text-grape" aria-hidden="true"><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><path d="M6 9V3a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v6"></path><rect x="6" y="14" width="12" height="8" rx="1"></rect></svg> PDF imprimible</li>
    <li class="flex items-center gap-1.5"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-star size-4 text-tangerine" aria-hidden="true"><path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"></path></svg> Para toda la familia</li>
  </ul>
</div>'''

sec1 = re.sub(hero_cta_pattern, hero_replacement, sec1, flags=re.DOTALL)

# Add IDs to sections for clean navigation
sec1 = sec1.replace('<section class="relative isolate bg-confetti">', '<section id="hero" class="relative isolate bg-confetti">')
sec2 = sec2.replace('<section class="bg-background px-5 py-20 sm:py-24">', '<section id="que-vas-a-obtener" class="bg-background px-5 py-20 sm:py-24">')
sec3 = sec3.replace('<section class="relative bg-blush px-5 py-20 sm:py-24">', '<section id="solucion-inmediata" class="relative bg-blush px-5 py-20 sm:py-24">')
sec4 = sec4.replace('<section class="bg-card px-5 py-20 sm:py-24">', '<section id="que-recibiras" class="bg-card px-5 py-20 sm:py-24">')
sec5 = sec5.replace('<section class="relative overflow-hidden bg-foreground px-5 py-20 sm:py-24">', '<section id="bonos" class="relative overflow-hidden bg-foreground px-5 py-20 sm:py-24">')

# SECTION 6 — OFERTA PRINCIPAL
sec6 = '''<section id="oferta-principal" class="relative isolate bg-confetti px-5 py-20 sm:py-24">
  <div class="mx-auto max-w-4xl">
    <div class="relative overflow-hidden rounded-[2.5rem] border-4 border-dashed border-primary/40 bg-card p-8 sm:p-12 lg:p-16 text-center shadow-book">
      <!-- Decorative badge -->
      <div class="mx-auto flex max-w-fit items-center gap-2 rounded-full bg-sunshine px-4 py-1.5 text-sm font-extrabold text-sunshine-foreground shadow-sticker">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-sparkles size-4"><path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"></path><path d="M20 2v4"></path><path d="M22 4h-4"></path><circle cx="4" cy="20" r="2"></circle></svg>
        <span>Acceso Inmediato a la Oferta Principal</span>
      </div>

      <!-- Nombre del producto -->
      <h2 class="mt-6 text-3xl font-bold leading-tight text-foreground sm:text-4xl lg:text-5xl font-display">
        365 Actividades para desarrollar el potencial de tu hijo
      </h2>

      <!-- Resumen breve de lo incluido -->
      <p class="mx-auto mt-4 max-w-2xl text-base leading-relaxed text-muted-foreground sm:text-lg">
        La guía digital completa con <strong class="text-foreground">365 actividades prácticas</strong> para cada día del año (12 temáticas mensuales, fichas paso a paso con materiales de casa y cero pantallas) más los <strong class="text-foreground">4 bonos exclusivos de regalo</strong> incluidos hoy.
      </p>

      <!-- PRECIO EXACTO CON ANCLAJE -->
      <div class="mt-8 flex flex-col items-center justify-center">
        <!-- Precio antes tachado -->
        <span class="text-base sm:text-lg font-bold line-through text-muted-foreground/70 uppercase tracking-wider">
          ANTES: $27 USD
        </span>
        
        <!-- Precio actual destacado -->
        <div class="mt-1 flex flex-wrap items-baseline justify-center gap-2 font-display">
          <span class="text-2xl sm:text-3xl font-extrabold text-primary">AHORA SOLO:</span>
          <span class="text-5xl sm:text-6xl lg:text-7xl font-extrabold text-foreground tracking-tight">$7 USD</span>
        </div>
        <p class="mt-1 text-sm font-extrabold uppercase tracking-wide text-teal">
          Pago único · Sin suscripciones
        </p>
      </div>

      <!-- PRIMER BOTÓN DE COMPRA -->
      <div class="mt-8 flex flex-col items-center">
        <a href="https://pay.hotmart.com/T108126453C" target="_blank" rel="noopener noreferrer" class="inline-flex w-full max-w-lg items-center justify-center gap-2 rounded-full bg-primary font-display font-semibold text-primary-foreground shadow-cta transition-transform hover:-translate-y-0.5 hover:bg-primary/95 active:translate-y-0.5 active:shadow-none h-16 px-6 text-lg sm:h-[4.25rem] sm:px-10 sm:text-xl cursor-pointer text-center no-underline">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-calendar-heart size-6 shrink-0"><path d="M12.127 22H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v5.125"></path><path d="M14.62 18.8A2.25 2.25 0 1 1 18 15.836a2.25 2.25 0 1 1 3.38 2.966l-2.626 2.856a.998.998 0 0 1-1.507 0z"></path><path d="M16 2v4"></path><path d="M3 10h18"></path><path d="M8 2v4"></path></svg>
          ¡QUIERO MIS 365 ACTIVIDADES AHORA!
        </a>

        <p class="mt-3 text-sm font-bold text-muted-foreground">
          Pago 100% seguro · Pago único · Acceso inmediato
        </p>

        <!-- Urgencia honesta -->
        <p class="mt-2 text-sm font-semibold text-foreground/80">
          Accede hoy al precio disponible
        </p>
      </div>

      <!-- MÉTODOS DE PAGO COMO IMAGEN HORIZONTAL -->
      <div class="mt-8 flex flex-col items-center">
        <img src="metodos-pago-hotmart.svg" alt="Métodos de pago compatibles con Hotmart" class="w-full max-w-lg h-auto rounded-xl shadow-sm" loading="lazy" />
      </div>

      <!-- MENSAJE DE SEGURIDAD -->
      <div class="mt-8 mx-auto flex max-w-md items-center justify-center gap-3 rounded-2xl bg-muted/60 p-4 text-xs sm:text-sm font-semibold text-muted-foreground">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-shield-check size-5 shrink-0 text-leaf"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/></svg>
        <span>Transacción protegida mediante cifrado SSL de 256 bits procesada por Hotmart.</span>
      </div>
    </div>
  </div>
</section>'''

# SECTION 7 — TESTIMONIOS
sec7 = '''<section id="testimonios" class="bg-background px-5 py-20 sm:py-24">
  <div class="mx-auto max-w-6xl">
    <div class="mx-auto max-w-3xl text-center">
      <span class="font-hand text-2xl font-bold sm:text-3xl text-primary">Experiencias y opiniones</span>
      <h2 class="mt-2 text-2xl font-bold leading-snug text-foreground sm:text-3xl lg:text-4xl">
        Únete a personas de todo el mundo que quieren ver a sus hijos aprender jugando y reducir las pantallas
      </h2>
      <p class="mx-auto mt-4 max-w-2xl text-lg text-muted-foreground">
        Y obtén 365 Actividades para transformar las tardes en casa en momentos únicos de conexión y aprendizaje.
      </p>
    </div>

    <!-- EXACTAMENTE 4 ESPACIOS PARA CAPTURAS DE WHATSAPP -->
    <div class="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
      <!-- Espacio 1 -->
      <div class="flex flex-col items-center justify-center rounded-3xl border-2 border-dashed border-leaf/40 bg-card p-6 text-center shadow-sticker min-h-[260px] sm:min-h-[290px]">
        <div class="flex size-14 items-center justify-center rounded-2xl bg-leaf/15 text-leaf shadow-sm">
          <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-message-circle"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
        </div>
        <span class="mt-4 inline-flex items-center gap-1.5 rounded-full bg-leaf/10 px-3 py-1 text-xs font-extrabold uppercase tracking-wide text-leaf">Captura de WhatsApp 1/4</span>
        <p class="mt-4 font-display text-base font-bold text-muted-foreground">Reemplazar por testimonio real</p>
      </div>

      <!-- Espacio 2 -->
      <div class="flex flex-col items-center justify-center rounded-3xl border-2 border-dashed border-leaf/40 bg-card p-6 text-center shadow-sticker min-h-[260px] sm:min-h-[290px]">
        <div class="flex size-14 items-center justify-center rounded-2xl bg-leaf/15 text-leaf shadow-sm">
          <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-message-circle"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
        </div>
        <span class="mt-4 inline-flex items-center gap-1.5 rounded-full bg-leaf/10 px-3 py-1 text-xs font-extrabold uppercase tracking-wide text-leaf">Captura de WhatsApp 2/4</span>
        <p class="mt-4 font-display text-base font-bold text-muted-foreground">Reemplazar por testimonio real</p>
      </div>

      <!-- Espacio 3 -->
      <div class="flex flex-col items-center justify-center rounded-3xl border-2 border-dashed border-leaf/40 bg-card p-6 text-center shadow-sticker min-h-[260px] sm:min-h-[290px]">
        <div class="flex size-14 items-center justify-center rounded-2xl bg-leaf/15 text-leaf shadow-sm">
          <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-message-circle"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
        </div>
        <span class="mt-4 inline-flex items-center gap-1.5 rounded-full bg-leaf/10 px-3 py-1 text-xs font-extrabold uppercase tracking-wide text-leaf">Captura de WhatsApp 3/4</span>
        <p class="mt-4 font-display text-base font-bold text-muted-foreground">Reemplazar por testimonio real</p>
      </div>

      <!-- Espacio 4 -->
      <div class="flex flex-col items-center justify-center rounded-3xl border-2 border-dashed border-leaf/40 bg-card p-6 text-center shadow-sticker min-h-[260px] sm:min-h-[290px]">
        <div class="flex size-14 items-center justify-center rounded-2xl bg-leaf/15 text-leaf shadow-sm">
          <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-message-circle"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>
        </div>
        <span class="mt-4 inline-flex items-center gap-1.5 rounded-full bg-leaf/10 px-3 py-1 text-xs font-extrabold uppercase tracking-wide text-leaf">Captura de WhatsApp 4/4</span>
        <p class="mt-4 font-display text-base font-bold text-muted-foreground">Reemplazar por testimonio real</p>
      </div>
    </div>
  </div>
</section>'''

# SECTION 8 — RECAPITULACIÓN
sec8 = '''<section id="recapitulacion" class="relative bg-blush px-5 py-20 sm:py-24">
  <div class="mx-auto max-w-6xl">
    <div class="mx-auto max-w-3xl text-center">
      <span class="font-hand text-2xl font-bold sm:text-3xl text-primary">Resumen completo</span>
      <h2 class="mt-1 text-3xl font-bold leading-tight sm:text-4xl lg:text-5xl text-foreground font-display">
        RECAPITULEMOS TODO LO QUE TE LLEVARÁS
      </h2>
    </div>

    <!-- BUNDLE Y LISTAS DE CONTENIDO -->
    <div class="mt-14 grid items-center gap-12 lg:grid-cols-12 lg:gap-10">
      
      <!-- COMPOSICIÓN TIPO BUNDLE -->
      <div class="lg:col-span-6">
        <div class="relative mx-auto w-full max-w-lg">
          <div class="relative mx-auto aspect-[5/4] w-full flex items-center justify-center">
            <!-- Bono 2 izq fondo -->
            <img src="./__l5e/assets-v1/293b7353-218a-4449-b80a-593d1b983081/bono-manualidades-recicladas.jpg" alt="Bono 2 Manualidades con Material Reciclado" loading="lazy" class="absolute left-0 bottom-4 w-[42%] -rotate-12 rounded-xl border-4 border-card shadow-book" />
            <!-- Bono 1 izq medio -->
            <img src="./__l5e/assets-v1/7095ec54-41ab-489a-aae6-84d74e9f63c6/bono-calendarios-mensuales.jpg" alt="Bono 1 Calendarios Mensuales" loading="lazy" class="absolute left-[12%] top-2 w-[44%] -rotate-6 rounded-xl border-4 border-card shadow-book z-10" />
            <!-- Bono 3 der medio -->
            <img src="./__l5e/assets-v1/6a7d2163-e048-47b4-beb6-d7a3e1dc2cd4/bono-rutina-sin-pantallas.jpg" alt="Bono 3 Rutina Familiar sin Pantallas" loading="lazy" class="absolute right-[12%] top-2 w-[44%] rotate-6 rounded-xl border-4 border-card shadow-book z-10" />
            <!-- Bono 4 der fondo -->
            <img src="./__l5e/assets-v1/8711434f-96a2-4e26-a120-6ea639096482/bono-actividades-5-minutos.jpg" alt="Bono 4 50 Actividades en 5 Minutos" loading="lazy" class="absolute right-0 bottom-4 w-[42%] rotate-12 rounded-xl border-4 border-card shadow-book" />
            <!-- PRODUCTO PRINCIPAL AL CENTRO -->
            <img src="./__l5e/assets-v1/0fe3cf70-fa9b-4fcb-870b-89f20b942e93/portada-365-actividades.jpg" alt="Portada de la guía 365 actividades para desarrollar el potencial de tu hijo" class="relative z-20 mx-auto w-[56%] rounded-2xl border-[6px] border-card shadow-book" />
            
            <!-- Sticker de Bundle -->
            <div class="absolute -top-3 right-4 z-30 flex size-20 -rotate-12 flex-col items-center justify-center rounded-full bg-sunshine text-center text-sunshine-foreground shadow-sticker sm:size-24">
              <span class="font-display text-xl sm:text-2xl font-bold leading-none">BUNDLE</span>
              <span class="text-[10px] font-extrabold uppercase sm:text-xs">COMPLETO</span>
            </div>
          </div>
        </div>
      </div>

      <!-- LISTAS CON CHECK Y REGALO -->
      <div class="space-y-6 lg:col-span-6">
        <!-- Lista de contenidos principales con icono check -->
        <div class="rounded-3xl border-2 border-primary/30 bg-card p-6 shadow-sticker">
          <p class="font-display text-lg font-bold text-primary flex items-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-book-open text-primary"><path d="M12 7v14"/><path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/></svg>
            Producto Principal:
          </p>
          <ul class="mt-3 space-y-2.5">
            <li class="flex items-start gap-2.5 text-sm sm:text-base font-semibold text-foreground">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-badge-check shrink-0 text-leaf mt-0.5"><path d="M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z"></path><path d="m9 12 2 2 4-4"></path></svg>
              <span>Guía digital completa con 365 actividades prácticas (1 para cada día del año).</span>
            </li>
            <li class="flex items-start gap-2.5 text-sm sm:text-base font-semibold text-foreground">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-badge-check shrink-0 text-leaf mt-0.5"><path d="M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z"></path><path d="m9 12 2 2 4-4"></path></svg>
              <span>12 temáticas mensuales (ciencia, cocina, reciclaje, arte, movimiento, ingenio y más).</span>
            </li>
            <li class="flex items-start gap-2.5 text-sm sm:text-base font-semibold text-foreground">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-badge-check shrink-0 text-leaf mt-0.5"><path d="M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z"></path><path d="m9 12 2 2 4-4"></path></svg>
              <span>Fichas con materiales cotidianos de casa, tiempo estimado y paso a paso claro.</span>
            </li>
            <li class="flex items-start gap-2.5 text-sm sm:text-base font-semibold text-foreground">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-badge-check shrink-0 text-leaf mt-0.5"><path d="M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z"></path><path d="m9 12 2 2 4-4"></path></svg>
              <span>Formato digital PDF listo para ver en celular, tablet o imprimir.</span>
            </li>
          </ul>
        </div>

        <!-- Lista de los 4 bonos con icono regalo -->
        <div class="rounded-3xl border-2 border-sunshine/60 bg-card p-6 shadow-sticker">
          <p class="font-display text-lg font-bold text-tangerine flex items-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-gift text-tangerine"><path d="M12 7v14"></path><path d="M20 11v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-8"></path><path d="M7.5 7a1 1 0 0 1 0-5A4.8 8 0 0 1 12 7a4.8 8 0 0 1 4.5-5 1 1 0 0 1 0 5"></path><rect x="3" y="7" width="18" height="4" rx="1"></rect></svg>
            Los 4 Bonos de Regalo Incluidos:
          </p>
          <ul class="mt-3 space-y-2.5">
            <li class="flex items-start gap-2.5 text-sm sm:text-base font-semibold text-foreground">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-gift shrink-0 text-tangerine mt-0.5"><path d="M12 7v14"></path><path d="M20 11v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-8"></path><path d="M7.5 7a1 1 0 0 1 0-5A4.8 8 0 0 1 12 7a4.8 8 0 0 1 4.5-5 1 1 0 0 1 0 5"></path><rect x="3" y="7" width="18" height="4" rx="1"></rect></svg>
              <span><strong class="font-extrabold text-primary">Bono 1:</strong> 12 Calendarios Mensuales Imprimibles para Elegir la Actividad del Día sin Pensarlo.</span>
            </li>
            <li class="flex items-start gap-2.5 text-sm sm:text-base font-semibold text-foreground">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-gift shrink-0 text-tangerine mt-0.5"><path d="M12 7v14"></path><path d="M20 11v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-8"></path><path d="M7.5 7a1 1 0 0 1 0-5A4.8 8 0 0 1 12 7a4.8 8 0 0 1 4.5-5 1 1 0 0 1 0 5"></path><rect x="3" y="7" width="18" height="4" rx="1"></rect></svg>
              <span><strong class="font-extrabold text-primary">Bono 2:</strong> 100 Manualidades con Material Reciclado para Niños en Casa.</span>
            </li>
            <li class="flex items-start gap-2.5 text-sm sm:text-base font-semibold text-foreground">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-gift shrink-0 text-tangerine mt-0.5"><path d="M12 7v14"></path><path d="M20 11v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-8"></path><path d="M7.5 7a1 1 0 0 1 0-5A4.8 8 0 0 1 12 7a4.8 8 0 0 1 4.5-5 1 1 0 0 1 0 5"></path><rect x="3" y="7" width="18" height="4" rx="1"></rect></svg>
              <span><strong class="font-extrabold text-primary">Bono 3:</strong> 21 Días para Consolidar una Rutina Familiar sin Pantallas.</span>
            </li>
            <li class="flex items-start gap-2.5 text-sm sm:text-base font-semibold text-foreground">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-gift shrink-0 text-tangerine mt-0.5"><path d="M12 7v14"></path><path d="M20 11v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-8"></path><path d="M7.5 7a1 1 0 0 1 0-5A4.8 8 0 0 1 12 7a4.8 8 0 0 1 4.5-5 1 1 0 0 1 0 5"></path><rect x="3" y="7" width="18" height="4" rx="1"></rect></svg>
              <span><strong class="font-extrabold text-primary">Bono 4:</strong> 50 Actividades Listas en 5 Minutos para los Días sin Tiempo.</span>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- GANCHO DE PRECIO Y SEGUNDO CTA -->
    <div class="mt-14 mx-auto max-w-2xl rounded-3xl border-2 border-dashed border-primary/40 bg-card p-8 sm:p-10 text-center shadow-book">
      <!-- GANCHO DE PRECIO -->
      <span class="text-base sm:text-lg font-bold line-through text-muted-foreground/70 uppercase tracking-wider">
        ANTES: $27 USD
      </span>
      <div class="mt-1 flex flex-wrap items-baseline justify-center gap-2 font-display">
        <span class="text-2xl sm:text-3xl font-extrabold text-primary">AHORA SOLO:</span>
        <span class="text-5xl sm:text-6xl font-extrabold text-foreground tracking-tight">$7 USD</span>
      </div>
      <p class="mt-2 text-sm font-extrabold uppercase tracking-wide text-teal">
        Pago único · Acceso inmediato mediante Hotmart
      </p>

      <!-- SEGUNDO Y ÚLTIMO BOTÓN DE COMPRA -->
      <div class="mt-6 flex flex-col items-center">
        <a href="https://pay.hotmart.com/T108126453C" target="_blank" rel="noopener noreferrer" class="inline-flex w-full max-w-lg items-center justify-center gap-2 rounded-full bg-primary font-display font-semibold text-primary-foreground shadow-cta transition-transform hover:-translate-y-0.5 hover:bg-primary/95 active:translate-y-0.5 active:shadow-none h-16 px-6 text-lg sm:h-[4.25rem] sm:px-10 sm:text-xl cursor-pointer text-center no-underline">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-calendar-heart size-6 shrink-0"><path d="M12.127 22H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v5.125"></path><path d="M14.62 18.8A2.25 2.25 0 1 1 18 15.836a2.25 2.25 0 1 1 3.38 2.966l-2.626 2.856a.998.998 0 0 1-1.507 0z"></path><path d="M16 2v4"></path><path d="M3 10h18"></path><path d="M8 2v4"></path></svg>
          ¡SÍ, QUIERO MIS 365 ACTIVIDADES!
        </a>

        <p class="mt-3 text-sm font-bold text-muted-foreground">
          Pago 100% seguro · Pago único · Acceso inmediato
        </p>

        <!-- AVISO SOBRE EL PRECIO -->
        <p class="mt-3 inline-block text-xs sm:text-sm font-extrabold text-tangerine bg-tangerine/10 rounded-full px-4 py-1.5 border border-tangerine/20">
          IMPORTANTE: El precio actual de $7 USD puede cambiar en cualquier momento
        </p>

        <!-- MÉTODOS DE PAGO COMO IMAGEN HORIZONTAL -->
        <div class="mt-6 w-full flex justify-center">
          <img src="metodos-pago-hotmart.svg" alt="Métodos de pago compatibles con Hotmart" class="w-full max-w-md h-auto rounded-xl shadow-sm" loading="lazy" />
        </div>
      </div>
    </div>

  </div>
</section>'''

# SECTION 9 — PREGUNTAS FRECUENTES (EXACTAMENTE 6 PREGUNTAS EN FORMATO ACORDEÓN)
sec9 = '''<section id="preguntas-frecuentes" class="bg-card px-5 py-20 sm:py-24">
  <div class="mx-auto max-w-4xl">
    <div class="mx-auto max-w-3xl text-center">
      <span class="font-hand text-2xl font-bold sm:text-3xl text-primary">Resolvemos tus dudas</span>
      <h2 class="mt-1 text-3xl font-bold leading-tight sm:text-4xl lg:text-5xl text-foreground font-display">
        Preguntas frecuentes
      </h2>
    </div>

    <!-- EXACTAMENTE 6 PREGUNTAS EN FORMATO ACORDEÓN -->
    <div class="mt-12 space-y-4" id="faq-accordion-group">
      <!-- Pregunta 1 -->
      <div class="overflow-hidden rounded-2xl border-2 border-border bg-background transition-colors">
        <button type="button" class="faq-toggle flex w-full items-center justify-between gap-4 p-5 sm:p-6 text-left font-display text-lg sm:text-xl font-bold text-foreground cursor-pointer" aria-expanded="false">
          <span>1. ¿Qué incluye exactamente el producto?</span>
          <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-down shrink-0 text-primary transition-transform duration-200"><path d="m6 9 6 6 6-6"/></svg>
        </button>
        <div class="faq-content hidden px-5 pb-6 sm:px-6 text-base leading-relaxed text-muted-foreground border-t border-border/50 pt-4">
          La guía digital completa con 365 actividades prácticas organizadas en 12 temáticas mensuales (una actividad lista para cada día del año con fichas detalladas de materiales cotidianos, tiempo y pasos) más los 4 bonos de regalo: 12 Calendarios Mensuales Imprimibles, 100 Manualidades con Material Reciclado, Guía de 21 Días sin Pantallas y 50 Actividades Listas en 5 Minutos. Todo en formato digital PDF listo para descargar e imprimir.
        </div>
      </div>

      <!-- Pregunta 2 -->
      <div class="overflow-hidden rounded-2xl border-2 border-border bg-background transition-colors">
        <button type="button" class="faq-toggle flex w-full items-center justify-between gap-4 p-5 sm:p-6 text-left font-display text-lg sm:text-xl font-bold text-foreground cursor-pointer" aria-expanded="false">
          <span>2. ¿Cómo y cuándo se recibe el acceso?</span>
          <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-down shrink-0 text-primary transition-transform duration-200"><path d="m6 9 6 6 6-6"/></svg>
        </button>
        <div class="faq-content hidden px-5 pb-6 sm:px-6 text-base leading-relaxed text-muted-foreground border-t border-border/50 pt-4">
          El acceso es inmediato tras la confirmación del pago. Recibirás un correo electrónico automático de Hotmart con tus credenciales y el enlace directo para acceder al área de miembros y descargar todo el material a tu celular, tablet o computador.
        </div>
      </div>

      <!-- Pregunta 3 -->
      <div class="overflow-hidden rounded-2xl border-2 border-border bg-background transition-colors">
        <button type="button" class="faq-toggle flex w-full items-center justify-between gap-4 p-5 sm:p-6 text-left font-display text-lg sm:text-xl font-bold text-foreground cursor-pointer" aria-expanded="false">
          <span>3. ¿Para quién está diseñada esta guía?</span>
          <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-down shrink-0 text-primary transition-transform duration-200"><path d="m6 9 6 6 6-6"/></svg>
        </button>
        <div class="faq-content hidden px-5 pb-6 sm:px-6 text-base leading-relaxed text-muted-foreground border-t border-border/50 pt-4">
          Está especialmente diseñada para mamás, papás, cuidadores y docentes con niñas y niños de 4 a 10 años que desean alternativas divertidas, creativas y significativas para compartir en familia y reducir el tiempo frente a celulares, tablets y televisores.
        </div>
      </div>

      <!-- Pregunta 4 -->
      <div class="overflow-hidden rounded-2xl border-2 border-border bg-background transition-colors">
        <button type="button" class="faq-toggle flex w-full items-center justify-between gap-4 p-5 sm:p-6 text-left font-display text-lg sm:text-xl font-bold text-foreground cursor-pointer" aria-expanded="false">
          <span>4. ¿Se necesita experiencia previa o materiales costosos?</span>
          <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-down shrink-0 text-primary transition-transform duration-200"><path d="m6 9 6 6 6-6"/></svg>
        </button>
        <div class="faq-content hidden px-5 pb-6 sm:px-6 text-base leading-relaxed text-muted-foreground border-t border-border/50 pt-4">
          No necesitas experiencia previa ni conocimientos pedagógicos. Cada actividad fue pensada para ser explicada en pocos segundos y realizarse con elementos que ya tienes en casa: rollos de papel higiénico, cajas de cartón, botellas, papel, tijeras y cucharas.
        </div>
      </div>

      <!-- Pregunta 5 -->
      <div class="overflow-hidden rounded-2xl border-2 border-border bg-background transition-colors">
        <button type="button" class="faq-toggle flex w-full items-center justify-between gap-4 p-5 sm:p-6 text-left font-display text-lg sm:text-xl font-bold text-foreground cursor-pointer" aria-expanded="false">
          <span>5. ¿En qué dispositivos puede utilizarse?</span>
          <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-down shrink-0 text-primary transition-transform duration-200"><path d="m6 9 6 6 6-6"/></svg>
        </button>
        <div class="faq-content hidden px-5 pb-6 sm:px-6 text-base leading-relaxed text-muted-foreground border-t border-border/50 pt-4">
          Puedes abrir y consultar la guía en cualquier teléfono móvil (Android o iPhone), tablet, iPad o computador. Además, todo el material está en formato PDF imprimible, por lo que puedes imprimir las fichas o calendarios las veces que quieras.
        </div>
      </div>

      <!-- Pregunta 6 -->
      <div class="overflow-hidden rounded-2xl border-2 border-border bg-background transition-colors">
        <button type="button" class="faq-toggle flex w-full items-center justify-between gap-4 p-5 sm:p-6 text-left font-display text-lg sm:text-xl font-bold text-foreground cursor-pointer" aria-expanded="false">
          <span>6. ¿Cómo funcionan el pago y el acceso?</span>
          <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-down shrink-0 text-primary transition-transform duration-200"><path d="m6 9 6 6 6-6"/></svg>
        </button>
        <div class="faq-content hidden px-5 pb-6 sm:px-6 text-base leading-relaxed text-muted-foreground border-t border-border/50 pt-4">
          El pago se realiza mediante Hotmart, la plataforma más segura de productos digitales en el mundo, respaldada con cifrado SSL de 256 bits. Es un pago único (sin mensualidades ni cargos ocultos) y el acceso a los materiales queda habilitado de por vida.
        </div>
      </div>
    </div>
  </div>
</section>'''

# PIE DE PÁGINA (FOOTER)
footer = '''<footer class="border-t border-border bg-background px-5 py-12 text-center text-sm text-muted-foreground">
  <div class="mx-auto max-w-5xl space-y-4">
    <p class="font-display font-semibold text-foreground">
      © 2026 365 Actividades para desarrollar el potencial de tu hijo. Todos los derechos reservados.
    </p>
    <div class="flex flex-wrap justify-center gap-x-6 gap-y-2 text-xs font-semibold">
      <a href="#" class="hover:text-primary transition-colors">Términos y Condiciones</a>
      <span>·</span>
      <a href="#" class="hover:text-primary transition-colors">Política de Privacidad</a>
      <span>·</span>
      <a href="#" class="hover:text-primary transition-colors">Descargo de Responsabilidad</a>
    </div>
    <p class="mx-auto max-w-2xl text-[11px] leading-relaxed opacity-75">
      Este sitio no es parte del sitio web de Meta, Facebook o Google. Además, este sitio no está respaldado por Meta o Google de ninguna manera. Los resultados varían según el uso y la dedicación de cada familia. Hotmart es el distribuidor y procesador seguro de este producto.
    </p>
  </div>
</footer>'''

# CLIENT-SIDE INTERACTIVITY SCRIPT (Vanilla JS for Tabs and Accordions)
script = f'''<script>
// Month tabs interactivity
const monthsData = {json.dumps(months_data, ensure_ascii=False)};

document.addEventListener("DOMContentLoaded", () => {{
  const tablist = document.querySelector('[role="tablist"]');
  const panel = document.getElementById("modulo-panel");
  if (tablist && panel) {{
    const tabs = Array.from(tablist.querySelectorAll('[role="tab"]'));
    tabs.forEach((tab, index) => {{
      tab.addEventListener("click", () => {{
        // Update tabs active state
        tabs.forEach((t, i) => {{
          const isSelected = i === index;
          t.setAttribute("aria-selected", isSelected ? "true" : "false");
          if (isSelected) {{
            t.className = "flex flex-col items-start gap-1 rounded-2xl border-2 px-3 py-2.5 text-left transition-colors border-primary bg-primary text-primary-foreground shadow-sticker";
            const ringSpan = t.querySelector("span > span");
            if (ringSpan) ringSpan.className = "size-2.5 rounded-full " + monthsData[i].dot + " ring-2 ring-primary-foreground";
          }} else {{
            t.className = "flex flex-col items-start gap-1 rounded-2xl border-2 px-3 py-2.5 text-left transition-colors border-border bg-background text-foreground hover:border-primary/50";
            const ringSpan = t.querySelector("span > span");
            if (ringSpan) ringSpan.className = "size-2.5 rounded-full " + monthsData[i].dot;
          }}
        }});

        // Update panel content
        const m = monthsData[index];
        const numFormatted = String(index + 1).padStart(2, '0');
        panel.innerHTML = `
          <div class="flex items-center bg-blush p-4 sm:p-6">
            <img src="${{m.image}}" alt="Página interior del mes ${{index + 1}}: ${{m.name}}" loading="lazy" class="h-auto w-full rounded-2xl border-4 border-card shadow-book animate-in fade-in zoom-in-95 duration-300"/>
          </div>
          <div class="flex flex-col justify-center gap-4 p-6 sm:p-8">
            <div class="flex items-center gap-3">
              <span class="flex size-14 shrink-0 items-center justify-center rounded-2xl bg-teal font-display text-2xl font-bold text-teal-foreground shadow-sticker">${{numFormatted}}</span>
              <div>
                <p class="text-sm font-extrabold uppercase tracking-wide text-primary">Mes ${{index + 1}}</p>
                <h3 class="text-2xl font-bold leading-tight text-foreground">${{m.name}}</h3>
              </div>
            </div>
            <p class="font-hand text-2xl font-bold text-grape">${{m.tagline}}</p>
            <p class="text-base leading-relaxed text-muted-foreground">${{m.description}}</p>
            <div>
              <p class="mb-2 flex items-center gap-1.5 text-sm font-extrabold text-foreground">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-lightbulb size-4 text-sunshine"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"></path><path d="M9 18h6"></path><path d="M10 22h4"></path></svg>
                Algunas actividades:
              </p>
              <ul class="flex flex-wrap gap-2">
                ${{m.examples.map(ex => `<li class="rounded-full bg-accent px-3 py-1 text-sm font-semibold text-accent-foreground">${{ex}}</li>`).join('')}}
              </ul>
            </div>
            <p class="flex items-center gap-1.5 text-sm font-bold text-muted-foreground">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-clock size-4 text-teal"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg>
              ${{m.range}} · materiales, tiempo y edad en cada ficha
            </p>
          </div>
        `;
      }});
    }});
  }}

  // FAQ Accordions interactivity
  const faqToggles = document.querySelectorAll(".faq-toggle");
  faqToggles.forEach(toggle => {{
    toggle.addEventListener("click", () => {{
      const expanded = toggle.getAttribute("aria-expanded") === "true";
      const content = toggle.nextElementSibling;
      const chevron = toggle.querySelector("svg");

      if (expanded) {{
        toggle.setAttribute("aria-expanded", "false");
        content.classList.add("hidden");
        chevron.classList.remove("rotate-180");
      }} else {{
        // Close others
        faqToggles.forEach(other => {{
          other.setAttribute("aria-expanded", "false");
          other.nextElementSibling.classList.add("hidden");
          other.querySelector("svg").classList.remove("rotate-180");
        }});
        toggle.setAttribute("aria-expanded", "true");
        content.classList.remove("hidden");
        chevron.classList.add("rotate-180");
      }}
    }});
  }});
}});
</script>'''

# Assemble complete index.html
html = f'''<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>365 Actividades para desarrollar el potencial de tu hijo | Sin pantallas</title>
  <meta name="description" content="Una actividad lista para cada día del año: juegos, manualidades, ciencia y cocina para niños de 4 a 10 años, con materiales que ya tienes en casa."/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous"/>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&amp;family=Fredoka:wght@500;600;700&amp;family=Nunito:wght@400;600;700;800&amp;display=swap"/>
  <link rel="stylesheet" href="styles.css"/>
  <link rel="icon" href="favicon.ico" type="image/x-icon"/>
</head>
<body class="min-h-screen overflow-x-hidden bg-background text-foreground antialiased">
  <main class="min-h-screen overflow-x-hidden bg-background">
    {sec1}
    {sec2}
    {sec3}
    {sec4}
    {sec5}
    {sec6}
    {sec7}
    {sec8}
    {sec9}
  </main>
  {footer}
  {script}
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html written successfully! Size:", len(html))
