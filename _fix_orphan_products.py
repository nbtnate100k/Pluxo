"""One-off cleanup: remove orphaned log markup between page-fullz and page-products."""

path = "index (27).html"

with open(path, "r", encoding="utf-8") as f:
    s = f.read()

start_marker = (
    '            <!-- PRODUCTS / Cards shop -->\n'
    '                            <div class="log-offer-top log-offer-top--coral">'
)

end_anchor = (
    '            <!-- PRODUCTS / Cards shop -->\n'
    '            <div class="page-content" id="page-products" style="display:block;">'
)

idx = s.find(start_marker)
if idx == -1:
    raise SystemExit("start marker not found")

j = s.find(end_anchor)
if j == -1:
    raise SystemExit("end anchor not found")

replacement = (
    '            <!-- PRODUCTS / Cards shop -->\n'
    '            <div class="page-content" id="page-products" style="display:block;">'
)

new_s = s[:idx] + replacement + s[j + len(end_anchor) :]

with open(path, "w", encoding="utf-8") as f:
    f.write(new_s)

print("removed", j - idx, "bytes")
