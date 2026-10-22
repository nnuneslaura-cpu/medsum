# Folhas únicas do 4º semestre (D1 NCS 1.2-1.4, D2 HMEC partograma, D3 NCS 3.1-3.3) no estilo 2
# Conteúdo SÓ dos resumos publicados (PDFs do Drive). Pedido da Laura (22/10/2026).
import sys, os
os.environ.setdefault('PASTA', 'v2-g1')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from folha2 import render, ul, nc, mn, sec, card, box, cards, passos

D1 = '4º sem D1 · NCS · '
D3 = '4º sem D3 · NCS · '

# ======================= SP 1.2 · EVASÃO E PRÓSTATA (A) =======================
render(D1 + 'SP 1.2 · Mecanismos de evasão e câncer de próstata - resumo em 1 folha', dict(layout='A',
 titulo='Mecanismos de Evasão e Câncer de Próstata',
 sub='Como o tumor escapa da morte, cresce e se espalha · próstata: anatomia, NIP, PSA, Gleason e rastreio',
 vars='--fs:7.75pt;--lh:1.48;--gap:3mm;--h1:21pt',
 corpo=f'''<div class="gL"><div>
{sec('Apoptose: as duas vias', '''<table><tr><th></th><th>Intrínseca (mitocondrial)</th><th>Extrínseca (receptor de morte)</th></tr>
<tr><td>Gatilho</td><td>Dano ao DNA → <b>p53</b></td><td>NK ou TCD8: <b>Fas (CD95) + FasL</b></td></tr>
<tr><td>Caminho</td><td>BAX/BAK furam a mitocôndria → citocromo C + <b>APAF-1</b> (apoptossomo)</td><td>Trimerização → <b>FADD</b> → procaspase-8</td></tr>
<tr><td>Iniciadora</td><td><span class="k">Caspase-9</span></td><td><span class="k">Caspase-8</span></td></tr>
<tr><td>Freio do tumor</td><td>↑ BCL2/BCL-XL, ↓ BAX, perda de APAF-1, ↑ IAP</td><td>↓ CD95, <b>c-FLIP</b> bloqueia a caspase-8</td></tr></table>
<p style="margin-top:2px">As duas terminam na <b>caspase-3</b> (executora). BH3-only (BAD, BID, PUMA) são pró-apoptóticas: bloqueiam BCL2.</p>''')}
{sec('Outras armas do câncer', '''<ul><li><b>Autofagia:</b> no início freia o tumor; na fase avançada <b>ajuda a sobreviver</b> (recicla nutrientes)</li>
<li><b>Telômeros:</b> célula normal faz 60–70 divisões → senescência (p53/RB). Sem p53: cromossomos dicêntricos e ciclo <b>ponte-fusão-quebra</b>; <b>telomerase</b> reativada = imortal</li>
<li><b>Angiogênese</b> (tumor &gt; 1–2 mm): hipóxia → <b>HIF-1α</b> (VHL não degrada) → <b>VEGF</b>; freio: TSP-1, induzida pela p53</li>
<li><b>Metástase:</b> perde E-caderina → proteases (MMP) → novos sítios na MEC → motilidade autócrina → êmbolo com plaquetas → adesão (integrinas, selectinas)</li>
<li><b>Efeito Warburg:</b> glicólise aeróbica mesmo com O₂: 2 ATP (× 36), porém rápida e fornece matéria-prima (Burkitt)</li>
<li><b>Imune:</b> ↓ MHC I, variante sem antígeno, TGF-β, <b>PD-L1</b> inativa o CTL → anti-PD-1 (efeito adverso autoimune, ex. colite)</li>
<li><b>Instabilidade genômica</b> (perda do reparo) e <b>inflamação crônica</b> (Barrett, RCU, H. pylori: EROs)</li>
<li><b>Wnt/β-catenina:</b> APC degrada a β-catenina; APC mutado (70–80% do câncer de cólon) → β-catenina no núcleo → ciclina D1, MYC</li></ul>''')}
{sec('Próstata: anatomia que cai', '''<ul><li>Abaixo da bexiga; até 24 g; líquido levemente ácido (pH ~6,5) com ácido cítrico e <b>PSA</b>; ~25% do sêmen</li>
<li>Artérias: ramos da ilíaca interna (vesical inferior, pudenda interna, retal média)</li>
<li>Plexo venoso prostático ↔ <b>plexo de Batson</b> (vertebral interno): via de metástase para a coluna</li>
<li><b>Zona periférica</b> (posterior, palpável no toque) = câncer · <b>transição</b> (em volta da uretra proximal) = HPB · central (ductos ejaculatórios)</li></ul>''')}
</div><div>
{box('Câncer de próstata', '''<ul><li><b>Adenocarcinoma acinar</b>, multicêntrico, na zona periférica</li>
<li>Precursor: <b>NIP de alto grau</b> (camada basal intacta; p63, CK34βE12)</li>
<li>Genes: perda de PTEN, RB, TP53; MYC; fusão <b>TMPRSS2-ERG</b>; GSTP1 hipermetilado</li>
<li>Resistência à castração: receptor de andrógeno ativo sem ligante</li>
<li>Metástase óssea <b>osteoblástica</b> (pelve, coluna, costelas)</li>
<li>Clínica: muitas vezes assintomático; LUTS, hematúria, dor óssea, nódulo endurecido</li></ul>''')}
{box('Exames', '''<ul><li><b>Biópsia</b> (guiada por USG transretal) = padrão-ouro</li>
<li>PSA: 4,1–10 sugere mais HPB; <b>&gt; 10</b> risco maior de câncer</li>
<li>RM multiparamétrica localiza</li>
<li><b>Gleason</b> = padrão 1º + 2º (2–10) → ISUP 1–5</li>
<li>MS/INCA: <b>não</b> rastreia a população</li></ul>''')}
{nc(['Intrínseca é caspase-9; extrínseca é caspase-8.', 'BCL2 é antiapoptótica; BAX e BAK são pró.', 'Normóxia: VHL destrói o HIF-1α.', 'NIP de alto grau tem camada basal; o carcinoma não.', 'PSA alto não é diagnóstico: só a biópsia.', 'Câncer é na periférica; HPB é na transição.'])}
</div></div>
{mn([('Intrínseca é 9, extrínseca é 8, as duas acabam no 3', 'caspases iniciadoras e a executora.'), ('BCL2 Blinda, BAX Bate', 'BCL2 protege a célula; BAX fura a mitocôndria.'), ('Hipóxia acorda o HIF, o VHL põe pra dormir', 'sem VHL agindo, sobe VEGF e nascem vasos.'), ('Periférica é Perigosa', 'zona periférica = câncer; transição = hiperplasia.'), ('Batson é o elevador da próstata para a coluna', 'plexo venoso vertebral sem passar pela cava.')]).replace('class="mn"', 'class="mn" style="display:grid;grid-template-columns:1fr 1fr 1fr;column-gap:5mm"').replace('<h3>Para não esquecer</h3>', '<h3 style="grid-column:1/-1">Para não esquecer</h3>')}''',
 fontes='Elaborado pela MedSum com base no resumo da SP 1.2 do 4º semestre (Robbins; Bogliolo; Rubin; Moore; Netter; INCA).'))

