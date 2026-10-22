# Folhas únicas do 8º D1 · HMEC e PMSUS no estilo 2 (layouts A/B/C + Não confunda + mnemônicos)
# Conteúdo SÓ dos resumos publicados (PDFs do Drive). Pedido da Laura (22/10/2026).
import sys, os
os.environ.setdefault('PASTA', 'v2-g5')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from folha2 import render, ul, nc, mn, sec, card, box, cards, passos

H = '8º sem D1 · HMEC · '
P = '8º sem D1 · PMSUS · '
F = ' - resumo em 1 folha'

# ======================= ACLS (B) =======================
FLX_ACLS = '''<div class="flx">
<div class="fb esc">Paciente grave · cena segura · responde? respira? pulso? (até 10 s)</div><div class="fa">↓</div>
<div class="fr"><div><div class="fb vi">Sem pulso (ou só gasping) = PCR</div><div class="fp">RCP + monitor</div></div>
<div><div class="fb ou">Com pulso</div><div class="fp">A → B → C → D: trate cada ameaça antes de avançar</div></div></div>
<div class="fa">↓</div>
<div class="fr"><div><div class="fb"><b>Chocável</b> (FV, TV sem pulso)<div class="fp">desfibrilar + RCP; adrenalina após falha dos choques; amiodarona ou lidocaína se refratária</div></div>
<div class="fb" style="margin-top:5px"><b>Não chocável</b> (AESP, assistolia)<div class="fp">RCP + adrenalina o mais cedo possível; 5H e 5T</div></div></div>
<div><div class="fb"><b>Taqui instável</b><div class="fp">cardioversão sincronizada (sedar)</div></div>
<div class="fb" style="margin-top:5px"><b>Bradi instável</b><div class="fp">atropina → marca-passo transcutâneo ou dopamina/adrenalina</div></div>
<div class="fb ok" style="margin-top:5px"><b>Estável</b><div class="fp">ECG 12 derivações, causa, droga do ritmo</div></div></div></div></div>'''

