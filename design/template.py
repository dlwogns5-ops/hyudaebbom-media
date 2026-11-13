from PIL import Image, ImageDraw, ImageFont
import os
W,H=1080,1920
B='/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'
R='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
M='/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc'
for p in (R,M):
    if not os.path.exists(p): raise SystemExit(p)
def f(p,s): return ImageFont.truetype(p,s,index=1)
BG=(244,241,246); BRAND=(169,34,86); INK=(33,26,37); LINE=(234,223,231); WHITE=(255,255,255); SUB=(110,98,116); KAKAO=(254,229,0)
scenes=[
 dict(tag="휴대뽐 꿀팁", title="매장 안 가고\n휴대폰 바꾸는 법", sub="전국 택배개통, 30초 정리"),
 dict(tag="STEP 1", title="카톡으로\n상담하기", sub="원하는 기종·요금제만\n말씀해 주세요"),
 dict(tag="STEP 2", title="온라인\n신청서 작성", sub="본인인증으로 간단하게"),
 dict(tag="STEP 3", title="기기를\n택배로 받기", sub="집이나 회사에서\n편하게 받기"),
 dict(tag="STEP 4", title="받은 후\n개통 진행", sub="개통되면 바로 사용!\n데이터 이동도 안내해요"),
 dict(tag="상담은 카톡으로", title="카톡에서\n'휴대뽐' 검색", sub="hyudaebbom.netlify.app", cta=True),
]
def ctext(d,y,text,font,fill,gap=20):
    for line in text.split("\n"):
        w=d.textlength(line,font=font); d.text(((W-w)/2,y),line,font=font,fill=fill); y+=font.size+gap
    return y
def header(d):
    d.rectangle((0,0,W,170),fill=WHITE); d.line((0,170,W,170),fill=LINE,width=3)
    lf=f(B,64); tw=d.textlength("휴대뽐",font=lf); x=(W-(100+20+tw))/2
    d.rounded_rectangle((x,35,x+100,135),radius=26,fill=BRAND)
    gf=f(B,66); gw=d.textlength("ㅎ",font=gf); d.text((x+50-gw/2,38),"ㅎ",font=gf,fill=WHITE)
    d.text((x+120,40),"휴대뽐",font=lf,fill=INK)
def banner(d):
    top=H-320
    d.rounded_rectangle((40,top,W-40,H-80),radius=40,fill=BRAND)
    ctext(d,top+30,"놓치면 손해!",f(B,66),WHITE)
    ctext(d,top+130,"인터넷·TV / 정수기 렌탈 혜택",f(R,50),(255,225,236))
os.makedirs('/tmp/reel/f2',exist_ok=True)
for i,s in enumerate(scenes):
    im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im); header(d)
    d.rounded_rectangle((60,260,W-60,1500),radius=56,fill=WHITE,outline=LINE,width=3)
    tf=f(R,46); tw=d.textlength(s['tag'],font=tf)
    d.rounded_rectangle(((W-tw)/2-40,350,(W+tw)/2+40,440),radius=45,fill=(250,232,240))
    d.text(((W-tw)/2,360),s['tag'],font=tf,fill=BRAND)
    y=ctext(d,540,s['title'],f(B,120),INK,28)
    d.rounded_rectangle((W/2-55,y+30,W/2+55,y+42),radius=6,fill=BRAND)
    if s.get('cta'):
        bf=f(B,58); txt="카카오톡 상담"; bw=d.textlength(txt,font=bf)
        d.rounded_rectangle(((W-bw)/2-70,y+100,(W+bw)/2+70,y+230),radius=65,fill=KAKAO)
        d.text(((W-bw)/2,y+122),txt,font=bf,fill=INK)
        ctext(d,y+290,s['sub'],f(M,46),SUB)
    else:
        ctext(d,y+110,s['sub'],f(M,56),SUB,18)
    banner(d); im.save(f'/tmp/reel/f2/s{i}.png')
Image.open('/tmp/reel/f2/s0.png').save('/tmp/reel/cover2.jpg',quality=92)
