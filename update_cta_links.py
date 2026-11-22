with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

url = "https://pay.hotmart.com/T108126453C"

# Button 1 replacement
target1 = '<button type="button" class="inline-flex w-full max-w-lg items-center justify-center gap-2 rounded-full bg-primary font-display font-semibold text-primary-foreground shadow-cta transition-transform hover:-translate-y-0.5 hover:bg-primary/95 active:translate-y-0.5 active:shadow-none h-16 px-6 text-lg sm:h-[4.25rem] sm:px-10 sm:text-xl cursor-pointer">\n          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-calendar-heart size-6 shrink-0"><path d="M12.127 22H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v5.125"></path><path d="M14.62 18.8A2.25 2.25 0 1 1 18 15.836a2.25 2.25 0 1 1 3.38 2.966l-2.626 2.856a.998.998 0 0 1-1.507 0z"></path><path d="M16 2v4"></path><path d="M3 10h18"></path><path d="M8 2v4"></path></svg>\n          ¡QUIERO MIS 365 ACTIVIDADES AHORA!\n        </button>'

replacement1 = f'<a href="{url}" target="_blank" rel="noopener noreferrer" class="inline-flex w-full max-w-lg items-center justify-center gap-2 rounded-full bg-primary font-display font-semibold text-primary-foreground shadow-cta transition-transform hover:-translate-y-0.5 hover:bg-primary/95 active:translate-y-0.5 active:shadow-none h-16 px-6 text-lg sm:h-[4.25rem] sm:px-10 sm:text-xl cursor-pointer text-center no-underline">\n          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-calendar-heart size-6 shrink-0"><path d="M12.127 22H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v5.125"></path><path d="M14.62 18.8A2.25 2.25 0 1 1 18 15.836a2.25 2.25 0 1 1 3.38 2.966l-2.626 2.856a.998.998 0 0 1-1.507 0z"></path><path d="M16 2v4"></path><path d="M3 10h18"></path><path d="M8 2v4"></path></svg>\n          ¡QUIERO MIS 365 ACTIVIDADES AHORA!\n        </a>'

# Button 2 replacement
target2 = '<button type="button" class="inline-flex w-full max-w-lg items-center justify-center gap-2 rounded-full bg-primary font-display font-semibold text-primary-foreground shadow-cta transition-transform hover:-translate-y-0.5 hover:bg-primary/95 active:translate-y-0.5 active:shadow-none h-16 px-6 text-lg sm:h-[4.25rem] sm:px-10 sm:text-xl cursor-pointer">\n          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-calendar-heart size-6 shrink-0"><path d="M12.127 22H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v5.125"></path><path d="M14.62 18.8A2.25 2.25 0 1 1 18 15.836a2.25 2.25 0 1 1 3.38 2.966l-2.626 2.856a.998.998 0 0 1-1.507 0z"></path><path d="M16 2v4"></path><path d="M3 10h18"></path><path d="M8 2v4"></path></svg>\n          ¡SÍ, QUIERO MIS 365 ACTIVIDADES!\n        </button>'

replacement2 = f'<a href="{url}" target="_blank" rel="noopener noreferrer" class="inline-flex w-full max-w-lg items-center justify-center gap-2 rounded-full bg-primary font-display font-semibold text-primary-foreground shadow-cta transition-transform hover:-translate-y-0.5 hover:bg-primary/95 active:translate-y-0.5 active:shadow-none h-16 px-6 text-lg sm:h-[4.25rem] sm:px-10 sm:text-xl cursor-pointer text-center no-underline">\n          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-calendar-heart size-6 shrink-0"><path d="M12.127 22H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v5.125"></path><path d="M14.62 18.8A2.25 2.25 0 1 1 18 15.836a2.25 2.25 0 1 1 3.38 2.966l-2.626 2.856a.998.998 0 0 1-1.507 0z"></path><path d="M16 2v4"></path><path d="M3 10h18"></path><path d="M8 2v4"></path></svg>\n          ¡SÍ, QUIERO MIS 365 ACTIVIDADES!\n        </a>'

# Check if target1 and target2 are present
assert target1 in content, "target1 not found in index.html"
assert target2 in content, "target2 not found in index.html"

content = content.replace(target1, replacement1).replace(target2, replacement2)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Both CTA buttons successfully updated to link to:", url)
