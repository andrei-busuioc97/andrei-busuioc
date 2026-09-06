from pathlib import Path

p = Path('lucrari/index.html')
s = p.read_text(encoding='utf-8')

if 'scara imbracata cu parchet 1.jpeg' not in s:
    proiect = '''
<div class="project"><span class="project-label">Proiect 03</span><h3>Scară îmbrăcată cu parchet</h3><p>Galerie proiect • 3 fotografii</p><div class="gallery">
<div class="photo"><img src="scara imbracata cu parchet 1.jpeg" alt="Scară îmbrăcată cu parchet - fotografia 1" loading="lazy" decoding="async"></div>
<div class="photo"><img src="scara imbracata cu parchet 2.jpeg" alt="Scară îmbrăcată cu parchet - fotografia 2" loading="lazy" decoding="async"></div>
<div class="photo"><img src="scara imbracata cu parchet 3.jpeg" alt="Scară îmbrăcată cu parchet - fotografia 3" loading="lazy" decoding="async"></div>
</div></div>
'''
    marker = '</div></section>\n<section id="contact"'
    if marker not in s:
        raise SystemExit('Nu am găsit finalul secțiunii portofoliu')
    s = s.replace(marker, proiect + '</div></section>\n<section id="contact"', 1)
    p.write_text(s, encoding='utf-8')
