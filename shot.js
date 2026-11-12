const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:800},deviceScaleFactor:1.6});
for(const s of ['home','pay','thanks','ad']){await p.goto('file://'+process.cwd()+'/screens.html#'+s);await p.waitForLoadState('networkidle');await p.evaluate(()=>document.fonts.ready);await p.reload();await p.waitForLoadState('networkidle');await p.waitForTimeout(300);await p.screenshot({path:'scr_'+s+'.png'});}
await b.close();})();
