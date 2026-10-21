# Folhas únicas do 6º D2 (hematologia) feitas SÓ com o texto dos resumos publicados no site (versões de 21/10/2026)
import sys, os
os.environ.setdefault('PASTA', 'folhas-publicadas')
sys.path.insert(0, os.path.dirname(__file__))
from folha import render

NC = 'Não confunda na prova'; NS = 'Os distratores que mais derrubam'

# ---------------- SP 2.1 ----------------
render('6º sem D2 · NCS · SP 2.1 · Coagulopatias hereditárias e PTI - resumo em 1 folha', dict(
 titulo='Coagulopatias e PTI',
 sub='Hemostasia, PTI, doença de von Willebrand, hemofilias, TEV e antitrombóticos em uma página',
 mais=['**Padrão do sangramento** localiza o defeito', '**TTPa isolado** + teste de mistura', '**PTI**: trata-se o sangramento', '**Hemofilia**: dose de fator e profilaxia'],
 secoes=[
  ('Onde está o defeito', 'olhe o sangramento antes do exame', '''
<table><tr><th></th><th>Plaquetas ou FvW (primária)</th><th>Fatores (secundária)</th></tr>
<tr><td>Onde</td><td>Pele e mucosas: petéquias, epistaxe, gengivorragia, <b>menorragia</b></td><td>Planos profundos: <b>hemartrose</b>, hematoma muscular</td></tr>
<tr><td>Quando</td><td>Imediato após trauma</td><td>Muitas vezes <b>tardio</b> (horas depois)</td></tr>
<tr><td>Exemplos</td><td>PTI, DvW 1 e 2, AAS</td><td>Hemofilias A e B, DvW tipo 3</td></tr></table>
<table><tr><th>TP</th><th>TTPa</th><th>Pense em</th></tr>
<tr><td>Normal</td><td>Longo</td><td>Hemofilias (VIII, IX, XI), DvW com FVIII baixo, heparina, anticoagulante lúpico</td></tr>
<tr><td>Longo</td><td>Normal</td><td>Deficiência de FVII, <b>início da varfarina</b> (FVII tem a menor meia-vida)</td></tr>
<tr><td>Longo</td><td>Longo</td><td>Vitamina K, hepatopatia, CIVD, via comum (X, V, II)</td></tr>
<tr><td>Normal</td><td>Normal</td><td>Hemostasia primária: PTI, AAS/AINE, trombocitopatias</td></tr></table>
<div class="dest"><b>Teste de mistura</b> (1:1 com plasma normal): <b>corrige = falta fator</b> (hemofilia) · <b>não corrige = inibidor</b> (anti-FVIII, anticoagulante lúpico). Deficiência de FXII alonga o TTPa e não sangra.</div>'''),
  ('Trombocitopenia imune (PTI)', 'plaquetas < 100.000 isoladas · exclusão', '''
<div class="cols c2"><div><b>Criança:</b> pico 2–6 anos, pós-viral, autolimitada (80–85% remitem em 12 meses). <b>Adulto:</b> crônica, mulheres. Recém-diagnosticada &lt; 3 meses · persistente 3–12 · crônica ≥ 12. Exame físico normal fora o sangramento (sem visceromegalia, linfonodos ou dor óssea).</div>
<div><b>Mielograma</b> só se atípico: visceromegalia, outras citopenias, falha do tratamento, &gt; 60 anos. <b>Alarme:</b> púrpura úmida e hemorragia retiniana. Adulto: sorologia HIV e HCV; Coombs se anemia (Evans).</div></div>
<table><tr><th>Situação</th><th>Conduta</th></tr>
<tr><td>Criança sem sangramento ou só cutâneo</td><td><b>Observação</b>, sem remédio</td></tr>
<tr><td>Mucosa sem risco de morte</td><td>Prednisona 2–4 mg/kg/dia 5–7 dias, ou dexametasona, ou <b>IgIV</b> 0,8–1 g/kg, ou anti-D</td></tr>
<tr><td>Emergência (HIC)</td><td><b>Plaquetas</b> + metilprednisolona 30 mg/kg + IgIV</td></tr>
<tr><td>Adulto</td><td>&gt; 30.000 não aumenta mortalidade · prednisona 1 mg/kg ou anti-D · 2ª linha: agonista de TPO, rituximabe, esplenectomia</td></tr></table>'''),
  ('Von Willebrand e hemofilias', '', '''
<div class="cols c2"><div class="cx"><b class="t">DOENÇA DE VON WILLEBRAND</b>Hereditária <b>mais comum</b>, autossômica (homens e mulheres). Tipo <b>1</b> (≥ 80%) quantitativo · <b>2B</b> plaquetopenia, <b>desmopressina contraindicada</b> · <b>2N</b> simula hemofilia A · <b>3</b> ausência, hemartroses. Mucocutâneo e <b>menorragia</b>. FvW:RCo/FvW:Ag ≥ 0,7 = tipo 1; &lt; 0,7 = tipo 2. <b>Desmopressina 0,3 µg/kg</b> no tipo 1; concentrado FVIII/FvW; antifibrinolítico.</div>
<div class="cx"><b class="t">HEMOFILIAS A (FVIII) E B (FIX)</b>Ligadas ao X · 30% sem história familiar. Grave <b>&lt; 1%</b> · moderada 1–5% · leve 5–40% (MS). Hemartrose (70–80%). TTPa longo que corrige; TP e plaquetas normais. <b>FVIII = (alvo − basal) × peso × 0,5</b> · FIX × 1. Meia-vida FVIII 8–12 h, FIX 24 h. TCE: 80–100% já, antes da TC. <b>Profilaxia</b> é o padrão na criança grave.</div></div>
<div class="dest"><b>Inibidor</b> (~30% na hemofilia A grave): Bethesda &lt; 5 UB → dobrar a dose · ≥ 5 UB → <b>agente de bypass</b> (CCPa ou FVIIa) · imunotolerância · <b>emicizumabe</b> no SUS (com inibidor; sem inibidor até 6 anos).</div>'''),
  ('TEV e antitrombóticos', '', '''
<div class="cols c2"><div>Virchow: estase, hipercoagulabilidade, lesão endotelial. Probabilidade baixa/moderada → <b>D-dímero</b> (só exclui); alta → imagem. TVP: <b>US com compressão</b>. EP: <b>angiotomografia</b>. EP maciça: <b>alteplase 100 mg em 2 h</b>. Anticoagular ≥ 3 meses.</div>
<div><b>HNF:</b> TTPa · protamina. <b>HBPM:</b> anti-Xa · protamina parcial. <b>Varfarina:</b> INR 2–3 · vit. K + complexo protrombínico. <b>Anti-Xa:</b> andexanet. <b>Dabigatrana:</b> idarucizumabe. <b>TIH</b> 5–10 dias → argatrobana ou fondaparinux.</div></div>'''),
 ],
 lado_tit=NC, lado_sub=NS,
 lado=['**Hemofílico forma o tampão:** ele só não se sustenta; sangra horas depois.',
       '**Petéquias = plaqueta**; hemartrose = fator.',
       '**TP isolado longo** no início da varfarina: FVII tem a menor meia-vida.',
       '**FXII baixo** alonga muito o TTPa e não sangra.',
       '**PTI ≠ dengue:** na PTI não há febre no sangramento; na dengue há leucopenia e hematócrito subindo.',
       '**Plaquetas muito baixas sangram pouco** na PTI: são jovens e funcionais.',
       '**Anticorpo antiplaquetário** não é de rotina na PTI.',
       '**Leucemia** raramente vem com plaquetopenia isolada; dor óssea e visceromegalia pedem mielograma.',
       '**Anti-D** só em Rh+, com baço e Coombs negativo.',
       '**Desmopressina** não funciona na hemofilia A grave nem na B, e é proibida no DvW 2B.',
       '**Grupo O** tem metade do FvW: exame normal não exclui DvW.',
       '**Mulher portadora** de hemofilia pode sangrar (fator de 22% a 116%).',
       '**Nunca AAS, AINE ou IM** em quem tem coagulopatia.',
       '**Ácido tranexâmico** não se usa na hematúria (coágulos).'],
 conta_tit='Números que caem',
 conta_html='<b>FVIII (UI)</b> = (alvo − basal) × peso × 0,5 · ex.: 70 kg, 0 → 100% = <b>3.500 UI</b><br><b>FIX (UI)</b> = (alvo − basal) × peso × 1<br><b>Plaquetas</b> 150–450 mil · <b>fibrinogênio</b> mínimo 100 mg/dL · <b>INR</b> 2–3',
 fontes='Elaborado pela MedSum com base no resumo da SP 2.1 (MS: protocolos de hemofilias e de DvW; Tratado de Pediatria SBP; Harrison).'))

