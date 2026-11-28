from PIL import Image, ImageDraw, ImageFont
import os
OUT='/home/claude/build/out'; os.makedirs(OUT,exist_ok=True)
W,H=1080,1920
B='/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'; R='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'; M='/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc'
f=lambda p,s: ImageFont.truetype(p,s,index=1)
BG=(244,241,246); BRAND=(169,34,86); INK=(33,26,37); LINE=(234,223,231); WHITE=(255,255,255); SUB=(110,98,116); PINK=(250,232,240); YEL=(254,229,0)
NAVY=(22,36,84); ORANGE=(255,122,24); RED=(222,36,48); GREY=(130,130,140); LGREY=(222,222,228); BYEL=(255,214,0)
N=8

def header(d,dark=False):
    if not dark: d.rectangle((0,0,W,170),fill=WHITE); d.line((0,170,W,170),fill=LINE,width=3)
    lf=f(B,60); tw=d.textlength("휴대뽐",font=lf); x=(W-(96+18+tw))/2
    d.rounded_rectangle((x,37,x+96,133),radius=26,fill=BRAND)
    gf=f(B,62); gw=d.textlength("ㅎ",font=gf); d.text((x+48-gw/2,38),"ㅎ",font=gf,fill=WHITE)
    d.text((x+114,40),"휴대뽐",font=lf,fill=WHITE if dark else INK)

def dots(d,i,y=1345):
    w=34; g=14; total=N*w+(N-1)*g+40; x=(W-total)/2
    for k in range(N):
        ww=w+40 if k==i else w; d.rounded_rectangle((x,y,x+ww,y+12),radius=6,fill=BRAND if k==i else LINE); x+=ww+g

def rich(d,y,lines,size,gap=22,font=B):
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

def xicon(d,y,size=180):
    cx=W/2; r=size/2; d.ellipse((cx-r,y,cx+r,y+size),fill=PINK)
    k=size*0.22; d.line((cx-k,y+r-k,cx+k,y+r+k),fill=BRAND,width=20); d.line((cx+k,y+r-k,cx-k,y+r+k),fill=BRAND,width=20)
    return y+size+40

def card(i,tag,title_lines,body,big=None,x=False,cta=False,body_size=50):
    im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im); header(d)
    d.rounded_rectangle((60,220,W-60,1400),radius=56,fill=WHITE,outline=LINE,width=3)
    tf=f(R,44); tw=d.textlength(tag,font=tf)
    d.rounded_rectangle(((W-tw)/2-40,280,(W+tw)/2+40,365),radius=42,fill=PINK); d.text(((W-tw)/2,289),tag,font=tf,fill=BRAND)
    def content(d,y):
        if x: y=xicon(d,y)
        if big: y=rich(d,y-10,[[(big,BRAND)]],200,0)+40
        y=rich(d,y,title_lines,92,20)
        if title_lines: d.rounded_rectangle((W/2-55,y+30,W/2+55,y+42),radius=6,fill=BRAND)
        y=ctext(d,y+90,body,f(M,body_size),SUB,18)
        if cta:
            bf=f(B,56); bt="카카오톡 상담"; bw=d.textlength(bt,font=bf)
            d.rounded_rectangle(((W-bw)/2-70,y+30,(W+bw)/2+70,y+150),radius=60,fill=YEL); d.text(((W-bw)/2,y+48),bt,font=bf,fill=INK)
            y=ctext(d,y+180,"hyudaebbom.netlify.app",f(M,42),SUB)
        return y
    hgt=content(ImageDraw.Draw(Image.new('RGB',(W,H))),0)
    y=content(d,max(410,410+(1310-410-hgt)/2))
    print(i,'content bottom',y)
    dots(d,i); return im

