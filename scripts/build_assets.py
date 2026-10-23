"""Rebuild original profile artwork using Python's standard library."""
from pathlib import Path
from html import escape
OUT = Path(__file__).resolve().parents[1] / 'assets'
OUT.mkdir(exist_ok=True)
def text(x,y,s,size=16,color='#a8aec6',weight=400,mono=False):
    font='DejaVu Sans Mono, monospace' if mono else 'DejaVu Sans, Arial, sans-serif'
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(s)}</text>'
def svg(w,h,body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs>
<linearGradient id="bg" x2="1" y2="1"><stop stop-color="#101326"/><stop offset="1" stop-color="#181130"/></linearGradient>
<linearGradient id="accent"><stop stop-color="#c4a7ff"/><stop offset="1" stop-color="#67e8f9"/></linearGradient>
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#c4a7ff" stroke-opacity=".055"/></pattern></defs>
<rect width="100%" height="100%" rx="18" fill="url(#bg)"/><rect width="100%" height="100%" rx="18" fill="url(#grid)"/>{body}</svg>'''
hero='''<path d="M0 1H960" stroke="url(#accent)" stroke-width="3"/>
<circle cx="773" cy="167" r="104" fill="#b69bff" fill-opacity=".035" stroke="#c4a7ff" stroke-opacity=".2"/>
<ellipse cx="773" cy="167" rx="126" ry="43" transform="rotate(-35 773 167)" fill="none" stroke="#67e8f9" stroke-opacity=".5"/>
<ellipse cx="773" cy="167" rx="68" ry="105" transform="rotate(-35 773 167)" fill="none" stroke="#c4a7ff" stroke-opacity=".35"/>
<path d="M699 124l-35 42 35 42M847 124l35 42-35 42M794 109l-40 114" fill="none" stroke="url(#accent)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="670" cy="211" r="5" fill="#67e8f9"/><circle cx="859" cy="83" r="5" fill="#c4a7ff"/>
<path d="M908 245v14m-7-7h14M633 71v10m-5-5h10" stroke="#c4a7ff" stroke-width="2"/>'''
hero+=text(48,47,'CHANADINH / DEVELOPER LOG',12,'#c4a7ff',mono=True)
hero+=text(45,128,"Hey, I'm Chan.",57,'#f4f2ff',700)
hero+=text(48,171,'AI / ML  ·  FULL-STACK  ·  REVERSE ENGINEERING',13,'#67e8f9',mono=True)
hero+=text(48,220,'Curious about how it works.',19,'#d6d6e7')
hero+=text(48,249,'Stubborn enough to build it.',19,'#d6d6e7')
hero+='<path d="M48 287H912" stroke="#34304a"/>'
hero+=text(48,315,'FLORIDA, US',11,mono=True)+text(681,315,'CODE / LEARN / REPEAT',11,mono=True)
(OUT/'header.svg').write_text(svg(960,340,hero))
projects=[
('threat-hunting','01 / AI + SECURITY','Threat Hunting Pipeline',['From threat feeds to detection rules.','LLM-assisted analysis, RAG, and reporting.'],'PYTHON / AWS / OPENSEARCH','#c4a7ff'),
('pokemon-x','02 / REVERSE ENGINEERING','Inside Pokémon X',['Reconstructing game logic in portable C.','Tested subsystems + a native asset viewer.'],'C / PYTHON / SDL2','#67e8f9'),
('portfolio','03 / FULL-STACK','Next.js Portfolio',['A home for projects, built as a product.','Admin dashboard, content, and MongoDB.'],'NEXT.JS / TYPESCRIPT / REACT','#f9b8d2'),
('medusa','04 / BOTS + APIS','Medusa Bot',['A Discord bot connecting multiple APIs.','A playground for useful integrations.'],'JAVASCRIPT / DISCORD','#a6e3a1')]
for slug,label,title,lines,stack,accent in projects:
    body='<rect x="1" y="1" width="466" height="216" rx="17" fill="none" stroke="#37314e"/>'
    body+=text(24,32,label,10,accent,mono=True)+text(24,79,title,23,'#f4f2ff',700)
    for i,line in enumerate(lines): body+=text(24,113+i*23,line,13)
    body+='<path d="M24 159H444" stroke="#34304a"/>'
    body+=text(24,189,stack,10,accent,mono=True)
    body+=f'<path d="M420 29h16v16m0-16-19 19" fill="none" stroke="{accent}" stroke-width="2" stroke-linecap="round"/>'
    (OUT/f'{slug}.svg').write_text(svg(468,218,body))
footer=text(28,38,'LESS SCROLLING. MORE BUILDING.',12,'#c4a7ff',mono=True)+text(662,38,'THANKS FOR STOPPING BY :)',11,'#67e8f9',mono=True)
(OUT/'footer.svg').write_text(svg(960,64,footer))
print('Built 6 SVG assets.')