# ---------------- SP 2.2 ----------------
render('6º sem D2 · NCS · SP 2.2 · Anemias carenciais - resumo em 1 folha', dict(
 titulo='Anemias Carenciais', css='body{font-size:8.25pt}.sec{margin-bottom:4.2mm}',
 sub='Anemia ferropriva e anemia megaloblástica (vitamina B12 e folato) em uma página',
 mais=['**Ferritina < 30** confirma (protocolo BR)', '**Ferropriva × inflamação × talassemia**', '**B12**: neuro e nunca folato isolado', '**Ferropenia no homem** = trato digestivo'],
 secoes=[
  ('Definir e classificar', '', '''
<div class="cols c2"><div><b>Anemia (OMS/MS):</b> homem &lt; 13 · mulher &lt; 12 · gestante &lt; 11 · criança &lt; 11 g/dL. Crônica pode ser pouco sintomática até Hb 7–8 (↑ 2,3-DPG, ↑ débito, redistribuição).</div>
<div><b>Índice reticulocítico &lt; 2</b> = produção/maturação (carenciais) · &gt; 2,5 = hemólise. <b>VCM</b> &lt; 80 micro · 80–100 normo · &gt; 100 macro. <b>RDW</b> alto na ferropriva, normal no traço talassêmico.</div></div>'''),
  ('Anemia ferropriva', 'a causa mais comum de anemia', '''
<div class="cols c2"><div>Absorção no <b>duodeno</b> (DMT-1), saída pela <b>ferroportina</b>. <b>Hepcidina</b> degrada a ferroportina: <b>cai</b> na falta de ferro e <b>sobe</b> na inflamação. Ordem da queda: <b>ferritina</b> → ferro/saturação → Hb e microcitose.</div>
<div><b>Causas:</b> perda (menstruação, TGI, parasitose), demanda (gestação, crescimento), dieta, má absorção (bariátrica, celíaca, IBP). <b>Clínica:</b> coiloníquia, queilite, <b>pica/pagofagia</b>, Plummer-Vinson.</div></div>
<table><tr><th></th><th>Ferropriva</th><th>Inflamação</th><th>Traço talassêmico</th></tr>
<tr><td>Ferritina</td><td><b>&lt; 30</b> (&lt; 15 grave)</td><td>Normal/alta (≥ 100)</td><td>50–300</td></tr>
<tr><td>TIBC</td><td><b>Alta</b> (&gt; 360)</td><td><b>Baixa</b> (&lt; 300)</td><td>Normal</td></tr>
<tr><td>Saturação</td><td>&lt; 10–20%</td><td>10–20%</td><td>30–80%</td></tr>
<tr><td>RDW</td><td>Alto</td><td>Normal ou alto</td><td><b>Normal</b></td></tr>
<tr><td>Eletroforese</td><td>Normal</td><td>Normal</td><td><b>HbA2 alta</b> (β)</td></tr></table>
<div class="dest"><b>Com inflamação:</b> saturação &lt; 20% + ferritina <b>30–100</b> = ferropenia associada; ferritina ≥ 100 + PCR alta = só inflamação.</div>
<div><b>Tratar:</b> <b>sulfato ferroso</b> longe das refeições · homem 120 mg/dia, mulher e gestante 100–200 mg (+ fólico 400 µg), criança 3–6 mg/kg · <b>mínimo 90 dias</b>, até ferritina ≥ 30. Reticulócitos sobem do <b>3º ao 5º dia</b> (pico 8–10); Hb ≥ 2 g/dL em 3–4 semanas. <b>IV</b>: intolerância, refratária em 8 semanas, bariátrica, DII, diálise. Transfusão só se instável.</div>'''),
  ('Anemia megaloblástica', 'defeito na síntese de DNA', '''
<div class="cols c2"><div>Sem B12, o folato fica "preso" (armadilha do folato). <b>Ácido metilmalônico sobe só na falta de B12</b>; homocisteína sobe nas duas. Eritropoese ineficaz: <b>LDH e BI altas com reticulócitos baixos</b>; pode haver pancitopenia.</div>
<div><b>B12:</b> anemia perniciosa (anti-FI específico; anticélula parietal sensível), gastrectomia, íleo, <b>veganos</b>, metformina e IBP somam. Reserva dura 3–4 anos. <b>Folato:</b> álcool, gestação, hemólise, metotrexato; reserva 3–4 meses.</div></div>
<div class="cols c2"><div class="cx"><b class="t">CLÍNICA E EXAMES</b>Glossite, icterícia leve. <b>Só a B12 lesa o nervo:</b> parestesias, perda vibratória, Romberg +, degeneração combinada subaguda. Macro-ovalócitos, <b>neutrófilos hipersegmentados</b>. B12 &lt; 200 pg/mL (&lt; 100 típico).</div>
<div class="cx"><b class="t">TRATAR</b><b>B12 1.000 µg IM</b> (ataque ~6 doses) → mensal, vitalício se causa permanente; VO 1.000–2.000 µg/dia também funciona. <b>Ácido fólico 5 mg/dia por 4 meses</b>. Gestação 400 µg (5 mg se DTN prévio). Monitorar potássio.</div></div>'''),
 ],
 lado_tit=NC, lado_sub=NS,
 lado=['**Ferropenia em homem ou pós-menopausa** = sangramento digestivo até prova em contrário: EDA e colonoscopia.',
       '**Ferritina é de fase aguda:** pode vir "normal" na inflamação e esconder a falta de ferro.',
       '**Inflamação** tem TIBC baixa; ferropriva tem TIBC alta.',
       '**Traço talassêmico** tem RDW normal e ferro normal: não dê ferro.',
       '**Doador frequente:** Hb quase normal com ferritina baixa.',
       '**Plaquetose** na ferropenia é reativa, não é doença da medula.',
       '**Falha do ferro oral:** adesão, perda que continua, má absorção, diagnóstico errado.',
       '**VCM "normal" na gestante** pode ser ferro + folato juntos; o RDW alto denuncia.',
       '**Nunca ácido fólico isolado** sem excluir ou tratar a B12: a lesão neurológica progride.',
       '**Neurológico pode vir sem anemia** e pode ficar irreversível.',
       '**Anemia perniciosa:** a via oral pode falhar; reposição IM e EDA (risco de câncer gástrico).',
       '**LDH alta na megaloblástica** não é hemólise periférica: é eritropoese ineficaz.',
       '**Choque hipovolêmico:** Hb pode estar normal nas primeiras horas; resistência vascular alta.',
       '**Anemia crônica grave:** IC de alto débito, pele quente, resistência vascular baixa.'],
 conta_tit='Contas e cortes',
 conta_html='<b>Saturação (IST)</b> = ferro × 100 ÷ TIBC · &lt; 20% = baixa<br><b>Ferritina</b>: &lt; 30 confirma · &lt; 15 grave (protocolo BR)<br><b>VCM</b> &lt; 80 · 80–100 · &gt; 100 fL<br><b>Ferro IV (Harrison)</b> = peso × 2,3 × (15 − Hb) + 500 a 1.000 mg',
 fontes='Elaborado pela MedSum com base no resumo da SP 2.2 (Conitec 2023: PCDT da anemia por deficiência de ferro; Tratado de Pediatria SBP; Harrison).'))

