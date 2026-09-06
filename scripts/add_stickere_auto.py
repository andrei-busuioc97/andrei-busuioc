from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# Elimină complet categoria Afișe Personalizate de pe homepage.
needle = '''              <h3>\n                Afișe Personalizate\n              </h3>'''
pos = s.find(needle)
if pos != -1:
    start = s.rfind('<a', 0, pos)
    end = s.find('</a>', pos)
    if start != -1 and end != -1:
        end += len('</a>')
        s = s[:start] + s[end:]

# Elimină eticheta Design & Print din hero.
marker = '''            <span>\n              Design & Print\n            </span>'''
s = s.replace(marker, '')

# Actualizează textele generale ale homepage-ului.
s = s.replace('Cinci direcții. Un singur brand.', 'Patru direcții. Un singur brand.')
s = s.replace('site-uri web, afișe personalizate și stickere auto —', 'site-uri web și stickere auto —')
s = s.replace('creare site-uri web și afișe personalizate A4.', 'creare site-uri web și stickere auto.')
s = s.replace('creare site-uri și afișe personalizate.', 'creare site-uri și stickere auto.')
s = s.replace('site-uri web și afișe personalizate.', 'site-uri web și stickere auto.')

# Păstrează cardul Stickere Auto cu imaginea premium.
start = s.find('href="stickere-auto/"')
end = s.find('</a>', start)
if start != -1 and end != -1:
    block = s[start:end]
    block = block.replace('src="logo-faurit.png"', 'src="stickere-auto/stickere-auto-premium.png"')
    block = block.replace('alt="Stickere auto personalizate Făurit de Busuioc"', 'alt="Stickere auto premium Făurit de Busuioc"')
    s = s[:start] + block + s[end:]

# Mută Stickere Auto exact în locul cardului Lucrări.
def card_block(text, comment):
    c = text.find(comment)
    if c == -1:
        return None
    a = text.find('<a', c)
    e = text.find('</a>', a)
    if a == -1 or e == -1:
        return None
    e += len('</a>')
    return c, e, text[c:e]

lucrari = card_block(s, '<!-- LUCRARI -->')
stickere = card_block(s, '<!-- STICKERE AUTO -->')
if lucrari and stickere:
    l0, l1, lb = lucrari
    s0, s1, sb = stickere
    if l0 < s0:
        middle = s[l1:s0]
        s = s[:l0] + sb + middle + lb + s[s1:]
    elif s0 < l0:
        middle = s[s1:l0]
        s = s[:s0] + lb + middle + sb + s[l1:]

p.write_text(s, encoding='utf-8')
