from PIL import Image, ImageDraw, ImageFont
W,H=1080,1920
B='/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'; R='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'; M='/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc'
f=lambda p,s: ImageFont.truetype(p,s,index=1)
BG=(244,241,246); BRAND=(169,34,86); INK=(33,26,37); LINE=(234,223,231); WHITE=(255,255,255); SUB=(110,98,116); PINK=(250,232,240); YEL=(254,229,0)
N=7
def header(d,dark=False):
    if not dark: d.rectangle((0,0,W,170),fill=WHITE); d.line((0,170,W,170),fill=LINE,width=3)
    lf=f(B,60); tw=d.textlength("휴대뽐",font=lf); x=(W-(96+18+tw))/2
    d.rounded_rectangle((x,37,x+96,133),radius=26,fill=BRAND)
    gf=f(B,62); gw=d.textlength("ㅎ",font=gf); d.text((x+48-gw/2,38),"ㅎ",font=gf,fill=WHITE)
    d.text((x+114,40),"휴대뽐",font=lf,fill=WHITE if dark else INK)
def banner(d):
    top=H-320; d.rounded_rectangle((40,top,W-40,H-80),radius=40,fill=BRAND)
    def c(y,t,fo,fi):
        w=d.textlength(t,font=fo); d.text(((W-w)/2,y),t,font=fo,fill=fi)
    c(top+30,"놓치면 손해!",f(B,66),WHITE); c(top+130,"인터넷·TV / 정수기 렌탈 혜택",f(R,50),(255,225,236))
def dots(d,i,y=1500):
    w=34; g=14; total=N*w+(N-1)*g+40; x=(W-total)/2
    for k in range(N):
        ww=w+40 if k==i else w; d.rounded_rectangle((x,y,x+ww,y+12),radius=6,fill=BRAND if k==i else LINE); x+=ww+g
def rich(d,y,lines,size,gap=24,font=B):
    # lines: list of list of (text,color)
    fo=f(font,size)
    for segs in lines:
        tw=sum(d.textlength(t,font=fo) for t,_ in segs); x=(W-tw)/2
        for t,col in segs: d.text((x,y),t,font=fo,fill=col); x+=d.textlength(t,font=fo)
        y+=size+gap
    return y
def ctext(d,y,text,fo,fi,gap=18):
    for l in text.split("\n"):
        w=d.textlength(l,font=fo); d.text(((W-w)/2,y),l,font=fo,fill=fi); y+=fo.size+gap
    return y
def card(i,tag,title_lines,body,big=None,cta=False):
    im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im); header(d)
    d.rounded_rectangle((60,250,W-60,1560),radius=56,fill=WHITE,outline=LINE,width=3)
    tf=f(R,46); tw=d.textlength(tag,font=tf)
    d.rounded_rectangle(((W-tw)/2-40,320,(W+tw)/2+40,410),radius=45,fill=PINK); d.text(((W-tw)/2,330),tag,font=tf,fill=BRAND)
    y=470
    if big=="X":
        cx=W/2; d.ellipse((cx-110,y,cx+110,y+220),fill=PINK); d.line((cx-50,y+60,cx+50,y+160),fill=BRAND,width=24); d.line((cx+50,y+60,cx-50,y+160),fill=BRAND,width=24); y+=270; big=None
    if big:
        y=rich(d,y,[[(big,BRAND)]],230,10)+40
    y=rich(d,y,title_lines,104,22)
    if title_lines: d.rounded_rectangle((W/2-55,y+20,W/2+55,y+32),radius=6,fill=BRAND)
    y=ctext(d,y+90,body,f(M,54),SUB,20)
    if cta:
        bf=f(B,58); bt="카카오톡 상담"; bw=d.textlength(bt,font=bf)
        d.rounded_rectangle(((W-bw)/2-70,y+40,(W+bw)/2+70,y+170),radius=65,fill=YEL); d.text(((W-bw)/2,y+62),bt,font=bf,fill=INK)
        ctext(d,y+215,"hyudaebbom.netlify.app",f(M,44),SUB)
    dots(d,i); banner(d); return im
scenes=[]
# 0 hook dark
im=Image.new('RGB',(W,H),INK); d=ImageDraw.Draw(im); header(d,dark=True)
tf=f(R,48); t="⚠ 확인 안 하면 매달 손해"; t="확인 안 하면 매달 손해"; tw=d.textlength(t,font=tf)
d.rounded_rectangle(((W-tw)/2-40,330,(W+tw)/2+40,425),radius=48,fill=BRAND); d.text(((W-tw)/2,341),t,font=tf,fill=WHITE)
y=rich(d,520,[[("약정 끝난 폰,",WHITE)],[("그냥",YEL),(" 쓰고",WHITE)],[("계세요?",WHITE)]],128,26)
ctext(d,y+60,"요금 25% 할인,\n신청 안 하면 못 받아요",f(R,60),(220,210,226),20)
banner(d); scenes.append(im)
scenes.append(card(1,"선택약정 할인이란?",[[("지원금 대신",INK)],[("매달 요금 할인",INK)]],"12개월·24개월 약정\n둘 다 할인율은 같아요",big="25%"))
scenes.append(card(2,"여기서 많이 놓쳐요",[[("자동으로",INK)],[("안 ",INK),("돼요",BRAND)]],"약정이 끝나면 할인도 끝\n다시 신청해야 적용돼요",big="X"))
im=card(3,"이런 폰도 대상",[],"",)
d=ImageDraw.Draw(im); fo=f(B,96); y=500
for t in ["약정 끝난 폰","자급제폰","중고폰"]:
    x=200; d.ellipse((x,y+10,x+100,y+110),fill=BRAND); d.line((x+25,y+62,x+45,y+82),fill=WHITE,width=14); d.line((x+45,y+82,x+80,y+38),fill=WHITE,width=14)
    d.text((x+140,y-5),t,font=fo,fill=INK); y+=160
ctext(d,y+40,"지원금 안 받은 폰이면\n확인해 볼 만해요",f(M,54),SUB,20)
scenes.append(im)
scenes.append(card(4,"확인하는 법",[[("114에 전화해서",INK)],[("이렇게 물어보세요",INK)]],"\"선택약정 25%\n적용 중인가요?\"\n\n스마트초이스에서도 조회 가능"))
scenes.append(card(5,"꼭 해드리세요",[[("부모님 폰",BRAND)],[("지금 확인!",INK)]],"같은 폰 3~4년 쓰셨다면\n할인 없이 내고 계실 수도"))
scenes.append(card(6,"폰 바꿀 땐 휴대뽐",[[("카톡에서",INK)],[("'휴대뽐' 검색",INK)]],"전국 택배개통 · 기기 먼저 받고 개통",cta=True))
for i,s in enumerate(scenes): s.save(f'/tmp/r3/s{i}.png')
scenes[0].save('/tmp/r3/cover.jpg',quality=93)
