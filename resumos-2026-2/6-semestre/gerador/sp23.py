import sys, os, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from builder import Resumo, paginas_dos_titulos
from fluxo import render

AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(AQUI, 'saida'); os.makedirs(SAIDA, exist_ok=True)
MOLDE = os.path.join(AQUI, '..', 'fontes', 'dm_completo.docx')
NOME = '6º sem D2 · NCS · SP 2.3 · Doença falciforme e anemias hemolíticas (rascunho 2026.2)'

# ---------------- fluxogramas ----------------
F1 = render('FLUXOGRAMA · INVESTIGAÇÃO DA HEMÓLISE', 'Anemia com <span>reticulócitos altos</span>: é hemólise?', [
    ('row', [('s', 'Anemia + reticulocitose', 'Afaste sangramento agudo e resposta a reposição (ferro, B12, folato)')]),
    ('arrow', 'confirme a hemólise'),
    ('row', [('n', 'Marcadores', '↑ LDH · ↑ bilirrubina indireta · ↓ haptoglobina · esfregaço de sangue periférico')]),
    ('arrow', 'Coombs direto (TAD)'),
    ('row', [('d', 'TAD positivo', 'Hemólise imune'), ('d', 'TAD negativo', 'Olhe o esfregaço e a história')]),
    ('arrow', ['IgG ± C3', 'C3d (IgM)', 'esquizócitos', 'esferócitos', 'drepanócitos', 'Heinz / mordidas']),
    ('row', [('r', 'AHAI quente', 'LES, LLC, linfoma, fármacos'), ('r', 'Crioaglutininas', 'Mycoplasma, EBV, linfoma'),
             ('r', 'MAT', 'PTT, SHU, CIVD, prótese'), ('r', 'Esferocitose', 'CHCM ↑, família, EMA'),
             ('r', 'Doença falciforme', 'Eletroforese / HPLC'), ('r', 'Def. de G6PD', 'gatilho oxidante')]),
    ('arrow', 'esfregaço sem pistas'),
    ('row', [('n', 'Pense também', 'Talassemia (microcitose com ferro normal) · HPN (citometria CD55/CD59) · infecções (malária, Clostridium) · hemólise mecânica')]),
], os.path.join(SAIDA, 'sp23_fluxo_hemolise.png'))

F2 = render('FLUXOGRAMA · PRONTO-ATENDIMENTO NA DOENÇA FALCIFORME', 'Chegou com <span>dor ou febre</span>: o que não pode passar', [
    ('row', [('s', 'Paciente com doença falciforme', 'Sinais vitais, SatO₂, Hb e reticulócitos comparados ao basal, exame do baço')]),
    ('arrow', ['febre', 'dor', 'palidez súbita', 'déficit neurológico']),
    ('row', [('d', 'Febre', 'Emergência: hemocultura + ceftriaxona sem esperar exames'),
             ('d', 'Crise dolorosa', 'Analgesia em até 1 h, reavaliar a cada 15–30 min'),
             ('d', 'Queda de Hb', 'Baço grande → sequestro · reticulócitos baixos → aplásica'),
             ('d', 'AVC', 'Imagem urgente + exsanguineotransfusão')]),
    ('arrow', ['dor torácica / infiltrado?', 'piora respiratória?', 'instabilidade?', '']),
    ('row', [('r', 'Síndrome torácica aguda', 'Infiltrado novo + febre, dor torácica, taquipneia ou hipoxemia → antibiótico (ceftriaxona + macrolídeo), O₂, analgesia, espirometria de incentivo, transfusão')]),
], os.path.join(SAIDA, 'sp23_fluxo_pa.png'))

# ---------------- documento ----------------
R = Resumo(MOLDE)
R.capa('Doença Falciforme e Anemias Hemolíticas',
       'Hemólise, hemoglobinopatias, membranopatias, enzimopatias e anemias hemolíticas adquiridas',
       '6º semestre · D2 · NCS · SP 2.3 · Ministério da Saúde (manual de condutas e PCDT da doença falciforme), ASH, TIF e Harrison',
       ['Fundamentos da Hemólise', 'Doença Falciforme', 'Talassemias', 'Membranopatias e Enzimopatias',
        'Anemias Hemolíticas Adquiridas'],
       'Medicina · 2026.2')

# ===== Capítulo 1
R.faixa('Fundamentos da Hemólise', 'DEFINIÇÃO, CLASSIFICAÇÃO E LABORATÓRIO')
R.h(3, 'Anemia hemolítica')
R.h(4, 'Definição')
R.p('A hemácia normal vive cerca de **120 dias** e é retirada da circulação pelos macrófagos do baço e do fígado. '
    'A **anemia hemolítica** acontece quando a hemácia é destruída **antes do tempo** e a medula óssea, mesmo '
    'aumentando a produção (até 6 a 8 vezes), não consegue compensar a perda.')
R.p('Por isso, a marca laboratorial da hemólise é a combinação de **anemia com reticulocitose**: a medula está '
    'respondendo, mas as hemácias somem da circulação. Se a hemólise é leve, a medula compensa e o paciente pode ter '
    '**hemólise compensada**, sem anemia.')
R.h(4, 'Classificação')
R.p('A forma mais útil de pensar é perguntar **onde está o defeito**: na própria hemácia (**intrínseco**, quase sempre '
    'hereditário) ou fora dela (**extrínseco**, quase sempre adquirido).')