# ======================= SP 1.3 · LEUCEMIAS (C) =======================
GRADE = '''<svg viewBox="-8 0 148 120" width="100%" aria-hidden="true" font-family="Inter">
<text x="52" y="10" font-size="8" fill="#8a5f12" font-weight="600" text-anchor="middle">Mieloide</text>
<text x="108" y="10" font-size="8" fill="#8a5f12" font-weight="600" text-anchor="middle">Linfoide</text>
<text x="-6" y="42" font-size="7.5" fill="#921827" font-weight="600">Aguda</text>
<text x="-6" y="94" font-size="7.5" fill="#921827" font-weight="600">Crônica</text>
<rect x="28" y="16" width="48" height="46" rx="7" fill="#f7e8ea"/><rect x="84" y="16" width="48" height="46" rx="7" fill="#f7e8ea"/>
<rect x="28" y="68" width="48" height="46" rx="7" fill="#f8f0de"/><rect x="84" y="68" width="48" height="46" rx="7" fill="#f8f0de"/>
<text x="52" y="38" font-size="11" fill="#921827" text-anchor="middle" font-family="DejaVu Serif">LMA</text><text x="52" y="51" font-size="6.5" fill="#76696b" text-anchor="middle">adulto · 65 a</text>
<text x="108" y="38" font-size="11" fill="#921827" text-anchor="middle" font-family="DejaVu Serif">LLA</text><text x="108" y="51" font-size="6.5" fill="#76696b" text-anchor="middle">criança</text>
<text x="52" y="90" font-size="11" fill="#8a5f12" text-anchor="middle" font-family="DejaVu Serif">LMC</text><text x="52" y="103" font-size="6.5" fill="#76696b" text-anchor="middle">40–60 a</text>
<text x="108" y="90" font-size="11" fill="#8a5f12" text-anchor="middle" font-family="DejaVu Serif">LLC</text><text x="108" y="103" font-size="6.5" fill="#76696b" text-anchor="middle">idoso · 72 a</text></svg>'''