# ---------------- SP 2.3 ----------------
render('6º sem D2 · NCS · SP 2.3 · Doença falciforme e anemias hemolíticas - resumo em 1 folha', dict(
 titulo='Anemias Hemolíticas',
 sub='Doença falciforme, talassemias, membranopatias, enzimopatias e hemólises adquiridas em uma página',
 mais=['Doença falciforme: **febre**, crises e profilaxia', '**Coombs direto** separa imune × não imune', '**Traço talassêmico** × anemia ferropriva', '**PTT/SHU**: esquizócitos + plaquetopenia'],
 secoes=[
  ('Reconhecer a hemólise', 'hemácia vive ~120 dias', '''
<div class="dest"><b>Anemia + reticulocitose</b> + <b>LDH ↑</b> + <b>bilirrubina indireta ↑</b> + <b>haptoglobina ↓</b> = hemólise. Próximo passo: <b>Coombs direto</b> e <b>esfregaço</b>.</div>
<table><tr><th></th><th>Intravascular</th><th>Extravascular</th></tr>
<tr><td>Onde</td><td>Dentro do vaso</td><td>Macrófagos do baço/fígado</td></tr>
<tr><td>Pistas</td><td>LDH muito ↑, <b>hemoglobinúria</b>, hemossiderinúria</td><td><b>Esplenomegalia</b>, esferócitos</td></tr>
<tr><td>Exemplos</td><td>G6PD na crise, PTT/SHU, HPN, ABO, prótese</td><td>Esferocitose, AHAI quente, DF, talassemias</td></tr></table>
<div class="cols c3"><div class="cx"><b class="t">ESFERÓCITOS</b>Esferocitose ou AHAI quente</div><div class="cx"><b class="t">ESQUIZÓCITOS</b>MAT (PTT, SHU, CIVD), prótese</div><div class="cx"><b class="t">HEINZ / MORDIDAS</b>Deficiência de G6PD</div></div>'''),
  ('Doença falciforme', 'Glu → Val na β-globina · autossômica recessiva', '''
<div class="cols c2"><div><b>SS</b> e <b>S/β⁰</b>: graves · <b>SC</b>: retinopatia e necrose óssea, baço persiste · <b>AS</b>: traço, não é doença. Pezinho: <b>FS</b> = DF · <b>FAS</b> = traço · <b>FSC</b>. Eletroforese confirma <b>após 6 meses</b>.</div>
<div>HbS polimeriza → <b>vaso-oclusão</b> + <b>hemólise</b>. <b>HbF protege</b>. <b>Asplenia funcional</b> em 94% aos 5 anos; pneumococo &gt; 70% das infecções. Hb basal 7–11,5 g/dL na SS.</div></div>
<table><tr><th>Quadro</th><th>Pista</th><th>Conduta</th></tr>
<tr><td>Febre</td><td>Risco de sepse</td><td>Avaliar em <b>até 4 h</b>, hemocultura, <b>antibiótico parenteral</b> sem esperar; internar &lt; 5 anos com &gt; 38,3 °C</td></tr>
<tr><td>Crise dolorosa</td><td>Dor óssea/abdominal</td><td>Analgesia <b>imediata</b> e escalonada (opioide se intensa), sem hiper-hidratar</td></tr>
<tr><td>STA</td><td><b>Infiltrado novo</b> + febre ou sintomas</td><td>Cefalosporina 2ª/3ª (+ macrolídeo), <b>O₂ para SatO₂ &gt; 92%</b>, fisioterapia, transfusão se piora</td></tr>
<tr><td>Sequestro</td><td>Baço cresce + Hb despenca</td><td>Cristaloide + transfusão <b>5 mL/kg</b>; esplenectomia (PCDT: após o 1º)</td></tr>
<tr><td>Aplástica</td><td><b>Reticulócitos baixos</b> · parvovírus B19</td><td>Suporte; hemácias fenotipadas</td></tr>
<tr><td>AVC</td><td>Déficit focal</td><td><b>Exsanguineotransfusão</b> (HbS &lt; 30%, Hb ≤ 10)</td></tr>
<tr><td>Priapismo</td><td>Sem melhora em 2 h</td><td>Internar · &gt; 4 h: urologia</td></tr></table>
<div class="dest"><b>Penicilina 3 meses–5 anos</b> (125 → 250 mg 12/12 h ou benzatina 50.000 UI/kg) · vacinas · <b>Doppler 2–16 anos</b>: ≥ 200 cm/s → transfusão crônica · <b>hidroxiureia</b> (2024): <b>a partir de 9 meses</b> na SS/Sβ⁰, mesmo sem sintomas; 15 → 35 mg/kg/dia · TCTH com irmão HLA é a cura.</div>'''),
  ('Talassemias', 'microcitose por falta de cadeia de globina', '''
<div class="cols c2"><div><b>β-menor:</b> Hb &gt; 10, hemácias e RDW normais, VCM muito baixo, <b>HbA2 &gt; 3,6–4%</b>. <b>β-maior (Cooley):</b> sintomas do 3º mês, Hb &lt; 7, deformidades de face/crânio → transfusão (Hb pré 9,5–10,5) + <b>quelação de ferro</b>.</div>
<div><b>α:</b> 1 gene = silencioso · 2 = traço · 3 = <b>doença da HbH</b> · 4 = <b>Hb Bart → hidropsia fetal</b>.</div></div>'''),
  ('Membrana, enzimas e adquiridas', '', '''
<div class="cols c2"><div class="cx"><b class="t">ESFEROCITOSE</b>Anemia + icterícia + esplenomegalia + litíase precoce · <b>CHCM &gt; 34</b>, <b>Coombs –</b>, EMA ou fragilidade osmótica · esplenectomia <b>conforme a gravidade</b> (grave: 4–6 anos), vacina antipneumocócica antes.</div>
<div class="cx"><b class="t">G6PD</b>Ligada ao X · hemólise 24–72 h após <b>infecção, fava, primaquina, dapsona, sulfa, rasburicase</b> · dosar <b>fora da crise</b> · pesquisar antes da primaquina (malária vivax).</div>
<div class="cx"><b class="t">AHAI QUENTE × FRIA</b>Quente: <b>IgG</b>, esferócitos → <b>prednisona 1 mg/kg</b>, rituximabe. Fria: <b>IgM/C3</b>, Mycoplasma, EBV, linfoma → evitar frio; corticoide não funciona.</div>
<div class="cx"><b class="t">HPN</b>Hemólise + <b>trombose atípica</b> (Budd-Chiari) + falência medular · citometria <b>CD55/CD59</b> · eculizumabe.</div></div>'''),
 ],
 lado_tit=NC, lado_sub=NS,
 lado=['**Toda febre na DF é emergência:** antibiótico parenteral sem esperar exames.',
       '**Crise aplástica ≠ sequestro:** aplástica tem reticulócitos baixos; sequestro tem baço grande.',
       '**Não transfunda** crise dolorosa não complicada: anemia crônica sozinha não indica.',
       '**Hiper-hidratação** na crise dolorosa pode precipitar STA.',
       '**STA começa como crise dolorosa:** reavalie o tórax todo dia.',
       '**Leucocitose na DF** nem sempre é infecção.',
       '**Baço palpável no adulto com DF:** pense em SC ou S/β-talassemia.',
       '**Esferócitos em dois lugares:** Coombs – = esferocitose; Coombs + = AHAI.',
       '**Microcitose com ferritina normal:** pense em talassemia, não dê ferro.',
       '**G6PD normal na crise** não exclui: repita fora da hemólise.',
       '**Hiper-hemólise** pós-transfusão: não transfundir; corticoide e imunoglobulina.',
       '**SHU típica:** antibiótico na fase diarreica se associa a mais SHU.',
       '**PTT:** troca plasmática sem esperar o ADAMTS13; evite plaquetas.',
       '**CIVD** tem TP/TTPa alargados e fibrinogênio baixo; PTT/SHU não.'],
 conta_tit='Contas e números',
 conta_html='<b>Índice reticulocítico</b> = ret % × (Ht ÷ 45) ÷ fator (≈ 2 com Ht 25%): &lt; 2 produção · &gt; 2,5–3 hemólise<br><b>ADAMTS13</b> &lt; 10% = PTT · <b>HbS &lt; 30%</b> na transfusão crônica<br><b>Doppler</b> &lt; 170 anual · 170–199 encurta · ≥ 200 transfusão',
 fontes='Elaborado pela MedSum com base no resumo da SP 2.3 (MS: PCDT da doença falciforme e atualização de 2024; Tratado de Pediatria SBP; Harrison).'))