R.tabela('Classificação das anemias hemolíticas',
         ['Grupo', 'Defeito', 'Exemplos'],
         [['Hereditárias (intrínsecas)', 'Hemoglobina (hemoglobinopatias)', 'Doença falciforme, talassemias, HbC'],
          ['', 'Membrana (membranopatias)', 'Esferocitose e eliptocitose hereditárias'],
          ['', 'Enzimas (enzimopatias)', 'Deficiência de G6PD, deficiência de piruvato-quinase'],
          ['Adquiridas (extrínsecas)', 'Imunes', 'AHAI quente, doença das crioaglutininas, induzida por fármacos, reação transfusional, doença hemolítica do recém-nascido'],
          ['', 'Microangiopáticas e mecânicas', 'PTT, SHU, CIVD, prótese valvar, hipertensão maligna'],
          ['', 'Infecções e agentes', 'Malária, Clostridium, babesiose, venenos, queimaduras'],
          ['Adquirida intrínseca (exceção)', 'Membrana sem proteínas ancoradas por GPI', 'Hemoglobinúria paroxística noturna (HPN)']],
         [2600, 3200, 4100], 'Adaptado de: Harrison, cap. de anemias hemolíticas (ref. 6); Hoffbrand (ref. 13).')
R.h(4, 'Hemólise intravascular × extravascular')
R.p('A maior parte das hemólises é **extravascular**: o macrófago do baço "come" a hemácia alterada. Na hemólise '
    '**intravascular**, a hemácia se rompe dentro do vaso e a hemoglobina livre cai no plasma e na urina.')
R.tabela('Diferenças entre hemólise intravascular e extravascular',
         ['Característica', 'Intravascular', 'Extravascular'],
         [['Local', 'Dentro dos vasos', 'Macrófagos do baço e do fígado'],
          ['Exemplos', 'G6PD na crise, PTT/SHU, HPN, reação transfusional ABO, malária grave, prótese valvar', 'Esferocitose, AHAI quente, doença falciforme, talassemias'],
          ['LDH', '**Muito** elevada', 'Elevada'],
          ['Haptoglobina', 'Indetectável', 'Baixa'],
          ['Urina', '**Hemoglobinúria** (urina escura, "cor de Coca-Cola") e hemossiderinúria', 'Urobilinogênio aumentado, sem hemoglobina'],
          ['Baço', 'Geralmente normal', '**Esplenomegalia** frequente'],
          ['Esfregaço', 'Esquizócitos (MAT), células mordidas (G6PD)', 'Esferócitos, drepanócitos, células em alvo']],
         [2300, 3800, 3800], 'Adaptado de: Harrison (ref. 6); Hoffbrand (ref. 13).')
R.h(4, 'Laboratório da hemólise')
R.bullets([
    '**Reticulócitos aumentados:** mostram resposta medular. Corrija pelo hematócrito: o **índice de produção '
    'reticulocitária (IPR)** = reticulócitos (%) × (Ht do paciente ÷ 45) ÷ fator de maturação (1,0; 1,5; 2,0 e 2,5 '
    'para Ht de 45, 35, 25 e 15%). **IPR > 2** = medula respondendo (hemólise ou sangramento).',
    '**LDH aumentada:** enzima liberada da hemácia rompida.',
    '**Bilirrubina indireta aumentada:** o heme vira bilirrubina não conjugada; icterícia sem colúria (acolúrica).',
    '**Haptoglobina baixa:** ela se liga à hemoglobina livre e é retirada da circulação.',
    '**Esfregaço de sangue periférico:** o exame que mais orienta a causa (Tabela 4).',
    '**Teste da antiglobulina direto (Coombs direto, TAD):** detecta anticorpo ou complemento na superfície da '
    'hemácia. **Positivo = hemólise imune.**'])
R.ponto_chave('Anemia + **reticulócitos altos** + **LDH alta** + **bilirrubina indireta alta** + **haptoglobina baixa** = '
              'hemólise. O próximo passo é sempre o **Coombs direto** e o **esfregaço**.')
R.tabela('Achados do esfregaço e o que sugerem',
         ['Achado', 'Sugere'],
         [['Esferócitos', 'Esferocitose hereditária, AHAI quente'],
          ['Esquizócitos (fragmentos)', 'Microangiopatia trombótica (PTT, SHU, CIVD), prótese valvar'],
          ['Drepanócitos (hemácias em foice)', 'Doença falciforme'],
          ['Células em alvo', 'Talassemias, hemoglobina C, hepatopatia, pós-esplenectomia'],
          ['Corpos de Heinz e células "mordidas"', 'Deficiência de G6PD (estresse oxidativo)'],
          ['Aglutinação das hemácias', 'Doença das crioaglutininas'],
          ['Corpúsculos de Howell-Jolly', 'Asplenia (anatômica ou funcional, como na doença falciforme)'],
          ['Eliptócitos', 'Eliptocitose hereditária']],
         [3800, 6100], 'Adaptado de: Hoffbrand (ref. 13).')
R.figura(F1, 'Investigação da anemia hemolítica', 'Fluxograma MedSum elaborado a partir de Harrison (ref. 6) e Jäger et al. (ref. 7).')

# ===== Capítulo 2
R.faixa('Doença Falciforme', 'GENÉTICA, FISIOPATOLOGIA, CRISES E SEGUIMENTO')
R.h(3, 'Doença falciforme')
R.h(4, 'Definição e genética')
R.p('**Doença falciforme (DF)** é o nome do grupo de doenças hereditárias em que predomina a **hemoglobina S (HbS)**. '
    'A HbS nasce de uma **mutação pontual no gene da β-globina** (cromossomo 11): troca do **ácido glutâmico por '
    'valina na posição 6**. A herança é **autossômica recessiva**.')
