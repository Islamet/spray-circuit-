from PIL import Image
import numpy as np, cv2
def recolour(rgb, reg, hmin=18, smin=.3, vmin=.18):
    hsv=cv2.cvtColor(rgb,cv2.COLOR_RGB2HSV).astype(np.float32)
    H,S,V=hsv[...,0]*2,hsv[...,1]/255,hsv[...,2]/255
    g=reg&(H>hmin)&(H<60)&(S>smin)&(V>vmin)
    hsv[...,0]=np.where(g,163,hsv[...,0])
    return cv2.cvtColor(hsv.astype(np.uint8),cv2.COLOR_HSV2RGB)
if __name__=="__main__":
    # front-on
    base=np.asarray(Image.open('../src/img-000.png').convert('RGB'))
    reg=np.ones(base.shape[:2],bool); reg[490:1130,2030:3610]=False; reg[400:1300,600:1700]=False; reg[1400:2000,850:1300]=False
    out=Image.fromarray(recolour(base,reg))
    scr=Image.open('scr_home.png').convert('RGB').resize((1001,630),Image.LANCZOS)
    out.paste(Image.blend(scr,Image.fromarray(base).crop((640,528,1641,1158)),0.06),(640,528))
    out.putalpha(Image.open('../src/img-001.png').convert('L')); out.save('machine_circuit.png')
    # club
    base=np.asarray(Image.open('../src/img-005.png').convert('RGB')).astype(np.float32)
    s=Image.open('scr_home.png').convert('RGB'); H=s.size[1]
    sq=np.asarray(s.crop((0,0,H,H)).resize((800,800))).astype(np.float32)
    M=cv2.getPerspectiveTransform(np.float32([[0,0],[800,0],[800,800],[0,800]]),np.float32([[1409,506],[1606,498],[1606,695],[1411,691]]))
    h,w=base.shape[:2]
    war=cv2.warpPerspective(sq,M,(w,h)); m=cv2.GaussianBlur(cv2.warpPerspective(np.ones((800,800),np.float32),M,(w,h)),(3,3),0)
    img=(base*(1-m[...,None])+war*m[...,None]).clip(0,255).astype(np.uint8)
    reg=np.zeros((h,w),bool); reg[380:1130,1650:2400]=True; reg[440:720,1680:2110]=False; reg[1040:1200,1600:1800]=False
    img=recolour(img,reg,smin=.3,vmin=.2)
    reg=np.zeros((h,w),bool); reg[1040:1200,1600:1800]=True
    img=recolour(img,reg,hmin=30,smin=.55,vmin=.35)
    Image.fromarray(img).save('club_circuit.jpg',quality=90)
