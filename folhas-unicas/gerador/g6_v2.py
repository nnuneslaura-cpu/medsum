# Folhas únicas do 8º semestre · NCS (D1 SP 1.1–1.4 e D2 SP 2.1–2.2) no estilo 2
# (layouts A/B/C + Não confunda + mnemônicos). Conteúdo SÓ dos resumos publicados (PDFs do Drive).
# Tratamento do IAM: o PDF publicado é só fluxograma em imagem; o texto-base é o capítulo
# "Tratamento" do resumo de Síndrome coronariana aguda (mesma SP 1.2).
import sys, os
os.environ.setdefault('PASTA', 'v2-g6')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from folha2 import render, ul, nc, mn, sec, card, box, cards, passos

D1 = '8º sem D1 · NCS · '
D2 = '8º sem D2 · NCS · '


# ---------- traçado de ECG simples (SVG próprio) ----------
def ecg(ev, w=300, h=34, b=24, cor='#921827'):
    """ev: lista de ('P', x) | ('Q', x) estreito | ('W', x) largo | ('T', x)."""
    larg = {'P': 10, 'Q': 10, 'W': 18, 'T': 16}
    d, fim = f'M0,{b}', 0
    # QRS e T têm prioridade: a P que cair em cima some (fica "escondida")
    ocup = [(x, x + larg[t]) for t, x in ev if t != 'P']
    ev = [e for e in ev if e[0] != 'P' or all(e[1] + 10 <= a or e[1] >= z for a, z in ocup)]
    for t, x in sorted(ev, key=lambda e: e[1]):
        if x < fim:
            continue  # onda escondida dentro de outra
        d += f' L{x},{b}'
        if t == 'P':
            d += f' Q{x+5},{b-7} {x+10},{b}'
        elif t == 'Q':
            d += f' L{x+2},{b+3} L{x+5},{b-20} L{x+8},{b+5} L{x+10},{b}'
        elif t == 'W':
            d += f' L{x+4},{b-16} L{x+9},{b-19} L{x+14},{b+6} L{x+18},{b}'
        elif t == 'T':
            d += f' Q{x+8},{b-8} {x+16},{b}'
        fim = x + larg[t]
    d += f' L{w},{b}'
    return (f'<svg viewBox="0 0 {w} {h}" width="100%" aria-hidden="true">'
            f'<path d="{d}" fill="none" stroke="{cor}" stroke-width="1.3" stroke-linejoin="round"/></svg>')


def batida(x, pr, largo=False, t=True):
    e = [('P', x), ('W' if largo else 'Q', x + 10 + pr)]
    if t:
        e.append(('T', x + 10 + pr + (26 if largo else 20)))
    return e


def bloqueado(x):
    return [('P', x)]


S_1G = ecg(sum([batida(4 + 60 * i, 18) for i in range(5)], []))
S_M1 = ecg(batida(4, 4) + batida(52, 12) + batida(108, 20) + bloqueado(172) + batida(212, 4) + batida(260, 12))
S_M2 = ecg(batida(4, 6) + batida(56, 6) + bloqueado(108) + batida(160, 6) + batida(212, 6) + bloqueado(264))
S_TT = ecg([('P', x) for x in range(6, 300, 34)] + [('W', 22), ('T', 48), ('W', 112), ('T', 138), ('W', 202), ('T', 228)])


def tira(t, svg, x):
    return f'<div style="margin-bottom:1.6mm"><b>{t}</b> <span class="m">· {x}</span>{svg}</div>'