R.tabela('Genótipos da doença falciforme e do traço',
         ['Genótipo', 'O que é', 'Gravidade'],
         [['HbSS', '**Anemia falciforme**: herdou HbS do pai e da mãe', 'A forma mais comum e mais grave'],
          ['HbS/β⁰-talassemia', 'HbS + gene que não produz β', 'Grave, semelhante à SS (com microcitose)'],
          ['HbSC', 'HbS + hemoglobina C', 'Moderada; mais retinopatia e necrose óssea'],
          ['HbS/β⁺-talassemia', 'HbS + gene que produz pouca β', 'Mais leve'],
          ['HbAS', '**Traço falciforme**: um gene normal e um S', 'Não é doença; em geral assintomático']],
         [2300, 4300, 3300], 'Adaptado de: Brasil. MS, Doença falciforme: condutas básicas (ref. 1).')
R.h(4, 'Epidemiologia e triagem neonatal')
R.p('A DF é a **doença genética mais prevalente no Brasil**, com maior frequência na população negra e parda e '
    'nos estados com maior ascendência africana (a Bahia lidera). O Ministério da Saúde estima o nascimento de '
    'cerca de 3 mil crianças com DF e de 200 mil com traço falciforme por ano.')
R.p('O diagnóstico precoce é feito no **teste do pezinho** (Programa Nacional de Triagem Neonatal), que inclui as '
    'hemoglobinopatias. O laudo mostra as hemoglobinas em ordem de quantidade:')
R.bullets(['**FA:** normal (F = fetal, que predomina no recém-nascido).',
           '**FAS:** traço falciforme.',
           '**FS:** doença falciforme (SS ou S/β⁰-talassemia).',
           '**FSC:** hemoglobinopatia SC.',
           'O resultado alterado é **confirmado** com nova amostra (eletroforese/HPLC) e a criança entra no '
           'acompanhamento em centro de referência **antes dos 3 meses de vida**, quando começa a profilaxia.'])
R.h(4, 'Fisiopatologia')
R.p('Quando perde oxigênio, a HbS **polimeriza** e deforma a hemácia em **foice**. A hemácia falcizada fica rígida, '
    'adere ao endotélio e vive só 10 a 20 dias. Daí saem dois grandes mecanismos de doença:')
R.tabela('Os dois mecanismos da doença falciforme',
         ['Mecanismo', 'Como acontece', 'Manifestações típicas'],
         [['**Vaso-oclusão**', 'Hemácias rígidas + adesão ao endotélio + inflamação entopem a microcirculação → isquemia e infarto', 'Crise dolorosa, dactilite, síndrome torácica aguda, sequestro esplênico, autoesplenectomia, necrose avascular, AVC'],
          ['**Hemólise**', 'Hemoglobina livre consome o óxido nítrico → vasoconstrição e lesão endotelial', 'Anemia crônica, icterícia, litíase biliar, hipertensão pulmonar, priapismo, úlceras de perna']],
         [1900, 4000, 4000], 'Adaptado de: Harrison (ref. 6); NHLBI 2014 (ref. 3).')
R.bullets(['**Pioram a falcização:** hipóxia, desidratação, acidose, febre/infecção, frio, estresse e esforço intenso.',
           '**Protege:** a **hemoglobina fetal (HbF)**. Por isso os sintomas começam por volta dos **6 meses**, quando a '
           'HbF cai, e a **hidroxiureia** funciona (aumenta a HbF).',
           '**Asplenia funcional precoce:** infartos repetidos destroem o baço nos primeiros anos. A criança fica '
           'vulnerável a **germes encapsulados** (pneumococo, Haemophilus, meningococo) e a **Salmonella** (osteomielite).'])
R.ponto_chave('A infecção grave (sepse pneumocócica) é a principal causa de morte em crianças pequenas com DF. '
              '**Toda febre é emergência** e a **penicilina profilática** + vacinas mudaram essa história.')
R.h(4, 'Manifestações clínicas')
R.bullets(['**Anemia hemolítica crônica:** Hb basal em geral de 6 a 9 g/dL na SS, normocítica, com reticulocitose; '
           'icterícia e **litíase biliar** (cálculos de bilirrubinato).',
           '**Dactilite (síndrome mão-pé):** edema doloroso de mãos e pés em lactentes de 6 meses a 2 anos; muitas vezes '
           'é a **primeira manifestação**.',
           '**Crises dolorosas (vaso-oclusivas):** a manifestação mais frequente; ossos longos, coluna, tórax e abdome.',
           '**Esplenomegalia** no lactente, que some com a autoesplenectomia (na SC o baço pode persistir).',
           '**Rim:** hipostenúria (enurese, desidratação fácil), hematúria, albuminúria e doença renal crônica.',
           '**Osso:** necrose avascular da cabeça do fêmur e do úmero, osteomielite.',
           '**Olho:** retinopatia proliferativa (mais na SC).',
           '**Pele:** úlceras maleolares. **Pulmão:** hipertensão pulmonar. **Pênis:** priapismo.',
           '**Crescimento:** baixo peso, atraso puberal.'])
R.h(4, 'Diagnóstico')
R.bullets(['**Triagem neonatal** (teste do pezinho) e confirmação por **eletroforese de hemoglobina** ou **HPLC**.',
           '**Hemograma:** anemia normocítica (microcitose sugere S/β-talassemia ou ferropenia associada), '
           'reticulocitose, leucocitose e plaquetose discretas.',
           '**Esfregaço:** drepanócitos, células em alvo, corpúsculos de Howell-Jolly (asplenia).',
           'Teste de falcização e solubilidade **não** distinguem traço de doença: o diagnóstico é pela eletroforese/HPLC.'])
