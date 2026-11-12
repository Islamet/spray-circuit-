const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1000,height:970},deviceScaleFactor:1});
await p.goto('file://'+process.cwd()+'/sq.html');await p.waitForLoadState('networkidle');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await p.screenshot({path:'scr_sq.png'});await b.close();})();
