# Folhas únicas do 8º D1 · TOCE no estilo 2 (layouts A/B/C + Não confunda + mnemônicos)
# Conteúdo SÓ dos resumos publicados (PDFs do Drive, versão 2026.2). Pedido da Laura (22/10/2026).
import sys, os
os.environ.setdefault('PASTA', 'toce8-v2')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from folha2 import render, ul, nc, mn, sec, card, box, cards, passos

N = '8º sem D1 · TOCE · '

# ======================= HEMORRAGIA DIGESTIVA (C) =======================
TREITZ = '''<svg viewBox="0 0 130 160" width="100%" aria-hidden="true" font-family="Inter">
<path d="M62 4 C62 28 60 34 54 44" stroke="#c9a96a" stroke-width="7" fill="none" stroke-linecap="round"/>
<path d="M54 44 C32 60 42 82 64 76 C84 70 86 54 74 50" stroke="#c9a96a" stroke-width="13" fill="none" stroke-linecap="round"/>
<path d="M74 50 C72 66 66 72 68 84 C72 96 92 92 88 104" stroke="#c9a96a" stroke-width="6" fill="none" stroke-linecap="round"/>
<path d="M88 104 C72 112 42 104 32 120 C24 136 48 146 72 140 C94 134 100 120 94 110" stroke="#dcc6c9" stroke-width="7" fill="none" stroke-linecap="round"/>
<line x1="16" y1="97" x2="126" y2="97" stroke="#921827" stroke-width="1.4" stroke-dasharray="4 3"/>
<text x="126" y="93" font-size="8" text-anchor="end" fill="#921827" font-weight="600">ângulo de Treitz</text>
<text x="4" y="30" font-size="10" fill="#8a5f12" font-weight="600">HDA</text>
<text x="4" y="122" font-size="10" fill="#921827" font-weight="600">HDB</text>
<text x="70" y="16" font-size="6.5" fill="#76696b">esôfago</text>
<text x="20" y="62" font-size="6.5" fill="#76696b">estômago</text>
<text x="92" y="74" font-size="6.5" fill="#76696b">duodeno</text>
<text x="34" y="157" font-size="6.5" fill="#76696b">jejuno, íleo, cólon</text></svg>'''

