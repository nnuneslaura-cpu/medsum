// Uso: NODE_PATH=$(npm root -g) node modelos/render.js <arquivo.html> <saida.png> [largura] [altura|auto]
const {chromium}=require('playwright');
(async()=>{const [,,src,out,w='1200',h='auto']=process.argv;const b=await chromium.launch();
const p=await b.newPage({viewport:{width:+w,height:h==='auto'?800:+h}});
await p.goto('file://'+require('path').resolve(src));await p.waitForTimeout(300);
await p.screenshot({path:out,fullPage:h==='auto'});await b.close();})();
