const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:810}});
await p.goto('file://'+process.cwd()+'/brochure.html');await p.waitForLoadState('networkidle');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
await p.pdf({path:'brochure_circuit.pdf',width:'1440px',height:'810px',printBackground:true,preferCSSPageSize:true});await b.close();})();
