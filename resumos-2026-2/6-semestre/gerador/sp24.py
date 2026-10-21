import sys, os, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from builder import Resumo, paginas_dos_titulos
from fluxo import render

AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(AQUI, 'saida'); os.makedirs(SAIDA, exist_ok=True)
MOLDE = os.path.join(AQUI, '..', 'fontes', 'dm_completo.docx')
NOME = '6º sem D2 · NCS · SP 2.4 · Linfomas e leucemias agudas (rascunho 2026.2)'

F1 = render('FLUXOGRAMA · SUSPEITA DE LEUCEMIA AGUDA', 'Citopenias e <span>blastos</span>: o caminho do diagnóstico', [
    ('row', [('s', 'Suspeita clínica', 'Palidez, febre, sangramento, dor óssea, hepatoesplenomegalia, linfonodos')]),
    ('arrow', 'hemograma + esfregaço'),
    ('row', [('n', 'Hemograma', 'Anemia, plaquetopenia, leucócitos baixos, normais ou muito altos; **blastos** no sangue periférico')]),
    ('arrow', 'urgente no mesmo dia'),
    ('row', [('d', 'Emergências primeiro', 'Coagulograma e fibrinogênio (CIVD), ácido úrico, K, P, Ca, creatinina (lise), leucometria (leucostase), febre (neutropenia febril)')]),
    ('arrow', 'mielograma ± biópsia de medula'),
    ('row', [('n', 'Confirma e classifica', 'Morfologia (≥ 20% de blastos) · **imunofenotipagem** por citometria de fluxo · citogenética e biologia molecular')]),
    ('arrow', ['linhagem mieloide', 'linhagem linfoide']),
    ('row', [('r', 'LMA', 'MPO+, CD13, CD33, CD117; bastonetes de Auer'), ('r', 'LLA', 'TdT+, B: CD19, CD10, CD22, CD79a · T: CD3, CD7')]),
    ('arrow', ['promielócitos + CIVD?', 'Ph+ (BCR::ABL1)?']),
    ('row', [('d', 'LPA: iniciar ATRA já', 'Na suspeita, sem esperar o PML::RARA'), ('d', 'LLA Ph+', 'Associar inibidor de tirosina-quinase')]),
], os.path.join(SAIDA, 'sp24_fluxo_leucemia.png'))

F2 = render('FLUXOGRAMA · LINFONODOMEGALIA', 'Quando o linfonodo <span>preocupa</span> e precisa de biópsia', [
    ('row', [('s', 'Linfonodo aumentado', 'História (infecção recente, sintomas B, idade, exposições) e exame de todas as cadeias + fígado e baço')]),
    ('arrow', ['localizada, com causa aparente', 'sem causa aparente']),
    ('row', [('n', 'Provável reacional', 'Doloroso, móvel, fibroelástico, após infecção → tratar a causa e reavaliar em 3–4 semanas'),
             ('d', 'Sinais de alarme', '> 2 cm, endurecido, aderido, indolor, **supraclavicular**, generalizado, > 4–6 semanas, sintomas B, idade > 40 anos, citopenias')]),
    ('arrow', ['persistiu ou cresceu', 'investigar']),
    ('row', [('n', 'Reavaliar', 'Hemograma, sorologias (HIV, EBV, toxoplasmose, sífilis), PPD/IGRA, imagem'),
             ('r', 'Biópsia excisional', 'Linfonodo inteiro para histologia + imuno-histoquímica · a punção aspirativa (PAAF) **não** classifica linfoma')]),
    ('arrow', ['', 'confirmado linfoma']),
    ('row', [('n', ' ', 'Reed-Sternberg CD15+/CD30+ → Hodgkin · demais → não Hodgkin (B ou T)'),
             ('r', 'Estadiar', 'PET-CT, LDH, hemograma, função renal e hepática, HIV, HBV, HCV, eco antes de antraciclina')]),
], os.path.join(SAIDA, 'sp24_fluxo_linfonodo.png'))

R = Resumo(MOLDE)
R.capa('Linfomas e Leucemias Agudas',
       'Leucemia linfoblástica e mieloide aguda, emergências oncológicas, linfoma de Hodgkin e não Hodgkin',
       '6º semestre · D2 · NCS · SP 2.4 · OMS 2022, ICC 2022, ELN 2022, Lugano, INCA e Harrison',
       ['Fundamentos das Neoplasias Hematológicas', 'Leucemias Agudas', 'Emergências Onco-hematológicas',
        'Linfadenopatia e Linfoma de Hodgkin', 'Linfomas Não Hodgkin'],
       'Medicina · 2026.2')

# ===== Cap 1
R.faixa('Fundamentos das Neoplasias Hematológicas', 'HEMATOPOESE, CLASSIFICAÇÃO E EPIDEMIOLOGIA')
R.h(3, 'Neoplasias hematológicas')
R.h(4, 'Da célula-tronco às neoplasias')
R.p('Todas as células do sangue nascem da **célula-tronco hematopoética** na medula óssea, que se divide em duas '
    'grandes linhagens: **mieloide** (hemácias, plaquetas, granulócitos e monócitos) e **linfoide** (linfócitos B, T e '
    'NK). Uma neoplasia hematológica surge quando uma célula dessas linhagens acumula alterações genéticas e passa a '
    'proliferar sem controle.')
