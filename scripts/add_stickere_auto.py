from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

s = s.replace('Patru direcții. Un singur brand.', 'Cinci direcții. Un singur brand.')
s = s.replace('site-uri web și afișe personalizate —', 'site-uri web, afișe personalizate și stickere auto —')

marker = '''            <span>
              Design & Print
            </span>'''
if 'Stickere Auto' not in s and marker in s:
    s = s.replace(marker, marker + '''

            <span>
              Stickere Auto
            </span>''')

if 'href="stickere-auto/"' not in s:
    card = '''


          <!-- STICKERE AUTO -->


          <a
            href="stickere-auto/"
            class="hub-card reveal">

            <div class="hub-image">

              <img
                src="logo-faurit.png"
                alt="Stickere auto personalizate Făurit de Busuioc">

            </div>


            <div class="hub-content">

              <span class="hub-number">
                05 • AUTO DESIGN
              </span>

              <h3>
                Stickere Auto
              </h3>

              <p>
                Design personalizat pentru capotă,
                portiere, lunetă, logo-uri și
                personalizare vizuală auto.
              </p>

              <div class="hub-link">
                Vezi categoria
                <span>→</span>
              </div>

            </div>

          </a>
'''
    needle = '''              <h3>
                Afișe Personalizate
              </h3>'''
    pos = s.find(needle)
    if pos == -1:
        raise SystemExit('Cardul Afișe Personalizate nu a fost găsit')
    close = s.find('          </a>', pos)
    if close == -1:
        raise SystemExit('Finalul cardului Afișe nu a fost găsit')
    close += len('          </a>')
    s = s[:close] + card + s[close:]

p.write_text(s, encoding='utf-8')
