# Folhas únicas do 6º semestre (D1 HMEC, D1 NCS, D3 NCS) no estilo 2 (layouts A/B/C + Não confunda + mnemônicos)
# Conteúdo SÓ dos resumos publicados (PDFs do Drive). Pedido da Laura (22/10/2026).
import sys, os
os.environ.setdefault('PASTA', 'v2-g3')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from folha2 import render, ul, nc, mn, sec, card, box, cards, passos

S1 = '6º sem D1 · NCS · '

# ======================= HMEC · ENTREVISTA, EEM E IDOSO (A) =======================
render('6º sem D1 · HMEC · Entrevista psiquiátrica, exame do estado mental e avaliação do idoso - resumo em 1 folha', dict(
 layout='A', titulo='Entrevista Psiquiátrica, Exame do Estado Mental e Avaliação do Idoso',
 sub='Vínculo, exame psíquico, escalas de rastreio, risco de suicídio e avaliação multidimensional', vars='--fs:7.55pt;--lh:1.44;--gap:2.5mm;--h1:18pt',
 corpo=f'''<div class="gL"><div>
{sec('A entrevista', '''<ul><li>Só funciona com <b>rapport</b> (vínculo de confiança); a primeira impressão é decisiva</li>
<li><b>Perguntas abertas</b> ("Em que posso ajudá-lo?"), escutar mais que falar, silêncios terapêuticos; evitar perguntas indutivas</li>
<li><b>Transferência:</b> o paciente projeta no médico figuras da infância · <b>contratransferência:</b> o médico projeta seus conflitos no paciente</li>
<li>Evitar: frieza, calor artificial, julgamentos, revidar hostilidade (responder em voz mais baixa), anotar demais</li>
<li>Roteiro (Porto): identificação → queixa nas palavras do paciente → HDA (início, curso, precipitantes, impacto) → antecedentes → hábitos → família → acompanhante (ouvir o paciente primeiro) → exame psíquico</li></ul>''')}
{sec('Escalas que caem', '''<table><tr><th>Escala</th><th>Para quê</th><th>Corte</th></tr>
<tr><td>CAGE</td><td>Álcool, 4 perguntas</td><td>≥ 2 = suspeita</td></tr>
<tr><td>AUDIT</td><td>Álcool (OMS), 10 itens, 0–40</td><td>≥ 8 uso problemático · ≥ 15 dependência</td></tr>
<tr><td>ASSIST</td><td>Várias substâncias (OMS)</td><td>baixo 0–3 (álcool 0–10) · moderado 4–26 · alto ≥ 27</td></tr>
<tr><td>Fagerström</td><td>Nicotina, 0–10</td><td>6–7 elevada · 8–10 muito elevada</td></tr>
<tr><td>PHQ-2</td><td>Triagem de depressão</td><td>≥ 3 → aplicar PHQ-9</td></tr>
<tr><td>PHQ-9</td><td>Depressão, 0–27</td><td>5 leve · 10 moderada · 15 mod. grave · 20 grave</td></tr>
<tr><td>GDS-15</td><td>Depressão no idoso, sim/não</td><td>0–5 normal · 6–10 sugestivo · 11–15 provável</td></tr>
<tr><td>GAD-7</td><td>Ansiedade, 0–21</td><td>5 leve · 10 moderada · 15 grave</td></tr></table>''')}
{sec('Risco de suicídio', '''<ul><li><b>IRIS</b> (12 itens): &lt; 5 reduzido · 5–9 intermédio · <b>≥ 10 elevado</b></li>
<li><b>Contextos</b> (peso 2): doença psiquiátrica grave, álcool/drogas, isolamento, doença física grave, perda recente, internação psiquiátrica prévia, suicídio na família</li>
<li><b>Plano suicida estruturado</b> (método, preparativos, acesso a meios) = <span class="k">valor máximo (20)</span> sozinho · tentativas: ≥ 2 ou 1 grave</li>
<li><b>SAD PERSONS</b> (precursor): 1 ponto por item; falha ao pontuar mais o homem solteiro de 50 anos que a mulher deprimida com plano</li></ul>''')}
{sec('Idoso: capacidade intrínseca e funcional', '''<ul><li><b>Capacidade intrínseca</b> (OMS 2015) em 5 domínios: <b>locomoção, vitalidade, cognição, psicológico, sensorial</b>; ela precede e determina a capacidade funcional</li>
<li><b>ABVD</b> (autocuidado: banho, vestir, higiene, transferência, continência, comer) → <b>Katz</b>, Barthel · <b>AIVD</b> (telefone, compras, refeições, dinheiro, remédios, transporte) → <b>Lawton</b>, Pfeffer · <b>AAVD</b>: dirigir, esportes, voluntariado</li>
<li>Perder AIVD <b>vem antes</b> de perder ABVD e diferencia quem já tem demência</li>
<li>Outros: MEEM, MoCA, relógio, <b>CAM</b> (delirium), TUG, Tinetti, CFS, MNA, PAINAD</li></ul>''')}
{sec('Sarcopenia (EWGSOP2) e fragilidade (Fried)', '''<table><tr><th>Teste</th><th>Alterado se</th></tr>
<tr><td>Preensão palmar</td><td>&lt; 27 kg homem · &lt; 16 kg mulher</td></tr>
<tr><td>Sentar e levantar 5×</td><td>&gt; 15 s</td></tr>
<tr><td>Velocidade de marcha (4 m)</td><td>≤ 0,8 m/s</td></tr>
<tr><td>Panturrilha</td><td>&lt; 31 cm (triagem de massa)</td></tr>
<tr><td>SPPB (0–12)</td><td>≤ 8 baixo desempenho</td></tr></table>
<p style="margin-top:2px">Força baixa = <b>provável</b> · + massa baixa (DXA, BIA, TC, RM) = <b>confirmada</b> · + desempenho baixo = <b>grave</b>.<br><b>Fried (5):</b> perda ≥ 4,5 kg ou ≥ 5%/ano, exaustão, preensão baixa, marcha lenta, pouca atividade física. 1–2 = pré-frágil · <b>≥ 3 = frágil</b>.</p>''')}
</div><div>
{box('Exame psíquico: ARCA PAVIS', '''<p><b>A</b>valiação geral · <b>R</b>elação com o entrevistador · <b>C</b>onsciência · <b>A</b>tenção (subtração seriada) · <b>P</b>ensamento: forma e conteúdo (delírios, obsessões) · <b>A</b>fetividade e humor · <b>V</b>ontade · <b>I</b>nteligência, memória, juízo e insight · <b>S</b>ensopercepção (alucinações, ilusões)</p>''')}
{nc(['Delírio é alteração do pensamento (conteúdo); alucinação é da sensopercepção.', 'Plano estruturado já fecha risco elevado, mesmo sem outros itens.', 'Katz normal com Lawton alterado: dependência em AIVD, não em ABVD.', 'Marcha e SPPB não diagnosticam sarcopenia: graduam a gravidade.', 'Panturrilha só faz triagem de massa; não confirma.'])}
{mn([('CAGE com 2 sins, a gaiola fecha', 'Cut, Annoyed, Guilty, Eye-opener.'), ('Katz cuida do corpo, Lawton cuida da vida', 'básicas × instrumentais.'), ('Primeiro larga o banco, depois o banho', 'AIVD cai antes da ABVD.'), ('Força, Massa, Marcha', 'provável, confirmada, grave: cada achado sobe um degrau.'), ('Fried frita com 3', '≥ 3 critérios = frágil.')])}
{box('Números que caem', '<p>CAGE ≥ 2 · AUDIT ≥ 8 · IRIS ≥ 10<br>GDS-15 ≥ 11 · PHQ-9 ≥ 20 grave<br>preensão 27/16 kg · marcha 0,8 m/s<br>panturrilha 31 cm · SPPB ≤ 8</p>')}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de entrevista psiquiátrica, exame do estado mental e avaliação do idoso do 6º semestre (Porto; Dalgalarrondo; Botega; IRIS; EWGSOP2; Fried).'))

# ======================= NEUROANATOMIA (C) =======================
CEREBRO = '''<svg viewBox="0 0 160 122" width="100%" aria-hidden="true" font-family="Inter">
<path d="M18 62 C16 34 44 10 84 10 C122 10 152 32 150 62 C149 74 142 80 132 80 C122 80 114 82 108 88 C100 98 76 100 60 94 C46 90 34 86 26 80 C21 75 18 70 18 62Z" fill="#f8f0de" stroke="#c9a96a" stroke-width="2"/>
<ellipse cx="128" cy="92" rx="20" ry="11" fill="#f7e8ea" stroke="#dcc6c9" stroke-width="1.5"/>
<path d="M104 88 L106 116 L114 116 L114 90" fill="#f7e8ea" stroke="#dcc6c9" stroke-width="1.5"/>
<path d="M84 12 C80 27 78 41 72 59" stroke="#921827" stroke-width="5" opacity=".28" fill="none"/>
<path d="M97 12 C93 27 91 41 86 59" stroke="#c9a96a" stroke-width="5" opacity=".55" fill="none"/>
<path d="M90 11 C86 26 84 40 79 59" stroke="#8a5f12" stroke-width="1.4" fill="none"/>
<path d="M36 72 C56 66 84 62 106 64" stroke="#8a5f12" stroke-width="1.4" fill="none"/>
<path d="M134 18 C136 34 138 46 136 62" stroke="#8a5f12" stroke-width="1.1" stroke-dasharray="3 2" fill="none"/>
<circle cx="44" cy="64" r="3.2" fill="#921827"/><circle cx="104" cy="70" r="3.2" fill="#921827"/>
<text x="34" y="42" font-size="8" fill="#8a5f12" font-weight="600">Frontal</text>
<text x="104" y="36" font-size="8" fill="#8a5f12" font-weight="600">Parietal</text>
<text x="128" y="72" font-size="7" fill="#8a5f12" font-weight="600">Occ.</text>
<text x="60" y="84" font-size="8" fill="#8a5f12" font-weight="600">Temporal</text>
<text x="118" y="96" font-size="6.5" fill="#76696b">cerebelo</text>
<text x="80" y="114" font-size="6.5" fill="#76696b">tronco</text>
<text x="36" y="58" font-size="6" fill="#921827">Broca</text>
<text x="96" y="78" font-size="6" fill="#921827">Wernicke</text>
<text x="60" y="8" font-size="6" fill="#76696b">sulco central</text>
<text x="2" y="80" font-size="6" fill="#76696b">sulco lateral</text></svg>'''

render(S1 + 'SP 1.1 · Neuroanatomia - resumo em 1 folha', dict(layout='C', titulo='Neuroanatomia',
 sub='Divisões do encéfalo, lobos, giros que caem, comissuras, núcleos da base, límbico e diencéfalo', vars='--fs:8.1pt;--lh:1.52;--gap:3.6mm',
 corpo=f'''<div class="vis sec" style="--vw:58mm"><div>{CEREBRO}<p class="m" style="font-size:.85em;text-align:center">vinho: giro pré-central (motor) · dourado: pós-central (sensitivo)</p></div><div>
{cards([('SNC', 'encéfalo + medula', 'SNP: nervos somáticos, autônomos e entéricos'), ('Encéfalo', '4 partes', 'telencéfalo, diencéfalo, cerebelo e tronco (mesencéfalo, ponte, bulbo)'), ('Líquor', '4 ventrículos', 'feito no plexo corioide; circula no espaço subaracnóideo')])}
<p class="m" style="margin-top:2.5mm">Meninges de fora para dentro: <b>dura-máter, aracnoide, pia-máter</b>. Giros são as dobras; sulcos, as fendas: central (de <b>Rolando</b>), lateral (de <b>Sylvius</b>), parieto-occipital, calcarino, do cíngulo.</p></div></div>
<div class="sec"><h2>Os lobos</h2>{passos([('Frontal', 'até o sulco central: motor voluntário (pré-central), planejamento, julgamento, comportamento social; <span class="k">Broca</span> (fala) no dominante'), ('Parietal', 'pós-central = somatossensorial primário (<span class="k">3, 1, 2</span>); <span class="k">angular</span>: leitura, escrita, cálculo; supramarginal: fonologia, gestos'), ('Temporal', 'abaixo do sulco lateral: <span class="k">Heschl</span> = auditivo primário (do geniculado medial); <span class="k">Wernicke</span> = compreensão; memória; fusiforme: faces'), ('Occipital', 'visual primário no <span class="k">calcarino</span>; <span class="k">cúneo</span> (acima) vê a metade inferior do campo contralateral'), ('Ínsula', 'escondida pelos opérculos: paladar, víscera, dor, emoção, empatia')])}</div>
<div class="g2"><div>
{sec('Comissuras e núcleos da base', '''<ul><li><b>Corpo caloso</b> (a maior comissura): rostro e joelho = pré-frontal · tronco = parietal/temporal · <b>esplênio</b> = occipital (visão bilateral)</li>
<li><b>Comissura anterior:</b> temporais anteriores e amígdalas</li>
<li><b>Estriado</b> = caudado + putâmen · <b>lentiforme</b> = putâmen + globo pálido · <b>estriado ventral</b> (accumbens) = recompensa</li>
<li>Ventrículo lateral: cornos frontal, occipital e temporal (até o hipocampo); <b>forame interventricular</b> leva ao 3º; <b>septo pelúcido</b> separa os dois laterais</li></ul>''')}
{sec('Límbico, diencéfalo e tronco', '''<ul><li><b>Cíngulo</b> (emoção, motivação), <b>parahipocampal</b> (memória, navegação), giro dentado (neurogênese); <b>fímbria → fórnice</b> leva a informação do hipocampo</li>
<li><b>Tálamo:</b> retransmite sensibilidade (exceto olfato) e motricidade ao córtex · <b>hipotálamo:</b> temperatura, fome, sede, sono, endócrino · <b>epitálamo:</b> pineal, melatonina · <b>subtálamo:</b> modula movimento</li>
<li><b>Tronco:</b> FC, respiração, PA, tosse, deglutição; maioria dos núcleos dos nervos cranianos</li></ul>''')}
</div><div>
{nc(['Estriado é caudado + putâmen; o globo pálido entra no lentiforme, não no estriado verdadeiro.', 'Heschl ouve; Wernicke entende.', 'Cúneo fica acima do calcarino e vê o campo inferior.', 'O olfato não passa pelo tálamo.'])}
{mn([('Lentiforme é PP', '<b>P</b>utâmen + <b>P</b>álido.'), ('Broca bota para fora, Wernicke entende', 'frontal produz, temporal compreende.'), ('Cunha de cima, campo de baixo', 'cúneo vê o campo visual inferior.'), ('Esplênio enxerga', 'liga os lobos occipitais.'), ('Tálamo é a recepção: todo mundo passa, menos o cheiro', '')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de neuroanatomia do 6º semestre (Snell; Netter; Sobotta).'))

# ======================= TRANSTORNOS DEPRESSIVOS (A) =======================
render(S1 + 'SP 1.1 · Transtornos depressivos - resumo em 1 folha', dict(layout='A', titulo='Transtornos Depressivos',
 sub='Neurotransmissores, diagnóstico (DSM-5), subtipos, fisiopatologia e antidepressivos', vars='--fs:7.85pt;--lh:1.5;--gap:3.1mm',
 corpo=f'''<div class="gL"><div>
{sec('Transtorno depressivo maior (DSM-5)', '''<p><b>≥ 5 de 9 sintomas</b>, quase todos os dias, por <b>≥ 2 semanas</b>, sendo um deles <span class="k">humor deprimido</span> ou <span class="k">anedonia</span>: peso/apetite (± 5% em 1 mês), insônia ou hipersonia, agitação ou retardo, fadiga, culpa ou inutilidade, concentração, pensamentos de morte. Com prejuízo e <b>sem mania/hipomania</b> prévia.</p>
<ul><li>Mulheres 1,5–3×; pico de incidência na década dos 20; Brasil ~7%</li><li>Recorre mais: início precoce, vários episódios, sintomas residuais. Psicose, adolescência e história familiar → pode virar bipolar</li>
<li><b>Distimia</b> (persistente): ≥ <b>2 anos</b> (1 em jovens), ≥ 2 sintomas, sem melhora &gt; 2 meses; "sempre fui assim"</li>
<li>Diferenciais: bipolar (mania prévia), hipotireoidismo, substâncias, TDAH (crônico desde a infância), transtorno de adaptação e tristeza normal (proporcionais ao estressor)</li></ul>''')}
{sec('Subtipos', '''<table><tr><th>Tipo</th><th>Chave</th></tr>
<tr><td>Melancólica</td><td>Piora matinal, despertar precoce, perde peso, culpa, pouca reatividade</td></tr>
<tr><td>Atípica</td><td>Come mais, dorme mais, corpo pesado, sensível à rejeição, reage a coisas boas</td></tr>
<tr><td>Sazonal</td><td>Outono/inverno, remite na primavera por ≥ 2 anos; carboidrato, sono, peso</td></tr>
<tr><td>Psicótica</td><td>Delírios de culpa, ruína, doença; alucinações auditivas; grave</td></tr>
<tr><td>Bipolar</td><td>Início precoce, história familiar, não responde a antidepressivo</td></tr></table>''')}
{sec('Fisiopatologia', '''<ul><li><b>Monoaminas:</b> ↓ 5-HT (impulsividade suicida), ↓ NE (energia), ↓ <b>DA → anedonia</b>; ACh em excesso (lentidão), ↓ GABA, glutamato em excesso (neurotoxicidade no hipocampo)</li>
<li><b>Neurotrófica:</b> estresse crônico ↓ <b>BDNF</b> → atrofia do hipocampo</li>
<li><b>Eixo HHS hiperativo:</b> ↑ CRH e cortisol, <b>dexametasona não suprime</b></li>
<li><b>Sono:</b> latência REM ↓, densidade REM ↑, sono profundo ↓ (persiste após remissão)</li>
<li>Imagem: hipofrontalidade esquerda, cingulado anterior ↓, <b>amígdala hiper-responsiva</b></li>
<li><b>Beck:</b> tríade negativa (eu, mundo, futuro) · <b>Seligman:</b> impotência aprendida</li></ul>''')}
{sec('Antidepressivos', '''<table><tr><th>Classe</th><th>Exemplos e o que cai</th></tr>
<tr><td>ISRS</td><td><b>1ª escolha</b> (fluoxetina, sertralina, escitalopram); náusea, disfunção sexual, hiponatremia, síndrome serotoninérgica</td></tr>
<tr><td>IRSN</td><td>Venlafaxina, duloxetina; também dor crônica; HAS dose-dependente</td></tr>
<tr><td>Tricíclicos</td><td>Amitriptilina; anticolinérgico, hipotensão, <b>arritmia e morte na overdose</b> (bicarbonato IV)</td></tr>
<tr><td>IMAO</td><td>Tranilcipromina; <b>tiramina</b> (queijo, vinho) → crise hipertensiva</td></tr>
<tr><td>Outros</td><td>Bupropiona (sem disfunção sexual; convulsão), mirtazapina (sono, apetite), trazodona (priapismo)</td></tr></table>
<p style="margin-top:2px">Efeito pleno em <b>2–4 semanas</b>: o autorreceptor 5-HT1A precisa dessensibilizar. Fluoxetina: norfluoxetina de meia-vida longa, inibe CYP2D6. Não farmacológico: psicoterapia, exercício, <b>ECT</b> (o mais eficaz: grave, psicótica, catatônica, resistente), EMTr.</p>''')}
{sec('Quando encaminhar já', '<p>Ideação com <b>plano</b> ou tentativa recente, agressão, psicose, recusa alimentar grave, catatonia → emergência. PHQ-9 ≥ 9 sugere depressão na APS; casos graves → CAPS/RAPS.</p>')}
</div><div>
{box('Neurotransmissores', '''<p><b>Ionotrópicos</b> (rápidos): nicotínico, NMDA/AMPA/cainato, GABA-A, 5-HT3.<br><b>Metabotrópicos</b> (proteína G): muscarínicos, adrenérgicos, dopaminérgicos (D1/D5 ↑ AMPc; D2–D4 ↓), 5-HT (exceto 5-HT3), GABA-B.<br>Tirosina → L-DOPA (<b>tirosina-hidroxilase</b>, passo limitante) → DA → NE (<b>β-hidroxilase</b>, dentro da vesícula) → adrenalina.<br>5-HT: rafe · NE: locus coeruleus · glutamato excita · GABA inibe.</p>''')}
{nc(['Mania ou hipomania no passado tira o diagnóstico de depressão maior.', 'Na melancólica o dia começa pior; na atípica o apetite e o sono aumentam.', 'Tricíclico é o mais perigoso em superdose.', 'Na depressão a latência REM cai.', 'Dexametasona não suprime o cortisol na depressão.'])}
{mn([('INCA rápido, MAD 5G lento', 'nicotínico, canais de glutamato, GABA-A, 5-HT3 × muscarínico, adrenérgico, dopaminérgico, 5-HT, GABA-B.'), ('Sem dopamina, sem graça', 'anedonia.'), ('Beck vê tudo cinza: eu, mundo e futuro', ''), ('Queijo com IMAO, pressão no teto', 'tiramina.'), ('O freio precisa cansar', '5-HT1A dessensibiliza em 2–4 semanas.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de transtornos depressivos do 6º semestre (DSM-5; Kandel; Sadock; Katzung; Tratado da ABP).'))

# ======================= TRANSTORNOS DE ANSIEDADE (B) =======================
FLX_MEDO = '''<div class="flx">
<div class="fb esc">Estímulo percebido como ameaça</div><div class="fa">↓</div>
<div class="fb">Tálamo → <b>amígdala lateral</b> (condiciona o medo)</div><div class="fa">↓</div>
<div class="fb vi">Amígdala central (hiperativa)</div><div class="fa">↓ projeta para</div>
<div class="fr3"><div class="fb">Hipotálamo<div class="fp">CRH → ACTH → cortisol</div></div><div class="fb">Tronco<div class="fp">simpático: FC, sudorese</div></div><div class="fb">Periaquedutal<div class="fp">congelar, fugir</div></div></div>
<div class="fr" style="margin-top:5px"><div class="fb ou">CPF medial = freio<div class="fp">hipoativo: não extingue o medo</div></div><div class="fb ou">Hipocampo = contexto<div class="fp">menor no TEPT: generaliza o medo</div></div></div></div>'''

render(S1 + 'SP 1.2 · Transtornos de ansiedade - resumo em 1 folha', dict(layout='B', titulo='Transtornos de Ansiedade',
 sub='Tipos (DSM-5), TAG e pânico, circuito do medo, ansiolíticos e glândula suprarrenal', vars='--fs:7.95pt;--lh:1.5;--gap:3.4mm',
 corpo=f'''<div class="gB"><div>
{card('O circuito do medo', FLX_MEDO)}
{card('Neurotransmissores', '<p>Excitadores ↑: <b>NE</b> (locus coeruleus, pico no pânico), <b>CRH</b>, 5-HT em receptor ansiogênico (<b>5-HT2C</b> &gt; 5-HT1A) · inibidores ↓: <b>GABA</b>, neuropeptídeo Y, galanina. Hiperventilação → hipocapnia → tontura e parestesias.</p>')}
{card('Tratamento', '''<ul><li><b>ISRS</b> (sertralina, escitalopram) e <b>IRSN</b> (venlafaxina, duloxetina): 1ª linha de longo prazo · <b>TCC</b> é a psicoterapia padrão-ouro</li>
<li><b>Benzodiazepínicos</b> (clonazepam, alprazolam): modulador alostérico do GABA-A (entre α e γ2) → ↑ <b>frequência</b> de abertura do Cl⁻; só curto prazo. Uso crônico: menos GABA-A e mais NMDA/AMPA → retirada abrupta dá <b>convulsão</b></li>
<li><b>Flumazenil:</b> antagonista competitivo; ação em 1–2 min, dura ~1 h; no dependente pode convulsionar</li>
<li><b>Buspirona:</b> agonista parcial 5-HT1A; TAG; 2–4 semanas; sem dependência</li>
<li><b>Propranolol:</b> sintomas periféricos, ansiedade de desempenho; cuidado em asma</li></ul>''')}
{nc(['Crise de pânico isolada não é transtorno de pânico.', 'Benzodiazepínico não abre o canal sozinho: aumenta a frequência com GABA.', 'Benzo é ponte; o tratamento de longo prazo é ISRS/IRSN.', 'Propranolol trata o corpo, não a ansiedade central.', 'Medo é ameaça real e imediata; ansiedade é antecipação.'])}
</div><div>
{card('Os tipos e o tempo', '''<table><tr><th>Quadro</th><th>Chave</th></tr>
<tr><td>Separação</td><td>Medo de ficar longe do apego; ≥ 4 sem (criança) ou ≥ 6 m (adulto)</td></tr>
<tr><td>Mutismo seletivo</td><td>Não fala em certas situações sociais; ≥ 1 mês</td></tr>
<tr><td>Fobia específica</td><td>Objeto/situação; a <b>mais prevalente</b>; síncope no tipo sangue</td></tr>
<tr><td>Ansiedade social</td><td>Medo de ser avaliado; rubor, tremor</td></tr>
<tr><td>Agorafobia</td><td>≥ 2 de 5: transporte, aberto, fechado, multidão, sair só</td></tr>
<tr><td>TAG</td><td>≥ <b>6 meses</b>, difícil de controlar, ≥ <b>3 de 6</b>: inquietação, fadiga, "branco", irritabilidade, tensão muscular, sono</td></tr>
<tr><td>Pânico</td><td>Ataques <b>inesperados</b> (pico em minutos, ≥ 4 sintomas) + ≥ <b>1 mês</b> de medo de nova crise ou esquiva</td></tr></table>
<p style="margin-top:2px">Antes, afaste causa médica: hipertireoidismo, arritmia, feocromocitoma, hipoglicemia, cafeína, cocaína.</p>''')}
{card('Suprarrenal e eixo HHA', '''<ul><li>Córtex (mesoderma, 90%) de fora para dentro: <b>glomerulosa</b> → aldosterona (regida por renina-angiotensina e K⁺, não pelo ACTH) · <b>fasciculada</b> (65%) → cortisol · <b>reticulada</b> → andrógenos</li>
<li>Medula (crista neural): células cromafins → adrenalina e noradrenalina</li>
<li>Artérias: superior (frênica inferior), média (aorta), inferior (renal) · veia direita → VCI; <b>esquerda → renal esquerda</b></li>
<li>PVN → CRH → ACTH → cortisol, com feedback negativo; na ansiedade o eixo fica hiperativo</li></ul>''')}
{mn([('GFR: sal, açúcar, sexo', 'glomerulosa, fasciculada, reticulada, de fora para dentro.'), ('TAG: 6 meses, 3 de 6', ''), ('Pânico: pico em minutos, medo por um mês', ''), ('Flumazenil no dependente, convulsão de presente', ''), ('Buspirona busca calma sem viciar', '')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de transtornos de ansiedade e glândula suprarrenal do 6º semestre (DSM-5; Sadock; Goodman &amp; Gilman; Rang &amp; Dale; Junqueira; Moore).'))

# ======================= TRANSTORNOS PSICÓTICOS (B) =======================
FLX_TEMPO = '''<div class="flx">
<div class="fb esc">Sintomas psicóticos: quanto tempo?</div><div class="fa">↓</div>
<div class="fr3"><div class="fb ok"><b>1 dia a &lt; 1 mês</b><div class="fp">psicótico breve; volta ao normal</div></div><div class="fb ou"><b>1 a &lt; 6 meses</b><div class="fp">esquizofreniforme</div></div><div class="fb vi">≥ 6 meses<div class="fp" style="color:#fff">esquizofrenia</div></div></div>
<div class="fa">↓ e se...</div>
<div class="fr"><div class="fb">Só delírio, ≥ 1 mês<div class="fp">transtorno delirante; funciona bem</div></div><div class="fb">Humor na maior parte<div class="fp">esquizoafetivo: + ≥ 2 semanas de psicose sem humor</div></div></div>
<div class="fr" style="margin-top:5px"><div class="fb">Psicose só dentro do episódio de humor<div class="fp">humor com sintomas psicóticos</div></div><div class="fb">Droga, remédio ou doença<div class="fp">induzido / devido a condição médica</div></div></div></div>'''

render(S1 + 'SP 1.3 · Transtornos psicóticos - resumo em 1 folha', dict(layout='B', titulo='Transtornos Psicóticos',
 sub='Espectro da esquizofrenia, vias dopaminérgicas, antipsicóticos e rede de cuidado', vars='--fs:8.05pt;--lh:1.47;--gap:3.3mm',
 corpo=f'''<div class="gB"><div>
{card('Pelo tempo de doença', FLX_TEMPO)}
{card('Esquizofrenia (DSM-5)', '''<p><b>≥ 2</b> por ≥ 1 mês (um deles <b>delírio, alucinação ou discurso desorganizado</b>): delírios, alucinações, discurso desorganizado, comportamento desorganizado/catatônico, sintomas negativos. Prejuízo funcional e <b>≥ 6 meses</b> no total.</p>
<ul><li><b>Positivos</b> (excesso) · <b>negativos</b> (avolia, alogia, anedonia, embotamento; pior prognóstico) · desorganização · cognitivos</li>
<li>0,3–0,7%; início: homem ~20 anos, mulher fim dos 20 (e prognóstico melhor)</li>
<li>Gêmeo idêntico ~50%; ventrículos alargados; hipofunção <b>NMDA</b>; poda sináptica excessiva</li>
<li>Pior curso: início precoce, homem, negativos, déficit cognitivo</li></ul>''')}
{card('Rede de cuidado', '<p>Atenção básica = porta de entrada; <b>CAPS</b> no caso grave (I, II, III, i, ad), em regime intensivo, semi-intensivo ou não intensivo; hospital e urgência na crise.</p>')}
{nc(['Delírio é crença fixa; delirium é confusão aguda flutuante.', 'Psicose só durante o episódio de humor não é esquizofrenia.', 'Psicose com alucinação olfativa: pense em epilepsia temporal.', 'Antes de rotular, afaste lúpus, anti-NMDA, neurossífilis, HIV e drogas.', 'Sintoma negativo responde mal ao típico.'])}
</div><div>
{card('As 4 vias da dopamina', '''<table><tr><th>Via</th><th>Na doença</th><th>Bloqueio D2 causa</th></tr>
<tr><td>Mesolímbica</td><td>↑ DA → positivos</td><td>Efeito antipsicótico</td></tr>
<tr><td>Mesocortical</td><td>↓ DA → negativos e cognitivos</td><td>Piora negativos</td></tr>
<tr><td>Nigroestriatal</td><td>(Parkinson)</td><td>Extrapiramidais: distonia, parkinsonismo, acatisia, discinesia tardia</td></tr>
<tr><td>Tuberoinfundibular</td><td>DA inibe prolactina</td><td>Hiperprolactinemia: galactorreia, amenorreia</td></tr></table>''')}
{card('Antipsicóticos', '''<ul><li><b>Típicos</b> (haloperidol, clorpromazina): bloqueio D2. Alta potência = mais extrapiramidal; baixa potência = mais sedação e hipotensão</li>
<li><b>Atípicos</b> (risperidona, olanzapina, quetiapina, aripiprazol): D2 + <b>5-HT2A</b> → menos extrapiramidal, melhor nos negativos; custo <b>metabólico</b> (peso, glicemia, lipídios)</li>
<li><b>Clozapina:</b> única eficaz na <b>resistente</b> e reduz suicídio; <b>agranulocitose</b> → hemograma</li>
<li><b>Depósito (LAI)</b> para quem não adere · <b>biperideno</b> corrige extrapiramidal · benzo na agitação/catatonia</li>
<li><b>Síndrome neuroléptica maligna:</b> rigidez, febre, confusão, instabilidade autonômica</li></ul>''')}
{card('Além da dopamina', '<p>↓ interneurônios <b>GABA</b> soltam a dopamina · <b>5-HT2A</b>: seu bloqueio melhora sintomas · ACh/nicotina: déficit cognitivo; explica o <b>tabagismo</b> frequente (automedicação) · infecção intrauterina e idade paterna avançada aumentam o risco.</p>')}
{mn([('Breve, Forme, Fenia: 1 mês e 6 meses', 'os dois cortes de tempo.'), ('Mesolímbica é Mais, Mesocortical é Menos', 'positivos por excesso, negativos por falta de dopamina.'), ('Tubero tira o freio do leite', 'bloqueio D2 sobe a prolactina.'), ('Clozapina cura a resistente e cobra o hemograma', ''), ('Atípico troca o tremor pela balança', 'menos extrapiramidal, mais síndrome metabólica.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de transtornos psicóticos, esquizofrenia e antipsicóticos do 6º semestre (DSM-5; Sadock; Golan; Rang &amp; Dale; Ministério da Saúde).'))

# ======================= TRANSTORNO BIPOLAR (C) =======================
render(S1 + 'SP 1.4 · Transtorno bipolar - resumo em 1 folha', dict(layout='C', titulo='Transtorno Bipolar',
 sub='Tipo I, tipo II e ciclotimia, diferenciais, estabilizadores do humor e o que não usar', vars='--fs:8pt;--lh:1.47;--gap:3.1mm',
 corpo=f'''<div class="sec">{cards([('Mania', '≥ 7 dias', 'ou qualquer duração se internou'), ('Hipomania', '≥ 4 dias', 'sem prejuízo grave, sem psicose'), ('Ciclotimia', '≥ 2 anos', '1 ano em jovens; nunca episódio completo'), ('Ciclagem rápida', '≥ 4/ano', 'episódios em 12 meses')])}</div>
<div class="g2"><div>
{sec('Os três quadros', '''<table><tr><th></th><th>Precisa de</th><th>Curso</th></tr>
<tr><td>Tipo I</td><td><b>1 episódio maníaco</b> basta; depressão não é obrigatória</td><td>Início ~18 anos; &gt; 90% recorrem</td></tr>
<tr><td>Tipo II</td><td>≥ 1 <b>hipomania</b> + ≥ 1 <b>depressão maior</b>; nunca mania</td><td>~25 anos; mais tempo deprimido, mais tentativas; 5–15% viram tipo I</td></tr>
<tr><td>Ciclotimia</td><td>Hipo e depressão subclínicas na metade do tempo, sem pausa &gt; 2 meses</td><td>Crônica; pode virar I ou II</td></tr></table>
<p style="margin-top:2px"><b>Mania:</b> humor elevado ou irritável + ≥ 3 (≥ 4 se só irritável): grandiosidade, menos sono, fala acelerada, fuga de ideias, distraibilidade, mais atividade, risco. <b>Estado misto</b> = mania + depressão juntas: maior risco de suicídio.</p>''')}
{sec('Diferenciais e exames', '''<ul><li><b>TDAH:</b> crônico desde a infância · <b>borderline:</b> instável e reativo, não episódico · <b>ansiedade:</b> contínua · <b>DDHM</b> (criança): irritabilidade crônica</li>
<li>Induzido: cocaína, anfetamina, corticoide, antidepressivo, L-dopa · início tardio → procure causa médica</li>
<li>Pedir: hemograma, TSH/T4, função renal e hepática, eletrólitos, sorologias (HIV, sífilis), toxicológico, imagem</li></ul>''')}
{sec('Fisiopatologia', '<p>DA e NE ↑ na mania e ↓ na depressão; glutamato (NMDA) hiperativo; ↓ GABA; ↓ BDNF; eixo HHS ↑. Imagem: menos substância cinzenta no cíngulo anterior e ínsula, ventrículos maiores.</p>')}
{sec('O que não usar', '''<ul><li><b>Antidepressivo em monoterapia</b> (ISRS, IRSN, tricíclico, bupropiona): virada e ciclagem rápida; se precisar, sempre com estabilizador</li>
<li><b>Tricíclicos:</b> altíssimo risco de virada · <b>IRSN:</b> mais virada que ISRS</li>
<li><b>Estimulantes</b> (metilfenidato, anfetamina): podem precipitar mania ou psicose</li>
<li><b>Benzodiazepínico</b> de longo prazo: dependência, não trata o transtorno</li>
<li><b>Álcool:</b> desestabiliza o humor e, com o lítio, desidrata e sobe a litemia</li></ul>''')}
</div><div>
{sec('Tratamento', '''<ul><li><b>Lítio</b>, padrão-ouro na mania (inibe IMPase e GSK-3): tremor, poliúria/<b>DI nefrogênico</b>, <b>hipotireoidismo</b>, nefrotoxicidade; tiazídico, AINE e álcool ↑ litemia</li>
<li><b>Valproato:</b> mania mista; hepatotoxicidade, pancreatite, <b>tubo neural</b></li>
<li><b>Lamotrigina:</b> depressão bipolar; <b>Stevens-Johnson</b></li>
<li><b>Carbamazepina:</b> SIADH (hiponatremia), leucopenia; <b>indutor CYP3A4</b> (corta anticoncepcional e varfarina)</li>
<li><b>Atípicos:</b> quetiapina (1ª linha na depressão bipolar I e II), lurasidona, aripiprazol, risperidona; olanzapina + fluoxetina</li>
<li>Fases: aguda → continuação (4–9 meses) → manutenção (anos)</li></ul>''')}
{nc(['Antidepressivo sozinho no bipolar: nunca (virada e ciclagem).', 'Tipo II não é "mais leve" que o tipo I.', 'Hipomania com psicose ou internação já é mania.', 'Benzodiazepínico só como ponte na agitação ou insônia.'])}
{mn([('Mania dura a semana; hipomania, um feriadão', '7 dias × 4 dias.'), ('Uma mania basta para o tipo I', ''), ('Lítio cobra do rim e da tireoide', 'poliúria, DI nefrogênico, hipotireoidismo.'), ('Carbamazepina carrega as enzimas e leva o sódio', 'indutor do CYP3A4 e SIADH.'), ('Lamotrigina, olho na pele', 'Stevens-Johnson.'), ('Valproato vai ao fígado e ao tubo neural', '')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de transtornos bipolares e estabilizadores de humor do 6º semestre (DSM-5; Sadock; Tratado da ABP; Porto).'))

# ======================= NEOPLASIA E SÍNDROME CONSUMPTIVA (A) =======================
render('6º sem D3 · NCS · SP 3.3 · Neoplasia e síndrome consumptiva - resumo em 1 folha', dict(layout='A', titulo='Neoplasia e Síndrome Consumptiva',
 sub='Hallmarks, por que o câncer emagrece, caquexia, rastreamento, quimioterápicos e câncer de ovário', vars='--fs:8.1pt;--lh:1.5;--gap:3.4mm',
 corpo=f'''<div class="gL"><div>
{sec('Hallmarks do câncer (Hanahan e Weinberg)', '''<ul><li><b>2000 (6):</b> autossuficiência em sinais de crescimento, insensibilidade a antiproliferativos, evasão da apoptose, replicação ilimitada (telomerase), angiogênese (VEGF), invasão e metástase</li>
<li><b>2011:</b> + metabolismo desregulado (<b>Warburg</b>) e evasão imune (PD-L1); capacitadoras: instabilidade genômica e <b>inflamação</b></li>
<li><b>2022:</b> plasticidade fenotípica, reprogramação epigenética, microbiomas, células senescentes (SASP)</li></ul>''')}
{sec('Por que o câncer emagrece', '''<ul><li><b>Warburg:</b> glicólise mesmo com oxigênio; o tumor gasta muito para pouco ATP e drena glicose, aminoácidos e lipídios</li>
<li><b>TNF-α, IL-1, IL-6:</b> inibem NPY/AgRP e ativam POMC/CART no hipotálamo (fome desligada), aumentam gasto basal, lipólise, proteólise e <b>resistência anabólica</b></li>
<li>Quimio lesa o TGI (mucosite) → mais citocinas → anorexia e náusea</li>
<li>Doença avançada: ↓ T3 e ↑ T3 reverso (eutireoidiano doente); GH sobe com a hipoglicemia</li></ul>''')}
{sec('Caquexia', '''<p>Perda de peso <b>involuntária e progressiva, sobretudo de músculo</b>, com inflamação sistêmica; responde por <b>&gt; 20%</b> das mortes em oncologia. Tríade caquexia–anorexia–astenia. Avaliar: IMC, circunferências, PCR, albumina, relação neutrófilo/linfócito e <b>TC em L3</b> (massa muscular). Sarcopenia é componente, mas sozinha superestima a caquexia. Cuidados paliativos desde o diagnóstico de doença ameaçadora.</p>''')}
{sec('Rastreamento (resumo)', '''<table><tr><th>Câncer</th><th>Quem e como</th></tr>
<tr><td>Mama</td><td>Mamografia 50–69 anos, a cada 2 anos</td></tr>
<tr><td>Colo do útero</td><td>Citologia 25–64 anos; após 2 anuais normais, a cada 3 anos</td></tr>
<tr><td>Colorretal</td><td>50–75: sangue oculto anual ou colonoscopia a cada 10 anos</td></tr>
<tr><td>Próstata</td><td>PSA 50–69 por decisão compartilhada (45 se negro ou família)</td></tr>
<tr><td>Pulmão</td><td>TC de baixa dose anual: 55–80 anos, ≥ 30 maços-ano, parou há ≤ 15 anos</td></tr>
<tr><td>Fígado</td><td>USG ± AFP a cada 6 meses na cirrose ou hepatite B</td></tr>
<tr><td>Ovário</td><td>Não há rastreio populacional (USG + CA-125 só em alto risco)</td></tr></table>''')}
{sec('Metabolismo em 3 tempos', '<p><b>Alimentado</b> (0–4 h): insulina, glicogênese, lipogênese · <b>jejum curto</b> (4–12 h): glucagon, glicogenólise · <b>prolongado</b> (&gt; 24–48 h): cortisol, GH, catecolaminas, lipólise, corpos cetônicos</p>')}
{sec('Quimioterápicos', '<p><b>Taxanos</b> estabilizam microtúbulos · <b>vinca</b> impede a polimerização · <b>platinas</b> fazem ligações cruzadas · alquilantes (ciclofosfamida) · antraciclinas (doxorrubicina: intercala, topo II) · antimetabólitos (5-FU, metotrexato, 6-MP)</p>')}
</div><div>
{box('Ovário', '<p><b>Seroso de alto grau</b> (o mais comum; nasce na fímbria, STIC; disseminação peritoneal) · <b>endometrioide</b> e <b>células claras</b> (endometriose, ARID1A). Tratamento: carboplatina + paclitaxel. Veia ovariana D → VCI; E → renal E. Carcinoma × cistadenoma: <b>invasão do estroma</b>, necrose, atipia.</p>')}
{nc(['Caquexia não é só falta de comida: é inflamação e músculo.', 'Ovário não tem rastreio populacional.', 'Taxano estabiliza; vinca impede a montagem.', 'O que define malignidade no ovário é a invasão estromal.'])}
{mn([('Warburg é perdulário', 'queima glicose sem usar o oxigênio.'), ('Citocina desliga o NPY e liga o POMC', 'fome em off.'), ('Taxano trava, vinca veta', 'microtúbulos.'), ('Aos 50 começa a fila', 'mama, cólon e próstata.'), ('Esquerda faz escala na renal', 'veia ovariana esquerda.')])}
{box('Números que caem', '<p>caquexia: &gt; 20% das mortes<br>massa muscular: TC em L3<br>mama 50–69, a cada 2 anos<br>colo 25–64 · cólon 50–75<br>pulmão: ≥ 30 maços-ano<br>fígado: USG a cada 6 meses</p>')}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de neoplasia e síndrome consumptiva do 6º semestre (Hanahan e Weinberg 2000, 2011, 2022; Bogliolo; Rang &amp; Dale; Whalen; Miola).'))