R.tabela('Leucemia × linfoma: onde está a doença',
         ['', 'Leucemia', 'Linfoma'],
         [['Onde começa', '**Medula óssea**, com células neoplásicas no sangue', '**Tecido linfoide** (linfonodos, baço, MALT)'],
          ['Apresentação típica', 'Citopenias (anemia, plaquetopenia, neutropenia) e células anormais no sangue', 'Linfonodomegalia, massa, sintomas B'],
          ['Diagnóstico', 'Mielograma/biópsia de medula + imunofenotipagem', '**Biópsia do linfonodo** (histologia + imuno-histoquímica)'],
          ['Sobreposição', 'LLA e linfoma linfoblástico são a mesma doença em locais diferentes (> 25% de blastos na medula = leucemia)', '']],
         [2000, 4000, 3900], 'Adaptado de: OMS 2022 (refs. 1 e 2); Harrison (ref. 12).')
R.h(4, 'Aguda × crônica')
R.bullets(['**Aguda:** bloqueio da maturação. A medula se enche de **blastos** (células imaturas) que não funcionam; '
           'evolução em **dias a semanas**, fatal sem tratamento, mas potencialmente curável.',
           '**Crônica:** a célula amadurece, porém se acumula; evolução em **meses a anos** (LMC, LLC).'])
R.h(4, 'Classificação')
R.p('Hoje as neoplasias hematológicas são classificadas pela **OMS 2022 (5ª edição)** e pela **Classificação de '
    'Consenso Internacional (ICC 2022)**, que juntam morfologia, imunofenótipo, citogenética e biologia molecular. A '
    'antiga classificação FAB (M0 a M7, L1 a L3) só aparece por tradição.')
R.tabela('Classificações atuais: OMS 2022 × ICC 2022 (LMA)',
         ['Tema', 'OMS 2022 (5ª ed.)', 'ICC 2022'],
         [['Blastos para LMA em geral', '≥ 20%', '≥ 20%'],
          ['LMA com alteração genética definidora (ex.: PML::RARA, RUNX1::RUNX1T1, CBFB::MYH11, NPM1)', '**Qualquer percentual** de blastos (exceto BCR::ABL1 e CEBPA, que exigem ≥ 20%)', '**≥ 10%** de blastos'],
          ['Faixa de 10 a 19% de blastos', 'Síndrome mielodisplásica com excesso de blastos', 'Nova categoria **SMD/LMA**']],
         [3300, 3300, 3300], 'Fontes: Khoury et al., OMS 2022 (ref. 1); Arber et al., ICC 2022 (ref. 3).', quadro=True)
R.h(4, 'Epidemiologia no Brasil')
R.bullets(['A **leucemia é o câncer mais comum da infância** (cerca de um terço dos casos), e a maioria é **LLA**.',
           'Nos adultos predomina a **LMA**, com mediana de idade perto dos 70 anos.',
           'O INCA inclui as leucemias e os linfomas não Hodgkin entre os cânceres mais incidentes do país; o linfoma de '
           'Hodgkin é menos frequente e acomete principalmente adolescentes e adultos jovens.'])
R.h(4, 'Fatores de risco')
R.tabela('Fatores de risco para leucemias e linfomas',
         ['Fator', 'Associação'],
         [['Radiação ionizante, benzeno, quimioterapia prévia (alquilantes, inibidores de topoisomerase)', 'LMA (relacionada à terapia), LLA'],
          ['Síndromes genéticas: **Down**, Fanconi, Li-Fraumeni, ataxia-telangiectasia', 'LLA e LMA (Down: risco 10 a 20 vezes maior)'],
          ['Doenças hematológicas prévias: SMD, neoplasias mieloproliferativas', 'LMA secundária'],
          ['**EBV**', 'Linfoma de Hodgkin, Burkitt endêmico, linfomas em imunossuprimidos'],
          ['**HIV** e imunossupressão (transplante)', 'LNH agressivos (Burkitt, difuso de grandes células B, primário do SNC)'],
          ['**HTLV-1**', 'Leucemia/linfoma de células T do adulto'],
          ['**H. pylori**', 'Linfoma MALT gástrico'],
          ['Hepatite C, doenças autoimunes (Sjögren, tireoidite de Hashimoto)', 'LNH (zona marginal, MALT)']],
         [5200, 4700], 'Adaptado de: Harrison (ref. 12); INCA (ref. 10).')

# ===== Cap 2
R.faixa('Leucemias Agudas', 'LLA, LMA E LEUCEMIA PROMIELOCÍTICA AGUDA')
R.h(3, 'Leucemias agudas: visão geral')
R.h(4, 'Quadro clínico')
R.p('Os sintomas vêm de duas fontes: a **falência da medula** (que não produz células normais) e a **infiltração** de '
    'órgãos pelos blastos. A história costuma ser curta, de **dias a poucas semanas**.')
R.tabela('Manifestações das leucemias agudas',
         ['Origem', 'Manifestação'],
         [['Anemia', 'Palidez, cansaço, dispneia, taquicardia'],
          ['Plaquetopenia', 'Petéquias, equimoses, gengivorragia, epistaxe'],
          ['Neutropenia', 'Febre e infecções de repetição ou graves'],
          ['Infiltração', '**Dor óssea** e recusa a andar (criança com LLA), hepatoesplenomegalia, linfonodomegalia, **hipertrofia gengival** e infiltração de pele (LMA monocítica), **massa mediastinal** (LLA-T), sistema nervoso central e testículo (LLA)'],
          ['Coagulopatia', 'Sangramento grave por **CIVD** (típico da leucemia promielocítica)']],
         [2300, 7600], 'Adaptado de: Harrison (ref. 12); INCA, diagnóstico precoce na criança (ref. 14).')
