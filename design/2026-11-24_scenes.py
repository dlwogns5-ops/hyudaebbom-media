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
tf=f(R,46); t="통신 3사 국정감사 자료"; tw=d.textlength(t,font=tf)
d.rounded_rectangle(((W-tw)/2-40,300,(W+tw)/2+40,392),radius=46,fill=BRAND); d.text(((W-tw)/2,311),t,font=tf,fill=WHITE)
y=rich(d,480,[[("해지한 통신사에",WHITE)],[("내 돈",YEL),("이",WHITE)],[("남아 있을 수도",WHITE)]],110,26)
y=ctext(d,y+50,"아직 주인 못 찾은 돈 30억원\n1분 조회법 알려드려요",f(R,56),(220,210,226),18)
print('hook bottom',y)
scenes.append(im)
scenes.append(card(1,"2026년 6월 기준 · 통신 3사",[[("63만 건",BRAND),(" 주인을",INK)],[("못 찾았어요",INK)]],"5년째 30억원 안팎 그대로\n국정감사 자료 (방통위 제출)",big="30.6억원",body_size=46))
scenes.append(card(2,"조회해 놓고도",[[("환급 신청은",INK)],[("1%도 안 돼요",BRAND)]],"누적 조회 약 215만 건 중\n실제 환급 신청 약 1만 6천 건",big="0.7%",body_size=46))
scenes.append(card(3,"왜 생길까?",[[("해지 후 정산",INK)],[("뒤에 남은 돈",BRAND)]],"요금할인 등에 따른 과납요금\n보증금 같은 선납금\n단말기 할부보증보험료 미환급액",body_size=46))
scenes.append(card(4,"조회 방법",[[("'스마트초이스'",BRAND)],[("검색",INK)]],"환급/혜택 → 통신 미환급액 조회\n이름 · 주민번호 입력 후 통신사 선택\n3사 망 알뜰폰도 같이 조회돼요\n오전 9시~오후 8시 (공휴일 휴무)",body_size=42))
scenes.append(card(5,"돈이 남아 있다면",[[("회원가입 후",INK)],[("환급 신청",BRAND)]],"본인 명의 계좌로만 받을 수 있어요\n미납금이 있으면 빼고 돌려줘요",body_size=46))
scenes.append(card(6,"결론",[[("해지했던 번호",INK)],[("1분만 조회",BRAND)]],"조회는 회원가입 없이 바로 가능\n부모님 · 가족 명의도 같이 확인하세요",body_size=44))
scenes.append(card(7,"폰 바꿀 땐 휴대뽐",[[("계약 전에",INK)],[("총액부터 비교",INK)]],"전국 택배개통 · 기기 먼저 받고 개통",cta=True,body_size=46))
bn=banner(); bn.save(f'{OUT}/banner.png')
for i,s in enumerate(scenes): s.save(f'{OUT}/s{i}.png')
cov=scenes[0].convert('RGBA'); cov.alpha_composite(bn); cov.convert('RGB').save(f'{OUT}/cover.jpg',quality=93)