def banner():
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    L,Rr=50,W-50; bottom=H-110; strip=96; white_h=250; top=bottom-strip-white_h
    # shadow
    d.rounded_rectangle((L+4,top+8,Rr+4,bottom+8),radius=36,fill=(0,0,0,60))
    d.rounded_rectangle((L,top,Rr,bottom),radius=36,fill=NAVY)
    d.rounded_rectangle((L,top,Rr,bottom-strip),radius=36,fill=WHITE)
    d.rectangle((L,bottom-strip-40,Rr,bottom-strip),fill=WHITE)
    # row1
    d.text((L+40,top+22),"놓치면 손해!",font=f(B,56),fill=NAVY)
    pf=f(B,38); pt="지원금 혜택"; pw=d.textlength(pt,font=pf)
    d.rounded_rectangle((Rr-40-pw-56,top+28,Rr-40,top+92),radius=32,fill=ORANGE); d.text((Rr-40-pw-28,top+34),pt,font=pf,fill=WHITE)
    # row2
    cols=[("인터넷 · TV","52만원",NAVY),("정수기 렌탈","30만원",NAVY),("휴대폰 지원금","최대 지원",RED)]
    cw=(Rr-L)/3; ry=top+112
    for k,(lab,val,col) in enumerate(cols):
        cx=L+cw*k+cw/2
        lf=f(R,32); lw=d.textlength(lab,font=lf); d.text((cx-lw/2,ry),lab,font=lf,fill=GREY)
        vf=f(B,52); vw=d.textlength(val,font=vf); d.text((cx-vw/2,ry+46),val,font=vf,fill=col)
        if k: d.line((L+cw*k,ry+6,L+cw*k,ry+112),fill=LGREY,width=3)
    sf=f(B,40); st="카톡 '휴대뽐' 검색 · 전국 택배개통"; sw=d.textlength(st,font=sf)
    d.text(((W-sw)/2,bottom-strip+16),st,font=sf,fill=BYEL)
    print('banner top',top)
    return im

scenes=[]
# 0 hook (dark)
im=Image.new('RGB',(W,H),INK); d=ImageDraw.Draw(im); header(d,dark=True)
tf=f(R,46); t="같은 통신사 2년 넘게 쓰셨다면"; tw=d.textlength(t,font=tf)
d.rounded_rectangle(((W-tw)/2-40,300,(W+tw)/2+40,392),radius=46,fill=BRAND); d.text(((W-tw)/2,311),t,font=tf,fill=WHITE)
y=rich(d,480,[[("오래 쓴 고객만",WHITE)],[("받는 데이터",YEL)],[("챙기셨나요?",WHITE)]],106,26)
y=ctext(d,y+50,"직접 눌러야 받는 혜택도 있어요\n통신 3사 장기고객 혜택 정리",f(R,56),(220,210,226),18)
print('hook bottom',y)
scenes.append(im)
scenes.append(card(1,"장기고객 혜택",[[("오래 쓴 만큼",INK)],[("쿠폰이 늘어요",BRAND)]],"가입 기간이 길수록\n데이터 쿠폰 개수가 많아져요\n통신 3사 모두 운영 중",body_size=44))
scenes.append(card(2,"SKT · 2년 이상",[[("리필 쿠폰",INK)],[("1년에 4~6장",BRAND)]],"2년 4장 · 3년 5장 · 4년 이상 6장\n기본 데이터를 한 번 더 채워줘요\nT world 앱 → '리필하기'",body_size=44))
scenes.append(card(3,"SKT · 가입 기념일",[[("가입 연수만큼",INK)],[("데이터 GB",BRAND)]],"가입한 달에 2년이면 2GB, 10년이면 10GB\n자동 지급 · 다음 달 1일 0시까지 사용\n(2026년 7월부터 2년 이상 고객)",body_size=42))
scenes.append(card(4,"KT · 합산 5년 이상",[[("쿠폰 6~10장",INK)],[("골라서 받기",BRAND)]],"모바일·인터넷·TV 합산 기간 기준\n5년 6장 · 10년 8장 · 20년 10장\n데이터 2GB · 통화 100분 등 중 선택",body_size=44))
scenes.append(card(5,"LG유플러스 · 2년 이상",[[("데이터 쿠폰",INK)],[("1년에 4~6장",BRAND)]],"2년 이상 4장 · 4년 이상 6장\n통신사 앱 혜택 메뉴에서\n남은 쿠폰부터 확인하세요",body_size=44))
scenes.append(card(6,"무제한 요금제라면",[[("데이터 쿠폰은",INK)],[("쓸 일 없어요",BRAND)]],"대신 공연·전시 할인, 초청 행사,\n멤버십 등급 혜택을 챙기세요\n추첨형 행사는 응모해야 받아요",x=True,body_size=44))
scenes.append(card(7,"폰 바꿀 땐 휴대뽐",[[("옮기기 전에",INK)],[("총액부터 비교",BRAND)]],"전국 택배개통 · 기기 먼저 받고 개통",cta=True,body_size=46))
bn=banner(); bn.save(f'{OUT}/banner.png')
for i,s in enumerate(scenes): s.save(f'{OUT}/s{i}.png')
cov=scenes[0].convert('RGBA'); cov.alpha_composite(bn); cov.convert('RGB').save(f'{OUT}/cover.jpg',quality=93)