R.h(4, 'Diagnóstico')
R.bullets(['**Hemograma:** anemia normocítica, plaquetopenia; leucócitos baixos, normais ou muito altos. Blastos no '
           'esfregaço (às vezes ausentes: "leucemia aleucêmica").',
           '**Mielograma** (aspirado) ± biópsia de medula: **≥ 20% de blastos** define leucemia aguda (com as exceções '
           'genéticas da LMA; na LLA pediátrica os protocolos usam ≥ 25%).',
           '**Imunofenotipagem por citometria de fluxo:** define a linhagem (mieloide × linfoide B ou T). É **o exame '
           'que separa LMA de LLA**.',
           '**Citogenética e biologia molecular:** classificação e **prognóstico** (risco), e escolha de terapia-alvo.',
           '**Exames do dia 1:** coagulograma e fibrinogênio, ácido úrico, potássio, fósforo, cálcio, creatinina, LDH, '
           'função hepática, sorologias, tipagem sanguínea, radiografia de tórax e, na LLA, líquor.'])
R.figura(F1, 'Investigação da suspeita de leucemia aguda', 'Fluxograma MedSum elaborado a partir de Döhner et al., ELN 2022 (ref. 4) e Harrison (ref. 12).')
R.h(3, 'Leucemia linfoblástica aguda (LLA)')
R.h(4, 'Epidemiologia e quadro')
R.bullets(['**Câncer mais comum da infância**, com pico entre **2 e 5 anos**. Também ocorre em adultos, com pior prognóstico.',
           'Quadro típico: criança com palidez, febre, petéquias, **dor óssea ou claudicação**, hepatoesplenomegalia e '
           'linfonodos. A LLA-T aparece em adolescente com **massa mediastinal** (risco de síndrome da veia cava superior) '
           'e leucometria alta.',
           'Sinal de alerta na pediatria: **dor óssea que acorda a criança** ou artralgia com citopenias, que pode ser '
           'confundida com artrite idiopática juvenil (cuidado com corticoide antes do mielograma: mascara o diagnóstico).'])
R.h(4, 'Imunofenótipo e genética')
R.tabela('LLA: imunofenótipo e alterações genéticas com valor prognóstico',
         ['Item', 'Detalhe', 'Significado'],
         [['LLA-B (cerca de 85% na criança)', 'TdT+, CD19, CD10, CD22, CD79a', 'Mais comum'],
          ['LLA-T', 'TdT+, CD3 citoplasmático, CD7', 'Adolescente, massa mediastinal, leucometria alta'],
          ['Hiperdiploidia (> 50 cromossomos)', 'LLA-B da criança', '**Bom prognóstico**'],
          ['t(12;21) ETV6::RUNX1', 'LLA-B da criança', '**Bom prognóstico**'],
          ['t(9;22) BCR::ABL1 (cromossomo Philadelphia)', 'Até 25% dos adultos', 'Pior prognóstico, mas responde a **inibidores de tirosina-quinase** (imatinibe, dasatinibe, ponatinibe)'],
          ['Rearranjo de KMT2A (MLL)', 'Lactentes < 1 ano', '**Mau prognóstico**'],
          ['Hipodiploidia', 'Criança e adulto', 'Mau prognóstico']],
         [3000, 3100, 3800], 'Adaptado de: Inaba e Mullighan (ref. 11); OMS 2022 (ref. 2).')
R.h(4, 'Fatores prognósticos')
R.bullets(['**Favoráveis:** idade de **1 a 9 anos**, leucometria inicial **< 50.000/mm³**, LLA-B, alterações genéticas '
           'favoráveis e **doença residual mínima negativa** ao fim da indução (o fator mais forte hoje).',
           '**Desfavoráveis:** < 1 ano ou ≥ 10 anos, leucometria ≥ 50.000/mm³, infiltração do SNC, genética adversa e '
           'doença residual mínima positiva.'])
R.h(4, 'Tratamento')
R.p('O tratamento dura cerca de **2 a 3 anos** e segue protocolos por fases (no Brasil, protocolos do GBTLI e do '
    'BFM). A cura na infância passa de **85 a 90%** nos centros de referência.')
R.tabela('Fases do tratamento da LLA',
         ['Fase', 'Objetivo', 'Exemplos de fármacos'],
         [['**Indução**', 'Remissão completa (< 5% de blastos e hemograma recuperado)', 'Corticoide, vincristina, asparaginase, antraciclina'],
          ['**Consolidação / intensificação**', 'Eliminar a doença residual', 'Metotrexato em alta dose, ciclofosfamida, citarabina'],
          ['**Profilaxia do SNC**', 'Evitar recaída no sistema nervoso central (santuário)', '**Quimioterapia intratecal** (metotrexato) e metotrexato em alta dose'],
          ['**Manutenção**', 'Manter a remissão por 2 a 3 anos', '**6-mercaptopurina** oral diária + **metotrexato** semanal'],
          ['Situações especiais', 'Ph+, recaída, alto risco', 'Inibidor de tirosina-quinase, blinatumomabe, CAR-T, transplante alogênico']],
         [2400, 3600, 3900], 'Adaptado de: Inaba e Mullighan (ref. 11); Harrison (ref. 12).')
R.h(3, 'Leucemia mieloide aguda (LMA)')
R.h(4, 'Epidemiologia e quadro')
R.bullets(['**Leucemia aguda mais comum no adulto**, com incidência que aumenta com a idade.',
           'Pode ser **de novo**, **secundária** a SMD ou neoplasia mieloproliferativa, ou **relacionada à terapia** '
           '(quimioterapia/radioterapia prévias).',
           'Pistas: **hipertrofia gengival** e lesões de pele (leucemia cútis) nas formas monocíticas; **sarcoma '
           'mieloide** (massa de blastos fora da medula); **CIVD** na promielocítica.'])
R.h(4, 'Diagnóstico e risco')
R.bullets(['Blastos com **bastonetes de Auer** (inclusões em agulha, patognomônicos de linhagem mieloide) e '
           'mieloperoxidase positiva.',
           'Imunofenótipo: **CD13, CD33, CD117, CD34, MPO**.',
           'A **genética define o risco (ELN 2022)** e o tratamento.'])
