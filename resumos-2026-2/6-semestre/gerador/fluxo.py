# Fluxogramas no estilo MedSum (HTML -> PNG com Playwright)
import subprocess, os, html

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1200px;background:#fff;font-family:'Inter','Helvetica Neue',Arial,sans-serif;color:#1e1517;padding:28px 30px}
.tag{font-size:17px;font-weight:800;letter-spacing:3px;color:#a8771c}
h2{font-size:34px;font-weight:900;letter-spacing:-.5px;margin:4px 0 18px}
h2 span{color:#921827}
.row{display:flex;gap:16px;justify-content:center;align-items:stretch}
.b{flex:1;border-radius:16px;padding:14px 16px;font-size:19px;line-height:1.3;text-align:center}
.b b{display:block;font-size:21px;font-weight:900;margin-bottom:3px}
.s{background:#1c1214;color:#fff}.s b{color:#e0b25a}
.d{background:#921827;color:#fff}
.r{background:#f6ecd6;border:3px solid #e0b25a}.r b{color:#7a1220}
.n{background:#f8f5f4;border:2px solid #e8dfdf;color:#3d3335}
.a{text-align:center;font-size:30px;color:#a8771c;font-weight:900;line-height:1.1;margin:6px 0}
.lab{font-size:16px;font-weight:800;color:#921827;letter-spacing:1px}
.foot{margin-top:14px;font-size:14px;color:#6c5f61;text-align:right}
"""


def caixa(c):
    cls, tit, txt = c
    import re
    txt = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', txt)
    t = f'<b>{html.escape(tit)}</b>' if tit else ''
    return f'<div class="b {cls}">{t}{txt}</div>'


def render(tag, titulo_html, linhas, png, rodape='MedSum · By Laura Nunes'):
    """linhas: lista de ('row', [caixas]) ou ('arrow', 'rótulo' ou lista de rótulos)."""
    out = [f'<div class="tag">{tag}</div><h2>{titulo_html}</h2>']
    for kind, val in linhas:
        if kind == 'row':
            out.append('<div class="row">' + ''.join(caixa(c) for c in val) + '</div>')
        else:
            labs = val if isinstance(val, list) else [val]
            out.append('<div class="row">' + ''.join(
                f'<div style="flex:1" class="a">↓<div class="lab">{html.escape(l)}</div></div>' for l in labs) + '</div>')
    out.append(f'<div class="foot">{rodape}</div>')
    src = png.replace('.png', '.html')
    open(src, 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(out)}</body></html>')
    env = dict(os.environ)
    env['NODE_PATH'] = subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip()
    subprocess.run(['node', '/home/user/medsum/modelos/render.js', src, png, '1200', 'auto'], check=True, env=env)
    return png
