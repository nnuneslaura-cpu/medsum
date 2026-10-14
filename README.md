# Imagens do Radar de Diretrizes (MedSum)
Ramo usado só para hospedar as imagens dos e-mails semanais do Radar.
Uma pasta por edição (data do domingo de fechamento). Não publicar este ramo em nenhum site.

## modelos/
- `capa.html` (1200×560): cabeçalho do e-mail. Trocar edição, manchete, subtítulo e data.
- `fluxo.html` (1080 de largura, altura automática): exemplo de fluxograma vertical, com letras grandes para ler no celular.
- `email.html`: corpo do e-mail aprovado (Gmail: usar bgcolor + background-color, nunca o atalho `background:`).
- `render.js`: transforma o HTML em PNG com Playwright.
Imagens publicadas em `AAAA-MM-DD/` e usadas pelo endereço
`https://raw.githubusercontent.com/nnuneslaura-cpu/medsum/radar-imagens/AAAA-MM-DD/<arquivo>.png`.

## Questão da semana
Cada edição guarda em `AAAA-MM-DD/questao.json` a questão usada (id no banco MedSum, gabarito, comentário e bônus).
A edição seguinte abre a seção "Resolução da semana passada" com esse arquivo e não repete questões já usadas.
O e-mail usa `{{NOME}}` na saudação; o script de envio (Apps Script) troca pelo primeiro nome de cada inscrito.

## Imagens no rascunho (importante)
O conector do Gmail remove as tags <img> e embrulha os links. Por isso o rascunho NUNCA leva <img>:
use a marcação `{{IMG AAAA-MM-DD/arquivo.png|texto alternativo|largura}}` (620 para a capa, 564 para o corpo).
O script de envio (Apps Script) troca a marcação pela imagem e desembrulha os links na hora de enviar.
