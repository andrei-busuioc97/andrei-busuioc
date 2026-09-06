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

# Adaugă o bandă animată proprie Făurit de Busuioc, imediat sub HERO.
if 'class="service-ticker"' not in s:
    ticker_css = r'''

    /* =========================
       SERVICE TICKER
    ========================= */

    .service-ticker {
      position: relative;
      z-index: 5;
      overflow: hidden;
      width: 100%;
      background: linear-gradient(90deg, #00b978, #00d68f, #14eba1, #00d68f);
      border-top: 1px solid rgba(255,255,255,.12);
      border-bottom: 1px solid rgba(0,0,0,.35);
      box-shadow: 0 12px 35px rgba(0,214,143,.13);
    }

    .service-ticker-track {
      display: flex;
      width: max-content;
      animation: serviceTicker 24s linear infinite;
      will-change: transform;
    }

    .service-ticker-group {
      display: flex;
      align-items: center;
      white-space: nowrap;
      flex-shrink: 0;
    }

    .service-ticker-item {
      display: inline-flex;
      align-items: center;
      gap: 22px;
      padding: 16px 26px;
      color: #03110c;
      font-size: 13px;
      font-weight: 900;
      letter-spacing: 2.2px;
      text-transform: uppercase;
    }

    .service-ticker-item::after {
      content: "◆";
      font-size: 8px;
      opacity: .65;
    }

    .service-ticker:hover .service-ticker-track {
      animation-play-state: paused;
    }

    @keyframes serviceTicker {
      from { transform: translateX(0); }
      to { transform: translateX(-50%); }
    }

    @media (max-width: 640px) {
      .service-ticker-item {
        padding: 13px 18px;
        font-size: 11px;
        letter-spacing: 1.6px;
        gap: 16px;
      }
      .service-ticker-track {
        animation-duration: 20s;
      }
    }

    @media (prefers-reduced-motion: reduce) {
      .service-ticker-track { animation: none; }
    }
'''
    s = s.replace('</style>', ticker_css + '\n  </style>', 1)

    group = '''
      <div class="service-ticker-group" aria-hidden="true">
        <span class="service-ticker-item">Stickere Auto</span>
        <span class="service-ticker-item">Branding Auto</span>
        <span class="service-ticker-item">Stickere Magnetice</span>
        <span class="service-ticker-item">Creare Site-uri</span>
        <span class="service-ticker-item">Amenajări Interioare</span>
        <span class="service-ticker-item">Statui Decorative</span>
        <span class="service-ticker-item">Design Personalizat</span>
      </div>'''

    ticker_html = '''

    <!-- BANDĂ ANIMATĂ SERVICII -->
    <div class="service-ticker" aria-label="Servicii Făurit de Busuioc">
      <div class="service-ticker-track">
''' + group + '\n' + group + '''
      </div>
    </div>

'''

    hero_marker = 'HERO'
    hero_pos = s.find(hero_marker, s.find('<main'))
    hero_end = s.find('</section>', hero_pos)
    if hero_end != -1:
        hero_end += len('</section>')
        s = s[:hero_end] + ticker_html + s[hero_end:]
    else:
        main_pos = s.find('<main>')
        if main_pos != -1:
            main_pos += len('<main>')
            s = s[:main_pos] + ticker_html + s[main_pos:]

p.write_text(s, encoding='utf-8')