render(N + 'Hemorragia digestiva - resumo em 1 folha', dict(layout='C', titulo='Hemorragia Digestiva',
 sub='Alta e baixa · estabilizar, estratificar, localizar e tratar', vars='--fs:7.95pt;--lh:1.5;--gap:3.2mm',
 corpo=f'''
<div class="vis sec" style="--vw:36mm"><div>{TREITZ}</div><div>{cards([('Transfundir se', '&lt; 7 g/dL', '&lt; 8 no cardiopata; varizes ~8'), ('Glasgow-Blatchford', '0–1', 'alta com seguimento; ≥ 2 interna'), ('EDA', '&lt; 24 h', '12 h no alto risco')])}
<p class="m" style="margin-top:2.5mm">Hematêmese e melena = <b>alta</b> · hematoquezia = <b>baixa</b> · enterorragia com choque pode ser <b>HDA maciça</b>.</p></div></div>
<div class="sec"><h2>O passo a passo</h2>{passos([('Estabilizar', 'ABCDE, 2 acessos calibrosos, cristaloide; corrigir coagulopatia; ácido tranexâmico não'), ('Estratificar', 'Blatchford antes da EDA (ureia, Hb, PAS, FC, melena, síncope); Rockall depois'), ('Localizar', 'EDA na alta; na baixa, colonoscopia ou angioTC se instável'), ('Tratar', 'endoscopia → embolização → cirurgia')])}</div>
<div class="g2"><div class="sec"><h2>HDA</h2>
<p><span class="k">Úlcera péptica</span> é a nº 1 (37–55%); depois erosões, varizes, esofagite, Mallory-Weiss.</p>
<table><tr><th>Aspecto na EDA</th><th>Conduta</th></tr><tr><td>Ativo ou vaso visível</td><td>Terapia endoscópica + IBP 80 mg + 8 mg/h por 72 h</td></tr><tr><td>Coágulo aderente</td><td>Sem consenso; IBP alto</td></tr><tr><td>Mancha plana, base limpa</td><td>Só IBP</td></tr></table>
<p style="margin-top:2px"><span class="k">Varizes</span> (cirrose, UTI): vasoativo já (octreotida/terlipressina), antibiótico 7 dias, <b>ligadura</b>. Refratário: balão de Sengstaken (ponte, máx. 24 h) e <b>TIPS</b>. Prevenção: betabloqueador não seletivo + ligadura seriada.</p></div>
<div class="sec"><h2>HDB</h2>
<p><span class="k">Doença diverticular</span> (principal &gt; 70 anos; 80% para sozinha) e <span class="k">angiodisplasia</span>; hemorroida, fissura, câncer, DII.</p>
<ul><li><b>Índice de choque</b> (FC/PAS) &gt; 1 → angioTC → embolização; negativa → EDA (11–15% têm fonte alta)</li><li>Estável: <b>Oakland ≤ 8</b> → alta e colonoscopia ambulatorial; &gt; 8 interna</li><li>Colonoscopia após estabilizar (clipe no divertículo)</li><li>Sem controle: cirurgia <b>segmentar</b> se o local é conhecido; <b>colectomia subtotal</b> se não</li></ul></div></div>
<div class="g2"><div>{nc(['Enterorragia com choque: afaste a fonte alta antes do cólon.', 'Ureia sobe na HDA: sangue digerido é proteína.', 'Adrenalina isolada não basta na úlcera.', 'Base limpa não leva terapia endoscópica.', 'Transfundir demais nas varizes sobe a pressão portal.', 'Balão não funciona no Mallory-Weiss (sangramento arterial).', 'Hemorroida não explica HDB volumosa.'])}</div>
<div>{mn([('Treitz é a fronteira', 'acima sangra pela boca ou fica preto (melena); abaixo sai vermelho.'), ('Varizes pedem VAL', '<b>V</b>asoativo, <b>A</b>ntibiótico, <b>L</b>igadura, nessa ordem.'), ('Adrenalina nunca dança sozinha', 'sempre com térmico ou clipe.'), ('Blatchford zero ou um? Vai pra casa.', ''), ('Choque maior que 1, tomografia primeiro', 'índice de choque na HDB.')])}</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de hemorragia digestiva do 8º semestre (ACG 2021; BSG 2019; HALT-IT 2020; Schwartz).'))

# ======================= ABDOME AGUDO (B) =======================
FLX_AA = '''<div class="flx">
<div class="fb esc">Dor abdominal aguda (&gt; 6 h, progressiva, com sinais sistêmicos)</div><div class="fa">↓</div>
<div class="fr"><div><div class="fb vi">Instável · peritonite</div><div class="fp">reanimar <b>antes</b> da TC · POCUS/FAST · centro cirúrgico</div></div>
<div><div class="fb ou">Estável</div><div class="fp">história + exame completo (hérnias, toque retal) · <b>β-hCG</b> na mulher fértil · <b>ECG</b> no idoso e na dor alta</div></div></div>
<div class="fa">↓ qual síndrome?</div>
<div class="fr3"><div class="fb">Inflamatória<div class="fp">piora em horas/dias, febre</div></div><div class="fb">Perfurativa<div class="fp">súbita, tábua, ar livre</div></div><div class="fb">Obstrutiva<div class="fp">cólica, distensão, vômito</div></div></div>
<div class="fr" style="margin-top:5px"><div class="fb">Vascular<div class="fp">dor ≫ exame, FA, lactato</div></div><div class="fb">Hemorrágica<div class="fp">súbita + choque</div></div></div></div>'''

render(N + 'Abdome agudo - resumo em 1 folha', dict(layout='B', titulo='Abdome Agudo',
 sub='Inflamatório, obstrutivo, vascular e hemorrágico', vars='--fs:8.15pt;--lh:1.52;--gap:3.6mm',
 corpo=f'''<div class="gB"><div>
{card('Por onde começar', FLX_AA)}
{card('Obstrutivo · tríade: cólica + distensão + vômitos', '''<p><b>Alta:</b> vômito precoce, pouca distensão · <b>baixa:</b> vômito tardio/fecaloide, muita distensão. <b>Bridas (~75%)</b>, hérnia, câncer de cólon, volvo.</p>
<ul><li>RX: <b>empilhamento de moedas</b> (delgado) · <b>grão de café</b> (volvo de sigmoide) · TC: transição, redemoinho</li><li>SNG + hidratação (75% das parciais melhoram em 24 h)</li><li><b>Cirurgia:</b> completa, estrangulamento, alça fechada (ceco &gt; 12 cm) ou parcial sem melhora em 48 h</li></ul>''')}
{card('Vascular e hemorrágico', '''<ul><li><b>Isquemia mesentérica:</b> embolia (FA) 40–50%, trombose (angina mesentérica), venosa, NOMI. Transmural após <b>12 h</b>; lactato normal não exclui; angioTC só no estável; revascularizar + second-look</li><li><b>Idoso tabagista:</b> aneurisma roto (dor lombar + massa pulsátil + choque) · <b>mulher fértil:</b> ectópica rota (Proust, Laffont)</li><li>Tríade letal: hipotermia, acidose, coagulopatia → 1:1:1 + ácido tranexâmico</li></ul>''')}
</div><div>
{card('Inflamatório · os quatro grandes', '''<table><tr><th>Doença</th><th>Chave da prova</th></tr>
<tr><td>Apendicite</td><td>Periumbilical → FID; Blumberg; diagnóstico clínico; TC &gt; 7 mm</td></tr>
<tr><td>Colecistite</td><td>HD &gt; 6 h + Murphy; <b>TG18</b>: I CVL precoce · II CVL ou drenar · III colecistostomia</td></tr>
<tr><td>Diverticulite</td><td>FIE, &gt; 40 anos; TC; <b>Hinchey</b> I–II clínico/drenar &gt; 4 cm · III–IV cirurgia</td></tr>
<tr><td>Pancreatite</td><td>Dor em barra; <b>2 de 3</b>; TC só após 48–72 h; Ringer; sem ATB profilático</td></tr></table>''')}
{nc(['Abdome inocente não descarta isquemia.', 'Sangramento vaginal não afasta ectópica: β-hCG sempre.', 'Dor lombar súbita no idoso = aneurisma roto até provar o contrário.', 'Instável não vai para a TC.', 'Colonoscopia é proibida na diverticulite aguda; obrigatória 4–6 semanas depois.', 'Amilase não mede gravidade.', 'Não espere vômito fecaloide para pensar em obstrução baixa.'])}
{mn([('O abdome grita de 5 jeitos', 'inflama, fura, entope, infarta e sangra.'), ('Dor de grito, barriga de anjo', 'é isquemia mesentérica até provar o contrário.'), ('Tóquio é ABC', '<b>A</b> local (Murphy) + <b>B</b> sistêmico (febre, leuco) = suspeita; + <b>C</b> imagem = certeza.'), ('Hinchey: perto, longe, pus, cocô', 'I pericólico · II distante · III purulenta · IV fecal.'), ('Pancreatite é DEI', '<b>D</b>or típica, <b>E</b>nzima ≥ 3×, <b>I</b>magem: bastam 2.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base nos resumos de abdome agudo inflamatório, obstrutivo e vascular/hemorrágico do 8º semestre (Sabiston; Harrison; TG18).'))

# ======================= TGI (A) =======================
render(N + 'TGI - resumo em 1 folha', dict(layout='A', titulo='TGI: do Esôfago ao Ânus',
 sub='Esôfago, estômago e duodeno, vias biliares e pâncreas, cólon, reto e ânus', vars='--fs:7.65pt;--lh:1.48;--gap:3mm',
 corpo=f'''<div class="gL"><div>
{sec('Esôfago', '''<ul><li><b>DRGE:</b> pirose e regurgitação; alarme (disfagia, emagrecimento, sangramento, anemia) → EDA. <b>pHmetria</b> (padrão-ouro) nos refratários sem esofagite; <b>manometria</b> antes de operar. IBP 6–12 semanas; cirurgia: <b>Nissen 360°</b> (Toupet se dismotilidade)</li>
<li><b>Barrett:</b> metaplasia intestinal, adenocarcinoma 30–40× → vigilância; displasia → ablação</li>
<li><b>Hérnia de hiato:</b> I deslizamento (~95%) · II paraesofágica · III mista · IV outros órgãos</li>
<li><b>Acalasia:</b> EEI não relaxa + aperistalse; manometria (Chicago); Heller + Dor ou POEM (tipo III)</li>
<li><b>Câncer:</b> CEC (tabaco + álcool) × adenocarcinoma (Barrett, obesidade); T1a endoscópico · T1b esofagectomia · avançado: CROSS + cirurgia</li></ul>''')}
{sec('Estômago e duodeno', '''<ul><li><b>Úlcera:</b> H. pylori (90% duodenais) e AINE; gástrica <b>sempre biopsia</b>. Erradicação: quádrupla com bismuto 10–14 dias; confirmar 4 semanas depois. Perfuração: rafia + <b>patch de Graham</b></li>
<li>Pós-gastrectomia: <b>dumping</b> (15–30 min) · alça aferente (alivia com vômito bilioso) · gastrite alcalina (não alivia) → Y de Roux</li>
<li><b>Adenocarcinoma:</b> Virchow, Irmã Maria José, Blumer, Krukenberg. Lauren <b>intestinal</b> (distal, idoso) × <b>difuso</b> (proximal, jovem, anel de sinete, pior). T1a: ESD · ressecável: FLOT + gastrectomia D2</li>
<li><b>MALT:</b> erradicar H. pylori · <b>GIST:</b> CD117/DOG1, ressecção sem linfadenectomia, imatinibe</li></ul>''')}
{sec('Vias biliares e pâncreas', '''<ul><li><b>Colelitíase:</b> cólica &lt; 6 h → CVL eletiva; assintomática observa (exceto porcelana, &gt; 3 cm, pólipo &gt; 10 mm)</li>
<li><b>Coledocolitíase (ASGE):</b> alto risco (cálculo no colédoco, colangite, BT &gt; 4 + colédoco &gt; 6 mm) → <b>CPRE</b> · intermediário → colangiorressonância/eco-EDA · baixo → CVL</li>
<li><b>Colangite:</b> Charcot e Reynolds → CPRE urgente</li>
<li><b>Periampular:</b> icterícia indolor + perda de peso; Courvoisier no tumor de cabeça; Klatskin = vesícula murcha; TC trifásica (duplo ducto); ressecável → <b>Whipple</b> sem biópsia</li></ul>''')}
{sec('Cólon, reto e ânus', '''<ul><li><b>Crohn</b> transmural, salteado, íleo terminal, fístulas; cirurgia não cura · <b>RCU</b> mucosa, contínua desde o reto; megacólon tóxico &gt; 6 cm; proctocolectomia cura</li>
<li><b>CCR:</b> direito = anemia · esquerdo = obstrução. Rastreio 45–50 a 75 anos com sangue oculto. Estágio III: <b>quimio sempre</b>; mínimo 12 linfonodos. Reto: RM + QRT + TME · canal anal: <b>Nigro</b></li>
<li>Hemorroida interna indolor (Goligher I–IV) · <b>fissura</b> posterior → nifedipina/nitrato, crônica: esfincterotomia · <b>abscesso:</b> drenar já</li></ul>''')}
</div><div>
{nc(['EDA normal não exclui DRGE.', 'Úlcera gástrica sempre biopsia; duodenal típica não.', 'Suspenda IBP 2 semanas antes de pesquisar H. pylori.', 'GIST não leva linfadenectomia.', 'Massa pancreática ressecável vai à cirurgia sem biópsia.', 'CPRE diagnóstica no risco intermediário: não.', 'Crohn não cura com cirurgia; RCU sim.', 'Câncer anal trata com Nigro, não com bisturi.'])}
{mn([('Os 4 F da pedra', '<b>F</b>emale, <b>F</b>orty, <b>F</b>ertile, <b>F</b>at.'), ('Charcot tem FID', '<b>F</b>ebre, <b>I</b>cterícia, <b>D</b>or. Reynolds soma choque e confusão.'), ('Duodenal Dá alívio, Gástrica Garante dor', 'comer melhora a duodenal e piora a gástrica.'), ('Vesícula que se sente e não dói, é tumor que corrói', 'sinal de Courvoisier.'), ('Crohn pula e fura; RCU sobe sem pular', 'salteado e transmural × contínuo desde o reto.'), ('Lauren Difuso Dói mais', 'jovem, anel de sinete, pior prognóstico.')])}
{box('Números que caem', '<p>pHmetria: pH &lt; 4 por &gt; 4% · colédoco &gt; 6 mm · BT &gt; 4<br>megacólon &gt; 6 cm · CCR 12 linfonodos</p>')}
</div></div>''',
 fontes='Elaborado pela MedSum com base nos resumos TGI I, II e III do 8º semestre (SBAD 2026, ASGE 2019, TG18, SBOC 2026, Harrison, Sabiston).'))

# ======================= HÉRNIAS (A) =======================
render(N + 'Hérnias da parede abdominal - resumo em 1 folha', dict(layout='A', titulo='Hérnias da Parede Abdominal',
 sub='Conceitos, inguinal e femoral, conduta e outras hérnias', vars='--fs:9pt;--lh:1.6;--gap:4.8mm',
 corpo=f'''<div class="gL"><div>
{sec('O que é (e o que não é)', '<p>Saída de órgão por ponto fraco da parede, dentro de um <b>saco peritoneal</b>, com pele íntegra. <b>Eventração</b> é hérnia; <b>evisceração</b> (pele e peritônio rotos) não é. <span class="k">75% são inguinais</span> (2/3 indiretas); homem 25× mais; mais à direita.</p>')}
{sec('Redutível, encarcerada ou estrangulada', '''<table><tr><th>Forma</th><th>O que é</th><th>Conduta</th></tr>
<tr><td>Redutível</td><td>Volta sozinha ou com manobra</td><td>Cirurgia eletiva</td></tr>
<tr><td>Encarcerada</td><td>Não volta, circulação preservada</td><td>Redução manual (analgesia + Trendelenburg)</td></tr>
<tr><td>Estrangulada</td><td>Sem circulação: isquemia</td><td><span class="k">Emergência</span> (enterectomia se necrose)</td></tr></table>''')}
{sec('Direta × indireta', '''<table><tr><th></th><th>Direta</th><th>Indireta</th></tr>
<tr><td>Onde</td><td><b>Medial</b> aos vasos epigástricos inferiores, no triângulo de Hesselbach</td><td><b>Lateral</b>, pelo anel inguinal interno</td></tr>
<tr><td>Por quê</td><td>Fraqueza do assoalho</td><td>Conduto peritônio-vaginal persistente</td></tr>
<tr><td>Valsalva + dedo</td><td>Bate na <b>polpa</b></td><td>Bate na <b>ponta</b>; pode ir ao escroto</td></tr></table>
<p style="margin-top:2px">Diagnóstico <b>clínico</b> (USG/TC/RM na dúvida); o tipo se confirma na cirurgia.</p>''')}
{sec('Femoral e cirurgia', '<ul><li><b>Femoral:</b> medial aos vasos femorais, canal estreito → mais em <b>mulheres</b> e a que <b>mais estrangula</b></li><li><b>Richter:</b> só a borda antimesentérica estrangula, sem obstrução clássica</li><li><b>Lichtenstein</b> (tela sem tensão) é o padrão · McVay usa o ligamento de Cooper (boa na femoral) · Bassini com tensão · Stoppa pré-peritoneal</li><li>Complicações: atrofia testicular (plexo pampiniforme), hiperestesia (genitofemoral)</li></ul>')}
{sec('Outras', '<ul><li><b>Umbilical:</b> na criança, anel &gt; 1 cm após 1 ano opera · <b>epigástrica:</b> linha alba · <b>Spieghel:</b> linha semilunar, difícil palpar</li><li><b>Incisional:</b> 1–8% das laparotomias (14–20% contaminadas) · lombares: Grynfeltt e Petit · paraestomal</li></ul>')}
</div><div>
{nc(['Evisceração não é hérnia.', 'Direta é medial; indireta é lateral.', 'Femoral é a que mais estrangula.', 'Richter estrangula sem quadro obstrutivo.', 'Encarcerada tenta reduzir; estrangulada vai para a sala.', 'Hérnia sem cirurgia só cresce.'])}
{mn([('Direta: Dentro e meDial', 'dentro do triângulo de Hesselbach, medial aos vasos.'), ('Hesselbach é RIP', '<b>R</b>eto abdominal, epigástricos <b>I</b>nferiores, <b>P</b>oupart (ligamento inguinal).'), ('Indireta faz o caminho e bate na ponta', 'desce pelo canal; a direta empurra a polpa.'), ('FEMoral é FEMinina', 'e a mais perigosa: estrangula mais.'), ('Richter só belisca', 'pega um pedaço da parede da alça.')])}
{box('Números que caem', '<p>75% inguinais · 2/3 indiretas · femoral ~5%<br>umbilical &gt; 1 cm após 1 ano</p>')}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de hérnias da parede abdominal do 8º semestre (Sabiston; Schwartz; HerniaSurge 2018).'))

# ======================= EPISTAXE (B) =======================
FLX_EP = '''<div class="flx">
<div class="fb esc">Epistaxe · instável? ABCDE primeiro</div><div class="fa">↓</div>
<div class="fb"><b>1. Compressão</b> da parte mole, 5–10 min, sentado e inclinado para a frente</div><div class="fa">↓ continua</div>
<div class="fb"><b>2. Vasoconstritor</b> (oximetazolina, adrenalina) + lidocaína</div><div class="fa">↓</div>
<div class="fb"><b>3. Cauterização</b> (nitrato de prata/ATA) · nunca bilateral</div><div class="fa">↓</div>
<div class="fb ou"><b>4. Tampão anterior</b> 24–48 h · reabsorvível no anticoagulado</div><div class="fa">↓ posterior</div>
<div class="fb vi">5. Tampão posterior (Foley, duplo balão) · INTERNA</div><div class="fa">↓ refratário</div>
<div class="fb"><b>6. TESPAL</b> (até 98%) ou embolização (~87%)</div></div>'''

render(N + 'Epistaxe - resumo em 1 folha', dict(layout='B', titulo='Epistaxe',
 sub='Anterior × posterior, causas e tratamento em escada', vars='--fs:9pt;--lh:1.6;--gap:4.6mm',
 corpo=f'''<div class="gB"><div>
{card('A escada do tratamento', FLX_EP)}
{nc(['Comprimir o osso não funciona: aperte a parte mole.', 'Cabeça para trás está errado.', 'Sangue na orofaringe = posterior.', 'Após os 40 anos, a posterior fica mais comum.', 'Etmoidais não se embolizam: ligam-se.', 'Suspender AAS não reverte na hora (7–10 dias).'])}
</div><div>
{card('Anterior × posterior', '''<table><tr><th></th><th>Anterior ~90%</th><th>Posterior 5–10%</th></tr>
<tr><td>Vaso</td><td>Plexo de Kiesselbach</td><td>A. esfenopalatina</td></tr>
<tr><td>Quem</td><td>Criança, trauma digital</td><td>&gt; 40 anos, HAS, AAS</td></tr>
<tr><td>Pista</td><td>Ponto visível na rinoscopia</td><td>Sangue na orofaringe</td></tr></table>''')}
{card('Causas que caem', '<ul><li><b>Locais:</b> trauma digital, corpo estranho (unilateral, fétido), rinite, desvio, <b>angiofibroma juvenil</b> (adolescente, unilateral profusa)</li><li><b>Sistêmicas:</b> HAS (não baixar a PA de rotina), anticoagulantes, von Willebrand, <b>Rendu-Osler-Weber</b>, cocaína, álcool</li></ul>')}
{card('Anticoagulado e Rendu-Osler', '<ul><li>Sem risco de vida: <b>medidas locais primeiro</b>. Varfarina grave: complexo protrombínico + vit. K · dabigatrana: idarucizumabe</li><li><b>Curaçao:</b> epistaxe recorrente, telangiectasias, MAV visceral, parente de 1º grau (3 = definitivo)</li></ul>')}
{mn([('Kiesselbach na frente, Esfenopalatina Escondida atrás', ''), ('Aperta o mole e olha o chão', 'compressão da asa nasal, inclinado para a frente.'), ('Septo dos dois lados? Furo garantido', 'não cauterize bilateral.'), ('Etmoidal + embolização = escuridão', 'risco de cegueira.'), ('Tampão de trás, cama no hospital', 'tamponamento posterior interna.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de epistaxe do 8º semestre (AAO-HNSF, Tunkel 2020; Cummings; Ballenger).'))

# ======================= OBESIDADE (C) =======================
render(N + 'Obesidade - resumo em 1 folha', dict(layout='C', titulo='Obesidade',
 sub='Diagnóstico, remédios (ABESO 2026), bariátrica e complicações', vars='--fs:8.1pt;--lh:1.5;--gap:3.4mm',
 corpo=f'''<div class="sec">{cards([('IMC', '≥ 30', 'I 30 · II 35 · III ≥ 40'), ('Cintura (risco)', '94 / 80 cm', 'muito alto: 102 / 88'), ('Bariátrica', '40 · 35 · 30', 'sozinho · + comorbidade · DM2'), ('Alta potência', '≥ 10%', 'semaglutida, tirzepatida')])}</div>
<div class="sec"><h2>Técnicas cirúrgicas</h2>{passos([('Banda / balão', 'restritivas; banda reversível, muita reoperação; balão é ponte'), ('Sleeve', 'tira 80% do estômago e o fundo: cai a <b>grelina</b>'), ('Bypass em Y de Roux', 'pouch 30 mL; <b>GLP-1 e PYY</b> altos; DM2 melhora cedo'), ('Duodenal switch', 'maior perda e maior risco nutricional')])}</div>
<div class="g2"><div>
{sec('Diagnóstico', '<p>IMC é populacional: some <b>cintura</b>, cintura/altura &gt; 0,5 e composição corporal. ABESO 2026: obesidade inalterada, reduzida ou controlada pelo peso máximo; Lancet: <b>clínica</b> (lesão de órgão) × <b>pré-clínica</b>.</p>')}
{sec('Remédios', '<ul><li>Sem mudança de estilo de vida, não se sustenta (dieta, exercício, TCC)</li><li><b>GLP-1:</b> insulina glicose-dependente, esvaziamento lento, saciedade; contraindicado se carcinoma medular ou NEM 2</li><li><b>Semaglutida 2,4 mg</b> (reduz risco CV, ICFEp, MASH) · <b>tirzepatida 15 mg</b> (MASH, apneia)</li><li>4–9,9%: liraglutida, naltrexona + bupropiona, sibutramina (não na DCV) · &lt; 4%: orlistate</li></ul>')}
{sec('Quem opera', '<p>18–65 anos com falha clínica: IMC <b>≥ 40</b> · <b>≥ 35</b> + comorbidade grave · <b>30–34,9</b> com DM2 refratário. Não opera: álcool/drogas ativos, psiquiátrico descompensado, sem adesão, ASA IV.</p>')}
</div><div>
{sec('Complicações', '<ul><li><b>Fístula</b> (sleeve, ângulo de His): taquicardia persistente, febre, dor</li><li><b>TEV</b>: principal causa de morte precoce → deambular cedo + HBPM</li><li>Deficiências (ferro, B12, folato, cálcio, vit. D): suplementar para sempre</li><li><b>Petersen:</b> cólica intermitente pós-bypass; TC falso-negativa em até 20% → explorar</li><li>Úlcera marginal (tabaco, AINE), colelitíase (ursodesoxicólico), dumping, reganho</li></ul>')}
{nc(['IMC normal não exclui risco: meça a cintura.', 'Taquicardia sem explicação no pós-operatório = fístula.', 'TEV mata mais cedo que a fístula.', 'Dor após bypass com TC normal: ainda pode ser Petersen.', 'GLP-1 não em carcinoma medular ou NEM 2.'])}
{mn([('40 vai sozinho, 35 vai acompanhado, 30 só com o diabetes', 'indicações de bariátrica.'), ('Sleeve tira o fundo e a fome', 'sai a grelina junto.'), ('Bypass é o rei do GLP-1', 'por isso o diabetes melhora antes do peso.'), ('94/80 acende a luz, 102/88 toca o alarme', 'cintura de homem/mulher.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de obesidade do 8º semestre (ABESO, diretriz farmacológica 2026; aula de Clínica Cirúrgica).'))