# ======================= 1. BLOQUEIOS NO ECG (C) =======================
render(D1 + 'SP 1.1 · Bloqueios no ECG - resumo em 1 folha', dict(layout='C', titulo='Bloqueios no ECG',
 sub='Sinoatrial, atrioventriculares, de ramo, divisionais e bifasciculares', vars='--fs:8.3pt;--lh:1.55;--gap:3.6mm',
 corpo=f'''
<div class="sec">{cards([('BAV 1º grau', 'PR &gt; 0,20 s', 'constante; todas as P conduzem'), ('Bloqueio de ramo', 'QRS ≥ 0,12 s', 'divisional isolado: QRS &lt; 0,12'), ('BDAS', 'além de −30°', '−45° é critério de certeza'), ('BDPI', 'além de +90°', 'raro: diagnóstico de exclusão')])}</div>
<div class="g2"><div>
{card('Os BAV no traçado (desenho esquemático)', tira('1º grau', S_1G, 'PR longo e igual') + tira('2º grau Mobitz I', S_M1, 'PR cresce até a P cair') + tira('2º grau Mobitz II', S_M2, 'PR fixo, P cai sem aviso') + tira('3º grau (BAVT)', S_TT, 'P e QRS sem relação'))}
{sec('BAV: o que cai', '''<ul><li><b>Mobitz I</b> (Wenckebach): nodal, QRS estreito, RR variável; bom prognóstico, raramente vira BAVT</li>
<li><b>Mobitz II</b>: pós-nodal/hissiano, bloqueio de ramo comum (mais o BRE); <span class="k">pode evoluir para BAVT</span></li>
<li><b>2:1</b> não define o tipo (não dá para ver o PR crescer) · <b>3:1</b> (2 P seguidas bloqueadas) = BAV <b>avançado</b></li>
<li><b>Avançado</b>: no mesmo traçado, períodos de tipo II e de BAVT</li>
<li><b>BAVT</b>: RR regular e lento (escape ~40 bpm), FC atrial &gt; ventricular e não múltipla; QRS largo se o escape é abaixo da bifurcação do His</li></ul>''')}
{nc(['2:1 não diz se é Mobitz I ou II.', 'RR irregular não é BAVT: pense em BAV parcial.', 'Bloqueio sinoatrial não é parada sinusal.', 'rSr′ com QRS estreito não é BRD completo.', 'BDPI só depois de excluir SVD e biotipo longilíneo.'])}
</div><div>
{sec('Ramos', '''<table><tr><th></th><th>BRD</th><th>BRE</th></tr>
<tr><td>V1</td><td>rSR′ (“M”), T negativa</td><td>rS ou QS (negativo)</td></tr>
<tr><td>Esquerda</td><td>S lenta em D1 e V6</td><td>R em torre em D1, aVL, V5, V6; T oposta</td></tr>
<tr><td>Eixo</td><td>desvio para a frente</td><td>normal</td></tr></table>
<p class="m" style="margin-top:2px">rSr′ com QRS &lt; 0,12 s = distúrbio do ramo direito (antigo “BRD incompleto”).</p>''')}
{sec('Divisionais e bifasciculares', '''<ul><li><b>BDAS</b>: rS em D2, D3 e aVF com S3 &gt; S2; o mais comum e a principal causa de desvio patológico à esquerda</li>
<li><b>BDPI</b>: rS em D1, qR inferior (R3 &gt; R2); excluir SVD, longilíneo, área inativa lateral</li>
<li><b>BDAM</b>: R crescente V1 &lt; V2 &lt; V3, eixo normal; raro</li>
<li><b>BRD + BDAS</b>: associação comum; manifestação inicial frequente na <span class="k">doença de Chagas</span> · BRD + BDPI: rara</li></ul>''')}
{sec('Bloqueio sinoatrial', '<p>Pausa sem P de ≈ <b>dobro</b> do ciclo normal, com frequência de base constante. Tipo II (mais comum): falha = múltiplo do PP · tipo I: PP encurta até a falha. Faz parte da doença do nó sinusal; não é parada sinusal.</p>')}
{mn([('Wenckebach avisa, Mobitz II não', 'PR cresce até cair × PR fixo e a P cai de repente.'), ('BAVT é divórcio', 'P e QRS, cada um no seu ritmo.'), ('Duas P seguidas caíram? É avançado', 'BAV 3:1 ou pior = BAV de alto grau.'), ('BRD faz M em V1; BRE ergue torre em V6', ''), ('Anterossuperior aponta para cima', 'BDAS: eixo além de −30°.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de bloqueios no ECG do 8º semestre (Friedmann, Eletrocardiograma em 7 aulas). Traçados: desenho esquemático.'))

# ======================= 2. DISTÚRBIOS DO RITMO (B) =======================
FLX_RI = '''<div class="flx">
<div class="fb esc">Arritmia na sala de emergência: tem pulso?</div><div class="fa">↓</div>
<div class="fr"><div><div class="fb vi">Sem pulso: TV sem pulso ou FV</div><div class="fp"><b>desfibrilar</b> 200 J bifásico / 360 J mono · RCP 2 min · adrenalina 1 mg a cada 3–5 min · amiodarona 300 → 150 mg</div></div>
<div><div class="fb ou">Com pulso e instável</div><div class="fp">hipotensão, EAP, angina, rebaixamento → <b>CVE sincronizada</b>: FA e flutter 200 J · TSVP 50–100 J · TV monomórfica 100 J · TV polimórfica: desfibrilar</div></div></div>
<div class="fa">↓ estável: olhe o QRS</div>
<div class="fr3"><div class="fb">Estreito regular<div class="fp">vagal → adenosina 6 → 12 mg → verapamil/diltiazem ou BB</div></div><div class="fb">Estreito irregular (FA)<div class="fp">frequência ou ritmo; &gt; 48 h: ACO 3 sem ou ECO-TE</div></div><div class="fb">Largo regular (TV)<div class="fp">amiodarona 150 mg em 10 min; corrigir K e Mg</div></div></div>
<div class="fa">↓ bradicardia sintomática</div>
<div class="fb ok"><b>Atropina</b> 0,5–1 mg (máx. 2–3 mg) se nodal → <b>marca-passo transcutâneo</b>; Mobitz II e BAVT de QRS largo: marca-passo (atropina não)</div></div>'''

render(D1 + 'SP 1.1 · Distúrbios do ritmo - resumo em 1 folha', dict(layout='B', titulo='Distúrbios do Ritmo',
 sub='FA, flutter, TSVP, TV, FV, taquicardia sinusal e BAV', vars='--fs:7.7pt;--lh:1.45;--gap:2.9mm',
 corpo=f'''<div class="gB"><div>
{card('Por onde começar', FLX_RI)}
{card('Fibrilação atrial', '''<ul><li>ECG: sem P, ondas f (350–600/min), <b>RR irregularmente irregular</b>; &gt; 30 s para chamar de FA</li>
<li><b>CHA₂DS₂-VA</b> (sem sexo): C, H, D, V, A (65–74) = 1 · A₂ (≥ 75) e S₂ (AVC/AIT) = 2. <b>≥ 2</b> anticoagula · 1 individualiza · 0 não. Anticoagula sempre: cardiomiopatia hipertrófica, amiloidose, hipertireoidismo</li>
<li>Frequência (idoso, assintomático): BB ou diltiazem/verapamil; alvo FC &lt; 80 (&lt; 110 se assintomático com FE preservada). ICFEr congesta: digoxina ou amiodarona</li>
<li>Ritmo (jovem, sintomático, ICFEr): &gt; 48 h ou tempo incerto → ACO 3 semanas ou ECO-TE; anticoagular 4 semanas depois. Amiodarona se cardiopatia; propafenona se coração normal</li>
<li><b>ACOD</b> 1ª linha; <b>varfarina</b> obrigatória na prótese mecânica e na estenose mitral reumática moderada/grave. AAS não previne AVC na FA</li></ul>''')}
{card('Flutter atrial', '<ul><li>Macrorreentrada no istmo cavotricuspídeo; átrio 240–320, <b>2:1 → ~150 bpm</b>; ondas F em dente de serra (anti-horário: negativas em DII, DIII, aVF)</li><li>Mesmo CHA₂DS₂-VA da FA · <b>ablação do istmo</b> é 1ª linha (sucesso &gt; 90%)</li><li>Classe IC sem bloquear o nó AV pode conduzir 1:1</li></ul>')}
{card('BAV na emergência', '<ul><li>IAM <b>inferior</b>: nó AV (coronária direita), transitório, responde à atropina · IAM <b>anterior</b>: infranodal, Mobitz II/BAVT de QRS largo, alto risco de assistolia</li><li>Marca-passo definitivo: Mobitz II, BAVT e bloqueios infranodais de alto grau, mesmo sem sintomas</li></ul>')}
</div><div>
{card('TSVP e Wolff-Parkinson-White', '''<ul><li>Regular, QRS estreito, 150–250 bpm, início e fim súbitos; <b>TRN ~60%</b> (P escondida, pseudo-r′ em V1, sinal do sapo) · TRAV ~30% (P retrógrada no ST)</li>
<li><b>Valsalva modificada</b>: soprar seringa 15 s e deitar com pernas a 45° (até 43%)</li>
<li><b>Adenosina 6 mg</b> em bolus + flush de 20 mL → 12 mg; evitar na asma grave/broncoespasmo, transplante recente, dipiridamol</li>
<li>WPW em sinusal: <b>PR curto + onda delta</b> + QRS largo. <span class="k">FA pré-excitada</span> (irregular, QRS largo): proibido bloquear o nó AV → CVE ou procainamida/amiodarona</li>
<li>Definitivo: ablação (&gt; 95% de cura)</li></ul>''')}
{card('Ventriculares e sinusal', '''<ul><li><b>TV</b>: ≥ 3 batimentos ventriculares &gt; 100 bpm; sustentada &gt; 30 s. Pistas: <b>dissociação AV</b>, captura, fusão, eixo na terra de ninguém, concordância precordial. Verapamil/diltiazem contraindicados no QRS largo</li>
<li><b>Torsades</b> (QT longo): sulfato de magnésio 1–2 g IV, K⁺ 4,5–5, marca-passo ou isoproterenol; suspender drogas que alargam o QT</li>
<li><b>FV</b>: só desfibrilação; nunca sincronizar. CDI na prevenção secundária e se FEVE ≤ 35% (≥ 40 dias pós-IAM)</li>
<li><b>Taquicardia sinusal</b>: trate a causa; nunca baixar a FC com BB no choque. Inapropriada: ivabradina</li></ul>''')}
{nc(['Sincronizar na FV impede o choque: desfibrile.', 'FA com WPW: nada de adenosina, BCC, BB ou digoxina.', 'Taquicardia sinusal é compensação, não alvo de remédio.', 'Atropina piora o bloqueio infranodal (Mobitz II, BAVT largo).', 'Propafenona e BCC não na ICFEr.'])}
{mn([('Sem pulso, desfibrila; com pulso instável, sincroniza', ''), ('Adenosina: 6, depois 12, sempre com flush', ''), ('Flutter 2:1 crava 150', 'FC regular de ~150 = procure as ondas F.'), ('Torsades pede magnésio', '1–2 g IV.'), ('A₂ e S₂ valem dois', '≥ 75 anos e AVC prévio no CHA₂DS₂-VA.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de distúrbios do ritmo do 8º semestre (SBC, Diretriz de FA 2025; ACC/AHA/ACCP/HRS 2023; SOCESP; Harrison; Friedmann).'))

# ======================= 3. TRATAMENTO DO IAM (B) =======================
FLX_IAM = '''<div class="flx">
<div class="fb esc">IAM com supra de ST · ECG em até 10 min do 1º contato</div><div class="fa">↓</div>
<div class="fr"><div><div class="fb ok">ICP primária (preferida)</div><div class="fp">PCM-dispositivo ≤ 90 min (chegada direta) ou ≤ 120 min (transferido)</div></div>
<div><div class="fb ou">ICP inviável em 120 min e sintomas &lt; 12 h</div><div class="fp"><b>fibrinolítico</b>, porta-agulha ≤ 30 min → transferir já para hemodinâmica</div></div></div>
<div class="fa">↓ 60–90 min após o lítico</div>
<div class="fr"><div><div class="fb ok">Reperfundiu</div><div class="fp">dor some; ST cai ≥ 50% (anterior) ou ≥ 70% (inferior) → angiografia em 2–24 h</div></div>
<div><div class="fb vi">Falhou</div><div class="fp">ICP de <b>resgate</b> imediata (via radial); nunca repetir o lítico</div></div></div>
<div class="fa">↓</div>
<div class="fb"><b>Choque cardiogênico</b>: revascularizar o vaso culpado (ICP ou CRM) em qualquer tempo; não tratar a artéria não culpada na hora; BIA ou ECMO de rotina, não</div></div>'''

render(D1 + 'SP 1.2 · Tratamento do IAM - resumo em 1 folha', dict(layout='B', titulo='Tratamento do IAM',
 sub='MONABCH atualizado, reperfusão, fibrinolíticos e falha de reperfusão', vars='--fs:8.05pt;--lh:1.5;--gap:3.3mm',
 corpo=f'''<div class="gB"><div>
{card('Reperfusão: angioplastia × trombólise', FLX_IAM)}
{card('Sem supra (SCASSST): estratégia invasiva', '<ul><li><b>Imediata (&lt; 2 h)</b>: angina refratária, instabilidade hemodinâmica ou elétrica</li><li><b>Precoce (&lt; 24 h)</b>: GRACE &gt; 140, troponina subindo, ST dinâmico</li><li>Demais: angiografia antes da alta · fibrinolítico <b>não</b> na infra isolada de ST (exceto IAM posterior)</li></ul>')}
{card('Fibrinolíticos', '''<ul><li><b>Tenecteplase</b>: bolus único por peso, 30 mg (&lt; 60 kg) a 50 mg (&gt; 90 kg); meia dose se &gt; 75 anos</li>
<li><b>Alteplase</b>: 15 mg bolus → 0,75 mg/kg em 30 min → 0,5 mg/kg em 60 min (máx. 100 mg)</li>
<li>Contraindicação absoluta: AVC hemorrágico prévio, AVCi &lt; 3 meses, lesão ou neoplasia intracraniana, suspeita de dissecção de aorta, sangramento ativo</li></ul>''')}
{nc(['Oxigênio de rotina com SpO₂ ≥ 90% não ajuda e pode piorar.', 'Lítico que falhou pede resgate, não 2ª dose.', 'Prasugrel é contraindicado com AVC ou AIT prévio.', 'Fondaparinux não pode ser o único anticoagulante na ICP.', 'AINE (exceto AAS) aumenta eventos: contraindicado.', 'Choque: abrir só o vaso culpado na hora.'])}
</div><div>
{card('MONABCH atualizado (primeiras 24 h)', '''<table><tr><th></th><th>O que fazer</th></tr>
<tr><td>M</td><td>Morfina 2–4 mg IV só na dor refratária; cuidado no IAM de VD</td></tr>
<tr><td>O</td><td>O₂ só se SpO₂ &lt; 90%</td></tr>
<tr><td>N</td><td>Nitrato SL 0,3–0,4 mg até 3× se PAS ≥ 90; não no IAM de VD nem após iPDE5 (24 h sildenafila, 48 h tadalafila)</td></tr>
<tr><td>A</td><td>AAS 162–325 mg mastigado → 75–100 mg/dia + P2Y12: ticagrelor 180 → 90 mg 12/12 h ou prasugrel 60 → 10 mg (na ICP)</td></tr>
<tr><td>B</td><td>Betabloqueador oral em 24 h, se não houver Killip II–IV, BAV 2º/3º grau, FC &lt; 50 ou broncoespasmo</td></tr>
<tr><td>C</td><td>Clopidogrel obrigatório na fibrinólise: 300 mg se ≤ 75 anos; sem ataque se &gt; 75</td></tr>
<tr><td>H</td><td>HNF 60 UI/kg (máx. 4.000) + 12 UI/kg/h na ICP · enoxaparina 1 mg/kg 12/12 h no IAMSSST e na fibrinólise · fondaparinux 2,5 mg</td></tr></table>
<p style="margin-top:3px">+ <b>Estatina alta intensidade</b> para todos (atorvastatina 40–80 ou rosuvastatina 20–40) · <b>IECA/BRA</b> em 24 h se FE ≤ 40%, HAS, DM ou IAM anterior · espironolactona se FE ≤ 40% com IC ou DM.</p>''')}
{card('Depois da fase aguda', '<ul><li><b>CDI</b> se FEVE ≤ 40%, a partir de 40 dias pós-IAM e 90 dias pós-revascularização</li><li><b>Marca-passo definitivo</b>: Mobitz II, BAV de alto grau, bloqueio de ramo alternante ou BAVT persistente/infranodal</li><li>FV/TV sustentada &gt; 48 h após a reperfusão = maior risco de morte</li></ul>')}
{mn([('10, 30, 90, 120', 'ECG em 10 min · agulha em 30 · balão em 90 · transferido em 120.'), ('No VD, sem Nitrato e cuidado com a Morfina', ''), ('Cinquenta na frente, setenta embaixo', 'queda do ST que mostra reperfusão: anterior ≥ 50%, inferior ≥ 70%.'), ('PrAsugrel é Proibido após AVC', ''), ('Lítico chama Clopidogrel', 'é o P2Y12 obrigatório na fibrinólise.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de tratamento do IAM e no capítulo de tratamento do resumo de síndrome coronariana aguda do 8º semestre (ACC/AHA/ACEP/NAEMSP/SCAI 2025).'))

# ======================= 4. CRISE HIPERTENSIVA (C) =======================
render(D1 + 'SP 1.3 · Crise hipertensiva - resumo em 1 folha', dict(layout='C', titulo='Crise Hipertensiva',
 sub='Emergência, elevação sem lesão aguda e pseudocrise (Diretriz Brasileira 2025)', vars='--fs:8pt;--lh:1.5;--gap:3.2mm',
 corpo=f'''
<div class="sec">{cards([('Crise hipertensiva', '≥ 180/110', 'quem define a gravidade é a LOA aguda'), ('1ª hora', 'até −25%', '160/100–110 em 2–6 h; normal em 24–48 h'), ('Dissecção de aorta', 'PAS &lt; 120', 'e FC &lt; 60 em até 20 min'), ('EAP e catecolaminas', 'PAS &lt; 140', 'já na 1ª hora')])}</div>
<div class="sec"><h2>Três quadros, três condutas</h2><table><tr><th></th><th>LOA aguda</th><th>Conduta</th></tr>
<tr><td>Emergência hipertensiva</td><td>Sim, progressiva, risco de morte</td><td>UTI, droga IV, monitorização (ideal: PA invasiva)</td></tr>
<tr><td>Elevação importante sem LOA (antiga urgência)</td><td>Não</td><td>Observar 30 min em local calmo → oral rápido (clonidina ou captopril) → reavaliar em 1–7 dias, alvo &lt; 160/100</td></tr>
<tr><td>Pseudocrise</td><td>Não; dor, ansiedade, enxaqueca</td><td>Tratar o gatilho (analgesia, ansiólise); sem anti-hipertensivo injetável</td></tr></table></div>
<div class="g2"><div>
{sec('Investigar a LOA', '<p>PA nos dois braços (diferença &gt; 15–20 mmHg sugere dissecção) · <b>fundo de olho</b> obrigatório · ECG, RX de tórax, hemograma (esquistócitos), troponina, creatinina, K⁺, urina I; β-hCG na mulher fértil. Déficit focal, convulsão ou papiledema → TC/RM de crânio; suspeita de dissecção → angioTC.</p>')}
{sec('Exceções às metas gerais', '''<ul><li><b>Dissecção</b>: betabloqueador IV (esmolol, metoprolol) <b>antes</b> do nitroprussiato; morfina para a dor</li>
<li><b>EAP</b>: nitroglicerina IV + furosemida ± VNI</li>
<li><b>Catecolaminas</b> (feocromocitoma, cocaína, suspensão de clonidina): benzodiazepínico + nitrato; feocromocitoma: α-bloqueio (doxazosina) antes de qualquer BB</li>
<li><b>AVCi</b>: para trombolisar &lt; 185/110 e manter &lt; 180/105 por 24 h; sem trombólise, só tratar se ≥ 220/120 (−15% em 24 h)</li>
<li><b>AVCH</b>: PAS 150–220 → &lt; 140 · &gt; 220 → &lt; 180</li>
<li><b>Gestante</b> ≥ 160/110 por &gt; 15 min: hidralazina 5 mg IV a cada 20–30 min (até 15 mg) ou nifedipina 10 mg VO; MgSO₄; IECA, BRA e atenolol contraindicados</li>
<li><b>SCA</b>: nitroglicerina ± BB; PAS &lt; 140 sem cair abaixo de 120</li>
<li><b>Encefalopatia</b>: −20–25% na 1ª h, 160/100 em até 48 h · <b>HA maligna</b> (papiledema): nitroprussiato, depois IECA/BRA</li></ul>''')}
{nc(['O número não define emergência: a LOA define.', 'Nifedipina de liberação rápida é proscrita.', 'Sem LOA não precisa de UTI nem de injetável.', 'Na dissecção, vasodilatador sozinho dá taquicardia reflexa: BB primeiro.', 'No AVCi sem trombólise, baixar a PA amplia o infarto.', 'Feocromocitoma: BB isolado sobe a PA (α sem oposição).'])}
</div><div>
{sec('Drogas IV', '''<table><tr><th>Droga</th><th>Quando</th></tr>
<tr><td>Nitroprussiato 0,25–10 µg/kg/min</td><td>A maioria; risco de cianeto; evitar no IAM (roubo coronariano)</td></tr>
<tr><td>Nitroglicerina 5–100 µg/min</td><td>SCA e EAP; não no IAM de VD nem após iPDE5</td></tr>
<tr><td>Esmolol / metoprolol</td><td>Dissecção (antes do NPS) e SCA</td></tr>
<tr><td>Hidralazina</td><td>Eclâmpsia; evitar na coronariopatia e na dissecção</td></tr>
<tr><td>Furosemida 20–60 mg</td><td>EAP e hipervolemia</td></tr></table>''')}
{sec('Depois da crise', '<p>Desmame do IV para via oral em 24–48 h; esquema padrão em comprimido único: <b>IECA ou BRA + BCC + tiazídico</b>. Meta de longo prazo &lt; 130/80. Investigar causa secundária (renal, renovascular, hiperaldosteronismo, apneia do sono).</p>')}
{mn([('Quem manda é a LOA, não o número', ''), ('25 na 1ª hora, 160/100 até a 6ª, normal em 2 dias', ''), ('Dissecção: 120 em 20, FC abaixo de 60', ''), ('Feocromocitoma: alfa antes de beta', ''), ('AVCi: 185 para trombolisar, 220 para mexer', '')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de crise hipertensiva do 8º semestre (Diretriz Brasileira de Hipertensão Arterial 2025; AHA/ACC 2025; ESC 2024; Guyton & Hall).'))

# ======================= 5. EMERGÊNCIAS OBSTÉTRICAS (A) =======================
render(D1 + 'SP 1.4 · Emergências obstétricas - eclâmpsia, HPP, DPP e comprometimento fetal persistente - resumo em 1 folha',
 dict(layout='A', titulo='Emergências Obstétricas', sub='Pré-eclâmpsia, eclâmpsia, HELLP, DPP, comprometimento fetal persistente e HPP',
 vars='--fs:8.5pt;--lh:1.54;--gap:3.7mm', corpo=f'''<div class="gL"><div>
{sec('Pré-eclâmpsia', '''<ul><li><b>≥ 140/90 após 20 semanas</b> + proteinúria (proteína/creatinina ≥ 0,3, 24 h ≥ 300 mg ou fita ≥ 2+) <b>ou</b> lesão de órgão-alvo (plaquetas, fígado, rim, EAP, sintomas neurológicos) <b>ou</b> disfunção placentária (RCF, Doppler)</li>
<li>Gravidade: PA ≥ 160/110 persistente após 15 min, iminência de eclâmpsia (cefaleia, escotomas, hiper-reflexia), epigastralgia · sFlt-1/PlGF &lt; 38 exclui por 1 semana</li>
<li><b>Crise</b> ≥ 160/110: nifedipino 10 mg VO, repetir 10 mg a cada 20–30 min, máx. 30 mg (preferencial) ou hidralazina 5 mg IV a cada 20 min; NPS se refratária ou EAP. Manutenção: metildopa, nifedipino retard</li>
<li>Prevenção: <b>AAS 100–150 mg</b> à noite, de 12–16 até 36 semanas, no alto risco (PE prévia, HAS, DM, DRC, lúpus, SAF, gemelar) ou ≥ 2 fatores moderados</li>
<li>Parto: sem gravidade com 37 sem · com gravidade: &lt; 24 sem interromper; 24–34 conservador + corticoide; parto já se eclâmpsia, HELLP, EAP, HAS refratária a 3 drogas, piora renal, DPP ou vitalidade fetal grave. PE não obriga cesárea</li></ul>''')}
{sec('Eclâmpsia e sulfato de magnésio', '''<ul><li>Convulsão tônico-clônica (ou coma) com PE, excluídas outras causas; imagem se refratária ao Mg, déficit focal ou &lt; 20 semanas</li>
<li><b>Pritchard</b>: 4 g IV + 10 g IM (5 g em cada glúteo), depois 5 g IM 4/4 h · <b>Zuspan</b>: 4 g IV em 15–20 min + 1–2 g/h. Manter 24 h após o parto</li>
<li>Seguro se reflexo patelar presente, FR ≥ 16 irpm e diurese ≥ 25 mL/h; intoxicação → suspender + <b>gluconato de cálcio</b> · neuroproteção fetal &lt; 32 semanas</li></ul>''')}
{sec('HELLP (Sibai)', '''<p>Hemólise (DHL &gt; 600, BT &gt; 1,2, esquizócitos) + AST/ALT &gt; 70 + plaquetas &lt; 100 mil. <b>Martin</b>: I ≤ 50 mil · II 50–100 mil · III 100–150 mil. ≥ 34 sem: parto após estabilizar; MgSO₄; cristaloide ≤ 100 mL/h; plaquetas &gt; 50 mil para cesárea e &gt; 20 mil para parto vaginal; bloqueio contraindicado &lt; 70 mil.</p>''')}
{sec('DPP e comprometimento fetal', '''<ul><li><b>DPP</b>: dor súbita, sangue escuro (oculto em 20%), hipertonia (“útero lenhoso”), choque desproporcional, CIVD; útero de Couvelaire. Feto vivo viável → <b>cesárea</b> (vaginal só se expulsão iminente) · feto morto → vaginal preferencial em 4–6 h</li>
<li><b>Fetal</b>: parto se PBF ≤ 4, DIP II repetitivas, variabilidade ausente, sinusoidal, STV &lt; 2,6 ms ou ducto venoso com onda a ausente/reversa · <b>diástole reversa</b> 30–32 sem · <b>diástole zero</b> 32–34 · centralização ou PFE &lt; p3: 36–38. Via: cesárea nos graves</li></ul>''')}
{sec('Hemorragia pós-parto', '''<ul><li>&gt; 500 mL (vaginal) ou &gt; 1.000 mL (cesárea) ou instabilidade · maciça: &gt; 2.000 mL/24 h, ≥ 4 CH, queda de Hb ≥ 4 g/dL ou coagulopatia</li>
<li>Prevenção: <b>ocitocina 10 UI IM/IV</b> logo após o nascimento · chamar ajuda, 2 acessos, sonda vesical, exames, <b>ácido tranexâmico</b> precoce, transfusão</li>
<li>Tono: massagem bimanual → ocitocina → misoprostol 800 mcg SL ou 600 mcg retal (ergot não na hipertensa) → balão de Bakri → B-Lynch/ligaduras → histerectomia · Tecido: revisão da cavidade; acretismo não se arranca · Trauma: suturar · Trombina: repor fatores</li></ul>''')}
</div><div>
{nc(['HELLP pode vir sem hipertensão e sem proteinúria.', 'Dor em epigástrio ou hipocôndrio direito após 20 sem: pense em HELLP.', 'Pré-eclâmpsia não é indicação de cesárea.', 'Reflexo patelar abolido: pare o magnésio.', 'DPP: o sangue visível engana, o choque não.', 'Placenta acreta não se arranca.'])}
{mn([('HELLP', '<b>H</b>emólise, <b>EL</b> = enzimas hepáticas altas, <b>LP</b> = plaquetas baixas.'), ('Os 4 T: Tono, Trauma, Tecido, Trombina', 'o tono responde por 70–80%.'), ('Magnésio seguro tem 3 R', '<b>R</b>eflexo presente, <b>R</b>espiração ≥ 16, <b>R</b>im com ≥ 25 mL/h.'), ('Pritchard vai no bumbum, Zuspan fica na veia', ''), ('Reversa nasce antes da zero', 'diástole reversa 30–32 sem; zero 32–34.')])}
{box('Números que caem', '<p>PE ≥ 140/90 · grave ≥ 160/110<br>P/C ≥ 0,3 · 24 h ≥ 300 mg<br>HELLP: DHL &gt; 600, AST &gt; 70, plaq. &lt; 100 mil<br>HPP 500 / 1.000 mL</p>')}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de emergências obstétricas do 8º semestre (Ministério da Saúde, Gestação de alto risco 2022; Tratado de Obstetrícia FEBRASGO 2025).'))

# ======================= 6. DIABETES MELLITUS (A) =======================
render(D2 + 'SP 2.1 · Diabetes Mellitus - resumo em 1 folha', dict(layout='A', titulo='Diabetes Mellitus',
 sub='Diagnóstico, DM1 × DM2, tratamento do DM2, insulina e metas (SBD 2026)', vars='--fs:7.7pt;--lh:1.48;--gap:3mm',
 corpo=f'''<div class="gL"><div>
{sec('Diagnóstico (mg/dL)', '''<table><tr><th>Exame</th><th>Normal</th><th>Pré-DM</th><th>DM</th></tr>
<tr><td>Glicemia de jejum</td><td>&lt; 100</td><td>100–125</td><td>≥ 126</td></tr>
<tr><td>HbA1c</td><td>&lt; 5,7%</td><td>5,7–6,4%</td><td>≥ 6,5%</td></tr>
<tr><td>TTGO 1 h (preferido)</td><td>&lt; 155</td><td>155–208</td><td>≥ 209</td></tr>
<tr><td>TTGO 2 h</td><td>&lt; 140</td><td>140–199</td><td>≥ 200</td></tr></table>
<p style="margin-top:2px">Assintomático: <b>2 exames</b> alterados (dois diferentes na mesma amostra ou o mesmo repetido). Sintomas + glicemia ao acaso ≥ 200: um basta. HbA1c engana em anemia, hemoglobinopatia, gestação, DRC e transfusão.</p>''')}
{sec('Rastreio e pré-diabetes', '<ul><li>Rastrear <b>todos ≥ 35 anos</b>; &lt; 35 com sobrepeso + ≥ 1 fator (familiar de 1º grau, DCV, HAS, HDL &lt; 35, TG &gt; 250, SOP, acantose) e quem teve pré-DM ou DMG</li><li>Repetir: 3 anos se normal e baixo risco · anual no pré-DM · 6 meses se só 1 exame no critério</li><li>Pré-DM: ~25% viram DM2 em 3–5 anos. MEV para todos; metformina se &lt; 60 anos, IMC &gt; 35, DMG prévio, síndrome metabólica, HAS ou GJ &gt; 110</li></ul>')}
{sec('DM1 × DM2', '''<table><tr><th></th><th>DM1</th><th>DM2</th></tr>
<tr><td>Frequência</td><td>5–10%</td><td>90–95%</td></tr>
<tr><td>Mecanismo</td><td>Destruição autoimune da célula β</td><td>Resistência à insulina + falência progressiva da célula β</td></tr>
<tr><td>Laboratório</td><td>Anti-GAD +; peptídeo C &lt; 0,6 ng/mL</td><td>Anticorpos −; peptídeo C &gt; 0,6</td></tr>
<tr><td>Crise típica</td><td>CAD</td><td>Estado hiperosmolar</td></tr></table>
<p style="margin-top:2px"><b>LADA</b>: adulto com anticorpo +, sem insulina por ≥ 6 meses · <b>MODY</b>: &lt; 25 anos, herança dominante em 2–3 gerações; GCK leve (geralmente sem tratamento); HNF1A/HNF4A respondem a sulfonilureia.</p>''')}
{sec('Tratamento do DM2 (SBD)', '''<ul><li>Avaliar risco cardiorrenal (RCR), IMC, HbA1c, TFG e albuminúria → <b>metformina + MEV</b> desde o início (TFG ≥ 30; 30–45: máx. 1 g/dia)</li>
<li>HbA1c ≥ 7,5% ao diagnóstico → terapia dupla · <b>RCR aumentado → iSGLT2</b> independentemente da HbA1c · IMC ≥ 30 → AR GLP-1 ou tirzepatida</li>
<li>Reavaliar a cada 3 meses: dupla → tripla → quádrupla → insulina. Muito sintomático (insulinopenia) → insulina já</li>
<li>Não associar AR GLP-1, tirzepatida e iDPP-4 entre si · SUS: metformina → sulfonilureia → dapagliflozina; insulina se HbA1c &gt; 9% ou GJ ≥ 300</li></ul>''')}
{sec('Insulina', '<ul><li><b>DM1</b>: basal-bolus desde o diagnóstico, 0,4–1,0 U/kg/dia (basal 30–50%). Fator de sensibilidade = 1.800 ÷ dose total; relação insulina/carboidrato = 400 ÷ dose total</li><li><b>DM2</b>: NPH ao deitar 10 U ou 0,1–0,2 U/kg, mantendo os orais; +2 U a cada 3 dias até jejum 80–130. Basal &gt; 0,5 U/kg/dia = excesso de basal</li></ul>')}
{sec('Complicações crônicas', '<p>Rastreio anual de <b>retina</b> (fundo de olho com pupila dilatada), <b>rim</b> (albumina/creatinina urinária + TFG), <b>nervo</b> (monofilamento 10 g, diapasão 128 Hz) e <b>pé</b>: no DM1, 5 anos após o diagnóstico; no DM2, já ao diagnóstico (8–16% já têm retinopatia). Cair 10% na HbA1c reduz a retinopatia em 40%.</p>')}
</div><div>
{nc(['Uma glicemia ao acaso ≥ 200 só basta com sintomas.', 'Adulto magro com início abrupto pode ser DM1 (ou LADA).', 'Suspeita de DM1 ou CAD: insulina sem esperar anticorpos.', 'iSGLT2 entra pelo risco cardiorrenal, não pela HbA1c.', 'DM2 rastreia retina, rim e nervo já ao diagnóstico; DM1 após 5 anos.', 'Metformina para com TFG &lt; 30.'])}
{mn([('Os 4 P', '<b>P</b>oliúria, <b>P</b>olidipsia, <b>P</b>olifagia e <b>P</b>erda de peso.'), ('Fez 35, rastreia', 'rastreio universal a partir dos 35 anos.'), ('Peptídeo C abaixo de 0,6: a fábrica fechou', 'deficiência grave de insulina (DM1).'), ('1.800 corrige, 400 come', 'fator de sensibilidade e relação insulina/carboidrato.')])}
{card('Efeito colateral que cai', '<ul><li><b>iSGLT2</b>: infecção geniturinária, CAD euglicêmica</li><li><b>AR GLP-1</b>: gastrointestinal; contraindicado no carcinoma medular de tireoide</li><li><b>Sulfonilureia</b>: hipoglicemia e ganho de peso</li><li><b>Pioglitazona</b>: retenção hídrica, IC, fraturas</li><li><b>Saxagliptina</b>: mais internação por IC · <b>metformina</b>: B12</li></ul>')}
{box('Metas (adulto)', '<p>HbA1c &lt; 7% (idoso saudável &lt; 7,5; comprometido &lt; 8)<br>Jejum 80–130 · 2 h pós &lt; 180<br>Tempo no alvo &gt; 70% · &lt; 70 mg/dL: &lt; 4%<br>HbA1c 7% ≈ glicemia média 154</p>')}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de diabetes mellitus do 8º semestre, revisado em 20/10/2026 (SBD 2026; PCDT DM2 2026; ADA Standards of Care 2026; Guyton & Hall).'))

# ======================= 7. EMERGÊNCIAS NO DIABETES (C) =======================
render(D2 + 'SP 2.2 · Emergências no diabetes - resumo em 1 folha', dict(layout='C', titulo='Emergências no Diabetes',
 sub='Cetoacidose, CAD euglicêmica, estado hiperosmolar e hipoglicemia (SBD 2026)', css='.cd .n{font-size:12.5pt}', vars='--fs:7.75pt;--lh:1.46;--gap:3mm',
 corpo=f'''
<div class="sec">{cards([('CAD', 'glicemia &gt; 200', 'pH &lt; 7,3 e/ou HCO₃⁻ &lt; 15; cetonemia ≥ 3 mmol/L'), ('Hiperosmolar (EHH)', 'glicemia &gt; 600', 'Osm efetiva &gt; 320; pH &gt; 7,3, cetonemia &lt; 3'), ('CAD euglicêmica', 'glicemia &lt; 200', 'pH &lt; 7,3, HCO₃⁻ &lt; 18; principal causa: iSGLT2'), ('Hipoglicemia', 'glicemia &lt; 70', 'nível 2 &lt; 54 · nível 3 precisa de ajuda')])}</div>
<div class="sec"><h2>O passo a passo da CAD</h2>{passos([('Hidratar', 'SF 0,9% 15–20 mL/kg na 1ª hora; depois Na⁺ corrigido &lt; 150 → SF 0,9%; ≥ 150 → NaCl 0,45% (250–500 mL/h)'), ('Potássio', '<span class="k">&lt; 3,3: não iniciar insulina</span>, repor · 3,3–5,2: 10–20 mEq por litro · &gt; 5,2: não repor, checar 2/2 h'), ('Insulina', 'regular IV 0,1 U/kg/h (bolus opcional); glicemia deve cair 50–70 mg/dL/h'), ('Glicose', 'glicemia 200–250 → SG 5% e insulina 0,02–0,05 U/kg/h; <span class="k">não desligar</span> até resolver a cetose')])}</div>
<div class="g2"><div>
{sec('CAD × EHH', '''<table><tr><th></th><th>CAD</th><th>EHH</th></tr>
<tr><td>Instalação</td><td>Horas a dias; DM1 jovem</td><td>Dias a semanas; DM2 idoso</td></tr>
<tr><td>Clínica</td><td>Kussmaul, hálito cetônico, dor abdominal, vômitos</td><td>Desidratação grave, rebaixamento, sinais focais, convulsão</td></tr>
<tr><td>Ânion gap</td><td>&gt; 12</td><td>Normal ou pouco alterado</td></tr>
<tr><td>Insulina</td><td>0,1 U/kg/h</td><td>0,05 U/kg/h, sem bolus; glicose com 250–300</td></tr>
<tr><td>Mortalidade</td><td>&lt; 1%</td><td>10–20%</td></tr></table>''')}
{sec('As contas', '<ul><li><b>AG</b> = Na⁺ − (Cl⁻ + HCO₃⁻); normal 4–12</li><li><b>Na⁺ corrigido</b> = Na⁺ + 1,6 × (glicemia − 100) ÷ 100 (fator 2,4 se glicemia &gt; 400)</li><li><b>Osm efetiva</b> = 2 × Na⁺ + glicemia ÷ 18; &gt; 320 define EHH; coma com Osm &lt; 320 → procure outra causa</li></ul>')}
{sec('Detalhes que caem', '<ul><li>Bicarbonato só se pH &lt; 6,9 · fosfato só se &lt; 1 mg/dL, anemia, ICC ou hipóxia</li><li>Resolução: alerta, comendo, acidose e cetose resolvidas → basal-bolus SC e manter a IV 1–2 h (≥ 2 h com regular); evitar degludeca</li><li><b>Edema cerebral</b> nas primeiras 12 h: cefaleia, confusão, tríade de Cushing → manitol 0,25–0,5 g/kg</li><li><b>CAD-E</b>: suspender o iSGLT2 e dar glicose desde o início; não deixar a glicemia cair abaixo de 200</li><li><b>Cetonemia</b>: &lt; 0,6 nada · 0,6–1,5 manejo em casa · 1,6–3,0 CAD iminente, hospital · &gt; 3,0 protocolo de CAD</li></ul>')}
{sec('EHH: o que muda', '<p>Perda de água maior (100–220 mL/kg): SF 0,9% 15–20 mL/kg na 1ª–2ª h, depois 10–14 mL/kg/h. Glicemia cai no máximo 90–120 mg/dL/h e a osmolalidade 3–8 mOsm/kg/h (risco de edema cerebral e mielinólise pontina). Manter glicemia 200–300 até Osm &lt; 315, paciente alerta e comendo.</p>')}
</div><div>
{sec('Hipoglicemia', '<ul><li>Nível 1 (54–69): <b>15 g</b> de carboidrato rápido (1 colher de sopa de açúcar, 150 mL de suco) e repetir a glicemia em 15 min</li><li>Nível 2 (&lt; 54), consciente: 30 g (PCDT) · nível 3: <b>glucagon</b>; nunca insulina</li><li>Com acarbose, só glicose pura · depois, lanche (risco de recorrência)</li></ul>')}
{nc(['K⁺ normal na admissão não é estoque normal: déficit de 3–6 mmol/kg.', 'Cetonúria engana: mede só acetoacetato e “piora” com o tratamento.', 'Acidose hiperclorêmica após muito SF não é CAD persistente.', 'Bicarbonato não é rotina.', 'Leucocitose &gt; 25 mil sugere infecção, não só CAD.'])}
{mn([('Potássio abaixo de 3,3, insulina fica no banco', 'repor antes de começar.'), ('CAD: 200, 7,3, 15 e 3', 'glicemia, pH, bicarbonato e cetonemia.'), ('EHH é 600 e 320', 'idoso seco e confuso.'), ('Regra dos 15', '15 g de açúcar, espera 15 min, mede de novo.'), ('Bateu 250, põe açúcar no soro', 'e baixa a insulina, sem desligar.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de emergências no diabetes do 8º semestre (SBD 2026: CAD, CAD euglicêmica e SHHNC; Umpierrez, Diabetes Care 2024; PCDT DM2 2026; ADA 2026).'))
