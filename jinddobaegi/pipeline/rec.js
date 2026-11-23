const {chromium}=require('playwright');const fs=require('fs');const path=require('path');const http=require('http');
const [,,root,page,outdir,fpsArg,probe]=process.argv; const fps=+fpsArg||30;
const L=process.env.LIBS;
const srv=http.createServer((q,r)=>{const f=path.join(root,decodeURIComponent(q.url.split('?')[0]));fs.readFile(f,(e,b)=>{if(e){r.writeHead(404);r.end();return;}const ext=path.extname(f);r.writeHead(200,{'content-type':{'.js':'text/javascript','.jsx':'text/javascript','.html':'text/html; charset=utf-8','.png':'image/png'}[ext]||'application/octet-stream'});r.end(b);});}).listen(0);
(async()=>{const port=srv.address().port;const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:1080,height:1920},deviceScaleFactor:1080/1055.25});
await ctx.route(/unpkg\.com/,rt=>{const u=rt.request().url();const m={'react.production.min.js':L+'/react/umd/react.production.min.js','react-dom.production.min.js':L+'/react-dom/umd/react-dom.production.min.js','babel.min.js':L+'/@babel/standalone/babel.min.js'};for(const k in m)if(u.endsWith(k))return rt.fulfill({path:m[k],contentType:'text/javascript'});rt.abort();});
await ctx.route(/fonts\.(googleapis|gstatic)\.com/,rt=>rt.abort());
const p=await ctx.newPage();p.on('pageerror',e=>console.error('ERR',e.message));
await p.goto(`http://127.0.0.1:${port}/${encodeURIComponent(page)}`);
const sel='[data-om-exportable-video-with-duration-secs]';await p.waitForSelector(sel,{timeout:60000});await p.waitForTimeout(1500);
const dur=+(await p.getAttribute(sel,'data-om-exportable-video-with-duration-secs'));
const el=await p.$(sel);const bb=await el.boundingBox();console.error('dur',dur,'box',JSON.stringify(bb));
const seek=t=>p.evaluate(([s,t])=>{document.querySelector(s).dispatchEvent(new CustomEvent('data-om-seek-to-time-frame',{detail:{time:t,sync:true}}));},[sel,t]);
fs.mkdirSync(outdir,{recursive:true});
const times= probe? probe.split(',').map(Number) : Array.from({length:Math.round(dur*fps)},(_,i)=>i/fps);
let i=0;for(const t of times){await seek(t);await p.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>r())));await el.screenshot({path:path.join(outdir,`f${String(i).padStart(4,'0')}.jpg`),type:'jpeg',quality:90});i++;}
await b.close();srv.close();})();