render(D1 + 'SP 1.3 · Leucemias - resumo em 1 folha', dict(layout='C', titulo='Leucemias',
 sub='Neoplasia, carcinogênese e hematopoese · LMA, LPA, LMC, LLA e LLC', vars='--fs:7.85pt;--lh:1.48;--gap:3.1mm',
 corpo=f'''
<div class="vis sec" style="--vw:40mm"><div>{GRADE}</div><div>{cards([('Aguda', '&gt; 20%', 'de blastos na medula'), ('LMC', 't(9;22)', 'Filadélfia · BCR-ABL1'), ('LPA', 't(15;17)', 'PML-RARA · trata com ATRA')])}
<p class="m" style="margin-top:2.5mm">Medula vermelha do adulto: esterno, costelas, vértebras, crânio, pelve (<b>ílio</b>) e epífises proximais de fêmur e úmero. Esterno e ílio são os locais de punção.</p></div></div>
<div class="sec"><h2>As quatro (e a quinta)</h2><table><tr><th>Tipo</th><th>Quem</th><th>Marca registrada</th><th>Genética</th><th>Tratamento-chave</th></tr>
<tr><td>LMA</td><td>Adulto, mediana 65 anos (aguda mais comum no adulto)</td><td><b>Bastonetes de Auer</b>; anemia, plaquetopenia, neutropenia</td><td>FLT3, NPM1, DNMT3A; t(8;21), inv(16), −5/−7</td><td>Indução (&lt; 5% de blastos) → consolidação → TCT se mau prognóstico</td></tr>
<tr><td>LPA</td><td>Adulto jovem (20–30 anos)</td><td>Promielócitos cheios de grânulos e Auer</td><td><b>PML-RARA</b> t(15;17): bloqueia a maturação</td><td><b>ATRA</b> (diferencia) + quimioterapia</td></tr>
<tr><td>LMC</td><td>40–60 anos, ~15% das leucemias</td><td>Leucocitose (até &gt; 200 mil) com todas as fases mieloides, <b>basofilia</b>, <b>esplenomegalia</b></td><td><b>BCR-ABL1</b>: tirosina quinase sempre ligada</td><td><b>Inibidor de tirosina quinase</b>; TCT é o único curativo</td></tr>
<tr><td>LLA</td><td>Criança (75% antes dos 6 anos); a doença maligna mais comum da infância</td><td>Linfoblastos; anemia, febre/infecção, sangramento</td><td>Hiperdiploidia e t(12;21) bom · hipodiploidia e t(9;22) ruim</td><td>—</td></tr>
<tr><td>LLC</td><td>Idoso (72 anos), homem 2:1</td><td><b>Linfonodos</b> simétricos, firmes, indolores; linfocitose; hipogamaglobulinemia</td><td>Trissomia 12; del 11, 13, 17; <b>TP53</b>, <b>ATM</b></td><td>— (B CD19+; CD38 e ZAP70 = prognóstico)</td></tr></table></div>
<div class="g2"><div>
{sec('Neoplasia e carcinogênese', '''<ul><li><b>Benigno:</b> expansivo, delimitado, diferenciado, sem metástase · <b>maligno:</b> infiltrativo, anaplásico, angiogênese intensa, metástase</li>
<li>Carcinoma = epitélio · sarcoma = mesênquima · blastoma = embrionário · teratoma = mais de um folheto</li>
<li>Etapas: <b>iniciação</b> (mutação irreversível) → <b>promoção</b> (expansão, reversível) → <b>progressão</b> (agressivo, sintomas)</li>
<li>Supressores: <b>gatekeeper</b> RB1 (freia o ciclo) × <b>caretaker</b> TP53 (repara o DNA)</li></ul>''')}
{sec('Complicações da LLC e da LMC', '<ul><li>LLC: infecções bacterianas no início; fúngicas e virais (herpes-zóster) no fim; anemia hemolítica autoimune</li><li>LMC: hiperuricemia (gota, insuficiência renal); raros priapismo e distúrbio visual</li></ul>')}
{nc(['Leucemia aguda se define por &gt; 20% de blastos na medula.', 'Bastonete de Auer é mieloide (LMA/LPA), não linfoide.', 'Filadélfia na LMC é regra; na LLA é sinal de mau prognóstico.', 'LPA trata com ATRA, que diferencia, e não só mata.', 'Hidroxicarbamida controla leucócitos, mas não age no BCR-ABL1.', 'LLC tem linfócito B maduro, não blasto.'])}
</div><div>
{box('Como se confirma a LMA', '<ul><li>Hemograma (leucocitose, anemia, plaquetopenia) → esfregaço (blastos, Auer) → <b>mielograma</b> (&gt; 20%) → citometria de fluxo (imunofenótipo) → citogenética e biologia molecular</li><li>Tratamento: suporte em todas as fases · indução (blastos &lt; 5%) · consolidação · TCT · doença residual mínima</li><li>LMC confirma com <b>BCR-ABL1</b> por RT-PCR (Ph em ~98%)</li></ul>')}
{mn([('Auer é mieloide', 'bastão de Auer aponta LMA ou LPA.'), ('LLA na creche, LLC no clube da terceira idade', 'aguda linfoide na criança; crônica linfoide no idoso.'), ('9 com 22 dá Filadélfia', 'BCR-ABL1: quinase que não desliga; o TKI desliga.'), ('RARA pede ácido Retinoico', 'PML-RARA da LPA responde ao ATRA.'), ('LMC dos dois B', '<b>B</b>aço grande e <b>B</b>asófilo alto.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo da SP 1.3 do 4º semestre (Hoffbrand; Robbins; Bogliolo; Moore; Tortora).'))

# ======================= SP 1.4 · ANTINEOPLÁSICOS E CCR (B) =======================
FLX_CCR = '''<div class="flx">
<div class="fb">Mucosa normal</div><div class="fa">↓ <b>APC</b> perdido (os 2 alelos) · β-catenina no núcleo</div>
<div class="fb">Mucosa proliferativa</div><div class="fa">↓ <b>KRAS</b> ativado</div>
<div class="fb ou">Adenoma · displasia de baixo grau</div><div class="fa">↓ <b>TP53</b> perdido · hipermetilação</div>
<div class="fb ou">Adenoma de alto grau</div><div class="fa">↓ <b>DCC</b> perdido · telomerase</div>
<div class="fb vi">Adenocarcinoma (in situ → invasivo)</div>
<div class="fp" style="margin-top:4px">Outra via: <b>instabilidade de microssatélites</b> (hMLH1, hMSH2) = <b>síndrome de Lynch</b></div></div>'''

render(D1 + 'SP 1.4 · Antineoplásicos e câncer colorretal - resumo em 1 folha', dict(layout='B',
 titulo='Antineoplásicos e Câncer Colorretal',
 sub='Modalidades de tratamento · intestino grosso · pólipos, sequência adenoma-carcinoma, rastreio e TNM',
 vars='--fs:8.3pt;--lh:1.52;--gap:3.4mm',
 corpo=f'''<div class="gB"><div>
{card('Sequência adenoma-carcinoma', FLX_CCR)}
{card('Pólipos adenomatosos', '''<table><tr><th>Tipo</th><th>Frequência</th><th>Risco</th></tr>
<tr><td>Tubular</td><td>~75% · pequeno, séssil</td><td>Baixo (sobe com tamanho e displasia)</td></tr>
<tr><td>Tubuloviloso</td><td>15–20%</td><td>Proporcional ao componente viloso</td></tr>
<tr><td>Viloso</td><td>~10% · grande, distal</td><td><span class="k">30–50%</span> viram câncer</td></tr></table>
<p style="margin-top:2px">Hiperplásico, hamartomatoso, juvenil e inflamatório são <b>não neoplásicos</b>. <b>PAF:</b> autossômica dominante, centenas a milhares de adenomas.</p>''')}
{card('Quando suspeitar', '<ul><li><b>Sangue nas fezes</b>: hematoquezia (vermelho vivo, sangramento baixo) × melena (preta, sangue digerido, fonte alta)</li><li>Fezes finas ou em fita (obstrução parcial), constipação crônica, cólica, evacuação incompleta</li><li>Perda de peso sem explicação e cansaço crônico</li></ul>')}
{card('Antineoplásicos', '''<ul><li>Tumor localizado: <b>cirurgia + radioterapia</b> (~1/3 cura) · micrometástase: <b>quimioterapia</b> (sozinha cura &lt; 10%)</li>
<li>Citotóxicos atacam DNA, nucleotídeos e fuso: mucosite, alopecia, diarreia, citopenias</li>
<li>Biológica (anticorpos: HER2, BCR-ABL) · hormonal (mama, próstata, endométrio) · alvo-dirigida (menos efeitos adversos)</li>
<li><b>Neoadjuvante</b> = antes (reduz o tumor) · <b>adjuvante</b> = depois (mata o resíduo)</li></ul>''')}
</div><div>
{card('Rastreamento', '''<ul><li><b>Risco médio:</b> dos 45–50 aos 75 anos (76–85 individualiza; &gt; 85 não)</li>
<li><b>Alto risco</b> (CCR/adenoma avançado, DII, família, PAF, Lynch): aos 40 ou 10 anos antes do caso mais jovem</li>
<li><b>FIT</b> anual/bienal: só detecta hemoglobina humana, dieta não interfere · <b>guaiacol</b> sofre com carne, brócolis, AAS</li>
<li><b>Colonoscopia</b> = padrão-ouro: normal → 10 anos · viloso, &gt; 1 cm ou alto grau → 3 anos · Lynch: anual desde 25–30 anos</li></ul>''')}
{card('TNM e metástase', '''<p>T1 submucosa · T2 muscular própria · T3 tecidos pericólicos · T4 órgãos vizinhos · <b>N1</b> 1–3 linfonodos · <b>N2</b> ≥ 4</p>
<p>Estágio II = T3–T4 N0 · <b>III = qualquer N+</b> · IV = M1</p>
<ul><li><b>Fígado</b> é o 1º sítio: VMS e VMI → veia porta</li><li><b>Pulmão</b> no reto médio/baixo (drenagem para a cava)</li><li>Irrigação: AMS (ileocólica, cólica direita e média) · AMI (cólica esquerda, sigmoides, retal superior) · arcos de Drummond e Riolan</li></ul>''')}
{nc(['Melena é alta; hematoquezia é baixa (CCR, pólipo, DII, hemorroida).', 'FIT positivo exige colonoscopia.', 'Viloso é o adenoma mais perigoso, não o mais comum.', 'APC precisa perder os dois alelos.', 'Lynch é instabilidade de microssatélites, não polipose.', 'Fezes em fita sugerem obstrução parcial.'])}
{mn([('Ai, Kuidado, Pólipo Danado', '<b>A</b>PC → <b>K</b>RAS → <b>P</b>53 → <b>D</b>CC, na ordem.'), ('Viloso é vilão', 'até metade vira câncer.'), ('Neo vem aNtes, Adjuvante vem Após', ''), ('Intestino vai pela porta e chega ao fígado', 'reto baixo pega a cava e vai ao pulmão.'), ('N1 até 3, N2 de 4 pra cima', '')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo da SP 1.4 do 4º semestre (Bogliolo; Rubin; Moore; Netter; Tortora).'))

# ======================= D2 HMEC · PARTO (C) =======================
CABECA = '''<svg viewBox="0 0 150 70" width="78%" style="display:block;margin:0 auto" aria-hidden="true" font-family="Inter">
<g fill="#f8f0de" stroke="#c9a96a" stroke-width="1.4">
<ellipse cx="20" cy="30" rx="14" ry="12"/><ellipse cx="57" cy="30" rx="14" ry="12"/><ellipse cx="94" cy="30" rx="14" ry="12"/><ellipse cx="131" cy="30" rx="14" ry="12"/></g>
<g fill="#921827"><circle cx="20" cy="19" r="2.6"/><circle cx="57" cy="19.5" r="2.6"/><circle cx="94" cy="21" r="2.6"/><circle cx="131" cy="40" r="2.6"/></g>
<g font-size="6.5" text-anchor="middle" fill="#76696b"><text x="20" y="54">fletida</text><text x="57" y="54">1º grau</text><text x="94" y="54">2º grau</text><text x="131" y="54">3º grau</text>
<text x="20" y="64" fill="#921827">occipício</text><text x="57" y="64" fill="#921827">bregma</text><text x="94" y="64" fill="#921827">fronte</text><text x="131" y="64" fill="#921827">face</text></g></svg>'''

render('4º sem D2 · HMEC · Partograma e assistência ao parto - resumo em 1 folha', dict(layout='C',
 titulo='Assistência ao Parto',
 sub='Trabalho de parto, trajeto, mecanismo do parto e estática fetal', vars='--fs:8.5pt;--lh:1.55;--gap:4mm',
 corpo=f'''<div class="sec">{cards([('Situação longitudinal', '99,5%', 'eixo do feto = eixo do útero'), ('Feto de termo', '~50 cm', 'em útero de ~30 cm: precisa se dobrar'), ('Apresentação definida', '6º mês', 'antes disso o feto gira com folga')])}</div>
<div class="sec"><h2>Os seis tempos do mecanismo de parto</h2>{passos([('Insinuação', 'cabeça passa o estreito superior: orientação + flexão'), ('Descida', 'sinclítica (parietais juntos) ou assinclítica'), ('Rotação interna', 'occipício gira para a sínfise púbica'), ('Desprendimento da cabeça', 'occipício sob o púbis; deflexão'), ('Rotação externa', 'cabeça volta à posição; biacromial gira 45°'), ('Desprendimento das espáduas', 'ombro anterior sob o púbis, depois o posterior')])}</div>
<div class="g2"><div>
{sec('Trabalho de parto e trajeto', '''<p>Contrações coordenadas e involuntárias → <b>apagamento e dilatação</b> do colo + descida fetal; com os puxos, expulsão.</p>
<ul><li><b>Trajeto duro</b> (ossos, rígido): promontório, espinhas isquiáticas (referência da descida), sacro e cóccix, arco púbico</li>
<li><b>Trajeto mole</b>: útero, colo, vagina, assoalho pélvico e períneo</li></ul>''')}
{sec('Estática fetal', '''<ul><li><b>Atitude:</b> relação das partes do feto entre si; normal = ovoide fletido (eixo lambda-cóccix ~25 cm)</li>
<li><b>Situação:</b> longitudinal, transversa ou oblíqua (transição)</li>
<li><b>Apresentação:</b> parte que ocupa o estreito superior: cefálica ou pélvica (longitudinal) · <b>córmica</b> (transversa; dorsoanterior é a mais comum)</li>
<li><b>Pélvica:</b> completa (coxas e pernas fletidas) · incompletas: modo de nádegas, de joelhos, de pés</li></ul>''')}
</div><div>
{sec('Cefálica: o grau de deflexão', f'{CABECA}<p class="m" style="margin-top:1mm">Fletida = mento no esterno, a mais comum. Bregma: suturas coronal + sagital (frente) · lambda: sagital + lambdoide (atrás).</p>')}
{nc(['Situação é eixo × eixo; apresentação é a parte que chega primeiro à pelve.', 'Situação transversa = apresentação córmica.', 'Defletida de 2º grau é a de fronte; a de face é a de 3º grau.', 'Na rotação externa a cabeça volta; quem gira 45° é o biacromial.'])}
</div></div>
{mn([('INfelizmente DEscemos Rápido, DEpois REtornamos DE lado', 'insinuação, descida, rotação interna, desprendimento, rotação externa, espáduas.'), ('Deflexão sobe: Bregma, Fronte, Face', '1º, 2º e 3º graus, de cima para baixo no rosto.'), ('Duro é osso, mole é carne', 'trajeto duro = pelve; mole = útero, colo, vagina, períneo.'), ('Feto atravessado, apresentação córmica', '')]).replace('class="mn"', 'class="mn" style="display:grid;grid-template-columns:1fr 1fr;column-gap:6mm"').replace('<h3>Para não esquecer</h3>', '<h3 style="grid-column:1/-1">Para não esquecer</h3>')}''',
 fontes='Elaborado pela MedSum com base no resumo de parto e partograma (Saúde da Mulher) do 4º semestre.'))

# ======================= SP 3.1 · TOXICOLOGIA (A) =======================
render(D3 + 'SP 3.1 · Toxicologia: conceitos básicos, drogas ilícitas e álcool - resumo em 1 folha', dict(layout='A',
 titulo='Toxicologia: Conceitos Básicos',
 sub='Toxicocinética, toxicodinâmica, colinérgicos e adrenérgicos, intoxicação por inseticidas', vars='--fs:8.35pt;--lh:1.55;--gap:3.6mm',
 corpo=f'''<div class="gL"><div>
{sec('Conceitos', '<p><b>Toxina</b> = origem biológica · <b>toxicante</b> = produzido pelo homem · <b>xenobiótico</b> = estranho ao organismo. Exposição <b>aguda</b> (1 episódio; intoxicação aguda = até 24 h, efeitos em até 2 semanas), <b>subcrônica</b> (semanas a meses), <b>crônica</b> (meses a anos).</p>')}
{sec('Toxicocinética: o caminho do tóxico', '''<ul><li><b>Absorção:</b> via IV não absorve. Gases: alto coeficiente sangue/ar (clorofórmio) depende da <b>respiração</b>; baixo (etileno) depende da <b>circulação</b>. Forma não ionizada atravessa melhor; glicoproteína P reduz</li>
<li><b>Distribuição:</b> órgãos muito irrigados recebem antes. Chumbo: 50% no fígado em 2 h → <b>90% no osso</b> em 30 dias. Só a fração <b>livre</b> sai do plasma; albumina leva ácidos, α1-glicoproteína ácida leva bases. Vd grande = espalha; pequeno = fica no plasma</li>
<li><b>Biotransformação</b> (fígado): <b>fase I</b> oxidação, redução, hidrólise (CYP450; pode gerar metabólito mais tóxico) · <b>fase II</b> conjugação (glicuronidação, sulfatação, glutationa, acetilação)</li>
<li><b>Excreção:</b> urina (polares), fezes/bile (ciclo êntero-hepático aumenta a meia-vida), pulmão (gases: quanto menos solúvel, mais rápido), leite (DDT)</li>
<li><b>Urina alcalina</b> (bicarbonato) ioniza ácidos e acelera a saída de AAS e barbitúricos</li></ul>''')}
{sec('Toxicodinâmica', '''<ul><li>DL50, IT = DL50/DE50; agonista pleno (morfina), parcial (buprenorfina), inverso; antagonista reversível (naloxona) ou irreversível (AAS na COX-1)</li>
<li>Canais: <b>tetrodotoxina</b> (baiacu) bloqueia Na⁺ · <b>botulínica</b> bloqueia a liberação de ACh</li>
<li>Cianeto inibe a citocromo c oxidase · nitritos geram metemoglobina · organofosforados inibem a acetilcolinesterase</li></ul>''')}
{sec('Sistema autônomo', '''<table><tr><th>Receptor</th><th>Onde e o quê</th></tr>
<tr><td>Nicotínico</td><td>Canal iônico; gânglios (simpático e parassimpático)</td></tr>
<tr><td>Muscarínico</td><td>Proteína G; órgãos efetores do parassimpático (e sudorípara)</td></tr>
<tr><td>α1 · α2</td><td>Vasoconstrição · pré-sináptico, regula liberação</td></tr>
<tr><td>β1 · β2 · β3</td><td>Coração ↑ FC e força · broncodilatação, vasodilatação, útero · lipólise</td></tr></table>
<p style="margin-top:2px">Todo pré-ganglionar é colinérgico. Agonista adrenérgico indireto: <b>anfetamina</b> libera noradrenalina; <b>cocaína</b> impede a recaptação.</p>''')}
{nc(['Via IV não tem absorção.', 'Fase I pode deixar o tóxico pior.', 'Ligado à proteína não filtra nem distribui.', 'Ciclo êntero-hepático prolonga o efeito.', 'Atropina não reativa a colinesterase: isso é a pralidoxima.', 'Miose é muscarínica; midríase pode ser nicotínica.'])}
</div><div>
{box('Inseticidas: carbamato e organofosforado', '''<ul><li>Inibem a acetilcolinesterase → excesso de ACh</li>
<li><b>Muscarínico:</b> diarreia, micção, miose, bradicardia, broncorreia, êmese, lacrimejamento, salivação</li>
<li><b>Nicotínico:</b> fasciculação, fraqueza, midríase, hipertensão</li>
<li>Carbamato <b>reversível</b>; organofosforado <b>envelhece</b> (irreversível)</li>
<li><b>Atropina</b> (muscarínico) + <b>pralidoxima</b> (reativa a enzima) · carvão ativado nas primeiras horas, sinais vitais, volume</li></ul>''')}
{mn([('DUMBELS da ACh', '<b>D</b>iarreia, <b>U</b>rina, <b>M</b>iose, <b>B</b>radicardia, <b>B</b>roncorreia, <b>E</b>mese, <b>L</b>ágrima, <b>S</b>aliva.'), ('Atropina seca, pralidoxima solta', 'uma seca as secreções; a outra solta a enzima.'), ('Carbamato larga, organofosforado envelhece', 'reversível × irreversível.'), ('Fase I expõe, fase II embrulha', 'funcionaliza e depois conjuga.'), ('Gordinho entra fácil e sai difícil', 'lipossolúvel absorve bem e acumula.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo da SP 3.1 do 4º semestre (Casarett e Doull; Oga; Whalen; MS 2018).'))

# ======================= SP 3.2 · CHUMBO, TRONCO SUPERIOR, ALUCINÓGENOS (B) =======================
FLX_PB = '''<div class="flx">
<div class="fb esc">Chumbo absorvido (inalação ou TGI; orgânico pela pele)</div><div class="fa">↓</div>
<div class="fr"><div><div class="fb vi">Bloqueia ALA-D</div><div class="fp">acumula <b>ALA</b> (neurotóxico) no sangue e na urina</div></div>
<div><div class="fb vi">Bloqueia ferroquelatase</div><div class="fp">ferro não entra na protoporfirina IX → <b>ZPP</b> alta</div></div></div>
<div class="fa">↓ menos heme</div>
<div class="fb ou"><b>Anemia microcítica e hipocrômica</b> · pontilhado basofílico · hemólise (↑ BI)</div><div class="fa">↓ mimetiza cálcio e zinco</div>
<div class="fr3"><div class="fb">Osso<div class="fp">deposita, sai em 20–30 anos</div></div><div class="fb">SNC<div class="fp">encefalopatia, ↓ QI</div></div><div class="fb">Rim e vaso<div class="fp">nefropatia, HAS, gota</div></div></div></div>'''

render(D3 + 'SP 3.2 · Intoxicação por chumbo, tronco superior e alucinógenos - resumo em 1 folha', dict(layout='B',
 titulo='Chumbo, Tronco Superior e Alucinógenos',
 sub='Chumbo, benzeno e mercúrio · plexo braquial · resíduos · maconha e LSD', vars='--fs:7.85pt;--lh:1.48;--gap:3.1mm',
 corpo=f'''<div class="gB"><div>
{card('Chumbo: o que ele faz', FLX_PB)}
{card('Chumbo: clínica e conduta', '''<ul><li>Fonte nº 1 na criança: <b>tinta</b> velha e poeira (mão na boca); adulto: comida, água, tiro, solda, cerâmica</li>
<li>Cólica plúmbica, constipação · <b>linha de Burton</b> na gengiva · infertilidade, aborto · QTc longo</li>
<li>Rim: proteinúria de baixo peso, <b>glicosúria sem hiperglicemia</b> (túbulo proximal)</li>
<li>Adulto: <b>neuropatia</b> com <b>punho caído</b> (radial) · RX: linhas densas nos ossos longos</li>
<li>Normal &lt; 5 µg/dL (criança) e &lt; 10 (adulto) · intoxicação &gt; 10 e &gt; 25</li>
<li>Tirar a fonte sempre · <b>quelar</b>: adulto sintomático &gt; 70 · criança com encefalopatia ou &gt; 45</li></ul>''')}
{card('Benzeno e mercúrio', '''<ul><li><b>Benzeno</b> (inalado): CYP450 → hidroquinona → <b>benzoquinona</b> na medula → pancitopenia, <b>aplasia</b>, mielodisplasia → <b>LMA</b>; sem antídoto</li>
<li><b>Hg metálico</b> (vapor) → SNC: tremor, irritabilidade (micromercurialismo), gengivite</li>
<li><b>Hg inorgânico</b> (oral) → <b>rim</b>: necrose do túbulo proximal (S3), IRA</li>
<li><b>Metilmercúrio</b> (peixe, biomagnificação) → parestesia, ataxia, perda de visão e audição</li></ul>''')}
{card('Resíduos e vigilância', '<p>Agenda 21 (1992) · 3 R: reduzir, reutilizar, reciclar · <b>logística reversa</b> obrigatória (agrotóxicos, pilhas, pneus, óleos, eletrônicos) · SINITOX (Fiocruz), CEATOX, CIPA.</p>')}
</div><div>
{card('Plexo braquial', '''<ul><li>Troncos: <b>superior</b> C5–C6 · <b>médio</b> C7 · <b>inferior</b> C8–T1</li>
<li>Divisões anteriores → flexores · posteriores → extensores</li>
<li>Fascículos: <b>lateral</b> (anteriores do superior e médio) · <b>posterior</b> (todas as posteriores) · <b>medial</b> (anterior do inferior)</li>
<li><b>Radial</b> (fascículo posterior): tríceps e extensores; dorso da mão e base do polegar</li>
<li><b>Ulnar</b> (fascículo medial, C7–T1): flexor ulnar do carpo, metade medial do flexor profundo, maioria dos intrínsecos; dedo mínimo e metade do anular</li></ul>''')}
{card('Drogas de abuso', '''<table><tr><th></th><th>Maconha</th><th>LSD</th></tr>
<tr><td>Age em</td><td>THC → <b>CB1</b></td><td><b>5-HT2A</b></td></tr>
<tr><td>Marca</td><td>Fome, conjuntivite, taquicardia, incoordenação</td><td>Alucinação visual intensa, perda do juízo</td></tr>
<tr><td>Apetite</td><td>Aumenta</td><td>Diminui</td></tr></table>
<p style="margin-top:2px"><b>Simpaticomiméticos</b> (cocaína, anfetaminas, MDMA, catinonas): taquicardia, HAS, hipertermia, taquipneia, midríase.</p>''')}
{nc(['Chumbo dá anemia microcítica, não macrocítica.', 'Punho caído do chumbo é lesão do radial.', 'Benzeno ataca a medula; mercúrio inorgânico ataca o rim.', 'Glicosúria do chumbo vem com glicemia normal.', 'Maconha abre o apetite; LSD fecha.'])}
{mn([('Chumbo pinta a hemácia e a gengiva', 'pontilhado basofílico e linha de Burton.'), ('Mercúrio: pelo ar vai à cabeça, pela boca vai ao rim, pelo peixe vai ao nervo', ''), ('Benzeno bate na medula', 'aplasia e, depois, LMA.'), ('Punho caiu? Radial sumiu', ''), ('Rita Toma Doce Feito Recheio', '<b>R</b>aízes, <b>T</b>roncos, <b>D</b>ivisões, <b>F</b>ascículos, <b>R</b>amos.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo da SP 3.2 do 4º semestre (Casarett e Doull; Oga; Whalen; Moore; MSD Manual; MS 2021).'))

# ======================= SP 3.3 · PARACETAMOL E METABOLIZAÇÃO (B) =======================
FLX_PAR = '''<div class="flx">
<div class="fb esc">Paracetamol (dose terapêutica)</div><div class="fa">↓ fígado</div>
<div class="fr3"><div class="fb ok">Glicuronidação<div class="fp"><b>50–60%</b> · inativo</div></div><div class="fb ok">Sulfatação<div class="fp"><b>20–30%</b> · inativo</div></div><div class="fb ou">CYP2E1<div class="fp"><b>5–10%</b> → NAPQI</div></div></div>
<div class="fa">↓ NAPQI + glutationa = inofensivo</div>
<div class="fb vi">Superdose: conjugação satura → mais NAPQI → glutationa acaba</div><div class="fa">↓</div>
<div class="fb">NAPQI liga proteínas → <b>necrose hepática</b> (e lesão renal)</div><div class="fa">↓ antídoto</div>
<div class="fb ok"><b>N-acetilcisteína</b>: grupos SH neutralizam o NAPQI</div></div>'''

render(D3 + 'SP 3.3 · Toxicidade por fármacos, paracetamol e metabolização hepática - resumo em 1 folha', dict(layout='B',
 titulo='Toxicidade por Fármacos e Paracetamol',
 sub='Dose-resposta, interações, AAS, paracetamol, descontaminação, fígado e exames toxicológicos', vars='--fs:8.05pt;--lh:1.52;--gap:3.3mm',
 corpo=f'''<div class="gB"><div>
{card('Paracetamol: o caminho do NAPQI', FLX_PAR)}
{card('Paracetamol: o que cai', '''<ul><li>Inibe prostaglandinas <b>no SNC</b>: analgésico e antitérmico, quase sem ação anti-inflamatória; <b>não é AINE</b>; não mexe nas plaquetas</li>
<li>Escolha na criança com virose e <b>varicela</b> (AAS → síndrome de Reye)</li>
<li>Pico em 30–60 min · meia-vida 2–3 h (dobra na superdose ou hepatopatia)</li>
<li><b>Alcoolista:</b> etanol induz CYP2E1 → hepatotoxicidade até em dose terapêutica</li></ul>''')}
{card('AAS', '<ul><li>75 mg/dia já inativa as plaquetas · dose 50–325 mg/dia</li><li>Vira ácido salicílico; 80–90% na albumina; cinética de Michaelis-Menten: meia-vida de 2–3 h vai a 15–30 h em dose alta</li><li>Urina alcalina (pH 8) aumenta a excreção</li></ul>')}
{nc(['Paracetamol não é AINE e não altera plaquetas.', 'Quem mata o hepatócito é o NAPQI, não o paracetamol.', 'NAC repõe a defesa (SH); não é carvão.', 'Potenciação: um deles sozinho não é tóxico.', 'Imunocromatografia positiva precisa ser confirmada.'])}
</div><div>
{card('Dose-resposta e interações', '''<p><b>IT = DL50/DE50</b>: quanto maior, mais seguro. Na superdose: absorção prolongada, ↑ fração livre, Vd muda e o metabolismo satura.</p>
<table><tr><th>Interação</th><th>Conta</th></tr><tr><td>Aditiva</td><td>2 + 2 = 4</td></tr><tr><td>Sinergismo</td><td>2 + 2 = 20</td></tr><tr><td>Potenciação</td><td>0 + 2 = 10</td></tr><tr><td>Antagonismo</td><td>funcional, químico (quelante), disposicional, de receptor</td></tr></table>
<p style="margin-top:2px">Alérgica = imune (hapteno) · idiossincrática = genética.</p>''')}
{card('Tirar o tóxico do corpo', '''<ul><li><b>Carvão ativado</b> em dose única, ideal até <b>1 h</b> (carbamazepina, digoxina, fenitoína); em doses repetidas faz a "diálise gastrintestinal"</li>
<li>Ipeca: contraindicada · lavagem gástrica: rara · irrigação intestinal (PEG): liberação lenta</li>
<li><b>Alcalinizar a urina:</b> salicilato e 2,4-D</li>
<li><b>Extracorpórea</b> (hemodiálise, hemoperfusão): grave sem antídoto, falência hepática/renal, retirada esperada ≥ 30%</li></ul>''')}
{card('Fígado e exames', '<p>1ª passagem: porta (mesentérica superior + esplênica) → fígado (nitroglicerina perde &gt; 90%). Lesão hepática → <b>hipertensão portal</b> (varizes, cabeça de medusa) · ↓ albumina → ascite · ↑ bilirrubina → icterícia. <b>Imunocromatografia</b> = triagem rápida, qualitativa · <b>cromatografia + massa</b> = confirma e quantifica.</p>')}
{mn([('Glicuronida a granel, sulfata a sobra, NAPQI é nanico', '50–60%, 20–30% e 5–10%.'), ('NAC devolve a glutationa', 'e o NAPQI para de agredir.'), ('Álcool liga o CYP2E1', 'paracetamol vira veneno mais cedo.'), ('2 + 2 = 20 é sinergismo; 0 + 2 = 10 é potenciação', ''), ('Imuno triagem, cromatografia confirma', '')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo da SP 3.3 do 4º semestre (Whalen; Katzung; Casarett e Doull; Oga; Moore).'))
