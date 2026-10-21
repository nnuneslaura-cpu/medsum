import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from folha import render

# ---------- SP 2.3 · Doença falciforme e anemias hemolíticas (só o conteúdo do resumo) ----------
render('6º sem D2 · NCS · SP 2.3 · Doença falciforme e anemias hemolíticas - resumo em 1 folha', dict(
 titulo='Anemias Hemolíticas',
 sub='Doença falciforme, talassemias, membranopatias, enzimopatias e hemólises adquiridas em uma página',
 mais=['Doença falciforme: **febre**, crises e profilaxia', '**Coombs direto** separa imune × não imune', '**Traço talassêmico** × anemia ferropriva', '**PTT/SHU**: esquizócitos + plaquetopenia'],
 secoes=[
  ('Reconhecer a hemólise', 'hemácia vive ~120 dias', '''
<div class="dest"><b>Anemia + reticulocitose</b> + <b>LDH ↑</b> + <b>bilirrubina indireta ↑</b> + <b>haptoglobina ↓</b> = hemólise. Próximo passo: <b>Coombs direto</b> e <b>esfregaço</b>. IPR &gt; 2 = medula respondendo.</div>
<table><tr><th></th><th>Intravascular</th><th>Extravascular</th></tr>
<tr><td>Onde</td><td>Dentro do vaso</td><td>Macrófagos do baço/fígado</td></tr>
<tr><td>Pistas</td><td>LDH muito ↑, haptoglobina indetectável, <b>hemoglobinúria</b></td><td>Esplenomegalia, esferócitos</td></tr>
<tr><td>Exemplos</td><td>G6PD na crise, PTT/SHU, HPN, ABO, prótese</td><td>Esferocitose, AHAI quente, DF, talassemias</td></tr></table>
<div class="cols c3"><div class="cx"><b class="t">ESFERÓCITOS</b>Esferocitose ou AHAI quente</div><div class="cx"><b class="t">ESQUIZÓCITOS</b>MAT (PTT, SHU, CIVD), prótese</div><div class="cx"><b class="t">HEINZ / MORDIDAS</b>Deficiência de G6PD</div></div>'''),
  ('Doença falciforme', 'Glu → Val na β-globina · autossômica recessiva', '''
<div class="cols c2"><div><b>SS</b> e <b>S/β⁰</b>: graves · <b>SC</b>: retinopatia e necrose óssea · <b>AS</b> (traço): não é doença. Teste do pezinho: <b>FS</b> = DF · <b>FAS</b> = traço · <b>FSC</b>. Confirmar por eletroforese/HPLC.</div>
<div>HbS polimeriza na hipóxia → <b>vaso-oclusão</b> (dor, STA, sequestro, AVC) + <b>hemólise</b> (anemia, litíase, priapismo, HP). <b>HbF protege</b> → sintomas após 6 meses. <b>Asplenia funcional</b> → germes encapsulados.</div></div>
<h3>Complicações agudas</h3>
<table><tr><th>Quadro</th><th>Pista</th><th>Conduta</th></tr>
<tr><td>Febre</td><td>Risco de sepse pneumocócica</td><td><b>Ceftriaxona</b> já, hemocultura</td></tr>
<tr><td>Crise dolorosa</td><td>Dor óssea/abdominal</td><td>Analgesia em <b>até 1 h</b> (opioide se intensa), sem hiper-hidratar</td></tr>
<tr><td>STA</td><td><b>Infiltrado novo</b> + febre, dor torácica ou hipoxemia</td><td>Ceftriaxona + macrolídeo, O₂, espirometria, transfusão</td></tr>
<tr><td>Sequestro esplênico</td><td>Baço cresce + Hb cai ≥ 2 g/dL</td><td>Transfusão em pequenas alíquotas</td></tr>
<tr><td>Crise aplástica</td><td><b>Reticulócitos baixos</b> · parvovírus B19</td><td>Transfusão</td></tr>
<tr><td>AVC</td><td>Déficit focal</td><td><b>Exsanguineotransfusão</b> (HbS &lt; 30%)</td></tr>
<tr><td>Priapismo</td><td>&gt; 4 h</td><td>Emergência: urologia</td></tr></table>
<div class="dest"><b>Seguimento:</b> penicilina dos <b>3 meses aos 5 anos</b> · vacinas do CRIE · ácido fólico · <b>Doppler transcraniano anual dos 2 aos 16 anos</b> (≥ 200 cm/s → transfusão crônica) · <b>hidroxiureia</b> ↑ HbF (PCDT: a partir de 2 anos) · TCTH é a cura.</div>'''),
  ('Talassemias', 'microcitose por falta de cadeia de globina', '''
<div class="cols c2"><div><b>β-menor:</b> Hb normal ou pouco baixa, VCM muito baixo, hemácias normais/altas, <b>HbA2 &gt; 3,5%</b>. <b>β-maior (Cooley):</b> sintomas aos 6–24 meses, fácies típica, dependente de transfusão + <b>quelação de ferro</b>.</div>
<div><b>α:</b> 1 gene = silencioso · 2 = traço · 3 = <b>doença da HbH</b> · 4 = <b>Hb Bart → hidropsia fetal</b>.</div></div>'''),
  ('Membrana, enzimas e adquiridas', '', '''
<div class="cols c2"><div class="cx"><b class="t">ESFEROCITOSE</b>Anemia + icterícia + esplenomegalia + litíase precoce · <b>CHCM ↑</b>, <b>Coombs –</b>, teste <b>EMA</b> · esplenectomia após os 6 anos (vacinas antes).</div>
<div class="cx"><b class="t">G6PD</b>Ligada ao X · hemólise 24–72 h após <b>infecção, fava, primaquina, dapsona, sulfa, rasburicase</b> · dosagem pode ser normal na crise: repetir em 2–3 meses.</div>
<div class="cx"><b class="t">AHAI QUENTE × FRIA</b>Quente: <b>IgG</b>, esferócitos, LES/LLC → <b>prednisona 1 mg/kg</b>, rituximabe. Fria: <b>IgM/C3d</b>, Mycoplasma, EBV, linfoma → evitar frio, rituximabe.</div>
<div class="cx"><b class="t">HPN</b>Hemólise + <b>trombose atípica</b> (Budd-Chiari) + falência medular · citometria <b>CD55/CD59</b> · inibidor de C5 (vacina meningocócica antes).</div></div>'''),
 ],
 lado_tit='Não confunda na prova', lado_sub='Os distratores que mais derrubam',
 lado=['**Toda febre na DF é emergência:** ceftriaxona sem esperar exames.',
       '**Crise aplástica ≠ sequestro:** aplástica tem reticulócitos baixos; sequestro tem baço grande.',
       '**Não transfunda** crise dolorosa não complicada.',
       '**Hiper-hidratação** na crise dolorosa pode precipitar STA.',
       '**STA começa como crise dolorosa:** reavalie o tórax todo dia.',
       '**Teste de falcização não diferencia** traço de doença: use eletroforese/HPLC.',
       '**Esferócitos em dois lugares:** Coombs – = esferocitose; Coombs + = AHAI.',
       '**Microcitose com ferritina normal:** pense em talassemia, não dê ferro.',
       '**HbA2** pode cair com ferropenia: corrija o ferro e repita.',
       '**G6PD normal na crise** não exclui: repita depois.',
       '**Rasburicase** é contraindicada na deficiência de G6PD.',
       '**SHU típica:** antibiótico não é indicado.',
       '**PTT:** troca plasmática sem esperar o ADAMTS13; evite plaquetas.',
       '**CIVD** tem TP/TTPa alargados e fibrinogênio baixo; PTT/SHU têm coagulograma normal.'],
 conta_tit='Contas e números',
 conta_html='<b>IPR</b> = reticulócitos % × (Ht ÷ 45) ÷ fator de maturação (1; 1,5; 2; 2,5)<br><b>Mentzer</b> = VCM ÷ hemácias: &lt; 13 talassemia · &gt; 13 ferropriva<br><b>ADAMTS13</b> &lt; 10% = PTT · Transfusão crônica: <b>HbS &lt; 30%</b>',
 fontes='Elaborado pela MedSum com base no resumo da SP 2.3 (MS: condutas básicas e PCDT da doença falciforme; ASH; TIF; ISTH; Harrison).'))