R.tabela('Estratificação de risco genético da LMA (ELN 2022, simplificada)',
         ['Risco', 'Alterações'],
         [['**Favorável**', 't(8;21) RUNX1::RUNX1T1; inv(16) ou t(16;16) CBFB::MYH11; **NPM1 mutado** sem alteração adversa; mutação bZIP do CEBPA'],
          ['**Intermediário**', 'NPM1 mutado com FLT3-ITD; t(9;11); alterações não classificadas como favoráveis ou adversas'],
          ['**Adverso**', '**TP53 mutado**, **cariótipo complexo**, −5/del(5q), −7, −17/abn(17p), t(6;9), inv(3), BCR::ABL1, mutações de ASXL1, RUNX1 e genes de splicing']],
         [2000, 7900], 'Adaptado de: Döhner et al., ELN 2022 (ref. 4).')
R.h(4, 'Tratamento')
R.bullets(['**Paciente apto para quimioterapia intensiva:** indução **"7 + 3"** (citarabina por 7 dias + daunorrubicina '
           'ou idarrubicina por 3 dias), com acréscimo de terapia-alvo conforme a mutação (midostaurina se FLT3, '
           'gentuzumabe-ozogamicina em CBF).',
           '**Consolidação:** citarabina em altas doses (risco favorável) ou **transplante alogênico** de células-tronco '
           '(risco intermediário e adverso, se houver doador).',
           '**Idoso ou não apto:** agentes hipometilantes (**azacitidina**) + **venetoclax**, ou cuidados de suporte.',
           'Suporte em todos: transfusões, profilaxia e tratamento de infecções, prevenção de lise tumoral.'])
R.h(3, 'Leucemia promielocítica aguda (LPA)')
R.p('É um subtipo de LMA (antiga M3) definido pela **t(15;17)**, que forma o gene de fusão **PML::RARA**. Os '
    'promielócitos anormais liberam substâncias pró-coagulantes e fibrinolíticas, e o paciente chega com **CIVD e '
    'hiperfibrinólise**: sangramentos graves (incluindo hemorragia intracraniana) são a principal causa de morte '
    'precoce.')
R.bullets(['**É emergência:** iniciar o **ácido transretinoico (ATRA)** já na **suspeita** (promielócitos + coagulopatia), '
           'sem esperar a confirmação genética.',
           'Suporte agressivo da coagulação: plaquetas > 30.000 a 50.000/mm³, fibrinogênio > 100 a 150 mg/dL '
           '(crioprecipitado), plasma.',
           'Tratamento de baixo/intermediário risco: **ATRA + trióxido de arsênio** (sem quimioterapia); alto risco '
           '(leucócitos > 10.000/mm³): ATRA + quimioterapia (antraciclina) ou ATRA + arsênio + citorredução.',
           '**Síndrome de diferenciação:** febre, dispneia, infiltrado pulmonar, derrame pleural, ganho de peso, '
           'hipotensão e lesão renal → **dexametasona 10 mg EV de 12/12 h** e, se grave, suspensão temporária do ATRA.',
           'Com o tratamento atual, a LPA é a leucemia aguda de **maior chance de cura** (> 90%).'])
R.ponto_chave('Paciente com leucemia aguda + sangramento + **fibrinogênio baixo** e TP/TTPa alargados: pense em '
              '**LPA** e comece o **ATRA imediatamente**.')

# ===== Cap 3
R.faixa('Emergências Onco-hematológicas', 'LISE TUMORAL, LEUCOSTASE E NEUTROPENIA FEBRIL')
R.h(3, 'Síndrome de lise tumoral (SLT)')
R.p('A destruição rápida de muitas células tumorais (espontânea ou após a quimioterapia) libera **potássio, fósforo e '
    'ácidos nucleicos** (que viram ácido úrico). O fósforo se liga ao cálcio e causa hipocalcemia. Cristais de ácido '
    'úrico e de fosfato de cálcio lesam o rim.')
R.bullets(['**Maior risco:** linfoma de **Burkitt**, **LLA** e LMA com leucometria alta, tumores volumosos, LDH alta e '
           'doença renal prévia.'])
R.tabela('Critérios de Cairo-Bishop para síndrome de lise tumoral',
         ['Lise tumoral laboratorial (≥ 2 critérios, de 3 dias antes a 7 dias após a quimioterapia)', 'Lise tumoral clínica (laboratorial + ≥ 1)'],
         [['Ácido úrico ≥ 8 mg/dL', 'Creatinina ≥ 1,5 vez o limite superior'],
          ['Potássio ≥ 6 mEq/L', 'Arritmia cardíaca ou morte súbita'],
          ['Fósforo ≥ 4,5 mg/dL (adulto) ou ≥ 6,5 mg/dL (criança)', 'Convulsão'],
          ['Cálcio ≤ 7 mg/dL', ''],
          ['(ou variação de 25% em relação ao basal)', '']],
         [5700, 4200], 'Adaptado de: Cairo e Bishop (ref. 7).')
R.h(5, 'Prevenção e tratamento')
R.bullets(['**Hidratação vigorosa** (2 a 3 L/m²/dia), buscando bom débito urinário; não é mais recomendado alcalinizar a urina.',
           '**Alopurinol** (impede a formação de ácido úrico) no risco intermediário; **rasburicase** (degrada o ácido '
           'úrico já formado) no alto risco ou na SLT estabelecida — **contraindicada na deficiência de G6PD**.',
           'Tratar a hipercalemia (gluconato de cálcio, insulina com glicose, resinas), evitar repor cálcio na '
           'hipocalcemia assintomática (precipita fosfato de cálcio) e indicar **diálise** se refratária.'])