render(H + 'ACLS' + F, dict(layout='B', titulo='ACLS',
 sub='Abordagem inicial, oxigênio, ritmos, terapia elétrica e RCP', vars='--fs:8pt;--lh:1.48;--gap:3.2mm',
 corpo=f'''<div class="gB"><div>
{card('Por onde começar', FLX_ACLS)}
{card('RCP de alta qualidade', '''<ul><li><b>100–120/min</b>, profundidade <b>5–6 cm</b>, retorno completo do tórax</li>
<li>Pausas &lt; 10 s; fração de compressão ≥ 60%; troca a cada 2 min</li>
<li>Sem via aérea avançada <b>30:2</b>; com via aérea, contínuas + <b>1 ventilação a cada 6 s</b></li>
<li><b>ETCO₂</b> ≥ 10 (ideal ≥ 20) mmHg; subida abrupta e sustentada sugere RCE</li>
<li>Adrenalina <b>1 mg a cada 3–5 min</b> · amiodarona <b>300 → 150 mg</b> · lidocaína 1–1,5 → 0,5–0,75 mg/kg</li></ul>''')}
{card('Depois do RCE', '<p>O₂ 100% até medir → SpO₂ <b>90–98%</b> · PaCO₂ 35–45 · <b>PAM ≥ 65</b> · temperatura 32–37,5 °C por ≥ 36 h em quem não obedece comandos · glicemia 70–180 · ECG já: supra → cateterismo.</p>')}
{card('Ritmos com pulso que caem', '<ul><li><b>TSV</b> (QRS estreito, regular, 150–250): vagal (20–30%; Valsalva + pernas elevadas ~50%) → adenosina</li><li><b>Flutter</b>: dente de serrote, 2:1 ≈ 150 bpm · <b>FA</b>: RR irregularmente irregular</li><li><b>Mobitz II</b> e <b>BAVT</b>: atropina costuma falhar → marca-passo</li></ul>')}
</div><div>
{card('Choque: qual e quanto (SBC 2019)', '''<table><tr><th></th><th>Desfibrilação</th><th>Cardioversão</th></tr>
<tr><td>Quando</td><td>FV, TV sem pulso, TV polimórfica</td><td>Taqui com pulso instável</td></tr>
<tr><td>Energia</td><td>Bifásico 120–200 J (ou máxima) · mono 360 J</td><td>FA 120–200 J · flutter e TSV 50–100 J · TV mono 100 J</td></tr>
<tr><td>Depois</td><td>RCP 2 min sem checar pulso</td><td>Reavaliar ritmo e pulso</td></tr></table>
<p class="m" style="margin-top:2px">AHA 2025: na FA, já começa com ≥ 200 J.</p>''')}
{card('Instável = basta 1 sinal', '<p>Hipotensão · alteração aguda do estado mental · choque · dor torácica isquêmica · IC aguda. Taqui costuma instabilizar com FC ≥ 150; bradi com FC &lt; 50.</p>')}
{card('Oxigênio', '<p>Dar se SpO₂ <b>&lt; 94%</b> (meta 94–98%) · máscara com reservatório 15 L/min no grave · na RCP, FiO₂ máxima. Oxímetro atrasa 30–60 s e engana no <b>monóxido de carbono</b>.</p>')}
{nc(['ABCD do ACLS: D é diagnóstico diferencial; no trauma é neurológico (e começa pelo x).', 'Gasping não é respiração: é PCR.', 'Taqui sinusal no séptico: trate a causa, não o ritmo.', 'TV polimórfica não sincroniza: desfibrila.', 'Adenosina em bolus rápido + flush; não na asma.', 'Marca-passo não serve para assistolia.'])}
{mn([('Chocável tem V de ventrículo', 'FV e TV sem pulso. AESP e assistolia: RCP + adrenalina.'), ('Tem pulso? Sincroniza. Parou? Desfibrila.', ''), ('Cem a cento e vinte, cinco a seis', 'aperta forte, aperta rápido, deixa o tórax voltar.'), ('Cai a pressão, cai a cabeça, cai a perfusão, aperta o peito, afoga o pulmão', 'os 5 sinais de instabilidade.'), ('Amiodarona 300, depois a metade', '150 mg na segunda dose.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de ACLS do 8º semestre (SBC 2019; AHA 2025; ATLS 11ª ed.).'))

# ======================= RCP EM RITMOS CHOCÁVEIS (B) =======================
FLX_RCP = '''<div class="flx">
<div class="fb esc">Não responde, sem respirar (ou gasping), sem pulso · ≤ 10 s</div><div class="fa">↓</div>
<div class="fb">Chamar ajuda, carrinho + desfibrilador · <b>RCP</b> já</div><div class="fa">↓ ritmo: FV / TV sem pulso</div>
<div class="fb vi">1º choque · bifásico 200 J · monofásico 360 J</div><div class="fa">↓</div>
<div class="fb">RCP 2 min + acesso IV/IO</div><div class="fa">↓ ainda FV/TV</div>
<div class="fb vi">2º choque</div><div class="fa">↓</div>
<div class="fb ou">RCP 2 min + <b>adrenalina 1 mg</b> (a cada 3–5 min)</div><div class="fa">↓ ainda FV/TV</div>
<div class="fb vi">3º choque</div><div class="fa">↓</div>
<div class="fb ou">RCP 2 min + <b>amiodarona 300 mg</b> (ou lidocaína 1–1,5 mg/kg)</div><div class="fa">↓ após o 4º choque</div>
<div class="fb">Amiodarona <b>150 mg</b> (ou lidocaína 0,5–0,75 mg/kg; máx. 3 mg/kg)</div></div>'''

render(H + 'RPC em ritmos chocáveis' + F, dict(layout='B', titulo='RCP em Ritmos Chocáveis',
 sub='FV e TV sem pulso · choque, drogas, via aérea, equipe e pós-PCR', vars='--fs:8.35pt;--lh:1.52;--gap:3.5mm',
 corpo=f'''<div class="gB"><div>
{card('O algoritmo', FLX_RCP)}
{nc(['Adrenalina só depois do 2º choque; antiarrítmico só depois do 3º.', 'Depois do choque, não cheque pulso: volta a comprimir na hora.', 'ETCO₂ sobe de repente e se mantém (em geral ≥ 40 mmHg) = RCE: pare e cheque o pulso.', 'ETCO₂ &lt; 10 mmHg = compressão ruim: melhore a RCP.', 'Supra de ST após RCE vai ao cateterismo mesmo em coma.', 'Magnésio só na torsades (QT longo), 1–2 g.'])}
{card('Equipe', '''<p><b>Líder</b> ao pé do leito, sem procedimento · <b>via aérea</b> na cabeceira · <b>compressores</b> trocam a cada 2 min · <b>medicação</b> e acesso · <b>desfibrilador</b>, cronômetro e anotação.</p>
<p>Alça fechada: cita o nome, ordem clara, o outro repete e confirma.</p>''')}
</div><div>
{card('Via aérea e capnografia', '''<ul><li>Sem via aérea avançada: <b>30:2</b> com bolsa-válvula-máscara, O₂ 15 L/min</li>
<li>Intubar sem parar as compressões por mais de 10 s; depois, <b>1 ventilação a cada 6 s</b> (10/min), compressões contínuas</li>
<li>Tubo confirmado pela curva de capnografia em ≥ <b>7</b> ventilações</li>
<li>ETCO₂ &lt; 10 após 20 min: chance muito baixa de sucesso</li></ul>''')}
{card('Pós-PCR', '''<ul><li>VC até 6 mL/kg, PEEP 5, SpO₂ <b>90–98%</b>, PaCO₂ 35–45 (ETCO₂ 30–40)</li>
<li>PAS ≥ 90 ou <b>PAM ≥ 65</b> com cristaloide e noradrenalina</li>
<li>Temperatura 32–37,5 °C por ≥ 36 h se não obedece comandos · glicemia 70–180 (alvo usual 140–180) · corrigir K e Mg</li>
<li>Passagem de caso SBAR · debriefing</li></ul>''')}
{card('Relógio da PCR', '<p>Ciclo <b>2 min</b> · troca de compressor a cada 2 min · pausa <b>≤ 10 s</b> · adrenalina a cada <b>3–5 min</b>.</p>')}
{mn([('5H', '<b>H</b>ipovolemia, <b>H</b>ipóxia, <b>H</b>idrogênio (acidose), <b>H</b>ipo/hipercalemia, <b>H</b>ipotermia.'), ('5T', '<b>T</b>ensão no tórax (pneumotórax), <b>T</b>amponamento, <b>T</b>oxinas, <b>T</b>rombose coronária, <b>T</b>rombose pulmonar.'), ('Choque, choque, adrenalina; choque, amiodarona', 'a ordem das drogas na FV/TV.'), ('Piorou no ventilador? DOPE', '<b>D</b>eslocamento, <b>O</b>bstrução, <b>P</b>neumotórax, <b>E</b>quipamento.'), ('Abaixo de 10, aperta melhor; pulou pra 40, procura o pulso', 'ETCO₂ na RCP.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de RCP em ritmos chocáveis do 8º semestre (AHA; ACLS; protocolo MS).'))

# ======================= SCA - NOCA vs OCA (C) =======================
render(H + 'SCA - NOCA vs OCA' + F, dict(layout='C', titulo='SCA: OCA × NOCA',
 sub='Do supra de ST à oclusão coronariana aguda (proposta Dante Pazzanese, 2024)', vars='--fs:8.9pt;--lh:1.58;--gap:4.4mm',
 corpo=f'''<div class="sec">{cards([('Sensibilidade do supra', '44–56%', 'para achar oclusão aguda'), ('IAMSSST ocluído', '25–45%', 'artéria culpada TIMI 0'), ('Mortalidade', '~2×', 'nesse "sem supra" ocluído'), ('Infra de ST em aVL', '99%', 'específico de oclusão inferior')])}</div>
<div class="sec"><h2>Na dor torácica, pense em oclusão</h2>{passos([('ECG', 'tem supra de ST clássico? Se não, não pare aí'), ('Caçar sinais', 'T hiperaguda, De Winter, aVL, V1–V4…'), ('Somar a clínica', 'dor refratária, eco com hipocinesia, angioTC'), ('OCA', 'reperfusão já, tempos do IAMCSST'), ('NOCA', 'troponina seriada e cateterismo sem pressa')])}</div>
<div class="g2"><div>
{sec('Os dois paradigmas', '''<table><tr><th></th><th>Tradicional</th><th>Novo</th></tr>
<tr><td>Base</td><td>ECG: tem ou não supra de ST</td><td>Anatomia: tem ou não <b>oclusão</b></td></tr>
<tr><td>Quem reperfunde já</td><td>Só o IAMCSST</td><td>Toda <b>OCA</b>, com ou sem supra</td></tr>
<tr><td>Troponina</td><td>Obrigatória para triar o sem supra</td><td>Não atrasa o cateterismo na OCA</td></tr></table>''')}
{sec('OCA × NOCA', '''<ul><li><span class="k">OCA</span>: oclusão total ou quase total de artéria epicárdica, pouca colateral, infarto transmural em curso → <b>reperfusão imediata</b> nos tempos do IAMCSST. Pistas: sinais sutis no ECG, <b>dor persistente ou refratária</b>, alteração de motilidade no eco, oclusão na angioTC</li>
<li><span class="k">NOCA</span>: SCA sem oclusão completa (placa instável) → cateterismo sem urgência &lt; 90 min; pode esperar a troponina seriada</li></ul>''')}
{nc(['Sem supra não quer dizer sem oclusão.', 'Troponina inicial negativa não exclui OCA: ela demora.', 'Infra em V1–V4 pode ser supra posterior (V7–V9).', 'Infra em aVL fala de oclusão inferior, não de pericardite.', 'BRE ou marca-passo: use Sgarbossa modificado por Smith.'])}
</div><div>
{sec('8 sinais de OCA sem supra clássico', ul(['<b>T hiperaguda</b>: ampla, simétrica, base larga', '<b>De Winter</b>: infra de 1–3 mm no ponto J em V1–V6 + T hiperaguda → DA proximal', '<b>Aslanger</b>: supra só em III + infra em V4–V6 (não V2), V1 &gt; V2 → inferior com doença multivascular', '<b>Bandeira da África do Sul</b>: supra em I e aVL + infra em III → ramo diagonal', '<b>Infra em V1–V4</b>: espelho da parede posterior', '<b>Infra em aVL</b>: oclusão inferior', '<b>Distorção terminal do QRS</b>: sem S e sem J em V2 ou V3', '<b>Sgarbossa–Smith</b>: oclusão com BRE ou marca-passo']))}
{mn([('OCA corre, NOCA calma', 'oclusão vai já para a hemodinâmica; sem oclusão espera a troponina.'), ('De Winter desce e sobe', 'ST desce no J, T sobe gigante: DA proximal.'), ('Bandeira hasteada no alto', 'I e aVL: diagonal.'), ('Aslanger mora no III', 'supra isolado em III, doença de vários vasos.'), ('Infra na frente é supra nas costas', 'V1–V4 abaixo, V7–V9 acima.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de SCA, NOCA × OCA do 8º semestre (Alencar et al., Arq Bras Cardiol 2024).'))

# ======================= SCA - PROTOCOLO INICIAL IAM (B) =======================
FLX_IAM = '''<div class="flx">
<div class="fb esc">Dor torácica no PS · monitor, oxímetro, acesso</div><div class="fa">↓</div>
<div class="fb vi">ECG de 12 derivações em até 10 min</div><div class="fa">↓</div>
<div class="fr"><div><div class="fb ou"><b>Supra de ST / BRE novo</b></div><div class="fp"><b>ICP primária</b> se possível em ≤ 120 min (meta ≤ 90 min) · senão, <b>fibrinólise em até 30 min</b> · troponina nunca atrasa</div></div>
<div><div class="fb"><b>Sem supra</b></div><div class="fp">hs-cTn 0 h e 1–2 h · GRACE/TIMI · ECG seriado</div></div></div>
<div class="fa">↓ sem supra: quando cateterizar?</div>
<div class="fr3"><div class="fb">&lt; 2 h<div class="fp">muito alto risco: instável, choque, dor refratária, arritmia grave, EAP</div></div>
<div class="fb">&lt; 24 h<div class="fp">alto risco: GRACE &gt; 140, IAMSSST pela troponina, ST/T dinâmico</div></div>
<div class="fb">&lt; 72 h<div class="fp">intermediário: GRACE 109–140, DM, DRC, revascularização prévia</div></div></div>
<div class="fa">↓ troponina negativa</div>
<div class="fb ok">Angina instável · estratificar · teste funcional ou angioTC antes da alta</div></div>'''

render(H + 'SCA - protocolo inicial de atendimento ao suspeito de IAM' + F, dict(layout='B', titulo='Suspeita de IAM no PS',
 sub='Os primeiros minutos: ECG, história, exame, troponina e para onde vai', vars='--fs:8.5pt;--lh:1.54;--gap:3.7mm',
 corpo=f'''<div class="gB"><div>
{card('O fluxo', FLX_IAM)}
{card('Exames', '<ul><li><b>Troponina de alta sensibilidade</b> na chegada; repetir em 1–2 h (convencional: 3–6 h)</li><li>Hemograma, função renal, eletrólitos, glicemia, coagulograma, lípides</li><li>RX portátil sem atrasar · <b>eco</b> se instável, choque, dúvida ou complicação mecânica</li></ul>')}
{nc(['Supra de ST não espera troponina.', 'Troponina convencional repete em 3–6 h; a ultrassensível, em 1–2 h.', 'Dor que muda com a respiração ou a palpação não é a típica.', 'PA diferente entre os braços: pense em dissecção.'])}
{card('Supra que conta', '<p>ST ≥ 1 mm em 2 derivações contíguas (ou BRE novo) · fibrinólise só com &lt; 12 h de sintomas · <b>choque cardiogênico</b>: revascularizar a qualquer tempo.</p>')}
</div><div>
{card('ECG: olhe além das 12', '<ul><li>Inicial normal com suspeita alta ou dor persistente → <b>ECG seriado</b></li><li>Infarto <b>inferior</b> (DII, DIII, aVF) → <b>V3R e V4R</b> (ventrículo direito)</li><li>Infra de ST em <b>V1–V3</b> → <b>V7, V8 e V9</b> (parede posterior)</li></ul>')}
{card('História e exame', '''<p><b>Dor isquêmica:</b> aperto, peso ou queimação retroesternal, irradia para braço, pescoço, mandíbula, dorso ou epigástrio, <b>&gt; 20 min</b>, não muda com palpação, posição ou respiração. Idosos, mulheres e diabéticos: dispneia, sudorese, náusea, síncope.</p>
<p><b>Exame:</b> PA nos <b>dois braços</b> (dissecção de aorta) · congestão, B3/B4 · sopro novo (insuficiência mitral por músculo papilar).</p>''')}
{card('Killip-Kimball', '<table><tr><td>I</td><td>Sem sinais de IC</td></tr><tr><td>II</td><td>Estertores basais ou B3</td></tr><tr><td>III</td><td>Edema agudo de pulmão</td></tr><tr><td>IV</td><td>Choque cardiogênico (PAS &lt; 90 + hipoperfusão)</td></tr></table>')}
{mn([('Dez minutos para o ECG', 'do primeiro contato médico ao traçado lido.'), ('Inferior? Olhe à direita. Infra na frente? Olhe as costas.', 'V3R/V4R e V7–V9.'), ('Balão 90, agulha 30', 'porta-balão e porta-agulha.'), ('Killip: limpo, chia, afoga, choca', 'I, II, III e IV.'), ('2, 24, 72', 'horas até o cateterismo no sem supra: muito alto, alto, intermediário.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de protocolo inicial ao suspeito de IAM do 8º semestre.'))

# ======================= ATENÇÃO HOSPITALAR (A) =======================
render(P + 'Atenção hospitalar - oficina 6' + F, dict(layout='A', titulo='Atenção Hospitalar na RAS',
 sub='Regulação, leitos, superlotação e a PNHOSP', vars='--fs:8.45pt;--lh:1.54;--gap:3.8mm',
 corpo=f'''<div class="gL"><div>
{sec('Regulação: três dimensões', '''<table><tr><th>Dimensão</th><th>Foco</th></tr>
<tr><td>De sistemas</td><td>O sistema todo: normas, planejamento, financiamento, fiscalização, incorporação de tecnologias</td></tr>
<tr><td>Da atenção</td><td>Os prestadores: contratualização, habilitação, controle, avaliação, auditoria (ligada ao PRI)</td></tr>
<tr><td>Do acesso</td><td>O usuário: centrais de regulação, protocolos, classificação de risco</td></tr></table>
<p class="m" style="margin-top:2px">A PNR-SUS (Portaria 9.262/2025) substituiu a política de 2008 e manteve as três dimensões.</p>''')}
{sec('Leitos no Brasil (2010 → 2022)', '''<ul><li>Densidade <b>2,23 → 1,99</b> por 1.000 hab. (OMS 3,2) · total caiu 2%</li>
<li>Queda só no <b>privado</b> (−31.670); o público <b>cresceu</b> (+22.924)</li>
<li>59% dos privados têm até 50 leitos · filantrópicos: 92% atendem o SUS e somam 61% dos leitos privados · 70% dos lucrativos não atendem o SUS</li></ul>''')}
{sec('Superlotação e hiperutilizadores', '''<ul><li>Causas: menos leitos e mal distribuídos, <b>cultura hospitalocêntrica</b> (~90% buscam o hospital por baixa complexidade), APS frágil, regulação burocrática</li>
<li>Hiperutilizadores: <b>1–5%</b> dos usuários, muito recurso. Multimorbidade, transtorno mental e adicção, vulnerabilidade social. Não é abuso: é <b>falha da rede</b></li>
<li>Respostas: plano pós-alta com a UBS, gestão de casos com PTS, <b>Melhor em Casa</b></li></ul>''')}
{sec('PNHOSP (Portaria 3.390/2013)', '''<ul><li>Diretrizes: universalidade, equidade, integralidade · cuidado centrado no usuário · <b>regionalização</b> · segurança do paciente · gestão eficiente</li>
<li>Internação: visita diária ≥ 2 h, acompanhante · eletivas e cirurgias <b>só pelas Centrais de Regulação</b></li>
<li>Público: PCEP com POA (metas) · filantrópico: <b>CEBAS ≥ 60%</b> ao SUS · CNES atualizado todo mês</li></ul>''')}
{sec('APS e hospital', '''<ul><li>APS: porta de entrada preferencial, <b>ordenadora</b>; na PNR-SUS regula o acesso das condições crônicas e gere as listas de espera do território</li>
<li>Efeitos: desmonta o modelo <b>piramidal</b>, racionaliza a demanda nas urgências, garante continuidade e <b>desospitalização</b> (menos reinternações)</li>
<li>Sem isso: filas, vazios assistenciais, PS lotado, inequidade, "porta giratória"</li></ul>''')}
</div><div>
{box('Como o hospital entra na rede', ul(['<b>Integração</b>: alta segura, informação volta à ESF', '<b>Acesso regulado</b>: sem porta aberta desordenada', '<b>Gestão da clínica</b>: giro de leitos, hospital-dia', '<b>Contratualização</b>: repasse por metas']) + '<p style="margin-top:3px">A <b>APS ordena</b> a rede; o hospital vira ponto de atenção, não "cabeça".</p>')}
{nc(['Leito caiu no privado, não no público.', 'Densidade caiu também porque a população cresceu.', 'Hiperutilizador não é "abusador".', 'Eletiva não entra por procura direta: vai pela central.', 'Regulação do acesso ≠ regulação da atenção.'])}
{mn([('Sistema, Atenção, Acesso', 'do gabinete ao balcão: as três regulações.'), ('Filantrópico dá 60', 'CEBAS exige 60% dos serviços ao SUS.'), ('Integra, regula, gira e contrata', 'os 4 jeitos de pôr o hospital na rede.'), ('Quem volta toda hora não abusa, falta rede', 'hiperutilizador.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de atenção hospitalar (oficina 6) do 8º semestre (PNHOSP; PRC nº 1/2017; PNR-SUS 2025).'))

# ======================= DISLIPIDEMIA (A) =======================
render(P + 'Dislipidemia - oficina 2' + F, dict(layout='A', titulo='Dislipidemia',
 sub='Diagnóstico, risco, metas e tratamento no SUS (PCDT) e na SBC 2025', vars='--fs:8.55pt;--lh:1.54;--gap:3.9mm',
 corpo=f'''<div class="gL"><div>
{sec('Fisiologia que vira remédio', '''<ul><li><b>Estatina</b> inibe a HMG-CoA redutase → mais receptor de LDL → LDL cai</li>
<li><b>Ezetimiba</b> bloqueia a NPC1-L1 (absorção intestinal) · <b>anti-PCSK9</b> impede a degradação do receptor · <b>fibrato</b> (PPAR-α) baixa TG</li>
<li>TG &gt; 500–1.000 mg/dL: risco de <b>pancreatite</b> · Lp(a): risco independente; dosar 1 vez na vida</li></ul>''')}
{sec('Diagnóstico', '''<ul><li>PCDT: CT, HDL e TG; <b>Friedewald</b> LDL = CT − HDL − TG/5 se TG &lt; 400</li>
<li>TG &gt; 400: <b>não-HDL</b> = CT − HDL (alvo = LDL + 30)</li>
<li>SBC 2025: Martin/Hopkins para todos; não-HDL se TG &gt; 800; sem jejum vale (TG &gt; 440 → repetir em jejum)</li>
<li>Clínica: silenciosa; xantomas, xantelasma, arco córneo &lt; 45 anos sugerem forma genética</li>
<li><b>HF (OMS):</b> xantoma tendinoso 6 · arco &lt; 45 anos 4 · LDL ≥ 330 = 8 → <b>&gt; 8 definitivo</b>, 6–8 provável, 3–5 possível</li></ul>''')}
{sec('Risco e metas (SBC 2025)', '''<table><tr><th>Risco</th><th>Quem</th><th>LDL</th><th>Não-HDL</th></tr>
<tr><td>Baixo</td><td>Escore &lt; 5%</td><td>&lt; 115</td><td>&lt; 145</td></tr>
<tr><td>Intermediário</td><td>5 a &lt; 20%; LDL 160–189</td><td>&lt; 100</td><td>&lt; 130</td></tr>
<tr><td>Alto</td><td>≥ 20%; LDL ≥ 190; CAC &gt; 100</td><td>&lt; 70</td><td>&lt; 100</td></tr>
<tr><td>Muito alto</td><td>Doença aterosclerótica, CAC &gt; 300</td><td>&lt; 50</td><td>&lt; 80</td></tr>
<tr><td>Extremo</td><td>Múltiplos eventos</td><td>&lt; 40</td><td>&lt; 70</td></tr></table>
<p class="m" style="margin-top:2px">SUS: Escore de Risco Global (Framingham) · SBC 2025: PREVENT. Agravantes sobem uma categoria.</p>''')}
{sec('Tratamento', '''<ul><li><b>Estilo de vida</b> para todos: sem gordura trans, 150 min/semana, parar de fumar</li>
<li><b>Estatina</b> é a base: alta intensidade (≥ 50%) atorvastatina 40–80 · moderada (30–50%) atorva 10–20, sinva 20–40. Rosuvastatina fora do PCDT</li>
<li><b>Fibrato</b> se TG ≥ 500 persistente · genfibrozila <b>nunca</b> com estatina · HIV com antirretroviral: <b>pravastatina</b></li>
<li>Ezetimiba e anti-PCSK9: <b>não incorporados</b> ao SUS</li>
<li>Suspender: CK &gt; 10× ou TGO/TGP &gt; 3× (PCDT)</li></ul>''')}
{sec('Quem recebe remédio no SUS (PCDT)', '''<ul><li>DM em homem &gt; 45 ou mulher &gt; 50 anos + ≥ 1 fator de risco maior · Framingham <b>&gt; 10%</b> em 10 anos · <b>doença aterosclerótica</b> clínica · <b>HF definitiva</b></li>
<li>Não entra: hipotireoidismo descompensado (TSH &gt; 10), gestação ou idade fértil sem contracepção, hepatopatia grave</li></ul>''')}
</div><div>
{nc(['PCDT trata o paciente em risco, não persegue número de LDL.', 'TG alto no obeso (&lt; 500): fibrato não.', 'TG ≥ 150 com risco CV: estatina, não fibrato.', 'Estatina à noite; fibrato de manhã.', 'Não dose CK de rotina sem sintoma (SBC 2025).', 'Lp(a) estratifica, não tem meta.'])}
{mn([('Friedewald divide por 5', 'LDL = CT − HDL − TG/5, só com TG &lt; 400.'), ('Não-HDL é LDL + 30', 'em todas as faixas de risco.'), ('115, 100, 70, 50, 40', 'o LDL desce a escada do risco.'), ('Genfibrozila com estatina, rabdo na esquina', ''), ('PCSK9 come o receptor', 'o anti-PCSK9 salva o receptor e o LDL cai.'), ('HIV pede PRAVA', 'pravastatina não mexe no P450.')])}
{box('Números que caem', '<p>CT &lt; 190 · TG &lt; 150 · HDL &gt; 40<br>cada 39 mg/dL de LDL a menos: −22% de eventos</p>')}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de dislipidemia (oficina 2) do 8º semestre (PCDT da Dislipidemia 2019; Diretriz SBC 2025).'))

# ======================= OBESIDADE (C) =======================
render(P + 'Obesidade - oficina 1' + F, dict(layout='C', titulo='Obesidade na RAS',
 sub='Diagnóstico, abordagem na APS, tratamento e linha de cuidado', vars='--fs:8.35pt;--lh:1.53;--gap:3.8mm',
 corpo=f'''<div class="sec">{cards([('IMC', '≥ 30', 'I 30 · II 35 · III ≥ 40'), ('Cintura (risco)', '&gt; 94 / &gt; 80', 'homem / mulher · cintura/altura &gt; 0,5'), ('Idoso normal', '22–27', 'por causa da sarcopenia'), ('Brasil (PNS 2020)', '1 em 4', 'obeso · 60% com excesso de peso')])}</div>
<div class="sec"><h2>Os 5As da conversa</h2>{passos([('Abordar', 'pedir licença para falar do peso, sem julgar'), ('Avaliar', 'causas, complicações e barreiras'), ('Aconselhar', 'riscos e opções'), ('Acordar', 'metas realistas juntos'), ('Ajudar', 'apoio contínuo e rede')])}</div>
<div class="g2"><div>
{sec('Diagnóstico', '<ul><li>IMC falha em &gt; 80 anos, muito musculosos, acamados, cadeirantes, amputados e orientais → some a <b>cintura</b></li><li>Cintura: ponto médio entre a <b>10ª costela</b> e a <b>crista ilíaca</b>, no fim da expiração</li><li>Rastrear todo adulto (IMC normal: 1 ano) e a família; registrar no SISVAN/e-SUS</li><li><b>SAHOS:</b> 2 de 3 (ronco, sonolência, apneia vista) → Epworth, STOP-BANG</li></ul>')}
{sec('Tratamento', '<ul><li>Déficit de <b>500–1.000 kcal/dia</b>; menos ultraprocessados; arroz com feijão; ≥ 3 refeições</li><li><b>≥ 150 min/semana</b>, sem passar 2 dias parado; força ≥ 2×/semana; teste da fala</li><li>Entrevista motivacional e TCC; grupos; PICS como apoio</li><li><b>SUS não incorporou</b> sibutramina nem orlistate</li><li>ABESO 2026: remédio se IMC ≥ 30 ou ≥ 27 com complicação; meta ≥ 10%. Alta potência: <b>semaglutida, tirzepatida</b></li></ul>')}
{nc(['IMC normal não exclui risco: meça a cintura.', 'Gordofobia é barreira de acesso e determinante social.', 'IMC ≥ 50 não precisa esperar 2 anos.', 'Remédio não é para gestante, lactante ou quem quer engravidar.', 'Sibutramina não na doença aterosclerótica.'])}
</div><div>
{sec('Bariátrica e linha de cuidado', '''<table><tr><th>IMC</th><th>Encaminhar</th></tr>
<tr><td>≥ 50</td><td>Direto à avaliação cirúrgica</td></tr>
<tr><td>40–49,9</td><td>Após ≥ 2 anos de tratamento clínico</td></tr>
<tr><td>35–39,9</td><td>+ comorbidade (RCV &gt; 20%, HAS/DM difícil, SAHOS, artrose) e ≥ 2 anos</td></tr></table>
<p style="margin-top:2px"><b>APS</b> cuida de IMC 25–49,9 · <b>especializada</b> nos casos complexos · <b>hospital</b> na bariátrica. UPA e hospital devolvem à APS quem tem IMC ≥ 25 (Portaria 424/2013).</p>''')}
{mn([('Pede licença antes de pesar', 'os 5As começam por Abordar.'), ('50 vai direto, 40 espera, 35 só acompanhado', 'encaminhamento para bariátrica.'), ('94 e 80, a cintura dá o alarme', 'homem e mulher.'), ('Ronca, cochila, para de respirar', 'SAHOS: bastam 2 de 3.'), ('No SUS, nem sibutra nem orlis', '')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo de obesidade (oficina 1) do 8º semestre (Linha de Cuidado MS 2020; ABESO 2026).'))

# ======================= RUE (C) =======================
CSS_MT = '''.cd.mt{border-top:4px solid var(--c)}.cd.mt .n{color:var(--ink)}'''
def mt(lst): return '<div class="cards" style="--nc:%d">' % len(lst) + ''.join(f'<div class="cd mt" style="--c:{c}"><span class="t">{t}</span><span class="n">{n}</span>{x}</div>' for c, t, n, x in lst) + '</div>'

render(P + 'RUE - rede de atenção às urgências e emergências - oficina 5' + F, dict(layout='C', titulo='Rede de Urgência e Emergência',
 sub='Conceitos, componentes, classificação de risco e regulação', vars='--fs:8.1pt;--lh:1.5;--gap:3.4mm', css=CSS_MT,
 corpo=f'''<div class="sec"><h2>Manchester: cor e tempo-alvo</h2>{mt([('#c62828', 'Vermelho', 'já', 'emergência'), ('#ef6c00', 'Laranja', '10 min', 'muito urgente'), ('#f9a825', 'Amarelo', '60 min', 'urgente'), ('#2e7d32', 'Verde', '120 min', 'pouco urgente'), ('#1565c0', 'Azul', '240 min', 'não urgente')])}</div>
<div class="sec"><h2>Integralidade na linha do IAM</h2>{passos([('SAMU ou UPA', 'Tele-ECG, protocolo, ACCR'), ('Regulação', 'central leva à UCO'), ('Retaguarda', 'leito clínico ou UCP'), ('Domicílio', 'reabilitação com EMAD/EMAP'), ('APS', 'seguimento e prevenção')])}</div>
<div class="g2"><div>
{sec('Conceitos (PNAU)', '<ul><li><b>Emergência:</b> risco iminente de morte, atendimento imediato</li><li><b>Urgência:</b> com ou sem risco de vida, espera de até <b>2 h</b></li><li><b>Não urgente:</b> acolher e direcionar à Atenção Básica</li></ul>')}
{sec('Acolhimento com classificação de risco', '<ul><li>Feito por <b>enfermeiro</b> com protocolo pactuado; troca a ordem de chegada pela gravidade</li><li><b>Inclusivo</b> (ninguém sai sem orientação) e <b>dinâmico</b> (reclassifica)</li><li>Ficha → classificação em até 15 min · SAMU: médico recebe na hora · violência: mínimo <b>amarelo</b> · autismo, deficiência, transtorno mental: mínimo verde com prioridade</li><li>Ambiência: <b>eixo vermelho</b> (graves: salas vermelha, amarela, verde) e <b>eixo azul</b> (não graves)</li></ul>')}
{sec('SAMU 192', '<p><b>USB</b>: condutor + técnico (2) · <b>USA</b>: condutor + enfermeiro + médico (3) · motolância: enfermagem · aeromédico, embarcação, VIR.</p>')}
{sec('Linhas de cuidado no hospital', '<ul><li><b>IAM</b> (Portaria 2.994/2011): UCO, Tele-ECG, trombólise, angioplastia primária</li><li><b>AVC</b> (Portaria 665/2012): U-AVC agudo ≥ 5 leitos, até 72 h · integral ≥ 10 leitos, até 15 dias</li><li><b>Cuidados prolongados</b>: UCP 15–25 leitos · HCP ≥ 40 leitos</li></ul>')}
</div><div>
{sec('Componentes', '<p>Promoção e vigilância · Atenção Básica · SAMU e centrais · <b>Sala de Estabilização</b> (&lt; 50 mil hab.) · UPA 24h · hospital (UCO, U-AVC, cuidados prolongados) · Atenção Domiciliar (AD1 na AB; AD2/AD3 com EMAD/EMAP; município ≥ 40 mil) · Força Nacional do SUS.</p>')}
{sec('Regulação (PNR-SUS 2025)', '<ul><li>Três dimensões: sistemas, atenção e <b>acesso</b></li><li><b>Agudo</b> → Central de Regulação de Urgência · <b>crônico</b> → APS</li><li>NIR no hospital; fila única e listas de espera públicas</li></ul>')}
{nc(['Classificação de risco não é triagem que exclui.', 'Urgência PNAU: até 2 h; amarelo de Manchester: 60 min.', 'Crônico que agudizou é agudo: vai pela Central de Urgência.', 'IAM no SUS mata ~15% (países ricos &lt; 5%).'])}
{mn([('Manchester dobra: 60, 120, 240', 'depois do vermelho já e do laranja 10.'), ('A de Avançada tem o doutor', 'USA leva médico; USB não.'), ('Agudo chama a central; crônico chama a APS', ''), ('Violência é no mínimo amarela', ''), ('AVC agudo 5 e 72, integral 10 e 15', 'leitos e tempo de permanência das U-AVC.')])}
</div></div>''',
 fontes='Elaborado pela MedSum com base no resumo da RUE (oficina 5) do 8º semestre (Manual instrutivo da RUE 2013; PNR-SUS 2025).'))