# ---------- SP 2.4 · Linfomas e leucemias agudas ----------
render('6º sem D2 · NCS · SP 2.4 · Linfomas e leucemias agudas - resumo em 1 folha', dict(
 titulo='Leucemias e Linfomas',
 sub='Leucemias agudas, emergências onco-hematológicas e linfomas em uma página',
 mais=['**LPA**: CIVD → ATRA na suspeita', '**Neutropenia febril**: antibiótico na 1ª hora', '**Linfonodo suspeito** → biópsia excisional', '**Hodgkin × não Hodgkin**'],
 secoes=[
  ('Leucemia aguda: diagnosticar', '≥ 20% de blastos na medula', '''
<div class="cols c2"><div><b>Falência medular:</b> anemia, <b>plaquetopenia</b> (petéquias), neutropenia (febre). <b>Infiltração:</b> dor óssea, hepatoesplenomegalia, linfonodos, hipertrofia gengival (monocítica), massa mediastinal (LLA-T).</div>
<div><b>Caminho:</b> hemograma + esfregaço → emergências (coagulograma, lise, leucometria, febre) → <b>mielograma</b> + <b>imunofenotipagem</b> (separa LMA × LLA) + citogenética/molecular (risco).</div></div>
<table><tr><th></th><th>LLA</th><th>LMA</th></tr>
<tr><td>Quem</td><td><b>Criança, pico 2–5 anos</b> (câncer infantil mais comum)</td><td><b>Adulto</b>, mediana ~70 anos</td></tr>
<tr><td>Marcadores</td><td>TdT+; B: CD19, CD10, CD22 · T: CD3, CD7</td><td>MPO+, CD13, CD33, CD117 · <b>bastonetes de Auer</b></td></tr>
<tr><td>Genética</td><td>Hiperdiploidia e ETV6::RUNX1 = bom · <b>BCR::ABL1 (Ph+)</b> → inibidor de tirosina-quinase · KMT2A no lactente = ruim</td><td>ELN 2022: favorável t(8;21), inv(16), NPM1 · adverso <b>TP53</b>, cariótipo complexo</td></tr>
<tr><td>Tratamento</td><td>Indução → consolidação → <b>profilaxia do SNC</b> (intratecal) → manutenção <b>6-MP + metotrexato</b> (2–3 anos). Cura 85–90%</td><td><b>"7 + 3"</b> (citarabina + antraciclina) → altas doses ou TCTH alogênico · idoso: <b>azacitidina + venetoclax</b></td></tr></table>
<div class="dest"><b>Bom prognóstico na LLA:</b> 1–9 anos, leucócitos &lt; 50.000, LLA-B, <b>doença residual mínima negativa</b> no fim da indução (o fator mais forte).</div>'''),
  ('Leucemia promielocítica (LPA)', 't(15;17) PML::RARA', '''
<div>Chega com <b>CIVD + hiperfibrinólise</b> (sangramento é a principal causa de morte precoce). <b>Iniciar ATRA já na suspeita</b>. Repor plaquetas &gt; 30–50 mil e fibrinogênio &gt; 100–150. Baixo/intermediário risco: <b>ATRA + trióxido de arsênio</b>. <b>Síndrome de diferenciação</b> (febre, dispneia, infiltrado, derrame, ganho de peso) → <b>dexametasona 10 mg 12/12 h</b>. Cura &gt; 90%.</div>'''),
  ('Emergências', '', '''
<div class="cols c3"><div class="cx"><b class="t">LISE TUMORAL</b>↑ ácido úrico, K, P · ↓ Ca (Cairo-Bishop) · Burkitt, LLA · <b>hidratação</b> + alopurinol ou <b>rasburicase</b> (não na G6PD).</div>
<div class="cx"><b class="t">LEUCOSTASE</b>Blastos &gt; 100.000 + sintomas pulmonares/neurológicos · quimioterapia, hidroxiureia, leucaférese · <b>evite transfundir hemácias</b>.</div>
<div class="cx"><b class="t">NEUTROPENIA FEBRIL</b><b>≥ 38,3 °C</b> ou ≥ 38 °C por 1 h + neutrófilos <b>&lt; 500</b> → culturas + <b>cefepima/pip-tazo</b> na 1ª hora · MASCC ≥ 21 = baixo risco.</div></div>'''),
  ('Linfomas', 'biópsia excisional · estadiamento de Lugano', '''
<div class="dest"><b>Linfonodo suspeito:</b> &gt; 2 cm, endurecido, aderido, indolor, <b>supraclavicular</b>, &gt; 4–6 semanas, sintomas B, &gt; 40 anos → <b>biópsia excisional</b> (PAAF não classifica). Evite corticoide antes.</div>
<table><tr><th></th><th>Hodgkin</th><th>Não Hodgkin</th></tr>
<tr><td>Célula</td><td><b>Reed-Sternberg CD15+ CD30+</b></td><td>B na maioria (85–90%)</td></tr>
<tr><td>Quem</td><td>Bimodal: 15–35 e &gt; 55 anos · EBV</td><td>Aumenta com a idade · HIV, EBV, HTLV-1, H. pylori</td></tr>
<tr><td>Disseminação</td><td><b>Contígua</b>, mediastino (esclerose nodular)</td><td><b>Não contígua</b>, extranodal frequente</td></tr>
<tr><td>Tratamento</td><td><b>ABVD</b> ± RT · cura 80–90%</td><td>LDGCB: <b>R-CHOP</b> · folicular: observar se pouca doença</td></tr></table>
<div class="cols c2"><div><b>LNH:</b> LDGCB (mais comum) · folicular <b>t(14;18) BCL2</b> · Burkitt <b>t(8;14) MYC</b>, "céu estrelado", lise espontânea · manto <b>t(11;14) ciclina D1</b> · MALT gástrico → <b>erradicar H. pylori</b>.</div>
<div><b>Lugano:</b> I uma região · II ≥ 2 do mesmo lado do diafragma · III dos dois lados · IV extranodal disseminado. <b>Sintomas B:</b> febre &gt; 38 °C, sudorese noturna, perda &gt; 10% do peso em 6 meses.</div></div>'''),
 ],
 lado_tit='Não confunda na prova', lado_sub='Os distratores que mais derrubam',
 lado=['**Leucemia aguda × crônica:** aguda é bloqueio da maturação (blastos); crônica acumula células maduras.',
       '**Leucemia × linfoma:** leucemia começa na medula; linfoma no tecido linfoide.',
       '**Imunofenotipagem** é o exame que separa LMA de LLA.',
       '**Bastonete de Auer** = linhagem mieloide.',
       '**LPA:** não espere o PML::RARA para começar o ATRA.',
       '**Corticoide antes do mielograma** mascara a LLA.',
       '**Dor óssea que acorda a criança** + citopenias: pense em LLA, não em artrite.',
       '**Rasburicase** é proibida na deficiência de G6PD.',
       '**Leucostase:** gasometria pode mostrar pseudo-hipoxemia; potássio pode vir falsamente alto.',
       '**Neutropenia febril:** sem neutrófilo não há pus; a febre pode ser o único sinal.',
       '**PAAF não basta** para linfoma: biópsia excisional.',
       '**Supraclavicular esquerdo** (Virchow) = abdome; direito = tórax.',
       '**Rituximabe reativa hepatite B:** rastrear antes.',
       '**Hodgkin efeitos tardios:** bleomicina (pulmão), antraciclina (coração), RT (mama, tireoide).'],
 conta_tit='Escores',
 conta_html='<b>IPI</b> (LDGCB, 1 ponto cada): idade &gt; 60 · <b>LDH ↑</b> · ECOG ≥ 2 · estádio III–IV · &gt; 1 sítio extranodal. 0–1 baixo · 2 intermediário-baixo · 3 intermediário-alto · 4–5 alto.<br><b>Cairo-Bishop:</b> ác. úrico ≥ 8 · K ≥ 6 · P ≥ 4,5 · Ca ≤ 7 (≥ 2 = laboratorial; + creatinina, arritmia ou convulsão = clínica).',
 fontes='Elaborado pela MedSum com base no resumo da SP 2.4 (OMS 2022, ICC 2022, ELN 2022, Lugano, IDSA/ASCO, INCA, Harrison).'))