R.h(3, 'Hiperleucocitose e leucostase')
R.bullets(['**Hiperleucocitose:** leucócitos (blastos) > 100.000/mm³.',
           '**Leucostase:** blastos grandes e pouco deformáveis entopem a microcirculação → **insuficiência respiratória** '
           '(hipoxemia, infiltrado) e **sintomas neurológicos** (confusão, cefaleia, alteração visual, AVC). Mais comum na LMA.',
           'Conduta: iniciar a **quimioterapia** o quanto antes; **hidroxiureia** para citorredução; leucaférese em casos '
           'selecionados; prevenir lise tumoral.',
           '**Evite transfundir hemácias** sem necessidade (aumenta a viscosidade); plaquetas podem ser transfundidas.',
           'Cuidado: a gasometria pode mostrar **pseudo-hipoxemia** (os blastos consomem O₂ no tubo) e o potássio pode '
           'vir falsamente alto.'])
R.h(3, 'Neutropenia febril')
R.p('É a emergência mais comum do paciente em quimioterapia. **Sem neutrófilos não há pus nem sinais clássicos**: a '
    'febre pode ser o único sinal de uma infecção grave.')
R.tabela('Definição de neutropenia febril',
         ['Item', 'Critério'],
         [['Febre', 'Temperatura oral **≥ 38,3 °C** em uma medida **ou ≥ 38,0 °C** mantida por 1 hora'],
          ['Neutropenia', 'Neutrófilos **< 500/mm³** ou < 1.000/mm³ com previsão de queda para < 500/mm³ em 48 horas'],
          ['Neutropenia profunda', 'Neutrófilos < 100/mm³']],
         [2500, 7400], 'Adaptado de: IDSA 2010 (ref. 9); ASCO/IDSA 2018 (ref. 8).')
R.bullets(['**Antibiótico em até 60 minutos**, depois de colher **hemoculturas** (periférica e do cateter), sem esperar resultados.',
           'Escolha: **β-lactâmico com ação antipseudomonas** em monoterapia: **cefepima**, **piperacilina-tazobactam** ou '
           'carbapenêmico (meropenem) se risco de germe resistente.',
           'Acrescentar **vancomicina** se instabilidade hemodinâmica, infecção de cateter ou de pele, pneumonia, '
           'mucosite grave ou colonização por MRSA.',
           'Estratificar risco (escore **MASCC**: ≥ 21 = baixo risco, pode ser tratado por via oral/ambulatorial em casos '
           'selecionados).',
           'Febre persistente após 4 a 7 dias: investigar **fungos** (Aspergillus, Candida) e considerar antifúngico.',
           'Na criança, a mesma lógica: neutropenia febril é emergência e o antibiótico não espera.'])
R.ponto_chave('Na neutropenia febril, o tempo até o antibiótico salva vidas: **colha culturas e dê o β-lactâmico '
              'antipseudomonas na primeira hora**.')
R.h(3, 'Outras emergências')
R.bullets(['**CIVD:** LPA e LMA monocítica (ver capítulo anterior).',
           '**Síndrome da veia cava superior:** massa mediastinal (LLA-T, linfoma linfoblástico, linfoma primário do '
           'mediastino, Hodgkin): edema de face e membros superiores, circulação colateral, dispneia. Cuidado com '
           'sedação/anestesia (colapso de via aérea).',
           '**Compressão medular** e **hipercalcemia** (mais em linfomas e mieloma).'])

# ===== Cap 4
R.faixa('Linfadenopatia e Linfoma de Hodgkin', 'QUANDO BIOPSIAR, DIAGNÓSTICO E ESTADIAMENTO')
R.h(3, 'Abordagem da linfadenopatia')
R.p('A maioria das linfadenopatias é **reacional** (infecções), principalmente em crianças. O desafio é reconhecer '
    'quando o linfonodo é suspeito e precisa de **biópsia**.')
R.tabela('Linfonodo provavelmente benigno × suspeito',
         ['Característica', 'Provavelmente benigno', 'Suspeito de neoplasia'],
         [['Tamanho', '< 1 cm (< 1,5 cm inguinal)', '**> 2 cm**'],
          ['Consistência', 'Fibroelástico', '**Endurecido**, pétreo ou borrachoso'],
          ['Mobilidade', 'Móvel', '**Aderido** a planos profundos'],
          ['Dor', 'Doloroso (inflamação aguda)', '**Indolor**'],
          ['Local', 'Cervical anterior, após infecção de vias aéreas', '**Supraclavicular** (sempre suspeito), epitroclear, generalizado'],
          ['Tempo', 'Regride em 2 a 4 semanas', '**Persiste > 4 a 6 semanas** ou cresce'],
          ['Contexto', 'Criança, quadro infeccioso', 'Idade > 40 anos, **sintomas B**, citopenias, hepatoesplenomegalia']],
         [2200, 3600, 4100], 'Adaptado de: Harrison (ref. 12).')
R.bullets(['**Supraclavicular esquerdo** (nódulo de Virchow): neoplasia abdominal; **direito**: tórax (pulmão, esôfago, mediastino).',
           'Para diagnosticar linfoma, faça **biópsia excisional** (linfonodo inteiro): a arquitetura é essencial. A '
           '**PAAF não basta** para diagnosticar ou classificar linfoma.',
           'Evite corticoide antes da biópsia: pode reduzir o linfonodo e mascarar o diagnóstico.'])
