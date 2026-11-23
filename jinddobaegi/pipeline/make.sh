#!/usr/bin/env bash
# 진또배기 주간 릴스 렌더러
# 사용법: bash make.sh "2026-12-06|주제이름|topicKey" "2026-12-07|...|..." ...
#  - topicKey 는 template/reels-visual-topics.js 의 RV_TOPICS 키 (먼저 추가해 둘 것)
#  - 결과: jinddobaegi/media/<날짜>/reel.mp4, cover.jpg
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
WORK="${WORK:-/tmp/jdb-render}"
mkdir -p "$WORK/render/assets" "$WORK/lib"
cp "$HERE"/template/{support.js,animations-v3.jsx,reels-visual.jsx,image-slot.js,reels-visual-topics.js} "$WORK/render/"
cp "$HERE"/template/assets/badge-sm.png "$WORK/render/assets/"
if [ ! -d "$WORK/lib/node_modules/react" ]; then
  (cd "$WORK/lib" && npm init -y >/dev/null && npm i react@18.3.1 react-dom@18.3.1 @babel/standalone@7.29.0 >/dev/null 2>&1)
fi
export LIBS="$WORK/lib/node_modules"
for item in "$@"; do
  IFS='|' read -r DATE NAME TOPIC <<< "$item"
  PAGE="reel-$DATE.dc.html"
  python3 - "$HERE/template/page-template.dc.html" "$WORK/render/$PAGE" "$WORK/render/reels-visual-topics.js" "$TOPIC" "$NAME" <<'EOF'
import sys,json,re,subprocess
tpl,out,topics,key,name=sys.argv[1:]
DUR={'hook':2.8,'phone':3.0,'stat':3.0,'compare':3.2,'check':3.0,'cta':3.2}
js="global.window={};eval(require('fs').readFileSync(%s,'utf8'));const t=window.RV_TOPICS[%s];if(!t)throw new Error('topic missing');console.log(JSON.stringify(t.scenes.map(s=>[s.kind,(s.title||'').replace(/\\n/g,' ')])))"%(json.dumps(topics),json.dumps(key))
sc=json.loads(subprocess.check_output(['node','-e',js]))
scenes=[{"name":f"S{i+1}","dur":DUR[k],"desc":f"{i+1:02d} "+('진또배기 카카오톡 CTA' if k=='cta' else t)} for i,(k,t) in enumerate(sc)]
h=open(tpl,encoding='utf-8').read()
h=re.sub(r"window\.RV_TOPIC = '.*?'",f"window.RV_TOPIC = '{key}'",h)
h=re.sub(r"window\.OM_SCENES = '.*?';",lambda m:"window.OM_SCENES = '"+json.dumps(scenes,ensure_ascii=False)+"';",h)
h=re.sub(r"<title>.*?</title>",f"<title>주간 릴스 {name}</title>",h)
open(out,'w',encoding='utf-8').write(h)
print(key, sum(DUR[k] for k,_ in sc))
EOF
  F="$WORK/frames/$DATE"; rm -rf "$F"
  node "$HERE/rec.js" "$WORK/render" "$PAGE" "$F" 30 2> "$WORK/rec-$DATE.log"
  if grep -q ERR "$WORK/rec-$DATE.log"; then cat "$WORK/rec-$DATE.log"; exit 1; fi
  D=$(python3 -c "import re;print(re.search(r'dur ([0-9.]+)',open('$WORK/rec-$DATE.log').read()).group(1))")
  OUT="$ROOT/media/$DATE"; mkdir -p "$OUT"
  ffmpeg -y -loglevel error -framerate 30 -i "$F/f%04d.jpg" -f lavfi -t "$D" -i anullsrc=r=44100:cl=stereo \
    -vf "scale=1080:1920,format=yuv420p" -c:v libx264 -preset veryfast -crf 18 -c:a aac -shortest -movflags +faststart "$OUT/reel.mp4"
  ffmpeg -y -loglevel error -ss 1.2 -i "$OUT/reel.mp4" -frames:v 1 -q:v 3 "$OUT/cover.jpg"
  echo "done $DATE $NAME"
done
