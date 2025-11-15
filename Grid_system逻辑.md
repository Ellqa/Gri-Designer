- first define page size: width ___ pt x hight ___ pt
- then, according to the page size, calculate the module number. the module number is the possible prime divisor of both width and hight. e.g. 20 pt x 50 pt, the the possible module number under 20 is 1, 2, 5.
- after we have our module number settled down, we will use this to setup our margin and grid and all other spacing. they are all multiples of module number.
	- margin
		- left, right (can be bound); top, down (can be bound)
	- Grid
		- layout grid (this is fixed to module number we selected before)
		- rows, spacing
		- columns, spacing



---

read below, ignore the above.

input: page_w, page_h, facing, bleed, spine, fs, bl, measure, lang, 
       min_cols=2, max_cols=6, gutter_candidates=[6,8,10,12], 
       margin_ratio=[2,3,3,4]

# 1) module size tied to baseline
m_candidates = [bl, bl/2, 2*bl] -> round to integer pt
m = pick_best(m_candidates)  # default bl

# 2) initial content box (page minus bleed/spine if any)
content_w = page_w - left_bleed - right_bleed - spine_allowance
content_h = page_h - top_bleed - bottom_bleed

# 3) margins by ratio, then snap to m
margins_raw = ratio_split(content_box, margin_ratio)
margins = round_to_multiple(margins_raw, m)
Wc = page_w - margins.left - margins.right

# 4) search best (k, g) by line length target
best = None; best_cost = +inf
for k in [min_cols..max_cols]:
  for g in gutter_candidates:
    if g % m != 0: continue  # prefer gutter integer multiple of m
    cw = (Wc - (k-1)*g) / k
    if lang == 'en':
      avg_char_w = 0.5 * fs      # allow override by user
    else: # 'zh'
      avg_char_w = fs
    est_chars = cw / avg_char_w
    cost = abs(est_chars - measure)
    if feasible(cw, g) and cost < best_cost:
      best = (k, g, cw, est_chars); best_cost = cost

# 5) row module
row_module = m   # or 2m/3m by user choice

# 6) output spec (all snapped to multiples of m)
export(GridSpec { m, bl, margins, k, g, cw, row_module, rules... })