R.figura(F2, 'Abordagem da linfonodomegalia', 'Fluxograma MedSum elaborado a partir de Harrison (ref. 12) e Cheson et al., Lugano (ref. 6).')
R.h(3, 'Linfoma de Hodgkin (LH)')
R.h(4, 'Definição e epidemiologia')
R.bullets(['Neoplasia de **linfócitos B** do centro germinativo em que poucas células malignas, as **células de '
           'Reed-Sternberg**, ficam cercadas por muitas células inflamatórias reacionais.',
           'Distribuição **bimodal**: pico em **adultos jovens (15 a 35 anos)** e outro após os 55 anos.',
           'Associação com **EBV** (sobretudo celularidade mista) e com HIV.'])
R.h(4, 'Classificação')
R.tabela('Subtipos do linfoma de Hodgkin',
         ['Subtipo', 'Características'],
         [['**LH clássico (cerca de 95%)**', 'Células de Reed-Sternberg **CD15+ e CD30+**, CD45−'],
          ['• Esclerose nodular', '**O mais comum**; mulheres jovens, **massa mediastinal**'],
          ['• Celularidade mista', 'Associado ao **EBV** e ao HIV; mais sintomas B e doença avançada'],
          ['• Rico em linfócitos', 'Bom prognóstico'],
          ['• Depleção linfocitária', 'Raro, idosos e HIV; pior prognóstico'],
          ['**LH predominância linfocitária nodular**', 'Células "em pipoca" **CD20+**, CD15− e CD30−; indolente (a OMS 2022 passou a chamá-lo também de linfoma B de predomínio linfocitário nodular)']],
         [3200, 6700], 'Adaptado de: OMS 2022 (ref. 2); Ansell (ref. 13).')
R.h(4, 'Quadro clínico')
R.bullets(['**Linfonodomegalia indolor**, geralmente **cervical ou supraclavicular**, que se espalha de forma **contígua** '
           '(de uma cadeia para a vizinha), o que torna o estadiamento previsível.',
           '**Massa mediastinal** (tosse, dispneia, síndrome da veia cava superior).',
           '**Sintomas B:** febre > 38 °C sem outra causa, **sudorese noturna** intensa e **perda de > 10% do peso em 6 meses**.',
           'Outros: **prurido** generalizado, **dor no linfonodo após ingerir álcool** (raro, mas típico), febre '
           'cíclica (Pel-Ebstein).'])
R.h(4, 'Estadiamento (Lugano / Ann Arbor modificado)')
R.tabela('Estadiamento de Lugano (Hodgkin e não Hodgkin)',
         ['Estádio', 'Definição'],
         [['**I**', 'Uma região linfonodal ou um único órgão extralinfático sem linfonodo (IE)'],
          ['**II**', '≥ 2 regiões linfonodais **do mesmo lado do diafragma** (± extensão extranodal contígua: IIE)'],
          ['**III**', 'Regiões linfonodais **dos dois lados do diafragma**, ou acima do diafragma + baço'],
          ['**IV**', 'Acometimento **extralinfático disseminado** (fígado, medula óssea, pulmão não contíguo)'],
          ['A / B', 'Ausência (A) ou presença (B) de sintomas B (mantidos no Hodgkin)'],
          ['Doença volumosa (bulky)', 'Massa ≥ 10 cm ou > 1/3 do diâmetro torácico (Hodgkin)']],
         [2600, 7300], 'Adaptado de: Cheson et al., classificação de Lugano (ref. 6).')
R.bullets(['Exames: **PET-CT** (estadiamento e resposta), hemograma, VHS, LDH, albumina, função renal e hepática, HIV, '
           'HBV e HCV. Com PET-CT, a biópsia de medula não é necessária no Hodgkin.',
           'Na prática, agrupa-se em **doença limitada** (I e II sem fatores desfavoráveis), **limitada desfavorável** '
           '(bulky, VHS alta, muitos sítios) e **avançada** (III e IV).'])
R.h(4, 'Tratamento e prognóstico')
R.bullets(['**ABVD** (doxorrubicina, bleomicina, vimblastina, dacarbazina) é o esquema base. Doença limitada: poucos ciclos '
           '± radioterapia de campo envolvido, guiados pelo PET interino. Avançada: ABVD, **brentuximabe-AVD** '
           '(anti-CD30) ou BEACOPP escalonado em centros selecionados.',
           'Recaída: quimioterapia de resgate + **transplante autólogo**; brentuximabe e **anti-PD-1** (nivolumabe, '
           'pembrolizumabe).',
           'Cura de **80 a 90%** no geral. Por isso importam os **efeitos tardios**: **toxicidade pulmonar da '
           'bleomicina**, **cardiotoxicidade das antraciclinas**, hipotireoidismo e **segunda neoplasia** (mama em '
           'mulheres irradiadas no tórax) após radioterapia.'])

# ===== Cap 5
R.faixa('Linfomas Não Hodgkin', 'INDOLENTES, AGRESSIVOS E MUITO AGRESSIVOS')
R.h(3, 'Linfomas não Hodgkin (LNH)')
R.h(4, 'Visão geral')
R.p('Os LNH são um grupo heterogêneo: cerca de **85 a 90% são de células B** e o restante de células T ou NK. Ao '
    'contrário do Hodgkin, espalham-se de forma **não contígua**, acometem mais **sítios extranodais** (trato '
    'gastrointestinal, pele, SNC, medula) e são mais comuns em idosos e imunossuprimidos.')
R.tabela('Comportamento dos LNH na prática',
         ['Grupo', 'Comportamento', 'Exemplos', 'Ideia do tratamento'],
         [['**Indolentes**', 'Evolução em anos; geralmente **incuráveis**, mas controláveis', 'Folicular, zona marginal/MALT, linfocítico (LLC)', 'Observação ("esperar e vigiar") se pouca doença; rituximabe ± quimioterapia quando sintomático'],
          ['**Agressivos**', 'Evolução em meses; **potencialmente curáveis**', 'Difuso de grandes células B, manto, T periféricos', 'Quimioimunoterapia (R-CHOP)'],
          ['**Muito agressivos**', 'Evolução em dias a semanas; curáveis com tratamento intensivo', 'Burkitt, linfoblástico', 'Protocolos intensivos + profilaxia do SNC e da lise tumoral']],
         [1800, 2600, 2700, 2800], 'Adaptado de: OMS 2022 (ref. 2); Harrison (ref. 12).')