R.h(4, 'Complicações agudas')
R.tabela('Complicações agudas da doença falciforme e conduta inicial',
         ['Complicação', 'Como reconhecer', 'Conduta'],
         [['**Febre / infecção**', 'Febre em criança com DF; risco de sepse fulminante por pneumococo', 'Avaliação imediata, hemograma, hemocultura, **ceftriaxona** empírica sem esperar exames; internar se toxemia, < 1 ano ou sinais de gravidade'],
          ['**Crise dolorosa**', 'Dor óssea/abdominal sem outra causa', 'Analgesia rápida e escalonada (ver abaixo), hidratação sem excesso, aquecimento'],
          ['**Síndrome torácica aguda (STA)**', '**Infiltrado pulmonar novo** + febre, dor torácica, tosse, taquipneia ou hipoxemia', 'Ceftriaxona + macrolídeo, O₂ se SatO₂ < 95%, analgesia, espirometria de incentivo, **transfusão** (simples ou exsanguineotransfusão se grave)'],
          ['**Sequestro esplênico agudo**', 'Crianças pequenas: **baço aumenta de repente** + Hb cai ≥ 2 g/dL do basal; risco de choque', 'Volume e **transfusão em pequenas alíquotas** (o baço devolve sangue); ensinar a família a palpar o baço'],
          ['**Crise aplástica**', 'Queda de Hb com **reticulócitos baixos**; causa típica: **parvovírus B19**', 'Transfusão; isolar de gestantes e imunossuprimidos'],
          ['**AVC isquêmico**', 'Déficit focal, convulsão, cefaleia intensa (pico na infância)', 'Imagem urgente e **exsanguineotransfusão** (meta HbS < 30%)'],
          ['**Priapismo**', 'Ereção dolorosa e prolongada', '> 4 h é emergência: analgesia, hidratação e urologia (aspiração/irrigação com fenilefrina)'],
          ['**Colecistite / colangite**', 'Dor em hipocôndrio direito, febre, icterícia que piora', 'Antibiótico e colecistectomia']],
         [2300, 3500, 4100], 'Adaptado de: Brasil. MS, condutas básicas (ref. 1); NHLBI 2014 (ref. 3); ASH 2020 (refs. 4 e 5).')
R.figura(F2, 'Pronto-atendimento na doença falciforme', 'Fluxograma MedSum elaborado a partir de MS (ref. 1) e NHLBI (ref. 3).')
R.h(5, 'Crise dolorosa: tratamento')
R.bullets(['**Rapidez:** analgesia em até **60 minutos** da chegada e reavaliação a cada 15 a 30 minutos.',
           '**Dor leve a moderada:** dipirona ou paracetamol + anti-inflamatório (atenção à função renal).',
           '**Dor intensa:** **opioide** (morfina) em doses programadas ou por bomba de analgesia controlada pelo paciente.',
           '**Hidratação:** oral ou venosa de manutenção; **evite hiper-hidratação** (risco de STA e edema pulmonar).',
           '**Espirometria de incentivo** para prevenir STA em dor torácica ou abdominal.',
           'O₂ apenas se hipoxemia. **Não transfunda** crise dolorosa não complicada.'])
R.ponto_chave('A STA é a principal causa de morte em adultos com DF e muitas vezes começa como uma crise dolorosa '
              'comum. Reavalie o tórax todos os dias de internação.')
R.h(4, 'Seguimento e prevenção')
R.tabela('Cuidados de rotina na doença falciforme',
         ['Medida', 'Como fazer'],
         [['**Penicilina profilática**', 'Dos **3 meses aos 5 anos**: penicilina V oral 125 mg 12/12 h até 3 anos e 250 mg 12/12 h dos 3 aos 5 anos, **ou** penicilina benzatina 50.000 UI/kg IM a cada 21 dias. Alergia: eritromicina'],
          ['**Vacinas**', 'Calendário completo + especiais no CRIE: pneumocócicas (conjugada e polissacarídica 23-valente), meningocócicas, Haemophilus, influenza anual e hepatite B'],
          ['**Ácido fólico**', 'Recomendado na rotina pelo manual do MS (hemólise crônica aumenta a demanda)'],
          ['**Doppler transcraniano**', 'Anual dos **2 aos 16 anos** (SS e S/β⁰). Velocidade **≥ 200 cm/s** = alto risco de AVC → programa de transfusão crônica'],
          ['**Hidroxiureia**', 'Aumenta a HbF: reduz crises, STA, internações, transfusões e mortalidade (ver Quadro 1)'],
          ['**Orientação à família**', 'Hidratação, evitar frio e esforço extremo, procurar o serviço na febre, palpar o baço'],
          ['**Rastreios**', 'Retina (fundo de olho), urina (albuminúria), ecocardiograma, avaliação de quadril e vesícula conforme a idade']],
         [2600, 7300], 'Adaptado de: Brasil. MS, condutas básicas (ref. 1) e PCDT da doença falciforme (ref. 2); ASH 2020 (ref. 5).')
R.tabela('Hidroxiureia: referência brasileira × internacional',
         ['Tema', 'Referência brasileira (prevalece)', 'Referência internacional'],
         [['Quando iniciar', 'PCDT do MS: crianças **a partir de 2 anos** e adultos que preencham critérios clínicos (crises frequentes, STA, AVC/Doppler alterado, anemia grave, entre outros)', 'NHLBI 2014/ASH: **oferecer a partir dos 9 meses** a todos com SS e S/β⁰, mesmo sem sintomas'],
          ['Monitorização', 'Hemograma periódico (risco de mielossupressão); ajuste de dose pela contagem de neutrófilos', 'Igual; titulação até a dose máxima tolerada'],
          ['Cuidados', 'Contracepção eficaz (teratogênica)', 'Igual']],
         [2000, 4100, 3800], 'Fontes: Brasil. MS, PCDT da doença falciforme (ref. 2); NHLBI 2014 (ref. 3). Na prova brasileira, siga o PCDT.', quadro=True)
