# Folhas únicas do 6º D2 · NCS (SP 2.1 a 2.3) no estilo 2 (layouts A/B/C + Não confunda + mnemônicos)
# Conteúdo SÓ dos resumos publicados (PDFs do Drive "6º sem D2 · NCS · SP 2.x · Título.pdf"). Pedido da Laura (22/10/2026).
# Hematologia (Coagulopatias e PTI, Anemias carenciais, Falciforme e hemolíticas, Linfomas e leucemias):
#   texto dos resumos publicados (PDFs enviados pela Laura, versões de 21/10/2026).
import sys, os
os.environ.setdefault('PASTA', 'v2-g4')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from folha2 import render, ul, nc, mn, sec, card, box, cards, passos

N = '6º sem D2 · NCS · '

# ======================= SP 2.1 · CHOQUE HIPOVOLÊMICO (B) =======================
FLX_CH = '''<div class="flx">
<div class="fb esc">Trauma + sinais de hipoperfusão</div>
<div class="fp">taquicardia · pele fria e pálida · pulso fino (pressão de pulso estreita) · TEC lento · oligúria · confusão</div><div class="fa">↓ hipotensão é tardia</div>
<div class="fb">Controle da hemorragia: pressão direta (torniquete só na exsanguinação de extremidade) · 2 acessos · tipagem precoce</div><div class="fa">↓ quanto perdeu?</div>
<div class="fr"><div><div class="fb ou">Classe I–II · até 30%</div><div class="fp">compensa · <b>cristaloide isotônico</b> (RL ou SF) até 1 L no adulto, 20 mL/kg na criança</div></div>
<div><div class="fb vi">Classe III–IV · &gt; 30–40%</div><div class="fp">falha a compensação · <b>hemácias, plasma e plaquetas 1:1:1</b> (ou sangue total); urgência: O negativo</div></div></div>
<div class="fa">↓</div>
<div class="fb ok"><b>Controle definitivo:</b> cirurgia ou angioembolização · estabilizar pelve e ossos longos</div><div class="fa">↓ enquanto isso</div>
<div class="fr3"><div class="fb">Hipotensão permissiva<div class="fp">PAS 70–80 · no TCE &gt; 90</div></div><div class="fb">Ácido tranexâmico<div class="fp">até 3 h: 1 g em 10 min + 1 g em 8 h</div></div><div class="fb">Fluidos a 39 °C<div class="fp">contra a tríade letal</div></div></div></div>'''