# ---------------- SP 2.4 ----------------
render('6º sem D2 · NCS · SP 2.4 · Linfomas e leucemias agudas - resumo em 1 folha', dict(
 titulo='Leucemias e Linfomas', css='body{font-size:7.95pt}.sec{margin-bottom:3.8mm}',
 sub='Leucemias agudas, emergências onco-hematológicas e linfomas em uma página',
 mais=['**LPA**: CIVD, emergência hemorrágica', '**Neutropenia febril**: antibiótico já', '**Linfonodo suspeito** → biópsia excisional', '**Hodgkin × não Hodgkin**'],
 secoes=[
  ('Leucemia aguda: diagnosticar', 'falência medular + infiltração', '''
<div class="cols c2"><div><b>Medula:</b> anemia, <b>plaquetopenia</b>, neutropenia (febre). <b>Infiltração:</b> dor óssea (criança com LLA), visceromegalia, hipertrofia gengival (monocítica), massa mediastinal (LLA-T), SNC e testículo.</div>
<div><b>LMA ≥ 20% de blastos</b> (qualquer % com t(15;17), t(8;21), inv(16)) · LLA pediátrica ≥ 25%. <b>Imunofenotipagem</b> separa LMA × LLA. Leucemia = 28% dos cânceres infantis (LLA 75–80%).</div></div>
<table><tr><th></th><th>LLA</th><th>LMA</th></tr>
<tr><td>Quem</td><td><b>Criança, pico 2–5 anos</b></td><td><b>Adulto</b> (80% das agudas), mediana 67 anos</td></tr>
<tr><td>Marcadores</td><td>TdT+; B: CD19, CD10, CD22 · T: CD3, CD7</td><td>MPO, CD13, CD33, CD117 · <b>bastonetes de Auer</b></td></tr>
<tr><td>Prognóstico</td><td>Bom: hiperdiploidia, t(12;21), <b>DRM negativa</b> · Ruim: &gt; 50.000, hipodiploidia, <b>Ph+</b> (→ inibidor de tirosina-quinase)</td><td>ELN: favorável t(8;21), inv(16), NPM1 · adverso TP53, cariótipo complexo, −5/−7 (2022: FLT3-ITD = intermediário)</td></tr>
<tr><td>Tratar</td><td>Indução → consolidação → <b>profilaxia do SNC</b> → manutenção <b>6-MP + MTX</b> (2–2,5 anos). Criança &gt; 85%; adulto 20–30% (HyperCVAD)</td><td><b>"7 + 3"</b> (citarabina + antraciclina) → citarabina ou TCTH · idoso: <b>azacitidina</b></td></tr></table>
<div class="dest"><b>LPA</b> t(15;17) PML-RARA: <b>CIVD</b>, risco de hemorragia intracraniana. Risco baixo: <b>ATRA + trióxido de arsênio</b>; alto: + antraciclina. <b>Síndrome de diferenciação</b> (3 primeiras semanas) → glicocorticoide. Cura ~85%.</div>'''),
  ('Emergências', '', '''
<div class="cols c3"><div class="cx"><b class="t">LISE TUMORAL</b>Burkitt, LLA, LDH &gt; 1.500 · 12–72 h após QT · ↑ ác. úrico, K, P · ↓ Ca · <b>hidratação 3 L/m²/dia</b> + alopurinol ou <b>rasburicase</b> (não na G6PD).</div>
<div class="cx"><b class="t">LEUCOSTASE</b>Blastos &gt; 100.000 + pulmão/neuro (mais na LMA) · QT logo, <b>hidroxiureia</b> · <b>evite transfundir hemácias</b> · pseudo-hipoxemia.</div>
<div class="cx"><b class="t">NEUTROPENIA FEBRIL</b><b>≥ 38,5 °C</b> ou 3 × ≥ 38 °C em 24 h + neutrófilos <b>&lt; 500</b> → culturas + <b>cefepima/pip-tazo</b> sem esperar · fungos se febre 4–7 dias.</div></div>'''),
  ('Linfomas', 'biópsia excisional · Ann Arbor / Lugano', '''
<div class="dest"><b>Linfonodo suspeito:</b> &gt; 2 cm, indolor, <b>supraclavicular</b>, &gt; 4–6 semanas, sintomas B, &gt; 40 anos · US: arredondado, <b>sem hilo</b>, vasos periféricos → <b>biópsia excisional</b> (PAAF e core não bastam). Evite corticoide antes.</div>
<table><tr><th></th><th>Hodgkin</th><th>Não Hodgkin</th></tr>
<tr><td>Célula</td><td><b>Reed-Sternberg CD30+ CD15+</b>, CD45−</td><td>B em ~90%</td></tr>
<tr><td>Quem</td><td>Bimodal · EBV, HIV · esclerose nodular (70–80%, mediastino)</td><td>Aumenta com a idade · HIV, EBV, HTLV-1, H. pylori</td></tr>
<tr><td>Disseminação</td><td><b>Contígua</b>, supradiafragmática</td><td><b>Não contígua</b>, extranodal</td></tr>
<tr><td>Tratar</td><td><b>ABVD</b> ± RT · BEACOPP esc. (alto risco &lt; 60) · cura ~75% (PCDT)</td><td>LDGCB: <b>R-CHOP</b> (cura 60–65%)</td></tr></table>
<div class="cols c2"><div><b>LNH:</b> LDGCB 30–40% · folicular <b>t(14;18)</b> (transforma ~3%/ano) · Burkitt <b>t(8;14)</b>, "céu estrelado", lise espontânea · manto <b>t(11;14)</b> · MALT gástrico → <b>erradicar H. pylori</b>.</div>
<div><b>Ann Arbor:</b> I uma cadeia · II ≥ 2 mesmo lado · III dois lados · IV extranodal disseminado · <b>B</b>: febre &gt; 38 °C, sudorese, perda &gt; 10% em 6 meses · <b>X</b> ≥ 10 cm.</div></div>'''),
 ],
 lado_tit=NC, lado_sub=NS,
 lado=['**Aguda × crônica:** aguda bloqueia a maturação (blastos); crônica acumula células maduras.',
       '**Leucemia × linfoma:** medula × tecido linfoide; LLA e linfoma linfoblástico são a mesma doença.',
       '**Imunofenotipagem** é o exame que separa LMA de LLA.',
       '**Bastonete de Auer** torna a LMA praticamente certa.',
       '**Sangramento + fibrinogênio baixo** na leucemia: pense em LPA.',
       '**Corticoide antes do mielograma** mascara a LLA.',
       '**Dor óssea + citopenias** na criança: LLA, não artrite.',
       '**Rasburicase** é proibida na deficiência de G6PD.',
       '**Lise tumoral é rara na LMA**; típica de Burkitt e LLA.',
       '**Neutropenia febril:** sem neutrófilo não há pus; a febre pode ser o único sinal.',
       '**Supraclavicular esquerdo** (Virchow) = abdome; direito = tórax.',
       '**Mediastino anterior:** os 4 Ts (timoma, teratoma, tireoide, "terríveis" linfomas).',
       '**Linfoma pode trazer AHAI** e plaquetopenia imune: peça provas de hemólise.',
       '**Hodgkin tardio:** hipotireoidismo (~50% após RT cervical), mama, coração, bleomicina no pulmão.'],
 conta_tit='Escores',
 conta_html='<b>IPI</b> (1 ponto cada): idade &gt; 60 · <b>LDH ↑</b> · ECOG ≥ 2 · estádio III–IV · &gt; 1 extranodal → 0–1: 73% · 2: 51% · 3: 43% · 4–5: 26% (sobrevida 5 anos)<br><b>IPS</b> (Hodgkin avançado, 7 fatores): homem, &gt; 45 anos, estádio IV, albumina &lt; 4, Hb &lt; 10,5, leucócitos &gt; 15.000, linfócitos &lt; 600',
 fontes='Elaborado pela MedSum com base no resumo da SP 2.4 (MS: PCDT do linfoma de Hodgkin; OMS 2022; ELN; Tratado de Pediatria SBP; Harrison).'))