R.h(5, 'Transfusão e terapias que mudam a doença')
R.bullets(['**Transfusão:** indicada em STA, AVC, sequestro esplênico, crise aplástica e no preparo cirúrgico. Em '
           'transfusão crônica, a meta é **HbS < 30%**. Evite Hb > 10 a 11 g/dL (hiperviscosidade).',
           'Use hemácias com **fenotipagem estendida** (menos aloimunização) e trate a **sobrecarga de ferro** com '
           'quelantes (deferasirox, deferoxamina).',
           '**Transplante de células-tronco hematopoéticas** (doador aparentado compatível): única terapia curativa '
           'disponível no SUS hoje.',
           'Outras: L-glutamina e crizanlizumabe (anti-P-selectina) em outros países; **terapias gênicas** aprovadas no '
           'exterior desde 2023. O voxelotor foi retirado do mercado em 2024 por segurança.'])
R.h(4, 'Traço falciforme')
R.p('O portador do traço (HbAS) tem cerca de 40% de HbS e **não tem anemia nem crises**. Merece **aconselhamento '
    'genético** (dois portadores têm 25% de chance de filho com DF por gestação). Raramente pode ter hematúria, '
    'hipostenúria e rabdomiólise em esforço extremo com desidratação.')
R.caso(['Ao ler o caso da SP, procure as pistas que separam as complicações: **febre** (infecção até prova em contrário), '
        '**baço** (sequestro), **reticulócitos** (aplásica × hemólise), **tórax** (STA) e **déficit focal** (AVC).',
        'Pergunte sempre: qual o genótipo, qual a Hb basal, está em uso de hidroxiureia e penicilina, vacinas em dia, '
        'quando foi o último Doppler.'])

# ===== Capítulo 3
R.faixa('Talassemias', 'DESEQUILÍBRIO DAS CADEIAS DE GLOBINA')
R.h(3, 'Talassemias')
R.h(4, 'Definição e fisiopatologia')
R.p('As talassemias são doenças hereditárias com **redução ou ausência da síntese** de uma das cadeias da globina. '
    'A cadeia que sobra em excesso precipita dentro do eritroblasto e da hemácia, causando **eritropoese ineficaz** '
    '(morte na medula) e **hemólise**. O resultado é uma anemia **microcítica e hipocrômica**.')
R.bullets(['**β-talassemia:** menos cadeia β (gene no cromossomo 11). Mais comum em descendentes de italianos, gregos e '
           'outros povos do Mediterrâneo, muito presentes no Sudeste do Brasil.',
           '**α-talassemia:** menos cadeia α (4 genes, 2 em cada cromossomo 16). Mais comum em descendentes de africanos '
           'e asiáticos.'])
R.h(4, 'β-talassemia')
R.tabela('Formas clínicas da β-talassemia',
         ['Forma', 'Genética', 'Quadro'],
         [['**Menor (traço)**', 'Um gene alterado (β/β⁰ ou β/β⁺)', 'Assintomática; Hb normal ou pouco baixa; **VCM muito baixo** com hemácias normais ou aumentadas; **HbA2 > 3,5%**'],
          ['**Intermédia**', 'Dois genes alterados, forma mais leve', 'Anemia moderada, transfusão ocasional; sobrecarga de ferro pela absorção intestinal aumentada'],
          ['**Maior (anemia de Cooley)**', 'β⁰/β⁰ ou β⁰/β⁺ grave', 'Sintomas a partir de **6 a 24 meses**: anemia grave, hepatoesplenomegalia, deformidades ósseas (fácies típica, crânio "em escova"), atraso de crescimento; **dependente de transfusão**']],
         [2300, 3200, 4400], 'Adaptado de: TIF 2021 (ref. 9); Hoffbrand (ref. 13).')
R.h(5, 'Tratamento da β-talassemia maior')
R.bullets(['**Transfusões regulares** a cada 2 a 5 semanas, mantendo Hb pré-transfusional de **9 a 10,5 g/dL**: '
           'corrige a anemia e freia a eritropoese ineficaz (e as deformidades ósseas).',
           '**Quelação de ferro** (deferasirox, deferiprona, deferoxamina): a sobrecarga de ferro lesa coração, fígado e '
           'glândulas e é a principal causa de morte.',
           '**Ácido fólico**; esplenectomia em casos selecionados (hiperesplenismo).',
           '**Transplante de células-tronco hematopoéticas:** curativo. Novas opções: luspatercepte e terapia gênica.'])
R.h(4, 'α-talassemia')
R.tabela('Formas da α-talassemia conforme o número de genes perdidos',
         ['Genes α perdidos', 'Nome', 'Quadro'],
         [['1 de 4', 'Portador silencioso', 'Sem alterações'],
          ['2 de 4', 'Traço α-talassêmico', 'Microcitose leve, sem anemia ou com anemia leve; eletroforese do adulto normal (diagnóstico molecular ou por exclusão)'],
          ['3 de 4', '**Doença da hemoglobina H** (β4)', 'Anemia hemolítica moderada, esplenomegalia, corpos de inclusão de HbH'],
          ['4 de 4', '**Hb Bart (γ4)**', '**Hidropsia fetal**: incompatível com a vida sem transfusão intrauterina']],
         [2000, 3000, 4900], 'Adaptado de: Harrison (ref. 6); Hoffbrand (ref. 13).')
R.h(4, 'Traço talassêmico × anemia ferropriva')
R.p('As duas causam **microcitose**, e a confusão leva a tratar com ferro quem não precisa (e pode sobrecarregar). '
    'O **índice de Mentzer** (VCM ÷ número de hemácias em milhões/µL) ajuda na triagem.')
