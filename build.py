"""Build the reviewed GekiChuMai PMS table from committed metadata snapshots."""
import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ALLOWED = {str(i) for i in range(1, 46)} | {'45+'}

def read(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8-sig'))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base-url', default='')
    args = parser.parse_args()
    normal = read('source-normal.json')
    by_hash = {r['md5']: r for r in normal if r['md5']}
    for entry in read('supplemental-charts.json'):
        r = entry['record']
        assert r['md5'] not in by_hash
        assert r['comment'].endswith('→' + entry['level'])
        by_hash[r['md5']] = dict(r, level=entry['level'],
            comment=entry['chart'] + ' — ' + r['comment'] + ' · Excluded upstream for BGA gore; rating retained from source comment.',
            source_url=entry['source_url'], source_category=r['level'])
    catalog = read('catalog.json')
    rows, mapping = [], {}
    for song in catalog:
        selected = [by_hash[h] for h in song['chart_md5']]
        assert song['evidence'] and song['games']
        for row in selected:
            assert row['level'] in ALLOWED
            assert row['md5'] not in mapping
            mapping[row['md5']] = song['name']
        song['count'] = len(selected)
        song['levels'] = sorted({r['level'] for r in selected}, key=lambda x: 46 if x == '45+' else int(x))
        rows.extend(selected)
    rows.sort(key=lambda r: (46 if r['level'] == '45+' else int(r['level']), r['title'].casefold(), r['md5']))
    base = args.base_url.rstrip('/')
    url = lambda f: base + '/' + f if base else f
    dist = ROOT / 'dist'
    dist.mkdir(exist_ok=True)
    header = dict(name='GekiChuMai × PMS — Beginner / Normal (1–45+)', symbol='GCM Lv',
                  data_url=url('data.json'), level_order=list(range(1,46))+['45+'])
    payload = dict(rows=rows, catalog=catalog, mapping=mapping, snapshot='2026-10-12')
    for name, value in [('data.json', rows), ('header.json', header), ('catalog-report.json', catalog)]:
        (dist / name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    (dist / 'data.js').write_text('window.PMS_DATA = '+json.dumps(payload, ensure_ascii=False).replace('<', '\\u003c')+';\n', encoding='utf-8')
    page = (ROOT / 'page.html').read_text(encoding='utf-8')
    (dist / 'index.html').write_text(page.replace('@@HEADER_URL@@', html.escape(url('header.json'), quote=True)), encoding='utf-8')
    summary = dict(source_charts=len(normal), charts=len(rows), songs=sum(bool(s['count']) for s in catalog),
                   charts_up_to_20=sum(int(r['level'].rstrip('+')) <= 20 for r in rows),
                   five_button_charts=sum('5BUTTONS' in r['title'] for r in rows),
                   touhou_songs=sum(s['touhou'] and bool(s['count']) for s in catalog))
    (ROOT / 'build-summary.json').write_text(json.dumps(summary, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(summary))

if __name__ == '__main__':
    main()
