const {useComposition, Easing, animate} = window;

const TEAL = '#153E3B', TEAL_MID = '#1D7A6E', AMBER = '#F0B25A', CREAM = '#F1ECDD', LIGHT = '#EAF4F2', RED = '#E0564B';
const INK = {red: RED, amber: '#C98424', teal: TEAL_MID, grey: '#7A9591'};
const F = "'Noto Sans KR', sans-serif";
const DUR = {hook: 2.8, phone: 3.0, stat: 3.0, compare: 3.2, check: 3.0, cta: 3.2};

const Badge = ({dark}) => (
  <div style={{position: 'absolute', top: 70, right: 60, zIndex: 20, background: dark ? 'rgba(255,255,255,0.14)' : TEAL, color: '#fff', borderRadius: 999, padding: '14px 28px', fontSize: 28, fontWeight: 800}}>휴대폰성지 진또배기 미아점</div>
);
const Banner = ({op, T = 0}) => {
  const CYCLE = 3.0, FADE = 0.35;
  const ph = T % (CYCLE * 2);
  const ease = (x) => Math.min(1, Math.max(0, x));
  const bOp = ph < CYCLE ? ease((ph - (CYCLE - FADE)) / FADE) * 0 + (ph > CYCLE - FADE ? ease((ph - (CYCLE - FADE)) / FADE) : 0) : (ph > CYCLE * 2 - FADE ? 1 - ease((ph - (CYCLE * 2 - FADE)) / FADE) : 1);
  const aOp = 1 - bOp;
  const B = window.RV_BANNER || {};
  const phoneMax = B.phoneMax ? '최대 ' + B.phoneMax : '최대 지원';
  const Item = ({k, v, hi}) => (
    <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 2, flex: 1, minWidth: 0}}>
      <div style={{fontSize: 32, fontWeight: 900, color: TEAL, whiteSpace: 'nowrap'}}>{k}</div>
      <div style={{fontSize: hi ? 50 : 54, fontWeight: 900, color: hi ? '#C98424' : TEAL, letterSpacing: '-0.04em', whiteSpace: 'nowrap'}}>{v}</div>
    </div>
  );
  return (
    <div style={{position: 'absolute', left: 40, right: 40, bottom: 290, opacity: op, borderRadius: 28, overflow: 'hidden', background: '#fff', border: '4px solid ' + TEAL, fontFamily: F, zIndex: 25}}>
      <div style={{position: 'relative'}}>
      <div style={{opacity: aOp, visibility: aOp <= 0.001 ? 'hidden' : 'visible'}}>
      <div style={{display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '18px 30px 6px'}}>
        <span style={{fontSize: 46, fontWeight: 900, color: TEAL, letterSpacing: '-0.04em'}}>놓치면 손해!</span>
        <span style={{fontSize: 26, fontWeight: 800, color: '#fff', background: '#C98424', borderRadius: 999, padding: '6px 18px'}}>지원금 혜택</span>
      </div>
      <div style={{display: 'flex', alignItems: 'center', padding: '6px 14px 16px'}}>
        <Item k="인터넷 · TV" v="52만원" />
        <div style={{width: 2, height: 70, background: '#DCE8E5'}}></div>
        <Item k="정수기 렌탈" v="30만원" />
        <div style={{width: 2, height: 70, background: '#DCE8E5'}}></div>
        <Item k="휴대폰 지원금" v={phoneMax} hi />
      </div>
      </div>
      {bOp > 0.001 ? <div style={{position: 'absolute', inset: 0, opacity: bOp, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 6, background: '#fff'}}>
        <div style={{display: 'flex', alignItems: 'center', gap: 14}}>
          <span style={{fontSize: 38, fontWeight: 900, color: '#fff', background: TEAL, borderRadius: 14, padding: '4px 16px'}}>인터넷·TV · 정수기 렌탈 · 휴대폰</span>
          <span style={{fontSize: 30, fontWeight: 900, color: '#fff', background: '#C98424', borderRadius: 999, padding: '4px 16px'}}>최대</span>
        </div>
        <div style={{display: 'flex', alignItems: 'baseline', gap: 22}}>
          <span style={{fontSize: 74, fontWeight: 900, color: TEAL, letterSpacing: '-0.05em'}}>놓치면 손해!</span>
          <span style={{fontSize: 40, fontWeight: 900, color: '#C98424'}}>최대</span>
          <span style={{fontSize: 92, fontWeight: 900, color: '#C98424', letterSpacing: '-0.05em', lineHeight: 1}}>152<span style={{fontSize: 52}}>만원</span></span>
        </div>
      </div> : null}
      </div>
      <div style={{background: TEAL, color: '#fff', fontSize: 40, fontWeight: 900, textAlign: 'center', padding: '14px 0', letterSpacing: '0.01em'}}>📞 010-7610-8594 · 진또배기 미아점</div>
    </div>
  );
};
const Watermark = () => (
  <img src={(window.OM_ASSETS || {}).badge} alt="" style={{position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%,-50%)', width: '70%', opacity: 0.06, borderRadius: '50%', pointerEvents: 'none'}} />
);
const Scene = ({op, rise, bg, dark, pb = 150, children}) => (
  <div style={{position: 'absolute', inset: 0, opacity: op, visibility: op <= 0.001 ? 'hidden' : 'visible', background: bg, fontFamily: F, overflow: 'hidden'}}>
    <div style={{position: 'absolute', inset: 0, padding: `200px 84px ${pb}px`, boxSizing: 'border-box', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: pb > 300 ? 32 : 44, transform: `translateY(${rise}px)`}}>{children}</div>
  </div>
);
const Tag = ({children, dark}) => (
  <div style={{background: dark ? AMBER : TEAL, color: dark ? TEAL : '#fff', borderRadius: 999, padding: '12px 30px', fontSize: 34, fontWeight: 900}}>{children}</div>
);
const H = ({children, dark, size = 78}) => (
  <div style={{fontSize: size, fontWeight: 900, color: dark ? '#fff' : TEAL, textAlign: 'center', lineHeight: 1.22, letterSpacing: '-0.03em', whiteSpace: 'pre-line', wordBreak: 'keep-all', textWrap: 'balance'}}>{children}</div>
);
const Sub = ({children, dark}) => (
  <div style={{fontSize: 40, fontWeight: 700, color: dark ? '#DCEFEB' : '#3C5E59', textAlign: 'center', lineHeight: 1.5, whiteSpace: 'pre-line', wordBreak: 'keep-all'}}>{children}</div>
);
const Phone = ({w = 290, tilt = 0, glow, children}) => (
  <div style={{width: w, height: w * 2.05, borderRadius: w * 0.16, background: '#0f1115', padding: w * 0.035, boxSizing: 'border-box', transform: `rotate(${tilt}deg)`, flexShrink: 0}}>
    <div style={{width: '100%', height: '100%', borderRadius: w * 0.13, background: '#F4F6F6', overflow: 'hidden', position: 'relative', display: 'flex', flexDirection: 'column'}}>
      <div style={{position: 'absolute', top: w * 0.035, left: '50%', transform: 'translateX(-50%)', width: w * 0.3, height: w * 0.085, borderRadius: 999, background: '#0f1115', zIndex: 3}}></div>
      {children}
    </div>
  </div>
);

const rvHasPhotos = () => ((window.RV_TOPICS || {})[window.RV_TOPIC] || {scenes: []}).scenes.some(sc => sc.photo || sc.photos);
if (rvHasPhotos() && !customElements.get('image-slot') && !document.querySelector('script[data-rv-slot]')) {
  const el = document.createElement('script'); el.src = './image-slot.js'; el.dataset.rvSlot = '1'; document.head.appendChild(el);
}
const Photo = ({id, label, h = 520}) => (
  <div style={{width: '100%', height: h, borderRadius: 32, overflow: 'hidden', background: '#fff', border: '3px solid #DCE8E5', flexShrink: 0, position: 'relative'}}>
    {React.createElement('image-slot', {id: 'rv-' + id, shape: 'rect', fit: 'cover', placeholder: '📷 ' + label, style: {width: '100%', height: '100%', display: 'block'}})}
  </div>
);

function renderScene(sc, s, A) {
  const pop = (t0) => animate({from: 0.85, to: 1, start: t0, end: t0 + 0.45, ease: Easing.easeOutBack})(s.local);
  const fade = (t0) => animate({from: 0, to: 1, start: t0, end: t0 + 0.3})(s.local);
  const pid = (window.RV_TOPIC || 'x') + '-' + s.idx;
  const ph = sc.photo ? <div style={{width: '100%', transform: `scale(${pop(0.15)})`}}><Photo id={pid} label={sc.photo} h={sc.kind === 'phone' ? 440 : 520} /></div> : null;
  const dark = s.dark;
  if (sc.kind === 'hook') {
    const P = ({p, right}) => (
      <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 20}}>
        <Phone w={250} tilt={right ? 6 : -6} glow={right ? 'rgba(240,178,90,0.45)' : null}>
          <div style={{flex: 1, background: right ? 'linear-gradient(160deg,#FCE3B8,#F0B25A)' : 'linear-gradient(160deg,#dfe7e6,#b9c9c6)', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 10, padding: '0 16px', textAlign: 'center'}}>
            {p.top ? <div style={{fontSize: 26, fontWeight: 900, color: RED}}>{p.top}</div> : null}
            <div style={{fontSize: 34, fontWeight: 900, color: TEAL, wordBreak: 'keep-all', lineHeight: 1.3}}>{p.screen}</div>
          </div>
        </Phone>
        <div style={{fontSize: 34, fontWeight: 900, color: right ? AMBER : '#B8D4CF'}}>{p.label}</div>
      </div>
    );
    return (<>
      <Tag dark>{sc.tag}</Tag>
      <H dark size={100}>{sc.title}</H>
      <div style={{display: 'flex', gap: 60, alignItems: 'flex-end', transform: `scale(${pop(0.3)})`}}>
        <P p={sc.left} />
        <div style={{fontSize: 70, fontWeight: 900, color: AMBER, paddingBottom: 260}}>VS</div>
        <P p={sc.right} right />
      </div>
    </>);
  }
  if (sc.kind === 'phone') return (<>
    <Tag>{sc.tag}</Tag>
    <H size={sc.photo ? 66 : 78}>{sc.title}</H>
    {ph}
    <div style={{transform: `scale(${pop(0.3)})`, ...(sc.photo ? {transform: `scale(${0.72 * pop(0.3)})`, margin: '-160px 0'} : {})}}>
      <Phone>
        <div style={{padding: '70px 0 0', flex: 1, display: 'flex', flexDirection: 'column'}}>
          <div style={{fontSize: 26, fontWeight: 900, color: '#2B3B39', padding: '0 24px 14px'}}>{sc.screen}</div>
          <div style={{background: '#fff', margin: '0 14px', borderRadius: 18}}>
            {sc.rows.map(([l, r, c], i) => (
              <div key={l} style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: 10, padding: '17px 20px', borderBottom: i < sc.rows.length - 1 ? '1px solid #E6ECEB' : 'none', fontSize: 23, fontWeight: 700, color: '#2B3B39', opacity: fade(0.45 + i * 0.18)}}>
                <span>{l}</span><span style={{color: INK[c] || TEAL, fontWeight: 900, textAlign: 'right'}}>{r}</span>
              </div>
            ))}
          </div>
          {sc.note ? <div style={{margin: 'auto 18px 26px', background: '#FDF1DC', borderRadius: 16, padding: '16px 18px', fontSize: 22, fontWeight: 800, color: '#8A5E17', lineHeight: 1.4, wordBreak: 'keep-all', opacity: fade(1.2)}}>{sc.note}</div> : null}
        </div>
      </Phone>
    </div>
  </>);
  if (sc.kind === 'stat') return (<>
    <Tag>{sc.tag}</Tag>
    <H size={sc.photo ? 66 : 78}>{sc.title}</H>
    {ph}
    <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: sc.photo ? 14 : 26, background: '#fff', borderRadius: 32, padding: sc.photo ? '30px 40px' : '48px 56px', border: '2px solid #DCE8E5', transform: `scale(${pop(0.3)})`, width: '100%', boxSizing: 'border-box'}}>
      <div style={{fontSize: 46, fontWeight: 900, color: '#9AAFAB', textDecoration: sc.strike ? 'line-through' : 'none', textAlign: 'center'}}>{sc.from}</div>
      <div style={{fontSize: 60, fontWeight: 900, color: AMBER, opacity: fade(0.7)}}>↓</div>
      <div style={{fontSize: 60, fontWeight: 900, color: TEAL_MID, textAlign: 'center', opacity: fade(0.9), wordBreak: 'keep-all'}}>{sc.to}</div>
      {sc.caption ? <div style={{fontSize: 30, fontWeight: 700, color: '#5E837D', textAlign: 'center', wordBreak: 'keep-all'}}>{sc.caption}</div> : null}
    </div>
  </>);
  if (sc.kind === 'compare') return (<>
    <H dark>{sc.title}</H>
    <div style={{display: 'flex', gap: 28, width: '100%'}}>
      {sc.cols.map(([t, items], i) => (
        <div key={t} style={{flex: 1, background: 'rgba(255,255,255,0.09)', borderRadius: 30, padding: '36px 30px', display: 'flex', flexDirection: 'column', gap: 22, transform: `scale(${pop(0.25 + i * 0.2)})`}}>
          {sc.photos ? <Photo id={pid + '-' + i} label={sc.photos[i]} h={380} /> : null}
          <div style={{fontSize: 38, fontWeight: 900, color: i ? '#7FD8C7' : AMBER, lineHeight: 1.3, wordBreak: 'keep-all'}}>{t}</div>
          {items.map(x => <div key={x} style={{fontSize: 34, fontWeight: 700, color: '#fff', lineHeight: 1.4, wordBreak: 'keep-all'}}>· {x}</div>)}
        </div>
      ))}
    </div>
  </>);
  if (sc.kind === 'check') return (<>
    <Tag>{sc.tag || '핵심 정리'}</Tag>
    <H>{sc.title}</H>
    <div style={{width: '100%', background: '#fff', borderRadius: 32, padding: '34px 44px', display: 'flex', flexDirection: 'column', gap: 22, border: '2px solid #DCE8E5', boxSizing: 'border-box'}}>
      {sc.items.map((x, i) => (
        <div key={x} style={{display: 'flex', alignItems: 'center', gap: 22, fontSize: 40, fontWeight: 800, color: TEAL, opacity: fade(0.3 + i * 0.25), wordBreak: 'keep-all'}}>
          <span style={{width: 56, height: 56, borderRadius: 16, background: TEAL_MID, color: '#fff', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 34, flexShrink: 0}}>✓</span>{x}
        </div>
      ))}
    </div>
    <Sub>{sc.sub || '📌 저장해두고 필요할 때 다시 보세요'}</Sub>
  </>);
  return (<>
    <H dark size={70}>{sc.title}</H>
    <div style={{background: '#fff', borderRadius: 36, padding: '40px 50px', display: 'flex', alignItems: 'center', gap: 40, width: '100%', boxSizing: 'border-box'}}>
      <img src={A.badge} alt="" style={{width: 200, height: 200, borderRadius: 30, background: TEAL, flexShrink: 0}} />
      <div style={{display: 'flex', flexDirection: 'column', gap: 12}}>
        <div style={{fontSize: 36, fontWeight: 900, color: TEAL, lineHeight: 1.35, wordBreak: 'keep-all'}}>💬 카카오톡 플러스친구 추가 해놓고 시세 대란 알림받으세요!</div>
        <div style={{fontSize: 30, fontWeight: 800, color: TEAL_MID}}>휴대폰성지 진또배기 미아점</div>
      </div>
    </div>
    <div style={{width: '100%', display: 'flex', flexDirection: 'column', gap: 18}}>
      <div style={{background: '#FEE500', borderRadius: 28, padding: '26px 30px', display: 'flex', alignItems: 'center', gap: 22}}>
        <div style={{fontSize: 58, flexShrink: 0}}>💬</div>
        <div style={{display: 'flex', flexDirection: 'column', gap: 6, minWidth: 0}}>
          <div style={{fontSize: 30, fontWeight: 800, color: '#3A1D1D'}}>카카오톡에서 검색하세요</div>
          <div style={{fontSize: 46, fontWeight: 900, color: '#191919', letterSpacing: '-0.03em'}}>진또배기 미아점</div>
        </div>
      </div>
      <div style={{background: AMBER, borderRadius: 28, padding: '26px 30px', display: 'flex', alignItems: 'center', gap: 22}}>
        <div style={{fontSize: 58, flexShrink: 0}}>📞</div>
        <div style={{display: 'flex', flexDirection: 'column', gap: 6}}>
          <div style={{fontSize: 30, fontWeight: 800, color: TEAL}}>전화 · 문자 상담</div>
          <div style={{fontSize: 54, fontWeight: 900, color: TEAL, letterSpacing: '-0.02em'}}>010-7610-8594</div>
        </div>
      </div>
      <div style={{border: '3px solid rgba(255,255,255,0.35)', borderRadius: 28, padding: '22px 30px', display: 'flex', alignItems: 'center', gap: 22}}>
        <div style={{fontSize: 52, flexShrink: 0}}>👆</div>
        <div style={{fontSize: 36, fontWeight: 900, color: '#fff', lineHeight: 1.35, wordBreak: 'keep-all'}}>프로필 링크 누르면<br />바로 카톡 상담 연결</div>
      </div>
    </div>
    <div style={{fontSize: 32, fontWeight: 700, color: '#DCEFEB', textAlign: 'center'}}>📍 서울 강북구 도봉로 143 1층 8호</div>
  </>);
}