R.tabela('Como diferenciar traço talassêmico de anemia ferropriva',
         ['Exame', 'Anemia ferropriva', 'Traço β-talassêmico'],
         [['Hemácias (milhões/µL)', 'Baixas', '**Normais ou aumentadas**'],
          ['VCM', 'Baixo', 'Muito baixo para o grau de anemia'],
          ['RDW', '**Aumentado**', 'Normal'],
          ['Índice de Mentzer', '> 13', '**< 13**'],
          ['Ferritina', '**Baixa**', 'Normal'],
          ['Eletroforese', 'Normal (HbA2 pode cair)', '**HbA2 > 3,5%**']],
         [2600, 3600, 3700], 'Adaptado de: Hoffbrand (ref. 13). Se houver ferropenia associada, corrija o ferro e repita a HbA2.')
R.ponto_chave('Microcitose com **ferritina normal** e hemácias normais ou altas: pense em **traço talassêmico** e peça '
              'eletroforese de hemoglobina antes de prescrever ferro.')

# ===== Capítulo 4
R.faixa('Membranopatias e Enzimopatias', 'ESFEROCITOSE HEREDITÁRIA E DEFICIÊNCIA DE G6PD')
R.h(3, 'Esferocitose hereditária')
R.h(4, 'Definição e fisiopatologia')
R.p('É a anemia hemolítica hereditária por defeito de membrana mais comum. Defeitos nas proteínas que prendem a '
    'membrana ao citoesqueleto (**anquirina**, **espectrina**, banda 3, proteína 4.2) fazem a hemácia perder '
    'membrana e virar **esferócito**: pequeno, redondo, rígido e retido no **baço**. A herança é **autossômica '
    'dominante** em cerca de 75% dos casos (história familiar positiva).')
R.h(4, 'Quadro clínico e diagnóstico')
R.bullets(['Tríade: **anemia, icterícia e esplenomegalia**; **litíase biliar precoce** (até em crianças).',
           'Pode ter **crise aplástica** (parvovírus B19) e crises hemolíticas com infecções.',
           'Laboratório: esferócitos no esfregaço, **CHCM aumentado (> 36 g/dL)**, reticulocitose, **Coombs direto '
           'negativo** (diferencia da AHAI, que também tem esferócitos).',
           'Confirmação: **teste de ligação da eosina-5-maleimida (EMA)** por citometria de fluxo (o mais usado hoje) '
           'ou fragilidade osmótica aumentada.'])
R.h(4, 'Tratamento')
R.bullets(['**Ácido fólico** nas formas moderadas e graves.',
           '**Esplenectomia** (total ou parcial) nas formas moderadas a graves, de preferência **após os 6 anos**: corrige a '
           'anemia, mas não o defeito.',
           'Antes da esplenectomia: **vacinas** contra pneumococo, meningococo e Haemophilus (pelo menos 2 semanas antes).',
           '**Colecistectomia** se litíase sintomática (pode ser feita no mesmo tempo).'])
R.h(4, 'Eliptocitose hereditária')
R.p('Defeito na espectrina com hemácias elípticas. A maioria é assintomática; formas graves (piropoiquilocitose) se '
    'comportam como esferocitose.')
R.h(3, 'Deficiência de G6PD')
R.h(4, 'Definição e fisiopatologia')
R.p('É a **enzimopatia eritrocitária mais comum do mundo**. A glicose-6-fosfato desidrogenase gera o **NADPH**, que '
    'mantém a **glutationa reduzida** e protege a hemácia contra oxidação. Sem ela, um **estresse oxidativo** '
    'desnatura a hemoglobina, que precipita em **corpos de Heinz**; o baço "morde" a hemácia (**células mordidas**) e '
    'há **hemólise aguda, principalmente intravascular**. A herança é **ligada ao X** (afeta sobretudo meninos e homens).')
R.h(4, 'Gatilhos')
R.tabela('Gatilhos de hemólise na deficiência de G6PD',
         ['Grupo', 'Exemplos'],
         [['Infecções', 'O gatilho mais comum (pneumonia, hepatite viral, gastroenterite)'],
          ['Alimentos', '**Fava** (favismo)'],
          ['Fármacos', '**Primaquina** e tafenoquina, **dapsona**, sulfametoxazol, nitrofurantoína, **rasburicase**, azul de metileno, quinolonas (algumas)'],
          ['Outros', 'Naftalina (bolinhas de naftalina), cetoacidose diabética']],
         [2300, 7600], 'Adaptado de: Luzzatto et al. (ref. 11).')
R.h(4, 'Quadro clínico, diagnóstico e tratamento')
R.bullets(['**Hemólise aguda 24 a 72 h após o gatilho:** palidez, icterícia, **urina escura** (hemoglobinúria), dor lombar.',
           'No recém-nascido: **icterícia neonatal** que pode ser grave (kernicterus).',
           'Esfregaço: corpos de Heinz (coloração supravital) e células mordidas. Coombs negativo.',
           '**Dosagem quantitativa da G6PD:** pode vir **falsamente normal na crise** (os reticulócitos novos têm mais '
           'enzima). Repita **2 a 3 meses** depois.',
           'Tratamento: **suspender o gatilho**, hidratação (proteção renal) e transfusão se anemia grave. A prevenção é '
           'orientar a lista de fármacos e alimentos a evitar.',
           'No Brasil, a deficiência importa no tratamento da **malária por P. vivax**: a primaquina pode causar '
           'hemólise grave em deficientes.'])
R.h(4, 'Deficiência de piruvato-quinase')
R.p('Enzimopatia da via glicolítica, **autossômica recessiva**, com hemólise **extravascular crônica** e '
    'esplenomegalia. Tratamento de suporte, esplenectomia nos graves e, mais recentemente, o ativador mitapivate.')

