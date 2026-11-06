#!/usr/bin/env bash
# E0: index Vaani (metadata only), speaker-disjoint splits, export dev clips, DSP-measure them.
#   bash scripts/01_index_and_dev.sh
set -euo pipefail
VAANI=${VAANI:-$HOME/Vaani/audio}
OUT=${OUT:-data}
for L in hi:Hindi ta:Tamil; do
  lang=${L%%:*}; name=${L##*:}
  python -m rimet2.data.vaani_index index --root "$VAANI/$name" --lang "$lang" --out "$OUT/index_$lang.parquet" \
    | tee "$OUT/index_${lang}_summary.json"
  # 300 dev clips per language (<=3 per speaker, district-stratified) for DevReal; 150 with transcripts
  python -m rimet2.data.vaani_index export --index "$OUT/index_$lang.parquet" --split dev --n 300 \
    --out "$OUT/wav/${lang}_dev"
  python -m rimet2.data.vaani_index measure --wavdir "$OUT/wav/${lang}_dev"
  ls "$OUT/wav/${lang}_dev"/*.wav | awk -v l="$lang" -F/ '{f=$NF; sub(/\.wav$/,"",f); print f"\t"$0"\t"l}' \
    > "$OUT/${lang}_dev.list"
done
echo "Next: annotate a 60-clip subset per language with docs/ANNOTATION_GUIDE.md -> data/rubric_<lang>.csv"
