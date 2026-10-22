# Folhas únicas do 4º D2 · NCS (SP 2.1 a 2.4) no estilo 2 (layouts A/B/C + Não confunda + mnemônicos)
# Conteúdo SÓ dos resumos publicados (PDFs do Drive "4º sem D2 · NCS · SP x.y · Título.pdf"). Pedido da Laura (22/10/2026).
# Sem fonte no Drive (puladas): SP 2.1 Mamas, câncer de mama e climatério · SP 2.2 Placenta e DMG ·
#   SP 2.3 Pelve, assoalho pélvico e ISTs · SP 2.4 Sangramento uterino anormal.
import sys, os
os.environ.setdefault('PASTA', 'v2-g2')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from folha2 import render, ul, nc, mn, sec, card, box, cards, passos

N = '4º sem D2 · NCS · '

# ======================= SP 2.1 · CÂNCER DE MAMA (C) =======================
render(N + 'SP 2.1 · Câncer de mama - resumo em 1 folha', dict(layout='C', titulo='Câncer de Mama',
 sub='Linfa, fatores de risco, rastreamento, BI-RADS, subtipos e tratamento', vars='--fs:7.7pt;--lh:1.45;--gap:2.9mm',
 corpo=f'''<div class="sec">{cards([('Rastreamento', '50–69 anos', 'mamografia a cada 2 anos (INCA)'), ('Mais comum', 'CDI 70–80%', 'carcinoma ductal invasivo'), ('Linfa', '≈ 75% axilar', '1ª estação: peitorais'), ('Biópsia', 'BI-RADS 4–5', '3 = controle em 6 meses')])}</div>
<div class="sec"><h2>Do achado ao tratamento</h2>{passos([('Suspeita', 'nódulo fixo e indolor (~90%), pele em casca de laranja, retração, descarga espontânea, linfonodo axilar'), ('Mamografia diagnóstica', 'com ou sem US; laudo em <b>BI-RADS</b>'), ('Biópsia + IHQ', 'RE, RP, HER2, Ki-67 e grau (1 bem, 3 mal diferenciado)'), ('Estadiar e tratar', 'TNM + biologia + condições da paciente')])}</div>
<div class="g2"><div>
{sec('Quem tem mais risco', '''<ul><li><b>Idade</b>: principal fator (raro &lt; 35 anos) · <b>história familiar</b> de 1º grau: associação mais forte</li>
<li><b>Mais estrogênio na vida</b>: menarca &lt; 12, menopausa &gt; 55, 1ª gestação &gt; 30, nuliparidade, ACO prolongado, TH</li>
<li><b>BRCA1</b> (cromossomo 17): antes dos 50, ovário, triplo-negativo · <b>BRCA2</b> (13): ovário, mama no <b>homem</b>, RH+ · TP53 (Li-Fraumeni) · CHEK2 dobra o risco</li>
<li>Álcool (acetaldeído, ↑ estradiol), obesidade (insulina, IGF-1, inflamação), radiação</li>
<li><b>Protegem:</b> amamentação (prolactina freia o eixo), gestação (progesterona), atividade física</li></ul>''')}
{sec('Tipos histológicos', '''<ul><li><b>In situ:</b> CDIS (câncer não invasivo, bom prognóstico) · CLIS (marcador de risco, não câncer propriamente)</li>
<li><b>Invasivos:</b> ductal 70–80% (massa palpável) · lobular 10–15% (difícil de detectar) · medular, mucinoso (lagos de mucina) e tubular (~5% cada; tubular tem prognóstico excelente)</li></ul>''')}
</div><div>
{sec('Subtipos moleculares', '''<table><tr><th>Subtipo</th><th>Perfil</th></tr>
<tr><td>Luminal A</td><td>RE e RP +, HER2 −, cresce devagar</td></tr>
<tr><td>Luminal B</td><td>RE e/ou RP +, Ki-67 alto, HER2 + ou −</td></tr>
<tr><td>HER2</td><td>Amplificação de HER2 (via PI3K/AKT/mTOR)</td></tr>
<tr><td>Triplo-negativo</td><td>RE, RP e HER2 −: quimio (± imuno)</td></tr></table>''')}
{sec('Tratamento por estádio', '<ul><li><b>I e II:</b> cirurgia (conservadora) ± radioterapia; sistêmico pelo risco de recorrência</li><li><b>III:</b> sistêmico <b>primeiro</b> (neoadjuvante), depois cirurgia e radioterapia</li><li><b>IV:</b> sistêmico; local só em casos restritos</li></ul>')}
{box('BI-RADS', '<p>1 normal · 2 benigno · 3 provavelmente benigno (6 meses) · 4 suspeito (biópsia) · 5 típico de câncer: nódulo espiculado, calcificações pleomórficas · 6 câncer já confirmado</p>')}
</div></div>
<div class="g2"><div>{nc(['CLIS não é câncer: é marcador de risco. CDIS é câncer, mas não invasivo.', 'Autoexame não é rastreamento: estimule o autoconhecimento.', 'US e RM não substituem a mamografia no risco habitual.', 'Rastrear antes dos 50 ou todo ano aumenta danos sem ganho (risco habitual).', 'Alto risco (BRCA, Li-Fraumeni, radiação antes dos 30): conduta individual, começa antes, pode somar RM.'])}</div>
<div>{mn([('BRCA1 tem 17, BRCA2 tem 13', 'os cromossomos de cada gene.'), ('O 2 também pega o homem', 'BRCA2 aumenta câncer de mama masculino.'), ('Dos 50 aos 69, de 2 em 2', 'mamografia de rastreamento.'), ('Três espera, quatro e cinco furam', 'BI-RADS 3 controla em 6 meses; 4 e 5 vão à biópsia.'), ('Mamar fecha a torneira do estrogênio', 'prolactina inibe o eixo: amamentar protege.')])}</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de câncer de mama do 4º semestre (INCA, diretrizes de detecção precoce; Robbins; Bogliolo; Moore).'))

# ======================= SP 2.2 · ANATOMIA E EIXO HORMONAL (B) =======================
FLX_EIXO = '''<div class="flx">
<div class="fb esc">Hipotálamo · GnRH pulsátil (sistema porta)</div><div class="fa">↓</div>
<div class="fb ou">Adeno-hipófise · FSH e LH</div><div class="fa">↓</div>
<div class="fr"><div class="fb"><b>Teca</b> (LH)<div class="fp">faz androgênios</div></div><div class="fb"><b>Granulosa</b> (FSH)<div class="fp">aromatase → estradiol · inibina</div></div></div>
<div class="fa">↓ estradiol alto e sustentado = feedback POSITIVO</div>
<div class="fb vi">Pico de LH → ovulação (~14º dia)</div><div class="fa">↓</div>
<div class="fb">Corpo lúteo · progesterona + estrogênio + inibina A</div><div class="fa">↓ sem gravidez</div>
<div class="fr"><div class="fb">Corpo albicante + menstruação</div><div class="fb ok">Com gravidez: <b>hCG</b> mantém o corpo lúteo</div></div>
<div class="fp" style="margin-top:3px">Estrogênio baixo: sobe FSH/LH · moderado: feedback negativo · inibina freia só o FSH</div></div>'''

render(N + 'SP 2.2 · Anatomia do sistema genital feminino e eixo hormonal - resumo em 1 folha', dict(layout='B',
 titulo='Genital Feminino e Eixo Hormonal', sub='Ovário, tubas e útero · ciclo menstrual · hormônios na gravidez · climatério',
 vars='--fs:8.4pt;--lh:1.52;--gap:3.6mm',
 corpo=f'''<div class="gB"><div>
{card('O eixo em uma linha', FLX_EIXO)}
{card('Ciclo ovariano × uterino', '''<table><tr><th>Ovário</th><th>Útero</th><th>Hormônio</th></tr>
<tr><td>Início da folicular</td><td>Menstruação (descama a funcional)</td><td>Queda de E e P</td></tr>
<tr><td>Folicular</td><td>Proliferativa</td><td>Estrogênio (folículo dominante)</td></tr>
<tr><td>Ovulação</td><td>Endométrio espesso</td><td>Pico de LH</td></tr>
<tr><td>Lútea</td><td>Secretora</td><td>Progesterona (corpo lúteo)</td></tr></table>''')}
{card('Gravidez e climatério', '''<ul><li><b>hCG</b> (sinciciotrofoblasto): pico 8–10 semanas; mantém o corpo lúteo até a placenta assumir a progesterona (8–10 semanas). Sangue detecta antes da urina; &gt; 5 mUI/mL</li>
<li><b>Estriol</b> predomina na gravidez · estrona na menopausa · estradiol na menacme · estetrol: fígado fetal</li>
<li><b>Climatério</b> = transição · <b>menopausa</b> = 12 meses sem menstruar (&gt; 45 anos). Na dúvida: 2 FSH com 4–6 semanas; &gt; 25 mUI/mL = transição</li>
<li>Menos folículos → ↓ inibina B → ↑ FSH → ↓ estradiol → sem pico de LH. Fogachos: <b>neurônios KNDy</b> (↑ neurocinina B)</li>
<li><b>TH:</b> 45–60 anos; com útero, estrogênio + progestagênio (endométrio)</li></ul>''')}
</div><div>
{card('Anatomia que cai', '''<ul><li><b>Ovário:</b> lig. <b>suspensor</b> leva a a. ovárica · lig. útero-ovárico liga ao útero · mesovário (do ligamento largo). Córtex com folículos; medula com vasos</li>
<li><b>Folículos:</b> primordial (pavimentoso) → primário (cúbico) → multilaminar → antral (Graaf) → corpo lúteo → albicante. ~2 milhões ao nascer, ~400 mil na puberdade; oócito parado no diplóteno até a puberdade</li>
<li><b>Tuba</b> (~10 cm): infundíbulo (fímbrias) → <b>ampola</b> (fecundação) → istmo → parte uterina</li>
<li><b>Útero:</b> fundo, corpo, istmo, colo · perimétrio, miométrio (3 camadas), endométrio (<b>basal</b> regenera, <b>funcional</b> descama) · ligamentos largo, uterossacros, transversos do colo, <b>redondos</b> (até os lábios maiores)</li>
<li>Puberdade: <b>telarca → pubarca → menarca</b> (2–3 anos após a telarca)</li></ul>''')}
{nc(['Climatério não é menopausa: a menopausa é o marco, definido depois de 12 meses.', 'Inibina freia o FSH, não o LH.', 'Estrogênio moderado freia o eixo; alto e sustentado dispara o pico de LH.', 'Teca faz androgênio; quem vira estradiol é a granulosa (aromatase).', 'Camada basal fica; a funcional é que descama.', 'Na menopausa os ovários param de responder: FSH alto, estrogênio baixo.'])}
{mn([('LH na Teca, FSH na Granulosa', 'duas células, dois hormônios: androgênio e depois estradiol.'), ('Amor na Ampola', 'a fecundação acontece na ampola da tuba.'), ('Inibina inibe', 'o FSH (o nome já entrega).'), ('Primeiro o peito, depois o pelo, por fim a menstruação', 'telarca, pubarca, menarca.'), ('esTRIol dos TRÊS trimestres', 'é o estrogênio da gravidez; estrOna, da menOpausa.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de anatomia do sistema genital feminino e eixo hormonal do 4º semestre (Moore; Junqueira; Tortora; Williams).'))

# ======================= SP 2.3 · PLACENTA E ALTERAÇÕES FISIOLÓGICAS (A) =======================
render(N + 'SP 2.3 · Placenta e alterações fisiológicas na gravidez - resumo em 1 folha', dict(layout='A',
 titulo='Placenta e Alterações da Gravidez', sub='Placenta, infecções do pré-natal, vacinas e adaptações maternas por sistema',
 vars='--fs:7.75pt;--lh:1.46;--gap:3mm',
 corpo=f'''<div class="gL"><div>
{sec('Placenta', '''<ul><li><b>Placa coriônica</b> (fetal: cório frondoso) × <b>placa basal</b> (materna: decídua basal), separadas pelo <b>espaço interviloso</b> com sangue materno. Cotilédones são as unidades funcionais; estrutura completa no 5º mês</li>
<li><b>Vilosidades:</b> primárias (cito + sinciciotrofoblasto) → secundárias (mesoderma) → terciárias (capilares)</li>
<li><b>Circulação:</b> artérias espiraladas → espaço interviloso → veias uterinas · feto: <b>2 artérias umbilicais</b> (sangue pobre em O₂) e <b>1 veia</b> (oxigenado). Barreira afina a partir do 4º mês</li>
<li><b>Transporte:</b> difusão simples (O₂, CO₂) · facilitada (<b>glicose</b>) · ativo (aminoácidos, Ca, Fe) · pinocitose (<b>IgG</b>: imunidade passiva)</li>
<li><b>Acretismo:</b> acreta adere · increta invade o miométrio · percreta ultrapassa a parede. <b>Prévia</b> sobre o orifício interno: baixa, marginal, parcial, completa (risco: prévia em gestação anterior, &gt; 35 anos, multiparidade, tabagismo, obesidade, endometriose)</li></ul>''')}
{sec('Infecções do pré-natal', '''<ul><li><b>Toxoplasmose:</b> IgG+ IgM− = imune · IgG− IgM− = suscetível (sorologia até o fim) · infecção recente: IgM/IgA, IgG subindo ou <b>avidez baixa</b> → tratar e avaliar o feto (US, PCR no líquido)</li>
<li><b>Sífilis:</b> não treponêmico (VDRL, RPR) faz triagem e segue o tratamento pela titulação; treponêmico (FTA-ABS) confirma e fica positivo para sempre. <b>Pró-zona</b>: excesso de anticorpo → falso-negativo. Trata com penicilina</li>
<li><b>Hepatite B:</b> HBsAg no início (repete no 3º tri se risco) · HBeAg = replicação, mais transmissão · aguda: HBsAg + anti-HBc IgM · vacinada: só anti-HBs · RN: vacina + HBIg</li>
<li><b>HIV:</b> ELISA para anticorpos; p24 aparece cedo</li>
<li>Rh−: Coombs indireto se pai Rh+; RN Rh+ → imunoglobulina anti-D</li></ul>''')}
{sec('Adaptações maternas', '''<table><tr><th>Sistema</th><th>O que muda</th></tr>
<tr><td>Sangue</td><td>Volume +40–45%; Hb cai por diluição (anemia se &lt; 11); ferro +1.000 mg; leucócitos até 30 mil no parto; fibrinogênio 300–600: <b>hipercoagulável</b></td></tr>
<tr><td>Coração</td><td>DC +30–50% (pico ~32 sem); PA mínima em 20–26 sem; supina comprime a cava → <b>decúbito lateral esquerdo</b>; sopro sistólico em até 90%</td></tr>
<tr><td>Pulmão</td><td>Diafragma sobe 4 cm; CRF −20–30%; ↑ volume corrente e ventilação (progesterona) → <b>alcalose respiratória compensada</b>; FR igual</td></tr>
<tr><td>Rim</td><td>TFG +50%; creatinina 0,5 mg/dL; glicosúria pode ser fisiológica; proteinúria anormal &gt; 300 mg/dia</td></tr>
<tr><td>TGI e fígado</td><td>Pirose, constipação, hemorroidas; apêndice sobe; FA alta (placentária); vesícula lenta (cálculo); colestase</td></tr>
<tr><td>Endócrino</td><td>Hipófise +135% (lactotrofos); prolactina até 10×; TBG ↑; GH placentário; hPL → resistência à insulina</td></tr>
<tr><td>Metabolismo</td><td>Ganho médio 12,5 kg; +300 kcal/dia; anabólico no início, lipólise no 3º tri</td></tr></table>''')}
{box('Vacinas', '<p><b>dTpa</b> a partir de 20 semanas em toda gestação (completa dT se preciso) · hepatite B (3 doses se não vacinada) · influenza em qualquer fase · COVID-19</p>')}
</div><div>
{nc(['Prévia é onde a placenta está; acreta é o quanto ela invade.', 'Hb baixa na gestação é diluição; anemia só abaixo de 11.', 'Treponêmico positivo não mede atividade: siga o VDRL.', 'VDRL negativo com sífilis florida: pense em pró-zona.', 'Anti-HBs sozinho = vacina; anti-HBc + anti-HBs = infecção curada.', 'Glicosúria na gravidez não fecha diabetes.', 'Sopro sistólico é comum na gestação.'])}
{mn([('Acreta Adere, Increta Invade, Percreta Passa', 'do mais raso ao mais fundo.'), ('Duas levam, uma traz', '2 artérias umbilicais saem do feto; 1 veia traz o sangue oxigenado.'), ('Avidez baixa, infecção novinha', 'IgG de baixa avidez = toxoplasmose recente.'), ('Treponêmico é tatuagem, VDRL é termômetro', 'um fica para sempre; o outro acompanha a cura.'), ('HBeAg: e de espalha', 'replicação alta, mais transmissão vertical.'), ('Grávida deita para a esquerda', 'tira o útero de cima da cava.')])}
{box('Sinais da gravidez', '<p><b>Hunter</b>: aréola secundária · <b>Haller</b>: rede venosa na mama · <b>Montgomery</b>: glândulas na aréola · <b>Halban</b>: lanugem · <b>Osiander</b>: pulso arterial aumentado no toque</p>')}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de placenta e alterações fisiológicas na gravidez do 4º semestre (Williams; FEBRASGO; Moore; Ministério da Saúde).'))

# ======================= SP 2.4 · DIABETES, HIPERTENSÃO, ECLÂMPSIA E HELLP (C) =======================
render(N + 'SP 2.4 · Diabetes, hipertensão, eclâmpsia e HELLP na gestação - resumo em 1 folha', dict(layout='C',
 titulo='Diabetes e Hipertensão na Gestação', sub='DMG, síndromes hipertensivas, pré-eclâmpsia, eclâmpsia e HELLP',
 vars='--fs:8.4pt;--lh:1.52;--gap:4mm',
 corpo=f'''<div class="sec">{cards([('Jejum (1ª consulta)', '92–125', 'mg/dL = DMG em qualquer fase'), ('TOTG 75 g', '24–28 sem', 'para todas sem diagnóstico'), ('Pontos do TOTG', '92 · 180 · 153', 'jejum · 1 h · 2 h: basta um'), ('Overt diabetes', '≥ 126 · ≥ 200', 'jejum · 2 h: é DM, não DMG')])}</div>
<div class="g2"><div>
{sec('Por que a gestante fica resistente à insulina', '''<ul><li><b>Fase anabólica</b> (até 24–26 sem; estrogênio e progesterona): guarda gordura, glicemia basal cai</li>
<li><b>Fase catabólica</b> (a partir de 26–30 sem; GH, cortisol, <b>hPL</b>): resistência à insulina e lipólise para o feto</li>
<li>Se o pâncreas não compensa → <b>DMG</b>. Disglicemia: tratar logo</li></ul>''')}
{sec('As quatro síndromes hipertensivas', '''<table><tr><th>Quadro</th><th>Como reconhecer</th></tr>
<tr><td>HAS crônica</td><td>Antes da gestação ou antes de 20 sem</td></tr>
<tr><td>Gestacional</td><td>≥ 140/90 após 20 sem, sem proteinúria nem lesão de órgão</td></tr>
<tr><td>Pré-eclâmpsia</td><td>Após 20 sem + proteinúria <b>ou</b> lesão de órgão-alvo</td></tr>
<tr><td>Superposta</td><td>Crônica que ganha proteinúria ou lesão de órgão</td></tr></table>''')}
{sec('Pré-eclâmpsia sem proteinúria', '<ul><li>Plaquetas &lt; 100.000 · TGO/TGP &gt; 70 · creatinina ≥ 1,2</li><li>Edema agudo de pulmão · cefaleia, escotomas, epigastralgia</li><li>Base: placentação ruim (artérias espiraladas sem remodelar) → lesão endotelial e fatores antiangiogênicos</li></ul>')}
</div><div>
{sec('Risco e conduta', '''<table><tr><th></th><th>Baixo</th><th>Moderado</th><th>Alto</th></tr>
<tr><td>PAD</td><td>&lt; 100</td><td>100–110</td><td>≥ 110</td></tr>
<tr><td>Início</td><td>≥ 34 sem</td><td>&lt; 34 sem</td><td>&lt; 34 sem</td></tr>
<tr><td>Feto</td><td>Normal</td><td>Normal</td><td>RCIU/oligo</td></tr>
<tr><td>Conduta</td><td>Consulta semanal, PBF quinzenal</td><td>2×/semana, Doppler + PBF</td><td><b>Internar</b>, Doppler + PBF diários</td></tr></table>''')}
{sec('Tratamento e HELLP', '''<ul><li><b>Anti-hipertensivo</b> controla a PA; <b>sulfato de magnésio</b> previne e trata a convulsão (eclâmpsia)</li>
<li>A cura da pré-eclâmpsia é o <b>parto</b> · vitalidade: US com PBF + Doppler (umbilical, cerebral média, ducto venoso)</li>
<li><b>HELLP</b>: Hemólise + enzimas hepáticas altas + plaquetas baixas; 3º tri, dor abdominal, náusea, cefaleia</li></ul>''')}
{box('Prevenção da pré-eclâmpsia', '<p><b>Primária:</b> não existe (o gatilho não é conhecido) · <b>secundária:</b> rastrear e intervir cedo · <b>terciária:</b> reduzir complicações da doença instalada</p>')}
</div></div>
<div class="g2"><div>{nc(['Hipertensão antes de 20 semanas é crônica, não gestacional.', 'Pré-eclâmpsia não exige proteinúria se houver lesão de órgão.', 'TOTG ≥ 200 em 2 h não é DMG: é diabetes diagnosticado na gestação.', 'TOTG em 24–28 semanas para todas, com ou sem fator de risco.', 'Magnésio não baixa a pressão: protege o cérebro.'])}</div>
<div>{mn([('92, 180, 153: basta um', 'jejum, 1 h e 2 h do TOTG 75 g.'), ('Antes de 20 é velha, depois de 20 é da gravidez', 'crônica × gestacional.'), ('Magnésio é para a convulsão, remédio é para a pressão', 'MgSO₄ × anti-hipertensivo.'), ('HELLP quebra, inflama e sangra', 'hemólise, fígado, plaquetas.'), ('Pré-eclâmpsia só sai com a placenta', 'a cura é o parto.')])}</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de diabetes, hipertensão, eclâmpsia e HELLP na gestação do 4º semestre (SBD 2020; Zugaib; Williams; FEBRASGO).'))

# ======================= SP 2.4 · PARTOGRAMA, PELVE E PERÍNEO (B) =======================
PARTO_SVG = '''<svg viewBox="0 0 230 128" width="100%" aria-hidden="true" font-family="Inter">
<g stroke="#ece3d6" stroke-width=".6">''' + ''.join(f'<line x1="24" y1="{10+i*10}" x2="222" y2="{10+i*10}"/>' for i in range(11)) + ''.join(f'<line x1="{24+j*18}" y1="10" x2="{24+j*18}" y2="110"/>' for j in range(12)) + '''</g>
''' + ''.join(f'<text x="18" y="{113-i*10}" font-size="6" text-anchor="end" fill="#76696b">{i}</text>' for i in range(0, 11, 2)) + '''
<text x="2" y="5" font-size="5.5" fill="#76696b">cm</text><text x="222" y="122" font-size="6" text-anchor="end" fill="#76696b">horas</text>
<line x1="24" y1="70" x2="132" y2="10" stroke="#a8771c" stroke-width="1.6"/><text x="70" y="36" font-size="7" fill="#8a5f12" font-weight="600" transform="rotate(-29 70 36)">alerta</text>
<line x1="96" y1="70" x2="204" y2="10" stroke="#921827" stroke-width="1.6"/><text x="150" y="36" font-size="7" fill="#921827" font-weight="600" transform="rotate(-29 150 36)">ação</text>
<path d="M24 70 l18-10 l18-12 l18-10" stroke="#2b2224" stroke-width="1" fill="none" stroke-dasharray="2 2"/>
<path d="M24 70 l-3 5 h6z M42 60 l-3 5 h6z M60 48 l-3 5 h6z M78 38 l-3 5 h6z" fill="#2b2224"/>
<line x1="24" y1="117" x2="96" y2="117" stroke="#921827" stroke-width=".8"/><text x="60" y="126" font-size="6" text-anchor="middle" fill="#921827">4 h</text></svg>'''


render(N + 'SP 2.4 · Partograma, pelve e períneo - resumo em 1 folha', dict(layout='B', titulo='Partograma, Pelve e Períneo',
 sub='Pelve, estática fetal, mecanismo e períodos do parto, partograma e cesárea', vars='--fs:7.9pt;--lh:1.46;--gap:3mm',
 corpo=f'''<div class="gB"><div>
{card('Partograma', f'''{PARTO_SVG}<ul style="margin-top:1.5mm"><li>Começa na <b>fase ativa</b>: ≥ 4 cm + 2–3 contrações em 10 min</li>
<li><b>Triângulo</b> = dilatação · <b>círculo</b> = altura da apresentação (com a variedade de posição)</li>
<li>Passou da <b>alerta</b>: atenção · cruzou a <b>ação</b> (4 h à direita): avaliar intervenção</li>
<li>Registra contrações (quadrados sombreados), FCF e sinais vitais maternos</li>
<li><b>De Lee:</b> −5 a +5; <b>0 = espinhas isquiáticas</b>; +5 = nascendo</li>
<li>Disfunções: fase prolongada, <b>parada secundária</b> (progredia e parou), parto rápido</li></ul>''')}
{card('Os quatro períodos', '''<table><tr><th>Período</th><th>Chave</th></tr>
<tr><td>1º Dilatação</td><td>Latente até 3–5 cm; ativa até 9 cm. Prolongado &gt; 20 h (primípara) ou &gt; 14 h (multípara)</td></tr>
<tr><td>2º Expulsão</td><td>Pélvica (acima de +3) e perineal. Prolongado: nulípara &gt; 3 h com analgesia / &gt; 2 h sem; multípara &gt; 2 h / &gt; 1 h</td></tr>
<tr><td>3º Dequitação</td><td>5–30 min; &gt; 30 min = prolongado</td></tr>
<tr><td>4º Greenberg</td><td>1ª hora pós-parto; risco de <b>atonia</b></td></tr></table>''')}
</div><div>
{card('Pelve e períneo', '''<ul><li>Pelve maior × menor (abertura superior). Menor distância fixa: <b>conjugata obstétrica</b> (promontório → face posterior da sínfise)</li>
<li><b>Ginecoide</b> (mais comum, ideal) · androide (coração) · antropoide (oval) · platipoide (transversa larga, rara)</li>
<li><b>Levantador do ânus:</b> puborretal, pubococcígeo, iliococcígeo · <b>pudendo</b> S2–S4, contorna a espinha isquiática</li></ul>''')}
{card('Estática fetal e nomenclatura', '''<ul><li><b>Situação</b>: longitudinal (99,5%), transversa (→ córmica), oblíqua · <b>apresentação</b> definida a partir do 6º mês</li>
<li>Cefálica fletida (occipício) · defletida 1º grau bregma · 2º fronte · 3º face (mento) · pélvica completa, nádegas, joelhos, pés</li>
<li><b>Sigla</b>: ponto de referência (O, B, N, M, S, A) + lado (D/E) + variedade (A, T, P). Ex.: <b>OEA</b></li></ul>''')}
{card('Mecanismo de parto (cefálica fletida)', '<p><b>1</b> Insinuação (passa o estreito superior: orientação + flexão) → <b>2</b> descida (sinclítica ou assinclítica) → <b>3</b> rotação interna (occipício para a sínfise) → <b>4</b> desprendimento da cabeça (deflexão sob o púbis) → <b>5</b> rotação externa (biacromial gira 45°) → <b>6</b> desprendimento das espáduas (anterior, depois posterior)</p>')}
{card('Cesárea (indicações do resumo)', '<p>Córmica e pélvica · placenta prévia total e acretismo · DPP (se não for mais rápido por baixo) · CTG categoria III ou Doppler com diástole zero/reversa · prolapso de cordão e vasa prévia · HIV com carga &gt; 1.000 após 34 sem · herpes ativo · macrossomia &gt; 5.000 g (&gt; 4.500 com diabetes) · gemelar com 1º não cefálico</p>')}
</div></div>
<div class="gB"><div>{nc(['De Lee: quanto mais positivo, mais baixo (perto da saída) está o bebê.', 'Partograma não começa na fase latente.', 'Linha de alerta não é intervenção; a de ação é.', 'Insinuação é passar o estreito superior, não chegar ao períneo.', 'Quem segura o útero quieto na gravidez é a progesterona.'])}</div>
<div>{mn([('Triângulo dilata, círculo desce', 'símbolos do partograma.'), ('Zero na espinha, mais é mais perto', 'planos de De Lee.'), ('Alerta avisa, ação age: 4 horas depois', 'linhas do partograma.'), ('Entra, desce, gira, sai, gira, ombros', 'os 6 tempos do mecanismo de parto.'), ('S2, S3, S4 seguram o assoalho', 'raízes do nervo pudendo.')])}</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de partograma, pelve e períneo do 4º semestre (Williams; FEBRASGO; Moore; Netter).'))