# ===== Capítulo 5
R.faixa('Anemias Hemolíticas Adquiridas', 'IMUNES, MICROANGIOPÁTICAS E HPN')
R.h(3, 'Anemia hemolítica autoimune (AHAI)')
R.h(4, 'Definição e classificação')
R.p('Na AHAI o paciente produz **autoanticorpos contra as próprias hemácias**. O **Coombs direto positivo** é o '
    'achado central. A classificação depende da temperatura em que o anticorpo age melhor.')
R.tabela('AHAI quente × doença das crioaglutininas',
         ['Característica', 'AHAI quente', 'Doença das crioaglutininas (fria)'],
         [['Frequência', '**Mais comum** (cerca de 70 a 80%)', 'Menos comum'],
          ['Anticorpo', '**IgG**, age a 37 °C', '**IgM**, age no frio (< 37 °C) e fixa complemento'],
          ['Coombs direto', 'IgG (± C3)', '**C3d**'],
          ['Onde destrói', 'Baço (extravascular)', 'Fígado (extravascular) e intravascular pelo complemento'],
          ['Esfregaço', '**Esferócitos**', '**Aglutinação** das hemácias'],
          ['Causas secundárias', 'LES e outras autoimunes, **LLC**, linfomas, imunodeficiências, fármacos', '**Mycoplasma pneumoniae**, **EBV** (mononucleose), linfomas e doença linfoproliferativa'],
          ['Quadro', 'Anemia, icterícia, esplenomegalia', 'Piora no frio: **acrocianose**, fenômeno de Raynaud, urina escura'],
          ['Tratamento', '**Prednisona 1 mg/kg/dia**; 2ª linha: **rituximabe**; depois esplenectomia ou imunossupressores', 'Evitar o frio, aquecer soros e hemoderivados; corticoide funciona pouco; **rituximabe**; sutimlimabe (anti-C1s)']],
         [2200, 3800, 3900], 'Adaptado de: Jäger et al., consenso internacional de AHAI (ref. 7).')
R.bullets(['Na AHAI quente, a resposta ao corticoide ocorre em 70 a 85% dos casos; reduza a dose devagar após a Hb '
           'estabilizar. Associe **ácido fólico** e considere **profilaxia de trombose** (a AHAI ativa é trombogênica).',
           'A prova cruzada é difícil (autoanticorpo reage com todas as bolsas), mas **não se nega transfusão** a quem tem '
           'anemia grave e sintomática.',
           '**Induzida por fármacos:** ceftriaxona, piperacilina, metildopa, entre outros. Suspenda o fármaco.'])
R.ponto_chave('Esferócitos aparecem na **esferocitose** e na **AHAI quente**. Quem separa é o **Coombs direto**: '
              'negativo na esferocitose, positivo na AHAI.')
R.h(3, 'Hemoglobinúria paroxística noturna (HPN)')
R.p('Doença **adquirida** da célula-tronco: uma mutação no gene **PIGA** impede a formação da âncora GPI. As células '
    'perdem as proteínas que as protegem do complemento (**CD55 e CD59**) e são destruídas por ele (hemólise '
    '**intravascular**).')
R.bullets(['Tríade: **hemólise** (urina escura, classicamente pela manhã), **trombose em locais atípicos** (veias '
           'hepáticas — síndrome de Budd-Chiari —, mesentéricas e cerebrais) e **falência medular** (associação com '
           'anemia aplásica).',
           'Diagnóstico: **citometria de fluxo** mostrando ausência de CD55/CD59 (e FLAER) em hemácias e granulócitos.',
           'Tratamento: **inibidores do complemento C5** (eculizumabe, ravulizumabe), com **vacina meningocócica** antes '
           '(risco de Neisseria); anticoagulação se trombose; transplante nos casos com falência medular.'])
R.h(3, 'Anemias hemolíticas microangiopáticas')
R.p('Microangiopatia trombótica (MAT) = **anemia hemolítica com esquizócitos** + **plaquetopenia** ± lesão de órgão. '
    'Pequenos trombos na microcirculação fragmentam as hemácias. Coombs negativo.')
R.tabela('Principais microangiopatias trombóticas',
         ['Doença', 'Mecanismo', 'Pistas', 'Conduta'],
         [['**PTT** (púrpura trombocitopênica trombótica)', 'Deficiência de **ADAMTS13** (< 10%), quase sempre por autoanticorpo', 'Adulto, plaquetas muito baixas, alterações neurológicas; febre e rim menos marcantes', '**Emergência: troca plasmática** + corticoide; caplacizumabe e rituximabe. Evitar transfusão de plaquetas'],
          ['**SHU típica**', 'Toxina **Shiga** (E. coli O157:H7)', 'Criança, **diarreia sanguinolenta** 5 a 10 dias antes, **lesão renal aguda**', 'Suporte, diálise se necessário; **antibiótico não é indicado**'],
          ['**SHU atípica**', 'Desregulação do **complemento**', 'Sem diarreia, recidivas, história familiar', 'Inibidor de C5 (eculizumabe)'],
          ['**CIVD**', 'Consumo de fatores e plaquetas (sepse, trauma, câncer, obstetrícia)', '**TP e TTPa alargados, fibrinogênio baixo, D-dímero alto** (na PTT/SHU a coagulação é normal)', 'Tratar a causa; repor hemoderivados se sangramento']],
         [2100, 2500, 2700, 2600], 'Adaptado de: Zheng et al., ISTH 2020 (ref. 8); Harrison (ref. 6).')
R.ponto_chave('Anemia com esquizócitos + plaquetopenia + **coagulograma normal** em adulto = **PTT até prova em '
              'contrário**: colha ADAMTS13 e inicie a troca plasmática sem esperar o resultado (o escore PLASMIC ajuda '
              'a estimar a probabilidade).')
