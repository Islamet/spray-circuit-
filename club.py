from PIL import Image
import numpy as np, cv2
from compose import recolour
orig=np.asarray(Image.open('../src/img-005.png').convert('RGB'))
base=orig.astype(np.float32)
sq=np.asarray(Image.open('scr_sq.png').convert('RGB')).astype(np.float32)
H,W=sq.shape[:2]
dst=np.float32([[1408,504],[1605,498],[1606,699],[1410,691]])
M=cv2.getPerspectiveTransform(np.float32([[0,0],[W,0],[W,H],[0,H]]),dst)
h,w=base.shape[:2]
war=cv2.warpPerspective(sq,M,(w,h),flags=cv2.INTER_AREA)
m=cv2.warpPerspective(np.ones((H,W),np.float32),M,(w,h),flags=cv2.INTER_LINEAR)
# haze from original mist: low saturation + brightness inside screen
hsv=cv2.cvtColor(orig,cv2.COLOR_RGB2HSV).astype(np.float32)
S=hsv[...,1]/255; V=hsv[...,2]/255
haze=np.clip((0.55-S)/0.55,0,1)*np.clip((V-0.25)/0.5,0,1)
haze=cv2.GaussianBlur(haze,(0,0),3)
# only where mist actually is: lower/left part; suppress clouds region at top by limiting to y>600
yy,xx=np.mgrid[0:h,0:w]
haze=haze*np.clip((yy-590)/40,0,1)*0.85
new=war*0.94+12  # slight glass lift
new=new*(1-haze[...,None])+np.array([205,205,210])*haze[...,None]
out=base*(1-m[...,None])+new*m[...,None]
out=out.clip(0,255).astype(np.uint8)
reg=np.zeros((h,w),bool); reg[380:1130,1650:2400]=True; reg[440:720,1680:2110]=False; reg[1040:1200,1600:1800]=False
out=recolour(out,reg,smin=.3,vmin=.2)
reg=np.zeros((h,w),bool); reg[1040:1200,1600:1800]=True
out=recolour(out,reg,hmin=30,smin=.55,vmin=.35)
Image.fromarray(out).save('club_circuit.jpg',quality=92)
Image.fromarray(out).crop((1360,450,1660,760)).resize((600,620)).save('z1.png')