R.h(4, 'Principais subtipos')
R.tabela('Principais linfomas não Hodgkin',
         ['Linfoma', 'Marcadores e genética', 'Clínica', 'Tratamento'],
         [['**Difuso de grandes células B (LDGCB)**', 'CD20+; subtipos de centro germinativo e de célula B ativada; "duplo hit" (MYC + BCL2) é mais agressivo', '**O LNH mais comum** (cerca de 30 a 40%); massa que cresce rápido, sintomas B, extranodal', '**R-CHOP** (rituximabe, ciclofosfamida, doxorrubicina, vincristina, prednisona) ou Pola-R-CHP; cura de 60 a 70%'],
          ['**Folicular**', 'CD20+, CD10+, **BCL2+; t(14;18)**', 'O indolente mais comum; linfonodomegalia generalizada indolor que oscila; pode transformar em LDGCB', 'Observação se pouca doença; rituximabe ± quimioterapia (bendamustina)'],
          ['**Burkitt**', 'CD20+, CD10+; **t(8;14) MYC**; Ki-67 ≈ 100%; padrão em **"céu estrelado"**', 'Endêmico (África, EBV, **mandíbula**); esporádico (**abdome**, região ileocecal); associado ao HIV; **lise tumoral espontânea**', 'Quimioterapia intensiva de curta duração + profilaxia do SNC; alta taxa de cura'],
          ['**Células do manto**', 'CD5+, **ciclina D1 (t(11;14))**', 'Homem idoso, doença disseminada, **polipose linfomatosa** do intestino', 'Quimioimunoterapia, inibidores de BTK (ibrutinibe), transplante autólogo'],
          ['**Zona marginal / MALT**', 'CD20+, CD5−, CD10−', 'Estômago (**H. pylori**), glândulas salivares (Sjögren), tireoide (Hashimoto)', 'MALT gástrico localizado H. pylori+: **erradicação da bactéria** (pode curar)'],
          ['**Linfoma linfocítico / LLC**', 'CD5+, CD23+', 'Idoso, linfocitose, linfonodos; "manchas de Gumprecht" no esfregaço', 'Observação ou terapia-alvo (BTK, venetoclax)'],
          ['**Linfomas T**', 'CD3+ (T periféricos, anaplásico ALK, micose fungoide)', 'Leucemia/linfoma T do adulto: **HTLV-1**, hipercalcemia, lesões de pele', 'Quimioterapia (CHOP ± brentuximabe nos CD30+); prognóstico pior que os B']],
         [2100, 2500, 2700, 2600], 'Adaptado de: OMS 2022 (ref. 2); Harrison (ref. 12).')
R.h(4, 'Diagnóstico e estadiamento')
R.bullets(['**Biópsia excisional** com imuno-histoquímica (e citogenética/FISH quando necessário).',
           '**PET-CT** nos linfomas ávidos por FDG (a maioria); tomografia nos não ávidos.',
           'Exames: hemograma, **LDH**, ácido úrico, função renal e hepática, **sorologias para HIV, hepatite B e C** (o '
           'rituximabe pode **reativar a hepatite B**: rastrear e fazer profilaxia), β2-microglobulina, ecocardiograma '
           'antes de antraciclina.',
           '**Biópsia de medula** em casos selecionados; **líquor** se alto risco de acometimento do SNC (Burkitt, '
           'linfoblástico, CNS-IPI alto, rim/suprarrenal/testículo).',
           'Estadiamento de **Lugano** (mesmo do Hodgkin; os sintomas B não entram na classificação do LNH, mas são descritos).'])
R.h(4, 'Prognóstico: IPI')
R.tabela('Índice Prognóstico Internacional (IPI) no LDGCB',
         ['Fator (1 ponto cada)', 'Interpretação'],
         [['Idade > 60 anos', '0–1 ponto: baixo risco'],
          ['**LDH** acima do normal', '2 pontos: risco intermediário-baixo'],
          ['Performance status (**ECOG**) ≥ 2', '3 pontos: risco intermediário-alto'],
          ['Estádio **III ou IV**', '4–5 pontos: alto risco'],
          ['> 1 sítio **extranodal**', '']],
         [4950, 4950], 'Adaptado de: Harrison (ref. 12). Mnemônico: "APLES" (Age, Performance, LDH, Extranodal, Stage).')
R.h(4, 'Hodgkin × não Hodgkin')
R.tabela('Diferenças entre linfoma de Hodgkin e não Hodgkin',
         ['Característica', 'Hodgkin', 'Não Hodgkin'],
         [['Célula característica', 'Reed-Sternberg (CD15+, CD30+)', 'Variável (B na maioria)'],
          ['Idade', 'Bimodal (jovens e > 55 anos)', 'Aumenta com a idade'],
          ['Disseminação', '**Contígua**', '**Não contígua**'],
          ['Extranodal', 'Raro', '**Frequente**'],
          ['Mediastino', 'Comum (esclerose nodular)', 'Menos comum (exceto linfoblástico e mediastinal primário)'],
          ['Prognóstico', 'Cura em 80 a 90%', 'Depende do subtipo']],
         [2600, 3600, 3700], 'Adaptado de: Harrison (ref. 12); Ansell (ref. 13).')