function Piece() {
  const {T, CUES} = useComposition();
  const A = window.OM_ASSETS || {};
  const topic = (window.RV_TOPICS || {})[window.RV_TOPIC] || {scenes: []};
  const scenes = topic.scenes;
  const FADE = 0.45;
  let alt = 0, cur = false, ctaOp = 0;
  const layers = (
    <div style={{position: 'absolute', inset: 0, background: CREAM}}>
      {scenes.map((sc, i) => {
        const k = 'S' + (i + 1);
        const cue = CUES[k] ?? 0, span = DUR[sc.kind] || 3, end = cue + span, last = i === scenes.length - 1;
        const fi = i === 0 ? 1 : animate({from: 0, to: 1, start: cue - FADE * 0.5, end: cue + FADE * 0.5, ease: Easing.easeInOutSine})(T);
        const fo = last ? 1 : animate({from: 1, to: 0, start: end - FADE * 0.5, end: end + FADE * 0.5, ease: Easing.easeInOutSine})(T);
        const rise = i === 0 ? 0 : animate({from: 30, to: 0, start: cue - FADE * 0.5, end: cue + 0.6, ease: Easing.easeOutCubic})(T);
        const dark = sc.kind === 'hook' || sc.kind === 'compare' || sc.kind === 'cta';
        const bg = dark ? TEAL : (alt++ % 2 ? CREAM : LIGHT);
        const s = {op: Math.min(fi, fo), rise, local: T - cue, dark, idx: i + 1};
        if (T < cue - 1 || T > end + 1) return null;
        if (s.op > 0.5) cur = dark;
        if (sc.kind === 'cta') ctaOp = Math.max(ctaOp, s.op);
        return <Scene key={k} op={s.op} rise={rise} bg={bg} dark={dark} pb={sc.kind === 'cta' ? 150 : 600}>{renderScene(sc, s, A)}</Scene>;
      })}
    </div>
  );
  return (
    <div style={{position: 'absolute', inset: 0}}>
      {layers}
      <div style={{position: 'absolute', inset: 0, zIndex: 30, pointerEvents: 'none'}}>
        <Watermark />
        <Badge dark={cur} />
        {ctaOp < 0.999 ? <Banner op={1 - ctaOp} T={T} /> : null}
      </div>
    </div>
  );
}

window.VisualReel = function VisualReel() {
  const {CompositionStage} = window;
  return (
    <CompositionStage width={1080} height={1920} scenes={window.OM_SCENES} playback={window.OM_PLAYBACK} bg={CREAM}>
      <Piece />
    </CompositionStage>
  );
};
