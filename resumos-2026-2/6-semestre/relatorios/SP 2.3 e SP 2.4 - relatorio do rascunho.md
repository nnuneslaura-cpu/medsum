# 6º semestre · D2 (hematologia) · SP 2.3 e SP 2.4 · relatório dos rascunhos

Pedido #2026-10-21-1 da ponte. Divisão combinada com a Laura em 21/10: o **Revisor** (Mac, com NotebookLM) faz a SP 2.1 (coagulopatias, PTI) e a SP 2.2 (anemias carenciais). A **sessão na nuvem** fez estes dois rascunhos.

**Status: RASCUNHO. Nada foi para o site nem para o Drive.** Os dois arquivos esperam (1) a conferência do Revisor com o NotebookLM e com os objetivos do roteiro 2026.2 e (2) o "sim" da Laura.

## Arquivos (nesta pasta)
| SP | Word | PDF | Páginas |
|---|---|---|---|
| 2.3 · Doença falciforme e anemias hemolíticas | `6º sem D2 · NCS · SP 2.3 · Doença falciforme e anemias hemolíticas (rascunho 2026.2).docx` | idem `.pdf` | 19 |
| 2.4 · Linfomas e leucemias agudas | `6º sem D2 · NCS · SP 2.4 · Linfomas e leucemias agudas (rascunho 2026.2).docx` | idem `.pdf` | 19 |

Os dois são **resumos novos** (não existia resumo desses temas na grade do 6º D2). O layout é o do Diabetes revisado (20/10/2026): capa com capítulos, sumário, faixas de capítulo, Título 3/4/5, tabelas vinho com "Adaptado de", caixas Ponto-chave, caixa "Aplicação aos casos da SP", Quadro Brasil × internacional, Pontos-Chave e referências em Vancouver. Fluxogramas novos no estilo MedSum (2 por resumo).

## Limitações (importante)
- **Sem NotebookLM:** a sessão na nuvem não alcança o Mac (navegador, caderno do NotebookLM, pasta LIVROS). O texto foi escrito com base nas diretrizes e livros citados nas referências, sem consulta direta aos PDFs.
- **Sem o roteiro 2026.2:** o `MAPA-2026-2.md` e os roteiros do Marcos ficam só no Mac. Os objetivos de aprendizagem da SP 2.3 e da SP 2.4 **não foram conferidos**; a caixa "Aplicação aos casos da SP" está genérica e precisa ser ajustada ao caso do roteiro.
- **Sem imagens das fontes:** só há fluxogramas próprios. Faltam figuras dos livros (esfregaços, Reed-Sternberg, bastonetes de Auer, "céu estrelado"), que devem ser tiradas das fontes sem alteração e traduzidas.
- Fontes do Drive usadas só como apoio: análise ENARE + ENAMED de hematologia (temas mais cobrados) e a prova D2 NCS antiga do 6º.
- O PDF foi gerado pelo LibreOffice (sem a fonte Cinzel); exporte pelo Word antes de subir. No Word, clique com o botão direito no sumário → Atualizar campo.

## Para o Revisor conferir com o NotebookLM
### SP 2.3
1. Objetivos do roteiro 2026.2 (SP 2.3) × capítulos do resumo; ajustar a caixa "Aplicação aos casos da SP".
2. PCDT da doença falciforme: confirmar se a Portaria Conjunta nº 05/2018 é a versão vigente e a idade de início da hidroxiureia (Quadro 1).
3. Manual do MS (condutas básicas): doses da penicilina profilática, recomendação de ácido fólico, idade do Doppler transcraniano.
4. Número de nascidos com DF e traço por ano (texto diz "cerca de 3 mil" e "200 mil").
5. Acrescentar figuras: esfregaço com drepanócitos, esferócitos, esquizócitos, corpos de Heinz.

### SP 2.4
1. Objetivos do roteiro 2026.2 (SP 2.4) × capítulos; ajustar a caixa do caso.
2. Dados do INCA (o texto evita números exatos; acrescentar os da estimativa vigente, se a Laura quiser).
3. Protocolos brasileiros de LLA (GBTLI/BFM) e DDT do Ministério da Saúde para LMA, LH e LDGCB, se houver no caderno.
4. Acrescentar figuras: célula de Reed-Sternberg, bastonete de Auer, Burkitt em "céu estrelado", estadiamento de Lugano.

## Para refazer os arquivos
`gerador/` tem os scripts (Python + python-docx + Playwright). O molde é o Word do Diabetes revisado (Drive: `8º sem D2 · NCS · SP 2.1 · Diabetes Mellitus (revisado 20-10-2026).docx`), salvo como `fontes/dm_completo.docx` ao lado da pasta `gerador/`.