R.h(3, 'Outras causas adquiridas')
R.bullets(['**Hemólise mecânica:** próteses valvares (principalmente com vazamento), marcha prolongada (hemoglobinúria '
           'da marcha).',
           '**Infecções:** malária (P. falciparum), Clostridium perfringens (hemólise maciça), babesiose.',
           '**Agentes físicos e químicos:** queimaduras extensas, venenos (loxoscelismo, ofidismo), chumbo.',
           '**Reação transfusional hemolítica aguda:** incompatibilidade ABO; hemólise intravascular, febre, dor lombar, '
           'choque. Pare a transfusão imediatamente.'])

# ===== fechamento
R.caixa('Pontos-Chave', [
    '• Hemólise = anemia + **reticulocitose** + LDH e bilirrubina indireta altas + haptoglobina baixa. Próximo passo: **Coombs direto** e esfregaço.',
    '• **Doença falciforme:** mutação na β-globina (Glu → Val), autossômica recessiva; diagnóstico no **teste do pezinho** e confirmação por eletroforese/HPLC.',
    '• Na DF, **febre é emergência** (ceftriaxona); **penicilina profilática dos 3 meses aos 5 anos**; Doppler transcraniano anual dos 2 aos 16 anos; hidroxiureia aumenta a HbF.',
    '• **STA** = infiltrado novo + sintomas respiratórios/febre: antibiótico, O₂, analgesia e transfusão. **Sequestro esplênico:** baço cresce e Hb despenca. **Crise aplástica:** parvovírus B19, reticulócitos baixos.',
    '• **Traço talassêmico:** microcitose com hemácias normais/altas, RDW normal, Mentzer < 13 e HbA2 > 3,5%. Não dar ferro sem ferropenia.',
    '• **Esferocitose:** esferócitos, CHCM alto, Coombs negativo, EMA; esplenectomia após os 6 anos com vacinas antes.',
    '• **G6PD:** ligada ao X, gatilhos oxidantes (infecção, fava, primaquina, dapsona, sulfas, rasburicase); dosagem pode ser normal na crise.',
    '• **AHAI quente:** IgG, esferócitos, prednisona 1 mg/kg. **Crioaglutininas:** IgM/C3d, Mycoplasma/EBV/linfoma, evitar frio.',
    '• **HPN:** hemólise + trombose atípica + falência medular; citometria CD55/CD59. **PTT:** ADAMTS13 < 10%, troca plasmática urgente. **SHU típica:** sem antibiótico.'])
R.referencias([
    'Brasil. Ministério da Saúde. Doença falciforme: condutas básicas para tratamento. Brasília: Ministério da Saúde; 2012.',
    'Brasil. Ministério da Saúde. Protocolo Clínico e Diretrizes Terapêuticas da Doença Falciforme. Portaria Conjunta SAS/SCTIE nº 05, de 19 de fevereiro de 2018. Brasília: Ministério da Saúde; 2018.',
    'National Heart, Lung, and Blood Institute. Evidence-based management of sickle cell disease: expert panel report. Bethesda: NHLBI; 2014.',
    'Brandow AM, Carroll CP, Creary S, et al. American Society of Hematology 2020 guidelines for sickle cell disease: management of acute and chronic pain. Blood Adv. 2020;4(12):2656-2701.',
    'DeBaun MR, Jordan LC, King AA, et al. American Society of Hematology 2020 guidelines for sickle cell disease: prevention, diagnosis, and treatment of cerebrovascular disease in children and adults. Blood Adv. 2020;4(8):1554-1588.',
    'Loscalzo J, Fauci AS, Kasper DL, Hauser SL, Longo DL, Jameson JL, editors. Harrison\'s principles of internal medicine. 21st ed. New York: McGraw Hill; 2022.',
    'Jäger U, Barcellini W, Broome CM, et al. Diagnosis and treatment of autoimmune hemolytic anemia in adults: recommendations from the First International Consensus Meeting. Blood Rev. 2020;41:100648.',
    'Zheng XL, Vesely SK, Cataland SR, et al. ISTH guidelines for the diagnosis of thrombotic thrombocytopenic purpura. J Thromb Haemost. 2020;18(10):2486-2495.',
    'Cappellini MD, Farmakis D, Porter J, Taher A, editors. 2021 Guidelines for the management of transfusion dependent thalassaemia (TDT). 4th ed. Nicosia: Thalassaemia International Federation; 2021.',
    'Bolton-Maggs PH, Langer JC, Iolascon A, Tittensor P, King MJ. Guidelines for the diagnosis and management of hereditary spherocytosis – 2011 update. Br J Haematol. 2012;156(1):37-49.',
    'Luzzatto L, Ally M, Notaro R. Glucose-6-phosphate dehydrogenase deficiency. Blood. 2020;136(11):1225-1240.',
    'Brodsky RA. Paroxysmal nocturnal hemoglobinuria. Blood. 2014;124(18):2804-2811.',
    'Hoffbrand AV, Moss PAH. Fundamentos em hematologia de Hoffbrand. 7. ed. Porto Alegre: Artmed; 2018.'])

# ---------------- salvar em 2 passos (sumário com páginas) ----------------
docx1 = os.path.join(SAIDA, NOME + '.docx')
n = sum(1 for k, _ in R.headings if k in (3, 4))
R.sumario(eval(os.environ['PG']) if os.environ.get('PG') else [1] * n)
R.salvar(docx1)
subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', SAIDA, docx1], capture_output=True)
if not os.environ.get('PG'):
    pg = paginas_dos_titulos(docx1[:-5] + '.pdf', R.headings)
    print('paginas', pg)
    subprocess.run([sys.executable, __file__], env=dict(os.environ, PG=repr(pg)), check=True)