R.caso(['No caso da SP, comece pelo hemograma: **citopenias com blastos** apontam para leucemia aguda (mielograma e '
        'imunofenotipagem); **linfonodo suspeito** sem blastos aponta para linfoma (biópsia excisional).',
        'Antes de qualquer conduta, procure as **emergências**: febre com neutropenia, sangramento com fibrinogênio baixo '
        '(LPA), leucometria muito alta (leucostase) e eletrólitos alterados (lise tumoral).'])

R.caixa('Pontos-Chave', [
    '• Leucemia aguda = **≥ 20% de blastos** na medula (exceções genéticas na LMA); a **imunofenotipagem** separa LMA de LLA.',
    '• **LLA:** câncer mais comum da infância (pico 2–5 anos), dor óssea, profilaxia do SNC, manutenção com 6-MP + metotrexato; cura de 85–90%. Ph+ recebe inibidor de tirosina-quinase.',
    '• **LMA:** adulto, bastonetes de Auer, risco pela genética (ELN 2022); indução "7 + 3"; idosos: azacitidina + venetoclax.',
    '• **LPA:** t(15;17) PML::RARA, CIVD → **ATRA na suspeita**; ATRA + arsênio; síndrome de diferenciação → dexametasona.',
    '• **Lise tumoral:** ↑ ácido úrico, K e P, ↓ Ca; hidratação, alopurinol ou rasburicase (não usar na deficiência de G6PD).',
    '• **Neutropenia febril:** ≥ 38,3 °C ou ≥ 38,0 °C por 1 h + neutrófilos < 500 → **β-lactâmico antipseudomonas na 1ª hora**.',
    '• Linfonodo **supraclavicular**, endurecido, indolor, > 2 cm ou > 4–6 semanas → **biópsia excisional** (PAAF não basta).',
    '• **Hodgkin:** Reed-Sternberg CD15+/CD30+, bimodal, disseminação contígua, mediastino, sintomas B; ABVD; cura 80–90%.',
    '• **LNH:** LDGCB é o mais comum (R-CHOP); folicular t(14;18); Burkitt t(8;14) e "céu estrelado"; manto t(11;14); MALT gástrico e H. pylori. Estadiamento de Lugano e IPI.'])
R.referencias([
    'Khoury JD, Solary E, Abla O, et al. The 5th edition of the World Health Organization Classification of Haematolymphoid Tumours: myeloid and histiocytic/dendritic neoplasms. Leukemia. 2022;36(7):1703-1719.',
    'Alaggio R, Amador C, Anagnostopoulos I, et al. The 5th edition of the World Health Organization Classification of Haematolymphoid Tumours: lymphoid neoplasms. Leukemia. 2022;36(7):1720-1748.',
    'Arber DA, Orazi A, Hasserjian RP, et al. International Consensus Classification of myeloid neoplasms and acute leukemias: integrating morphologic, clinical, and genomic data. Blood. 2022;140(11):1200-1228.',
    'Döhner H, Wei AH, Appelbaum FR, et al. Diagnosis and management of AML in adults: 2022 recommendations from an international expert panel on behalf of the ELN. Blood. 2022;140(12):1345-1377.',
    'Sanz MA, Fenaux P, Tallman MS, et al. Management of acute promyelocytic leukemia: updated recommendations from an expert panel of the European LeukemiaNet. Blood. 2019;133(15):1630-1643.',
    'Cheson BD, Fisher RI, Barrington SF, et al. Recommendations for initial evaluation, staging, and response assessment of Hodgkin and non-Hodgkin lymphoma: the Lugano classification. J Clin Oncol. 2014;32(27):3059-3068.',
    'Cairo MS, Bishop M. Tumour lysis syndrome: new therapeutic strategies and classification. Br J Haematol. 2004;127(1):3-11.',
    'Taplitz RA, Kennedy EB, Bow EJ, et al. Outpatient management of fever and neutropenia in adults treated for malignancy: American Society of Clinical Oncology and Infectious Diseases Society of America clinical practice guideline update. J Clin Oncol. 2018;36(14):1443-1453.',
    'Freifeld AG, Bow EJ, Sepkowitz KA, et al. Clinical practice guideline for the use of antimicrobial agents in neutropenic patients with cancer: 2010 update by the Infectious Diseases Society of America. Clin Infect Dis. 2011;52(4):e56-e93.',
    'Instituto Nacional de Câncer (Brasil). Estimativa 2023: incidência de câncer no Brasil. Rio de Janeiro: INCA; 2022.',
    'Inaba H, Mullighan CG. Pediatric acute lymphoblastic leukemia. Haematologica. 2020;105(11):2524-2539.',
    'Loscalzo J, Fauci AS, Kasper DL, Hauser SL, Longo DL, Jameson JL, editors. Harrison\'s principles of internal medicine. 21st ed. New York: McGraw Hill; 2022.',
    'Ansell SM. Hodgkin lymphoma: 2023 update on diagnosis, risk-stratification, and management. Am J Hematol. 2022;97(11):1478-1488.',
    'Instituto Nacional de Câncer (Brasil). Diagnóstico precoce do câncer na criança e no adolescente. 2. ed. Rio de Janeiro: INCA; 2014.'])

docx1 = os.path.join(SAIDA, NOME + '.docx')
n = sum(1 for k, _ in R.headings if k in (3, 4))
R.sumario(eval(os.environ['PG']) if os.environ.get('PG') else [1] * n)
R.salvar(docx1)
subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', SAIDA, docx1], capture_output=True)
if not os.environ.get('PG'):
    pg = paginas_dos_titulos(docx1[:-5] + '.pdf', R.headings)
    print('paginas', pg)
    subprocess.run([sys.executable, __file__], env=dict(os.environ, PG=repr(pg)), check=True)