render(N + 'SP 2.1 · Choque hipovolêmico, hemostasia sanguínea e drogas vasoativas - resumo em 1 folha', dict(layout='B',
 titulo='Choque Hipovolêmico e Vasoativas',
 sub='Reconhecer, repor, parar o sangramento · coagulação · vasopressores e inotrópicos', vars='--fs:7.7pt;--lh:1.46;--gap:3mm;--h1:22pt',
 corpo=f'''<div class="gB"><div>
{card('Choque hemorrágico: a conduta', FLX_CH)}
{card('Por que o corpo segura e depois cai', '''<p><b>PA = DC × RVS</b> e <b>DC = FC × VS</b>. Perde volume → cai pré-carga e VS (Frank-Starling) → taquicardia + vasoconstrição (catecolaminas, SRAA, ADH) seguram a PA → hipóxia → lactato, acidose → falência orgânica. Volume de sangue ≈ 7% do peso.</p>
<p><b>Onde sangra no trauma fechado:</b> tórax, abdome (baço 40–55%, fígado 35–45%), pelve/retroperitônio, fêmur (até 1.500 mL), tíbia ou úmero (até 750 mL). <b>FAST:</b> pericárdio, hepatorrenal, esplenorrenal, pelve; instável + FAST positivo → cirurgia.</p>
<p><b>Gravidade:</b> lactato &gt; 2 hipoperfusão, &gt; 4 grave · déficit de base ≤ −6 moderado, ≤ −10 grave.</p>''')}
{nc(['Hb e Ht normais não excluem choque hemorrágico: ainda não houve hemodiluição.', 'Hipotensão é sinal tardio: taquicardia e pulso fino vêm antes.', 'Vasopressor não é primeira linha na hemorragia: sobe a PA e piora a perfusão.', 'Neurogênico: hipotensão sem taquicardia (pode bradicardia) e pele quente.', 'Hemocomponente (hemácias, plaquetas, plasma, crio) ≠ hemoderivado (albumina, imunoglobulina, fatores).', 'Coloide não é rotina no choque hemorrágico.'])}
</div><div>
{card('Os 4 tipos de choque', '''<table><tr><th>Tipo</th><th>O que falha</th></tr>
<tr><td>Hipovolêmico</td><td>Volume (hemorragia: o mais comum no trauma)</td></tr>
<tr><td>Cardiogênico</td><td>Bomba: IAM extenso, rotura de papilar, contusão; congestão (B3, estertores, turgência jugular)</td></tr>
<tr><td>Obstrutivo</td><td>Enchimento: tamponamento, pneumotórax hipertensivo</td></tr>
<tr><td>Distributivo</td><td>Tônus: neurogênico (lesão medular alta), séptico</td></tr></table>''')}
{card('Drogas vasoativas', '''<table><tr><th>Droga</th><th>Chave da prova</th></tr>
<tr><td>Noradrenalina</td><td>Escolha no distributivo (séptico); na hemorragia só após volume</td></tr>
<tr><td>Adrenalina</td><td>α1, β1, β2; dose baixa β2, alta α1; <b>anafilaxia</b></td></tr>
<tr><td>Dopamina</td><td>1–3 D1 · 3–10 β1 · &gt; 10 α1; perdeu espaço (arritmia, mortalidade)</td></tr>
<tr><td>Vasopressina</td><td>V1 vasoconstrição, V2 retém água; adjuvante no séptico refratário; hiponatremia</td></tr>
<tr><td>Fenilefrina</td><td>α1 puro; neurogênico, anestesia; bradicardia reflexa</td></tr>
<tr><td>Inotrópicos</td><td><b>Dobutamina</b> β1 · <b>milrinone</b> PDE-3 · <b>levosimendan</b> sensibiliza o Ca²⁺; choque cardiogênico</td></tr></table>''')}
{card('Coagulação em 3 linhas', '''<ul><li>Lesão → colágeno e fator tecidual → vias convergem no <b>Xa</b> → protrombinase → trombina → fibrina → <b>XIIIa</b> estabiliza → plasmina dissolve (dímero-D)</li>
<li><b>TP/INR:</b> extrínseca + comum (VII) → varfarina · <b>TTPa:</b> intrínseca + comum → heparina não fracionada</li>
<li>Vitamina K: <b>II, VII, IX, X</b> + proteínas C e S · crioprecipitado: fibrinogênio + VIII</li></ul>''')}
{mn([('Frio, ácido e sangrando', 'a tríade letal: hipotermia, acidose e coagulopatia.'), ('Dopamina sobe a escada D, B, A', 'dose baixa Dopaminérgica, média Beta, alta Alfa.'), ('Fora tem 3 e 7; X marca o ponto', 'extrínseca = III e VII; a via comum começa no X.'), ('Dois mais sete, nove; mais um, dez', 'fatores da vitamina K: II, VII, IX e X.'), ('Neurogênico é quente e lento', 'pele quente, sem taquicardia.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo da SP 2.1 do 6º semestre (ATLS 10ª ed.; Bogliolo; Rang &amp; Dale; Harrison).'))

# ======================= SP 2.2 · ATEROSCLEROSE E DISSECÇÃO (A) =======================
render(N + 'SP 2.2 · Aterosclerose, dissecção aórtica, trombose e embolia - resumo em 1 folha', dict(layout='A',
 titulo='Aterosclerose, Aneurisma e Dissecção',
 sub='Da placa à aorta que rasga · hipertensão e anti-hipertensivos', vars='--fs:7.5pt;--lh:1.43;--gap:2.6mm',
 corpo=f'''<div class="sec"><h2>Como nasce a placa</h2>{passos([('Endotélio lesado', 'HAS, fumo, glicose, LDL, fluxo turbulento'), ('LDL oxidada', 'entra na íntima e inflama (TNF, IL-1)'), ('Célula espumosa', 'macrófago come LDL e forma a estria gordurosa'), ('Capa fibrosa', 'músculo liso migra da média (PDGF)'), ('Complica', 'ruptura → trombo; ou estenose, aneurisma')])}</div>
<div class="gL"><div>
{sec('Aterosclerose', '''<ul><li>Lipídio na íntima de artérias de médio e grande calibre. Locais: <b>aorta abdominal infrarrenal</b> (bifurcação ilíaca) &gt; coronárias &gt; carótidas internas &gt; renais &gt; femoral e poplítea</li>
<li>HAS abre caminho (lesão endotelial), LDL dá o material, diabetes acelera os dois</li>
<li><b>Placa estável</b> cresce devagar: angina estável, claudicação · <b>instável</b> rompe: IAM, AVC isquêmico, isquemia crítica de membro</li>
<li>Subclínica: placa na carótida, <b>ITB &lt; 0,9</b>, escore de cálcio &gt; 100, angioTC · manifesta: obstrução ≥ 50% · PCR-us &gt; 2 mg/L · HF: LDLR, ApoB, PCSK9</li>
<li>Risco em 10 anos: baixo &lt; 5% · intermediário 5–10% · alto 10–20% · muito alto &gt; 20% ou doença manifesta</li>
<li><b>HAS:</b> ≥ 140/90 em 2 ocasiões; ≥ 180/110 ou lesão de órgão-alvo = diagnóstico imediato; maior fator de risco para aneurisma e dissecção</li></ul>''')}
{sec('Aneurisma', '''<ul><li><b>Verdadeiro:</b> as três camadas · <b>pseudoaneurisma:</b> ruptura contida por tecido fibroso. Aorta: dilatação ≥ 50% do normal</li>
<li><b>Aterosclerose</b> na aorta abdominal (homem &gt; 50 anos, tabagista) · <b>sífilis</b> na ascendente (vasa vasorum) · <b>Marfan</b> (fibrilina-1) · <b>Kawasaki</b> nas coronárias</li>
<li>Sacular no polígono de Willis → hemorragia subaracnóidea · ascendente → insuficiência aórtica · descendente: silencioso até romper</li></ul>''')}
{sec('Dissecção aórtica', '''<ul><li>Rasgo na íntima → sangue entra na média → <b>falsa luz</b>. Dor torácica <b>súbita e intensa</b>, que imita IAM</li>
<li>HAS em 70–90%; Marfan, valva bicúspide, coarctação, cateterismo</li>
<li>Complica: tamponamento, insuficiência aórtica aguda, isquemia de ramos (coronária, renal, mesentérica, carótida)</li>
<li><b>Stanford</b> A ascendente · B descendente · <b>DeBakey</b> I ascendente + descendente · II só ascendente · III só descendente. Ascendente sem cirurgia: 80% de mortalidade em 2 semanas</li></ul>''')}
{sec('Anti-hipertensivos', '''<table><tr><th>Classe</th><th>Como age</th><th>Cai na prova</th></tr>
<tr><td>IECA</td><td>↓ Ang II, ↑ bradicinina</td><td>Tosse (~5%), angioedema, ↑ K⁺</td></tr>
<tr><td>BRA</td><td>Bloqueia AT₁</td><td>Sem tosse; não somar ao IECA</td></tr>
<tr><td>Tiazídico</td><td>NCC, túbulo distal</td><td>↓ K⁺, alcalose, <b>retém Ca²⁺</b></td></tr>
<tr><td>Alça</td><td>NKCC2, alça espessa</td><td>↓ K⁺, Mg²⁺ e Ca²⁺; congestão</td></tr>
<tr><td>Poupador de K⁺</td><td>ENaC ou aldosterona</td><td>↑ K⁺; espironolactona antifibrótica</td></tr>
<tr><td>β-bloqueador</td><td>β1 coração e renina</td><td>Carvedilol e labetalol também α1</td></tr>
<tr><td>α1-bloqueador</td><td>Vasodilata</td><td>1ª dose: hipotensão; não em monoterapia; HPB</td></tr>
<tr><td>BCC</td><td>Canal de Ca²⁺ tipo L</td><td>DHP: edema maleolar · verapamil: constipação</td></tr></table>''')}
</div><div>
{nc(['Pseudoaneurisma não tem as três camadas.', 'Dor torácica súbita pode ser dissecção, não IAM.', 'Tosse e angioedema são do IECA, não do BRA.', 'IECA e BRA: proibidos na gravidez; cuidado na estenose bilateral de renal.', 'Tiazídico segura o cálcio; alça joga fora.', 'Verapamil ou diltiazem + β-bloqueador: risco de BAV.', 'Mönckeberg calcifica a média e não estreita a luz.', 'BCC é preferido em idosos e negros (renina baixa).'])}
{mn([('Aterosclerose desce', 'a campeã é a aorta abdominal, abaixo das renais.'), ('Sífilis sobe', 'aneurisma da aorta ascendente.'), ('Stanford A de Ascendente', 'B de baixo: descendente.'), ('DeBakey conta até 3', 'I pega tudo, II só sobe, III só desce.'), ('Alça Arrasta, Tiazídico Trava', 'o cálcio: alça perde, tiazídico retém.'), ('IECA tosse de bradicinina', 'a que sobra sem a ECA; o BRA não mexe nela.')])}
{box('Números que caem', '<p>HAS ≥ 140/90 · urgente ≥ 180/110<br>ITB &lt; 0,9 · cálcio &gt; 100 · PCR-us &gt; 2<br>aneurisma ≥ 50% do diâmetro<br>dissecção: HAS em 70–90%</p>')}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo da SP 2.2 do 6º semestre (Rang &amp; Dale; Sobotta).'))

# ======================= SP 2.3 · TROMBOSE E ANTITROMBÓTICOS (C) =======================
VIRCHOW = '''<svg viewBox="0 0 150 132" width="100%" aria-hidden="true" font-family="Inter">
<polygon points="75,14 136,112 14,112" fill="#f7e8ea" stroke="#921827" stroke-width="1.6" stroke-linejoin="round"/>
<circle cx="75" cy="68" r="20" fill="#921827"/><text x="75" y="67" font-size="6.4" fill="#fff" text-anchor="middle" font-weight="600">TROMBO</text>
<text x="75" y="75" font-size="5.4" fill="#fff" text-anchor="middle">Virchow</text>
<text x="75" y="9" font-size="8" fill="#8a5f12" text-anchor="middle" font-weight="600">Lesão endotelial</text>
<text x="10" y="124" font-size="8" fill="#8a5f12" font-weight="600">Estase</text>
<text x="10" y="131" font-size="5.6" fill="#76696b">fluxo alterado</text>
<text x="140" y="124" font-size="8" fill="#8a5f12" text-anchor="end" font-weight="600">Hipercoagulação</text>
<text x="140" y="131" font-size="5.6" fill="#76696b" text-anchor="end">trombofilia</text></svg>'''

render(N + 'SP 2.3 · Trombose, embolia, antiplaquetários, anticoagulantes e trombolíticos - resumo em 1 folha', dict(layout='C',
 titulo='Trombose, Embolia e Antitrombóticos',
 sub='Virchow, TVP e TEP, coagulograma · antiplaquetários, anticoagulantes e trombolíticos', vars='--fs:7.7pt;--lh:1.46;--gap:3mm',
 corpo=f'''<div class="vis sec" style="--vw:40mm"><div>{VIRCHOW}</div><div>{cards([('TP / INR', 'extrínseca', 'VII + via comum · varfarina'), ('TTPa', 'intrínseca', 'XII, XI, IX, VIII + comum · heparina'), ('TT', 'fibrinogênio', 'heparina, dabigatrana, disfibrinogenemia')])}
<p class="m" style="margin-top:2.5mm">TTPa alongado isolado: hemofilia, heparina ou anticoagulante lúpico → <b>teste de mistura</b>: corrige = falta fator · não corrige = inibidor.</p></div></div>
<div class="sec"><h2>Cada remédio age num ponto</h2>{passos([('Antiplaquetário', 'impede o tampão de plaquetas: trombo arterial (IAM, AVC)'), ('Anticoagulante', 'impede a fibrina: TVP, TEP, FA; não dissolve o que já existe'), ('Trombolítico', 'plasminogênio → plasmina, que dissolve o coágulo: TEP maciço, AVC agudo')])}</div>
<div class="g2"><div>
{sec('Trombo e embolia', '''<ul><li><b>Arterial = branco</b> (plaquetas, alto cisalhamento) · <b>venoso = vermelho</b> (hemácias, estase) · <b>linhas de Zahn</b>: formado em vida</li>
<li>Destinos: propaga, emboliza, dissolve, organiza e recanaliza</li>
<li><b>TVP:</b> 80–95% nos membros inferiores; <b>proximal</b> (ilíaca, femoral, poplítea) embola mais. Wells → <b>dímero-D</b> (exclui na baixa probabilidade) → Doppler</li>
<li><b>TEP:</b> espaço morto, V/Q alterada, hipoxemia; VD dilata, septo empurra o VE → choque obstrutivo. Êmbolo a cavaleiro = morte súbita. AngioTC ou cintilografia V/Q</li>
<li>Outros êmbolos: <b>gordura</b> (fratura), <b>líquido amniótico</b> (TEP + CID), <b>gás</b> (mergulho), colesterol, séptico · <b>paradoxal</b>: TVP → forame oval patente</li>
<li><b>Trombofilia</b> herdada: fator V Leiden, protrombina G20210A, falta de AT, proteína C ou S · adquirida: câncer (Trousseau), SAF, HIT, gestação, ACO, nefrótica (perde AT)</li>
<li><b>CID:</b> plaquetas e fibrinogênio ↓, dímero-D ↑, TP, TTPa e TT ↑</li></ul>''')}
{nc(['Anticoagulante não dissolve trombo; o trombolítico, sim.', 'Heparina: TTPa · varfarina: TP/INR · HBPM: anti-Xa.', 'Varfarina não age na hora: 24–72 h (o VII cai primeiro, o II por último).', 'Varfarina na gestação, não; na amamentação, pode.', 'HBPM na insuficiência renal: prefira HNF.', 'Homans é pouco específico.'])}
</div><div>
{sec('Os remédios', '''<table><tr><th>Droga</th><th>Alvo e chave</th></tr>
<tr><td>AAS</td><td>COX-1 irreversível, ↓ TXA₂; 75–100 mg; dura 7–10 dias</td></tr>
<tr><td>Clopidogrel, prasugrel, ticagrelor</td><td>P2Y₁₂ (ADP); ticagrelor é reversível</td></tr>
<tr><td>Abciximabe, tirofibana</td><td>GPIIb/IIIa: via final da agregação</td></tr>
<tr><td>Heparina não fracionada</td><td>Ativa AT: IIa = Xa; IV, TTPa; <b>protamina</b>; risco de HIT</td></tr>
<tr><td>HBPM</td><td>Xa ≫ IIa; SC, sem monitorar; protamina parcial</td></tr>
<tr><td>Varfarina</td><td>VKORC1: II, VII, IX, X, C e S; INR; ↑ com amiodarona e metronidazol, ↓ com rifampicina e folhas verdes</td></tr>
<tr><td>Dabigatrana</td><td>Anti-IIa direta; renal; <b>idarucizumabe</b></td></tr>
<tr><td>Rivaroxabana, apixabana, edoxabana</td><td>Anti-Xa direto; <b>andexanete alfa</b></td></tr>
<tr><td>Trombolíticos</td><td>Estreptoquinase (sistêmica) · alteplase (tPA, seletiva p/ fibrina) · reteplase (bolus)</td></tr></table>''')}
{mn([('Virchow: parede, fluxo e sangue', 'lesão endotelial, estase e hipercoagulabilidade.'), ('Branco na artéria, vermelho na veia', 'artéria pede antiplaquetário; veia, anticoagulante.'), ('Tem XA no nome? Inibe o Xa', 'rivaroXAbana, apiXAbana, edoXAbana.'), ('A IDA da dabigatrana', 'IDArucizumabe reverte; protamina é da heparina.'), ('O AAS dura o que a plaqueta dura', 'sem núcleo, sem COX nova: 7 a 10 dias.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo da SP 2.3 do 6º semestre (Rang &amp; Dale; Goodman &amp; Gilman; Bogliolo; Bethesda).'))

# ======================= SP 2.1 · COAGULOPATIAS E PTI (B) =======================
FLX_SG = '''<div class="flx">
<div class="fb esc">Paciente que sangra: onde e como?</div><div class="fa">↓</div>
<div class="fr"><div><div class="fb ou">Pele e mucosas, imediato</div><div class="fp">petéquias, epistaxe, gengiva, <b>menorragia</b> → plaqueta ou FvW (primária)</div></div>
<div><div class="fb vi">Articulação e músculo, tardio</div><div class="fp"><b>hemartrose</b>, hematoma profundo → fator (secundária)</div></div></div>
<div class="fa">↓ hemograma, esfregaço, TP e TTPa</div>
<div class="fr"><div class="fb">Plaquetas baixas, TP e TTPa normais<div class="fp">PTI, AAS, trombocitopatias</div></div><div class="fb">TP normal, TTPa longo<div class="fp">hemofilias, DvW com FVIII baixo, heparina, lúpico</div></div></div>
<div class="fr" style="margin-top:5px"><div class="fb">TP longo, TTPa normal<div class="fp">falta de FVII, início da varfarina</div></div><div class="fb">TP e TTPa longos<div class="fp">vitamina K, hepatopatia, CIVD</div></div></div>
<div class="fa">↓ TTPa longo</div>
<div class="fb ok"><b>Teste de mistura 1:1:</b> corrige = falta fator · não corrige = inibidor (anti-FVIII, anticoagulante lúpico)</div></div>'''

render(N + 'SP 2.1 · Coagulopatias hereditárias e PTI - resumo em 1 folha', dict(layout='B',
 titulo='Coagulopatias Hereditárias e PTI',
 sub='Padrão do sangramento, PTI, doença de von Willebrand, hemofilias e TEV', vars='--fs:7.7pt;--lh:1.46;--gap:3mm;--h1:23pt',
 corpo=f'''<div class="gB"><div>
{card('Do sangramento ao exame', FLX_SG)}
{card('Trombocitopenia imune (PTI)', '''<p>Plaquetas <b>&lt; 100.000</b> isoladas, por autoanticorpo; diagnóstico de <b>exclusão</b>. Criança: pico 2–6 anos, pós-viral, 80–85% remitem em 12 meses. Adulto: crônica, mais em mulheres. Exame físico normal fora o sangramento.</p>
<ul><li><b>Mielograma</b> só se atípico: visceromegalia, linfonodos, outras citopenias, falha do tratamento, &gt; 60 anos</li>
<li><b>Alarme:</b> púrpura úmida (bolhas na boca) e hemorragia retiniana</li>
<li><b>Criança</b> sem sangramento ou só cutâneo: <b>observar</b> · mucosa: prednisona 2–4 mg/kg/dia por 5–7 dias, IgIV ou anti-D · HIC: plaquetas + metilprednisolona + IgIV</li>
<li><b>Adulto:</b> &gt; 30.000 não aumenta mortalidade · prednisona 1 mg/kg · 2ª linha: agonista de TPO, rituximabe, esplenectomia</li></ul>''')}
{card('TEV e antitrombóticos', '<p>Wells baixo ou moderado → <b>D-dímero</b> (só exclui); alto → imagem. TVP: US com compressão · EP: <b>angioTC</b>; maciça: alteplase 100 mg em 2 h. Anticoagular no mínimo 3 meses. HNF: TTPa e protamina · HBPM: anti-Xa · varfarina: INR 2–3 · TIH (5–10 dias): argatrobana ou fondaparinux.</p>')}
</div><div>
{card('Doença de von Willebrand', '''<p>A hereditária <b>mais comum</b>; autossômica (homens e mulheres). Sangramento mucocutâneo e <b>menorragia</b>. FvW carrega o FVIII: se cai muito, o TTPa alonga.</p>
<ul><li><b>Tipo 1</b> (≥ 80%) quantitativo · <b>2B</b> plaquetopenia, desmopressina contraindicada · <b>2N</b> imita hemofilia A · <b>3</b> ausência, hemartroses</li>
<li>FvW:RCo/FvW:Ag ≥ 0,7 = tipo 1 · &lt; 0,7 = tipo 2</li>
<li><b>Desmopressina 0,3 µg/kg</b> no tipo 1; concentrado de FVIII/FvW; antifibrinolítico</li></ul>''')}
{card('Hemofilias A (FVIII) e B (FIX)', '''<ul><li>Ligadas ao X; 30% sem história familiar. Grave <b>&lt; 1%</b> · moderada 1–5% · leve 5–40% (MS)</li>
<li>Hemartrose (70–80%): joelho, cotovelo, tornozelo. TTPa longo que corrige; TP e plaquetas normais</li>
<li><b>FVIII (UI) = (alvo − basal) × peso × 0,5</b> · FIX × 1 · 70 kg de 0 a 100% = 3.500 UI</li>
<li>TCE ou SNC: fator a 80–100% <b>antes da TC</b> · <b>profilaxia</b> é o padrão na criança grave</li>
<li><b>Inibidor</b> (~30% na A grave): &lt; 5 UB dobra a dose · ≥ 5 UB agente de bypass · emicizumabe no SUS</li></ul>''')}
{nc(['Hemofílico forma o tampão; ele só não se sustenta e sangra horas depois.', 'Falta de FXII alonga muito o TTPa e não sangra.', 'Grupo O tem metade do FvW: exame normal não exclui DvW.', 'Desmopressina não serve na hemofilia A grave nem na B.', 'Na PTI não há febre no sangramento; na dengue há leucopenia e hematócrito subindo.', 'Nunca AAS, AINE ou injeção IM em quem tem coagulopatia.'])}
{mn([('Plaqueta pinta, fator enche', 'petéquia na pele × sangue dentro da articulação.'), ('Corrigiu, faltava; não corrigiu, tem ladrão', 'teste de mistura: falta de fator × inibidor.'), ('Oito vale meio, nove vale um', 'FVIII: × 0,5 por kg · FIX: × 1.'), ('Hemofilia vem pelo X; von Willebrand pega todo mundo', 'ligada ao X × autossômica.'), ('No 2B, desmopressina sai de cena', 'piora a plaquetopenia.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo da SP 2.1 do 6º semestre (MS: protocolos de hemofilias e de DvW; Tratado de Pediatria SBP; Harrison).'))

# ======================= SP 2.2 · ANEMIAS CARENCIAIS (C) =======================
render(N + 'SP 2.2 · Anemias carenciais - resumo em 1 folha', dict(layout='C',
 titulo='Anemias Carenciais',
 sub='Ferropriva e megaloblástica (vitamina B12 e folato)', vars='--fs:7.9pt;--lh:1.48;--gap:3.2mm',
 corpo=f'''<div class="sec">{cards([('Anemia (OMS/MS)', '&lt; 13 · &lt; 12', 'homem · mulher; gestante e criança &lt; 11'), ('Ferritina', '&lt; 30', 'confirma falta de ferro; &lt; 15 grave'), ('Ferro oral', '≥ 90 dias', 'até ferritina ≥ 30'), ('B12 típica', '&lt; 200 pg/mL', '&lt; 100 é típico da megaloblástica')])}</div>
<div class="sec"><h2>Primeiro passo: reticulócito e VCM</h2>{passos([('Índice reticulocítico', '&lt; 2 = a medula não produz (carenciais) · &gt; 2,5 = hemólise'), ('VCM', '&lt; 80 micro (ferro) · 80–100 normo · &gt; 100 macro (B12, folato)'), ('RDW', 'alto na ferropriva; normal no traço talassêmico'), ('Exame-chave', 'ferritina (ferro) · B12 e folato; ácido metilmalônico se limítrofe')])}</div>
<div class="g2"><div>
{sec('Anemia ferropriva', '''<ul><li>Absorção no <b>duodeno</b>; a <b>hepcidina</b> degrada a ferroportina: cai na falta de ferro, sobe na inflamação</li>
<li>Ordem da queda: <b>ferritina</b> → ferro e saturação → Hb e microcitose</li>
<li>Causas: perda (menstruação, trato digestivo, parasitose), gestação e crescimento, dieta, má absorção (bariátrica, celíaca, IBP)</li>
<li>Clínica: coiloníquia, queilite, <b>pica</b> (pagofagia), Plummer-Vinson</li></ul>
<table><tr><th></th><th>Ferropriva</th><th>Inflamação</th><th>Traço talass.</th></tr>
<tr><td>Ferritina</td><td>&lt; 30</td><td>≥ 100</td><td>50–300</td></tr>
<tr><td>TIBC</td><td><b>Alta</b></td><td><b>Baixa</b></td><td>Normal</td></tr>
<tr><td>RDW</td><td>Alto</td><td>Normal/alto</td><td><b>Normal</b></td></tr></table>
<p style="margin-top:2px">Inflamação + saturação &lt; 20% + ferritina 30–100 = ferropenia associada. <b>Tratar:</b> sulfato ferroso longe das refeições (homem 120 mg/dia; mulher e gestante 100–200 mg; criança 3–6 mg/kg). Reticulócitos sobem do <b>3º ao 5º dia</b>; Hb +2 g/dL em 3–4 semanas. IV: intolerância, falha em 8 semanas, bariátrica, DII, diálise.</p>''')}
</div><div>
{sec('Anemia megaloblástica', '''<ul><li>Falha na síntese de DNA. <b>Ácido metilmalônico sobe só na falta de B12</b>; homocisteína sobe nas duas</li>
<li>Eritropoese ineficaz: <b>LDH e bilirrubina indireta altas</b> com reticulócitos baixos; pode haver pancitopenia</li>
<li><b>B12:</b> anemia perniciosa, gastrectomia, íleo, veganos, metformina e IBP; reserva de 3–4 anos · <b>folato:</b> álcool, gestação, hemólise, metotrexato; reserva de 3–4 meses</li>
<li><b>Só a B12 lesa o nervo:</b> parestesia, perda vibratória, Romberg, degeneração combinada subaguda</li>
<li>Macro-ovalócitos e <b>neutrófilos hipersegmentados</b> (5 ou mais lobos)</li>
<li><b>B12 1.000 µg IM</b> (~6 doses) → mensal, por toda a vida se a causa persiste · <b>ácido fólico 5 mg/dia por 4 meses</b> · gestação 400 µg</li></ul>''')}
{nc(['Falta de ferro no homem ou na pós-menopausa: procure sangramento digestivo.', 'Ferritina é de fase aguda: pode vir normal na inflamação.', 'Traço talassêmico: RDW e ferro normais; não dê ferro.', 'Nunca ácido fólico sozinho sem excluir falta de B12.', 'Lesão neurológica da B12 pode vir sem anemia.', 'LDH alta na megaloblástica não é hemólise periférica.'])}
{mn([('Ferritina abaixo de 30, falta ferro', 'corte do protocolo brasileiro.'), ('Hepcidina é a porteira: inflamou, fecha', 'segura o ferro e a absorção cai.'), ('B12 mexe com os nervos, folato não', 'neurológico é só da B12.'), ('Metilmalônico Marca a B12', 'sobe só na falta dela.'), ('Folato some em meses, B12 em anos', 'reserva de 3–4 meses × 3–4 anos.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo da SP 2.2 do 6º semestre (Conitec: PCDT da anemia por deficiência de ferro; Tratado de Pediatria SBP; Harrison).'))

# ======================= SP 2.3 · FALCIFORME E HEMOLÍTICAS (B) =======================
FLX_HE = '''<div class="flx">
<div class="fb esc">Anemia + reticulocitose + LDH ↑ + BI ↑ + haptoglobina ↓</div><div class="fa">↓ é hemólise: Coombs direto e esfregaço</div>
<div class="fr"><div><div class="fb vi">Coombs positivo · imune</div><div class="fp">AHAI quente (IgG) ou fria (IgM), transfusão, drogas</div></div>
<div><div class="fb ou">Coombs negativo</div><div class="fp">membrana, enzima, hemoglobina, mecânica, HPN</div></div></div>
<div class="fa">↓ o esfregaço aponta</div>
<div class="fr3"><div class="fb">Esferócitos<div class="fp">esferocitose ou AHAI quente</div></div><div class="fb">Esquizócitos<div class="fp">PTT, SHU, CIVD, prótese</div></div><div class="fb">Heinz, mordidas<div class="fp">deficiência de G6PD</div></div></div>
<div class="fp" style="margin-top:3px"><b>Intravascular:</b> hemoglobinúria, LDH muito alta · <b>extravascular:</b> baço grande, esferócitos</div></div>'''

render(N + 'SP 2.3 · Doença falciforme e anemias hemolíticas - resumo em 1 folha', dict(layout='B',
 titulo='Doença Falciforme e Anemias Hemolíticas',
 sub='Reconhecer a hemólise · crises da falciforme · talassemias, membrana, enzimas e adquiridas', vars='--fs:7.7pt;--lh:1.46;--gap:3mm;--h1:21pt',
 corpo=f'''<div class="gB"><div>
{card('Reconhecer a hemólise', FLX_HE)}
{card('Talassemias', '''<ul><li><b>β-menor:</b> Hb &gt; 10, VCM muito baixo, RDW normal, <b>HbA2 &gt; 3,6–4%</b> · <b>β-maior (Cooley):</b> do 3º mês, Hb &lt; 7, deformidade de face → transfusão + quelação de ferro</li>
<li><b>α:</b> 1 gene silencioso · 2 traço · 3 doença da HbH · 4 <b>Hb Bart → hidropsia fetal</b></li></ul>''')}
{card('Membrana, enzima e adquiridas', '''<ul><li><b>Esferocitose:</b> anemia + icterícia + baço + litíase precoce; <b>CHCM &gt; 34</b>, Coombs negativo, EMA; esplenectomia conforme a gravidade</li>
<li><b>G6PD:</b> ligada ao X; hemólise após infecção, fava, primaquina, dapsona, sulfa, rasburicase; dosar fora da crise</li>
<li><b>AHAI quente</b> IgG → prednisona 1 mg/kg · <b>fria</b> IgM (Mycoplasma, EBV, linfoma) → evitar o frio</li>
<li><b>HPN:</b> hemólise + trombose atípica + falência medular; citometria CD55/CD59</li>
<li><b>PTT:</b> esquizócitos + plaquetopenia + coagulograma normal; ADAMTS13 &lt; 10% → troca plasmática já</li></ul>''')}
</div><div>
{card('Doença falciforme', '''<p>Valina no lugar do ácido glutâmico na β-globina; HbS polimeriza → <b>vaso-oclusão + hemólise</b>; <b>HbF protege</b>. SS e Sβ⁰ graves · SC: retina e osso · AS: traço, não é doença. Pezinho: <b>FS</b> doença, <b>FAS</b> traço; eletroforese confirma após 6 meses. <b>Asplenia funcional</b> em 94% aos 5 anos.</p>
<table><tr><th>Quadro</th><th>Conduta</th></tr>
<tr><td>Febre</td><td>Avaliar em <b>até 4 h</b>; hemocultura e <b>antibiótico parenteral</b> sem esperar</td></tr>
<tr><td>Crise dolorosa</td><td>Analgesia imediata e escalonada; sem hiper-hidratar</td></tr>
<tr><td>Síndrome torácica aguda</td><td>Infiltrado novo: cefalosporina + macrolídeo, O₂ para SatO₂ &gt; 92%, transfusão se piora</td></tr>
<tr><td>Sequestro esplênico</td><td>Baço cresce + Hb despenca: cristaloide + hemácias 5 mL/kg</td></tr>
<tr><td>Crise aplástica</td><td><b>Reticulócitos baixos</b>, parvovírus B19: suporte</td></tr>
<tr><td>AVC</td><td><b>Exsanguineotransfusão</b> (HbS &lt; 30%)</td></tr>
<tr><td>Priapismo</td><td>Sem melhora em 2 h: hospital</td></tr></table>
<p style="margin-top:2px"><b>Prevenir:</b> penicilina dos 3 meses aos 5 anos · vacinas · Doppler transcraniano; ≥ 200 cm/s → transfusão crônica · <b>hidroxiureia a partir de 9 meses</b> na SS e Sβ⁰ (2024), 15 → 35 mg/kg/dia · TCTH cura.</p>''')}
{nc(['Toda febre na falciforme é emergência.', 'Aplástica tem reticulócito baixo; sequestro tem baço grande.', 'Hiper-hidratação na crise dolorosa pode precipitar síndrome torácica.', 'Esferócito com Coombs negativo = esferocitose; positivo = AHAI.', 'Microcitose com ferritina normal: pense em talassemia.', 'G6PD normal na crise não exclui: repita depois.'])}
{mn([('Febre na falciforme: antibiótico antes da pergunta', 'sepse por pneumococo no baço que não funciona.'), ('Quente é G, frio é M', 'AHAI quente IgG · fria IgM.'), ('Alfa conta genes: 1 cala, 2 traça, 3 H, 4 Bart', 'silencioso, traço, HbH, hidropsia.'), ('G6PD tem medo de fava', 'e de primaquina, sulfa e dapsona.'), ('HbF é o escudo', 'por isso a hidroxiureia funciona.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo da SP 2.3 do 6º semestre (MS: PCDT da doença falciforme e atualização de 2024; Tratado de Pediatria SBP; Harrison).'))

# ======================= SP 2.4 · LINFOMAS E LEUCEMIAS AGUDAS (A) =======================
render(N + 'SP 2.4 · Linfomas e leucemias agudas - resumo em 1 folha', dict(layout='A',
 titulo='Linfomas e Leucemias Agudas',
 sub='LLA × LMA, LPA, emergências onco-hematológicas, Hodgkin × não Hodgkin', vars='--fs:7.7pt;--lh:1.46;--gap:3mm',
 corpo=f'''<div class="gL"><div>
{sec('Leucemia aguda', '''<p><b>Falência medular</b> (anemia, plaquetopenia, febre por neutropenia) + <b>infiltração</b> (dor óssea na criança, visceromegalia, gengiva na monocítica, massa mediastinal na LLA-T). LMA: <b>≥ 20% de blastos</b> (qualquer % com t(15;17), t(8;21), inv(16)). A <b>imunofenotipagem</b> separa LMA de LLA.</p>
<table><tr><th></th><th>LLA</th><th>LMA</th></tr>
<tr><td>Quem</td><td><b>Criança</b>, pico 2–5 anos</td><td><b>Adulto</b>, idoso</td></tr>
<tr><td>Marcadores</td><td>TdT+; B: CD19, CD10 · T: CD3, CD7</td><td>MPO, CD13, CD33 · <b>bastonetes de Auer</b></td></tr>
<tr><td>Risco</td><td>Ruim: &gt; 50.000 leucócitos, hipodiploidia, Ph+ · bom: DRM negativa</td><td>Genética (ELN): t(8;21), inv(16), NPM1 favoráveis; TP53 adverso</td></tr>
<tr><td>Tratar</td><td>Indução, consolidação, <b>profilaxia do SNC</b>, manutenção 6-MP + MTX; 2–2,5 anos; criança &gt; 85%</td><td><b>"7 + 3"</b> (citarabina + antraciclina); idoso: azacitidina</td></tr></table>
<p style="margin-top:2px"><span class="k">LPA</span> t(15;17) PML-RARA: <b>CIVD</b> e risco de hemorragia intracraniana → <b>ATRA + trióxido de arsênio</b> já; síndrome de diferenciação nas 3 primeiras semanas → corticoide.</p>''')}
{sec('Emergências', '''<ul><li><b>Lise tumoral:</b> Burkitt, LLA, LDH &gt; 1.500; ↑ ácido úrico, K e P, ↓ Ca → hidratação 3 L/m²/dia + alopurinol ou rasburicase</li>
<li><b>Leucostase:</b> blastos &gt; 100.000 com pulmão ou neuro (mais na LMA) → quimioterapia logo, hidroxiureia; evitar transfundir hemácias; pseudo-hipoxemia</li>
<li><b>Neutropenia febril:</b> ≥ 38,5 °C (ou 3 × ≥ 38 °C em 24 h) + neutrófilos &lt; 500 → culturas + <b>cefepima ou piperacilina-tazobactam</b> sem esperar</li></ul>''')}
{sec('Linfomas', '''<p><b>Linfonodo suspeito:</b> &gt; 2 cm, indolor, <b>supraclavicular</b>, &gt; 4–6 semanas, sintomas B, &gt; 40 anos → <b>biópsia excisional</b> (PAAF não basta); evite corticoide antes.</p>
<table><tr><th></th><th>Hodgkin</th><th>Não Hodgkin</th></tr>
<tr><td>Célula</td><td><b>Reed-Sternberg</b> CD30+ CD15+</td><td>B em ~90%</td></tr>
<tr><td>Quem</td><td>Bimodal; EBV, HIV; esclerose nodular no mediastino</td><td>Cresce com a idade; HIV, EBV, H. pylori</td></tr>
<tr><td>Espalha</td><td><b>Contígua</b>, de cadeia em cadeia</td><td>Salteada, extranodal</td></tr>
<tr><td>Tratar</td><td><b>ABVD</b> ± radioterapia</td><td>Difuso de grandes células B: <b>R-CHOP</b></td></tr></table>
<p style="margin-top:2px">Folicular <b>t(14;18)</b> · Burkitt <b>t(8;14)</b>, "céu estrelado" · manto <b>t(11;14)</b> · MALT gástrico → erradicar H. pylori. <b>Ann Arbor:</b> I uma cadeia · II ≥ 2 do mesmo lado do diafragma · III dos dois lados · IV extranodal difuso · B: febre &gt; 38 °C, sudorese, perda &gt; 10% em 6 meses · X: massa ≥ 10 cm.</p>''')}
</div><div>
{nc(['Aguda bloqueia a maturação (blastos); crônica acumula células maduras.', 'Sangramento + fibrinogênio baixo na leucemia: pense em LPA.', 'Corticoide antes do mielograma mascara a LLA.', 'Dor óssea + citopenias na criança: LLA, não artrite.', 'Rasburicase é proibida na deficiência de G6PD.', 'Neutropênico não faz pus: a febre pode ser o único sinal.', 'Supraclavicular esquerdo (Virchow) aponta o abdome.'])}
{mn([('LLA é Lá na infância, LMA é Mais velho', 'criança × adulto.'), ('Auer é agulha de LMA', 'bastonete de Auer praticamente fecha o diagnóstico.'), ('LPA sangra: ATRA destrava', 'PML-RARA trava o promielócito; ATRA e arsênio liberam.'), ('Hodgkin anda de vizinho em vizinho', 'disseminação contígua.'), ('Febre com menos de 500: antibiótico já', 'neutropenia febril.'), ('Mediastino anterior tem 4 Ts', 'timoma, teratoma, tireoide e terríveis linfomas.')])}
{box('Números que caem', '<p>LMA ≥ 20% de blastos<br>lise: LDH &gt; 1.500 · 3 L/m²/dia<br>leucostase &gt; 100.000<br>neutropenia &lt; 500 · febre ≥ 38,5 °C<br>massa volumosa ≥ 10 cm</p>')}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo da SP 2.4 do 6º semestre (MS: PCDT do linfoma de Hodgkin; OMS 2022; ELN; Tratado de Pediatria SBP; Harrison).'))
