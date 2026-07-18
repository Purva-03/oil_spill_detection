import streamlit as st

# 🔥 MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="OilSense — Spill Detection AI",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── GLOBAL CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');

:root {
    --bg:        #f4f6fa;
    --surface:   #ffffff;
    --card:      #ffffff;
    --border:    #dde3ef;
    --accent:    #e84118;
    --accent2:   #f39c12;
    --safe:      #27ae60;
    --info:      #2980b9;
    --text:      #1a1f2e;
    --muted:     #6b7a99;
    --red:       #c0392b;
    --font-head: 'Syne', sans-serif;
    --font-mono: 'Space Mono', monospace;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: var(--font-mono);
}

#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid var(--border);
    box-shadow: 2px 0 12px rgba(0,0,0,0.06);
}
[data-testid="stSidebar"] * { color: var(--text) !important; }

/* ── Top banner ── */
.top-banner {
    background: linear-gradient(135deg, #ffffff 0%, #eef2fb 50%, #ffffff 100%);
    border: 1px solid var(--border);
    border-bottom: 3px solid var(--accent);
    border-radius: 12px;
    padding: 24px 32px 18px;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 2px 16px rgba(0,0,0,0.07);
}
.top-banner::before {
    content: '';
    position: absolute;
    top: -40%;
    right: -5%;
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, rgba(232,65,24,0.07) 0%, transparent 70%);
    pointer-events: none;
}
.banner-title {
    font-family: var(--font-head);
    font-weight: 800;
    font-size: 2.4rem;
    color: #1a1f2e;
    letter-spacing: -1px;
    margin: 0;
    line-height: 1.1;
}
.banner-title span { color: var(--accent); }
.banner-sub {
    font-size: 0.72rem;
    color: var(--muted);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 6px;
}
.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(39,174,96,0.1);
    border: 1px solid rgba(39,174,96,0.35);
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.68rem;
    color: var(--safe);
    margin-top: 10px;
}
.pulse { animation: pulse 1.8s infinite; }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.3} }

/* ── Metric cards ── */
.metric-row { display: flex; gap: 14px; margin-bottom: 24px; flex-wrap: wrap; }
.metric-card {
    flex: 1;
    min-width: 140px;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 18px 20px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.metric-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
}
.metric-card.red::after   { background: var(--red); }
.metric-card.amber::after { background: var(--accent2); }
.metric-card.blue::after  { background: var(--info); }
.metric-card.green::after { background: var(--safe); }
.metric-label { font-size: 0.60rem; letter-spacing: 2px; text-transform: uppercase; color: var(--muted); }
.metric-value { font-family: var(--font-head); font-size: 1.9rem; font-weight: 800; margin: 4px 0 0; color: var(--text); }
.metric-unit  { font-size: 0.68rem; color: var(--muted); }

/* ── Section headers ── */
.section-header {
    font-family: var(--font-head);
    font-size: 0.63rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--accent);
    border-bottom: 1px solid var(--border);
    padding-bottom: 8px;
    margin: 28px 0 16px;
}

/* ── Alert boxes ── */
.alert {
    border-radius: 8px;
    padding: 14px 18px;
    font-size: 0.82rem;
    margin: 14px 0;
    display: flex;
    align-items: flex-start;
    gap: 12px;
}
.alert.danger  { background: #fdecea; border: 1px solid #f5c6c2; color: #922b21; }
.alert.warning { background: #fef9e7; border: 1px solid #f9e4a0; color: #7d6608; }
.alert.safe    { background: #eafaf1; border: 1px solid #a9dfbf; color: #1e8449; }
.alert.info    { background: #eaf4fb; border: 1px solid #a9cce3; color: #1a5276; }
.alert-icon { font-size: 1.2rem; flex-shrink: 0; }
.alert-title { font-family: var(--font-head); font-weight: 600; margin-bottom: 3px; }
.alert-body  { font-size: 0.75rem; opacity: 0.9; }

/* ── GAN panel ── */
.gan-panel {
    background: #f0f6ff;
    border: 1px solid #c5d9f1;
    border-left: 3px solid var(--info);
    border-radius: 8px;
    padding: 18px 20px;
    margin: 14px 0;
}
.gan-title {
    font-family: var(--font-head);
    font-size: 0.68rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--info);
    margin-bottom: 12px;
}
.gan-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
.gan-key { font-size: 0.72rem; color: var(--muted); }
.gan-val { font-family: var(--font-head); font-size: 0.85rem; font-weight: 600; color: var(--text); }
.bar-wrap { background: #dde3ef; border-radius: 3px; height: 6px; margin-top: 4px; }
.bar-fill { height: 6px; border-radius: 3px; transition: width 0.6s ease; }

/* ── Drive panel ── */
.drive-panel {
    background: #f0fff4;
    border: 1px solid #a9dfbf;
    border-left: 3px solid var(--safe);
    border-radius: 8px;
    padding: 18px 20px;
    margin: 14px 0;
}
.drive-title {
    font-family: var(--font-head);
    font-size: 0.68rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--safe);
    margin-bottom: 12px;
}
.path-box {
    font-size: 0.70rem;
    color: var(--text);
    background: #eef2fb;
    padding: 6px 10px;
    border-radius: 4px;
    margin-bottom: 10px;
    font-family: var(--font-mono);
    word-break: break-all;
    border: 1px solid var(--border);
}
.folder-tree {
    font-size: 0.68rem;
    color: var(--muted);
    font-family: var(--font-mono);
    line-height: 2;
    background: #f4f6fa;
    padding: 10px 14px;
    border-radius: 6px;
    border: 1px solid var(--border);
    margin-top: 8px;
}

/* ── Risk badge ── */
.risk-badge {
    display: inline-block;
    padding: 5px 14px;
    border-radius: 4px;
    font-family: var(--font-head);
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}
.risk-critical { background: #fdecea; border: 1px solid var(--red);    color: var(--red); }
.risk-high     { background: #fef0eb; border: 1px solid var(--accent);  color: var(--accent); }
.risk-medium   { background: #fef9e7; border: 1px solid var(--accent2); color: #9a7d0a; }
.risk-low      { background: #eafaf1; border: 1px solid var(--safe);    color: var(--safe); }

/* ── Class legend ── */
.legend-row { display:flex; gap:10px; flex-wrap:wrap; margin:10px 0; }
.legend-item { display:flex; align-items:center; gap:6px; font-size:0.72rem; color:var(--muted); }
.legend-dot  { width:10px; height:10px; border-radius:50%; }

/* ── Upload area ── */
[data-testid="stFileUploader"] {
    background: #ffffff !important;
    border: 2px dashed var(--border) !important;
    border-radius: 10px !important;
    padding: 20px !important;
}
[data-testid="stFileUploader"]:hover {
    border-color: var(--accent) !important;
}

/* ── Buttons ── */
.stButton > button {
    background: var(--accent) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 6px !important;
    font-family: var(--font-mono) !important;
    font-size: 0.78rem !important;
    letter-spacing: 1px !important;
    padding: 10px 20px !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    background: #c0392b !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 16px rgba(232,65,24,0.25) !important;
}

/* ── Link button ── */
.stLinkButton > a {
    background: var(--safe) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 6px !important;
    font-family: var(--font-mono) !important;
    font-size: 0.78rem !important;
    letter-spacing: 1px !important;
    padding: 10px 20px !important;
    transition: all 0.2s !important;
    text-decoration: none !important;
}
.stLinkButton > a:hover {
    background: #1e8449 !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 16px rgba(39,174,96,0.25) !important;
}

/* ── Tabs ── */
[data-baseweb="tab-list"] {
    background: #f4f6fa !important;
    border-bottom: 1px solid var(--border) !important;
    gap: 4px;
}
[data-baseweb="tab"] {
    font-family: var(--font-mono) !important;
    font-size: 0.72rem !important;
    letter-spacing: 1px !important;
    color: var(--muted) !important;
    background: transparent !important;
    border-radius: 0 !important;
}
[aria-selected="true"] {
    color: var(--accent) !important;
    border-bottom: 2px solid var(--accent) !important;
}

/* ── Images ── */
[data-testid="stImage"] img {
    border-radius: 8px;
    border: 1px solid var(--border);
    box-shadow: 0 2px 8px rgba(0,0,0,0.07);
}

/* ── Selectbox / slider ── */
[data-baseweb="select"] div,
[data-baseweb="select"] span { color: var(--text) !important; }

/* ── Text area ── */
textarea {
    background: #ffffff !important;
    color: var(--text) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    font-family: var(--font-mono) !important;
    font-size: 0.75rem !important;
}
</style>
""", unsafe_allow_html=True)

import cv2
import numpy as np
import torch
import segmentation_models_pytorch as smp
from PIL import Image
import io
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import ListedColormap
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# ─── CONSTANTS ────────────────────────────────────────────────────────────────
DEVICE      = "cuda" if torch.cuda.is_available() else "cpu"
MODEL_PATH  = "/Users/shivanisunilwaghmare/Desktop/oilspill/best_model.pth"
NUM_CLASSES = 4

# ── Replace with your actual Google Drive shared folder link ──
GAN_DRIVE_FOLDER_URL = "https://drive.google.com/drive/folders/1OdJ6QyQp4Sodg2PCoXMOrqNRDfdpZIdT?usp=share_link"

CLASS_INFO = {
    0: {"name": "Background / Sea",  "color": [180, 210, 240], "hex": "#b4d2f0"},
    1: {"name": "Oil Spill",         "color": [192, 57,  43],  "hex": "#c0392b"},
    2: {"name": "Look-alike",        "color": [243, 156, 18],  "hex": "#f39c12"},
    3: {"name": "Ship / Object",     "color": [41,  128, 185], "hex": "#2980b9"},
}

# ─── BANNER ───────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="top-banner">
  <p class="banner-sub">AI-Powered SAR Image Analysis</p>
  <h1 class="banner-title"><span>Oil</span>Sense — Detection System</h1>
  <div class="status-pill">
    <span class="pulse">●</span> MODEL ONLINE &nbsp;|&nbsp; DEVICE: {DEVICE.upper()} &nbsp;|&nbsp; {datetime.now().strftime("%Y-%m-%d %H:%M")}
  </div>
</div>
""", unsafe_allow_html=True)

# ─── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<p class="section-header">⚙ Detection Settings</p>', unsafe_allow_html=True)
    confidence_threshold = st.slider("Confidence Threshold", 0.1, 0.9, 0.5, 0.05,
                                      help="Minimum confidence to classify a pixel as oil")
    overlay_alpha        = st.slider("Mask Overlay Opacity", 0.1, 0.9, 0.35, 0.05)
    spill_sensitivity    = st.select_slider("Spill Sensitivity",
                                             options=["Low", "Medium", "High", "Max"],
                                             value="Medium")

    st.markdown('<p class="section-header">📊 Output Options</p>', unsafe_allow_html=True)
    show_heatmap       = st.toggle("Show Probability Heatmap", value=True)
    show_class_dist    = st.toggle("Show Class Distribution",  value=True)
    show_contours      = st.toggle("Highlight Spill Contours", value=True)
    enable_reports     = st.toggle("Generate Report Summary",  value=True)

    st.markdown('<p class="section-header">ℹ System Info</p>', unsafe_allow_html=True)
    st.markdown(f"""
    <div style="font-size:0.68rem; color:var(--muted); line-height:2.2;">
    Model: <span style="color:var(--text);font-weight:600">DeepLabV3+ + EfficientNet-b3</span><br>
    Input: <span style="color:var(--text);font-weight:600">256×256 px</span><br>
    Classes: <span style="color:var(--text);font-weight:600">{NUM_CLASSES}</span><br>
    Framework: <span style="color:var(--text);font-weight:600">PyTorch + SMP</span>
    </div>
    """, unsafe_allow_html=True)

# ─── MODEL LOADING ────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    model = smp.DeepLabV3Plus(
    encoder_name="efficientnet-b3",
    encoder_weights=None,
    in_channels=3,
    classes=4)
    try:
        checkpoint = torch.load(MODEL_PATH, map_location=DEVICE)

        if isinstance(checkpoint, dict) and "model_state_dict" in checkpoint:
            model.load_state_dict(checkpoint["model_state_dict"])
        else:
            model.load_state_dict(checkpoint)
        
        
        model = model.to(DEVICE).float()
        model.eval()
        return model, True
    except Exception as e:
        return None, str(e)
model, model_status = load_model()

if model_status is not True:
    st.markdown(f"""
    <div class="alert warning">
      <div class="alert-icon">⚠️</div>
      <div>
        <div class="alert-title">Model weights not found</div>
        <div class="alert-body">Could not load <code>{MODEL_PATH}</code>.<br>
        Running in <strong>demo / simulation mode</strong> — all analysis will use synthetic predictions.<br>
        Error: {model_status}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    DEMO_MODE = True
else:
    DEMO_MODE = False

# ─── PROCESSING UTILS ─────────────────────────────────────────────────────────

def preprocess(img_bgr):
    img = cv2.resize(img_bgr, (256, 256))

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = img.astype(np.float32) / 255.0

    mean = np.array([0.485, 0.456, 0.406])
    std  = np.array([0.229, 0.224, 0.225])

    img = (img - mean) / std

    img = img.transpose(2, 0, 1)

    return torch.tensor(img).unsqueeze(0).float()

def predict(img_bgr):

    if DEMO_MODE:

        h, w = 256, 256

        probs = np.random.dirichlet(
            [8, 1, 0.5, 0.3],
            size=(h, w)
        ).transpose(2, 0, 1)

        probs = probs.astype(np.float32)

        cy, cx = h // 2, w // 2
        Y, X = np.ogrid[:h, :w]

        mask_blob = (
            (X - cx)**2 / 2500 +
            (Y - cy)**2 / 1600
        ) < 1

        probs[1][mask_blob] = np.random.uniform(
            0.6,
            0.95,
            mask_blob.sum()
        )

        probs = probs / probs.sum(
            axis=0,
            keepdims=True
        )

        confidence = float(probs.max())

        return (
            np.argmax(probs, axis=0).astype(np.uint8),
            probs,
            confidence
        )

    inp = preprocess(img_bgr).to(DEVICE)

    with torch.no_grad():

        logits = model(inp)

        probs = torch.softmax(logits, dim=1)

        confidence = float(
            probs.max().cpu().numpy()
        )

        probs = probs.squeeze().cpu().numpy()

        pred = torch.argmax(
            logits,
            dim=1
        ).squeeze().cpu().numpy().astype(np.uint8)

    return pred, probs, confidence

def resize_outputs(pred, probs, target_h, target_w):
    pred_r = cv2.resize(pred.astype(np.float32), (target_w, target_h),
                        interpolation=cv2.INTER_LINEAR)
    pred_r = np.round(pred_r).astype(np.uint8)
    probs_r = np.stack([
        cv2.resize(probs[c], (target_w, target_h), interpolation=cv2.INTER_LINEAR)
        for c in range(NUM_CLASSES)
    ])
    return pred_r, probs_r

def colorize(mask):
    h, w = mask.shape
    out = np.zeros((h, w, 3), dtype=np.uint8)
    for k, v in CLASS_INFO.items():
        out[mask == k] = v["color"]
    return out

def draw_contours(img_rgb, mask):
    out = img_rgb.copy()
    oil_mask = (mask == 1).astype(np.uint8) * 255
    contours, _ = cv2.findContours(oil_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(out, contours, -1, (192, 57, 43), 2)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 200:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(out, (x-2, y-2), (x+w+2, y+h+2), (231, 76, 60), 1)
    return out


def classify_oil_type_and_thickness(img_rgb, pred_mask):

    oil_pixels = img_rgb[pred_mask == 1]

    if len(oil_pixels) < 50:
        return {
            "type": "No Oil Detected",
            "thickness_um": 0.0,
            "confidence": 0.0
        }

    hsv = cv2.cvtColor(
        oil_pixels.reshape(-1,1,3).astype(np.uint8),
        cv2.COLOR_RGB2HSV
    )

    H = hsv[:,:,0]
    S = hsv[:,:,1]
    V = hsv[:,:,2]

    mean_h = float(np.mean(H))
    mean_s = float(np.mean(S))
    mean_v = float(np.mean(V))

    hue_std = float(np.std(H))

    # SILVER SHEEN
    if mean_v > 180 and mean_s < 40:

        return {
            "type": "Silver Sheen",
            "thickness_um": 0.075,
            "confidence": 0.85
        }

    # RAINBOW
    elif hue_std > 25 and mean_s > 80:

        return {
            "type": "Rainbow Sheen",
            "thickness_um": 0.20,
            "confidence": 0.80
        }

    # BROWN
    elif 10 < mean_h < 30 and mean_s > 70:

        return {
            "type": "Brown Oil",
            "thickness_um": 1.50,
            "confidence": 0.82
        }

    # BLACK / RED
    elif mean_v < 70:

        return {
            "type": "Black / Red Oil",
            "thickness_um": 5.00,
            "confidence": 0.88
        }

    else:

        return {
            "type": "Mixed Oil",
            "thickness_um": 2.00,
            "confidence": 0.60
        }

def estimate_volume(area_km2, thickness_um):

    area_m2 = area_km2 * 1_000_000

    thickness_m = thickness_um * 1e-6

    volume_m3 = area_m2 * thickness_m

    return volume_m3
    
def compute_area_stats(mask, pixel_size_m=5.0):
    total_px = mask.size
    counts   = {k: int(np.sum(mask == k)) for k in range(NUM_CLASSES)}
    oil_px   = counts[1]
    oil_pct  = oil_px / total_px * 100
    oil_km2  = (oil_px * pixel_size_m ** 2) / 1e6
    return counts, oil_px, oil_pct, oil_km2

def risk_level(oil_pct):
    score = oil_pct / 100
    if score > 0.5:  return "CRITICAL", "risk-critical"
    if score > 0.3:  return "HIGH",     "risk-high"
    if score > 0.1:  return "MEDIUM",   "risk-medium"
    return "LOW", "risk-low"

def build_heatmap_fig(probs, class_idx=1):
    fig, ax = plt.subplots(figsize=(5, 4), facecolor='#ffffff')
    ax.set_facecolor('#f4f6fa')
    im = ax.imshow(probs[class_idx], cmap='YlOrRd', vmin=0, vmax=1)
    cb = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cb.ax.yaxis.set_tick_params(color='#6b7a99')
    plt.setp(cb.ax.yaxis.get_ticklabels(), color='#6b7a99')
    ax.set_title("Oil Probability Map", color='#e84118', fontsize=9, pad=8)
    ax.tick_params(colors='#6b7a99', labelsize=7)
    for spine in ax.spines.values(): spine.set_edgecolor('#dde3ef')
    plt.tight_layout()
    return fig

def build_distribution_fig(counts):
    labels = [CLASS_INFO[k]["name"] for k in range(NUM_CLASSES)]
    values = [counts[k] for k in range(NUM_CLASSES)]
    colors = [f'#{CLASS_INFO[k]["color"][0]:02x}{CLASS_INFO[k]["color"][1]:02x}{CLASS_INFO[k]["color"][2]:02x}'
              for k in range(NUM_CLASSES)]
    fig = go.Figure(go.Pie(
        labels=labels, values=values, hole=0.55,
        marker=dict(colors=colors, line=dict(color='#ffffff', width=2)),
        textinfo='label+percent',
        textfont=dict(size=10, color='#1a1f2e'),
        hovertemplate="<b>%{label}</b><br>Pixels: %{value:,}<br>%{percent}<extra></extra>"
    ))
    fig.update_layout(
        paper_bgcolor='#ffffff', plot_bgcolor='#ffffff',
        font=dict(color='#1a1f2e', family='Space Mono'),
        legend=dict(font=dict(color='#1a1f2e', size=9), bgcolor='rgba(0,0,0,0)'),
        margin=dict(l=10, r=10, t=30, b=10),
        showlegend=True,
        annotations=[dict(text='Class<br>Split', x=0.5, y=0.5,
                          font_size=11, font_color='#1a1f2e', showarrow=False)]
    )
    return fig

def build_confidence_bar(probs_full, pred_mask):
    per_class_conf = []
    for k in range(NUM_CLASSES):
        pixels = probs_full[k][pred_mask == k]
        per_class_conf.append(float(np.mean(pixels)) if len(pixels) else 0.0)
    labels = [CLASS_INFO[k]["name"] for k in range(NUM_CLASSES)]
    colors = ['#b4d2f0', '#c0392b', '#f39c12', '#2980b9']
    fig = go.Figure(go.Bar(
        x=per_class_conf, y=labels, orientation='h',
        marker=dict(color=colors, line=dict(color='#ffffff', width=1)),
        text=[f'{v:.1%}' for v in per_class_conf],
        textfont=dict(color='#1a1f2e', size=9),
        textposition='outside',
    ))
    fig.update_layout(
        paper_bgcolor='#ffffff', plot_bgcolor='#f4f6fa',
        font=dict(color='#1a1f2e', family='Space Mono', size=9),
        xaxis=dict(range=[0, 1], tickformat='.0%', gridcolor='#dde3ef', color='#6b7a99'),
        yaxis=dict(gridcolor='#dde3ef', color='#6b7a99'),
        title=dict(text='Per-Class Prediction Confidence', font=dict(size=10, color='#e84118')),
        margin=dict(l=10, r=40, t=40, b=10),
    )
    return fig

# ─── UPLOAD & PIPELINE ────────────────────────────────────────────────────────
uploaded = st.file_uploader("📡 Upload Aerial / SAR Image (JPG · PNG · JPEG)",
                             type=["jpg", "png", "jpeg"])

if uploaded is not None:
    image   = Image.open(uploaded).convert("RGB")
    img_rgb = np.array(image)
    img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
    H, W    = img_rgb.shape[:2]

    with st.spinner("Running segmentation model…"):
        t0 = time.time()
        pred_256, probs_256, confidence = predict(img_bgr)
        pred, probs_full    = resize_outputs(pred_256, probs_256, H, W)

    # Remove small noise blobs from oil prediction
        oil_mask = (pred == 1).astype(np.uint8)
        num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(oil_mask)
        clean_mask = np.zeros_like(oil_mask)
        min_area = int(0.001 * pred.size)
        for i in range(1, num_labels):
            if stats[i, cv2.CC_STAT_AREA] >= min_area:
                clean_mask[labels == i] = 1
        pred[pred == 1] = 0
        pred[clean_mask == 1] = 1

        inf_time = time.time() - t0
        
    mask_col    = colorize(pred)
    overlay     = cv2.addWeighted(img_rgb, 1 - overlay_alpha, mask_col, overlay_alpha, 0)
    contour_img = draw_contours(img_rgb, pred) if show_contours else img_rgb.copy()
    counts, oil_px, oil_pct, oil_km2 = compute_area_stats(pred)

    oil_analysis = classify_oil_type_and_thickness(img_rgb,pred)

    oil_type = oil_analysis["type"]

    oil_conf = oil_analysis["confidence"]

    thickness_um = oil_analysis["thickness_um"]

    volume_m3 = estimate_volume(oil_km2,thickness_um)

    risk_label, risk_css = risk_level(oil_pct)
    # ── METRIC CARDS ──
    st.markdown('<p class="section-header">📊 Detection Summary</p>', unsafe_allow_html=True)
    

    st.markdown(f"""
    <div class="metric-row">
      <div class="metric-card red">
        <div class="metric-label">Oil Coverage</div>
        <div class="metric-value">{oil_pct:.1f}<span style="font-size:1rem">%</span></div>
        <div class="metric-unit">{oil_px:,} pixels</div>
      </div>
      <div class="metric-card amber">
        <div class="metric-label">Est. Area</div>
        <div class="metric-value">{oil_km2:.2f}<span style="font-size:1rem"> km²</span></div>
        <div class="metric-unit">at 5m/pixel resolution</div>
      </div>
      <div class="metric-card blue">
        <div class="metric-label">Risk Level</div>
        <div class="metric-value" style="font-size:1.3rem;">{risk_label}</div>
        <div class="metric-unit">combined assessment</div>
      </div>
      <div class="metric-card green">
        <div class="metric-label">Inference</div>
        <div class="metric-value">{inf_time:.2f}<span style="font-size:1rem">s</span></div>
        <div class="metric-unit">{DEVICE.upper()} · {"DEMO" if DEMO_MODE else "LIVE"}</div>
      </div>
      <div class="metric-card blue">
        <div class="metric-label">Volume</div>
        <div class="metric-value">{volume_m3:.2f}</div>
        <div class="metric-unit">m³</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    if oil_px == 0:
        st.markdown("""
        <div class="alert safe">
          <div class="alert-icon">✅</div>
          <div>
            <div class="alert-title">No Oil Spill Detected</div>
            <div class="alert-body">The segmentation model found no oil-class pixels in this image.
            Sea surface appears clean.</div>
          </div>
        </div>""", unsafe_allow_html=True)
    else:
        icon = "🚨" if "CRITICAL" in risk_label else "⚠️"
        st.markdown(f"""
        <div class="alert {'danger' if 'CRITICAL' in risk_label else 'warning'}">
          <div class="alert-icon">{icon}</div>
          <div>
            <div class="alert-title">Oil Spill Detected — Risk Level: <span class="risk-badge {risk_css}">{risk_label}</span></div>
            <div class="alert-body">
              Type: <b>{oil_type}</b>
              Thickness: <b>{thickness_um:.2f} μm</b>
              Volume: <b>{volume_m3:.2f} m³</b>
              Confidence: <b>{oil_conf:.0%}</b> &nbsp;|&nbsp;
              Coverage: <b>{oil_pct:.2f}%</b> &nbsp;|&nbsp;
              Est. area: <b>{oil_km2:.3f} km²</b>
            </div>
          </div>
        </div>""", unsafe_allow_html=True)

    # ── IMAGE GRID ──
    st.markdown('<p class="section-header">🖼 Visual Output</p>', unsafe_allow_html=True)
    tab1, tab2, tab3, tab4 = st.tabs(["Original", "Segmentation Mask", "Overlay", "Contour Detection"])
    with tab1:
        st.image(img_rgb, caption=f"Input Image — {W}×{H}px", use_container_width=True)
    with tab2:
        st.image(mask_col, caption="Predicted Segmentation Mask", use_container_width=True)
        st.markdown("""
        <div class="legend-row">
          <div class="legend-item"><div class="legend-dot" style="background:#b4d2f0;border:1px solid #aaa"></div> Background / Sea</div>
          <div class="legend-item"><div class="legend-dot" style="background:#c0392b"></div> Oil Spill</div>
          <div class="legend-item"><div class="legend-dot" style="background:#f39c12"></div> Look-alike</div>
          <div class="legend-item"><div class="legend-dot" style="background:#2980b9"></div> Ship / Object</div>
        </div>""", unsafe_allow_html=True)
    with tab3:
        st.image(overlay, caption=f"Overlay (opacity {overlay_alpha:.0%})", use_container_width=True)
    with tab4:
        st.image(contour_img, caption="Oil Spill Contour Detection", use_container_width=True)

    # ── GAN IMAGES — GOOGLE DRIVE SECTION ──
    st.markdown('<p class="section-header">🧠 GAN Generated Images — Google Drive</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="alert info">
      <div class="alert-icon">🧠</div>
      <div>
        <div class="alert-title">GAN Training Outputs</div>
        <div class="alert-body">
          Epoch-wise images generated by the <b>GANomaly</b> model during training are stored
          in Google Drive. Browse real vs generated SAR imagery across training epochs.
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button(
        "🔗 Open GAN Images on Google Drive",
        url=GAN_DRIVE_FOLDER_URL,
        use_container_width=True
    )

    # ── ANALYTICS ──
    if show_heatmap or show_class_dist:
        st.markdown('<p class="section-header">📈 Analytical Charts</p>', unsafe_allow_html=True)
        a1, a2 = st.columns(2)
        if show_heatmap:
            with a1:
                st.markdown("**Oil Probability Heatmap**")
                fig_heat = build_heatmap_fig(probs_full, class_idx=1)
                st.pyplot(fig_heat, use_container_width=True)
                plt.close(fig_heat)
        if show_class_dist:
            with a2:
                st.markdown("**Class Distribution**")
                fig_pie = build_distribution_fig(counts)
                st.plotly_chart(fig_pie, use_container_width=True)
        st.markdown("**Per-Class Confidence Scores**")
        fig_bar = build_confidence_bar(probs_full, pred)
        st.plotly_chart(fig_bar, use_container_width=True)

    # ── REPORT ──
    if enable_reports:
        st.markdown('<p class="section-header">📋 Incident Report</p>', unsafe_allow_html=True)
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        report_txt = f"""OIL SPILL DETECTION REPORT
═══════════════════════════════════
Generated : {ts}
File      : {uploaded.name}
Image     : {W} × {H} pixels
Device    : {DEVICE.upper()}
Mode      : {"DEMO" if DEMO_MODE else "LIVE"}

SEGMENTATION RESULTS
─────────────────────
Oil Spill Coverage : {oil_pct:.2f} %
Oil Pixel Count    : {oil_px:,}
Estimated Area     : {oil_km2:.4f} km² (@ 5m/px)
Oil Type           : {oil_type}
Oil Confidence     : {oil_conf:.0%}
Oil Appearance     : {oil_type}
Estimated Thickness: {thickness_um:.2f} μm
Estimated Volume   : {volume_m3:.2f} m³

CLASS DISTRIBUTION
─────────────────────
"""
        for k in range(NUM_CLASSES):
            pct = counts[k] / pred.size * 100
            report_txt += f"  {CLASS_INFO[k]['name']:<20}: {counts[k]:>8,} px  ({pct:.1f}%)\n"

        report_txt += f"""
RISK ASSESSMENT
─────────────────────
Risk Level         : {risk_label}
Recommended Action : {"Immediate response required" if risk_label in ("CRITICAL","HIGH") else "Monitor and log" if risk_label == "MEDIUM" else "Routine observation"}

GAN IMAGES
─────────────────────

Access Link        : {GAN_DRIVE_FOLDER_URL}

═══════════════════════════════════
Powered by OilSense AI — UNet + GANomaly
"""
        st.text_area("Full Report", report_txt, height=320)
        st.download_button(
            label="⬇ Download Report (.txt)",
            data=report_txt,
            file_name=f"oilspill_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )

else:
    # ── Empty state ──
    st.markdown("""
    <div style="text-align:center;padding:60px 20px;color:var(--muted);">
      <div style="font-size:3.5rem;margin-bottom:16px;">🛰️</div>
      <div style="font-family:'Syne',sans-serif;font-size:1.2rem;color:var(--text);margin-bottom:8px;">
        Awaiting Image Upload
      </div>
      <div style="font-size:0.78rem;max-width:400px;margin:0 auto;line-height:1.8;">
        Upload an aerial or SAR image to begin oil spill detection.<br>
        Supported formats: <b>JPG · PNG · JPEG</b>
      </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    for col, icon, title, body in [
        (c1, "🔬", "Semantic Segmentation", "U-Net + MobileNetV2 classifies every pixel into 4 sea-surface classes"),
        (c2, "🧠", "GAN Training Outputs", "Browse epoch-wise GAN-generated SAR images saved to Google Drive"),
        (c3, "📊", "Full Analytics Suite",  "Probability heatmaps, class distributions, confidence scores & reports"),
    ]:
        col.markdown(f"""
        <div style="background:#ffffff;border:1px solid var(--border);border-radius:10px;
                    padding:24px;text-align:center;box-shadow:0 2px 10px rgba(0,0,0,0.06);">
          <div style="font-size:2rem;margin-bottom:10px;">{icon}</div>
          <div style="font-family:'Syne',sans-serif;font-size:0.9rem;color:var(--text);
                      margin-bottom:8px;font-weight:600;">{title}</div>
          <div style="font-size:0.72rem;color:var(--muted);line-height:1.7;">{body}</div>
        </div>
        """, unsafe_allow_html=True)

    # ── Drive quick-access on landing page ──
    st.markdown('<p class="section-header" style="margin-top:40px;">🧠 GAN Images — Quick Access</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="alert info">
      <div class="alert-icon">🗂️</div>
      <div>
        <div class="alert-title">Browse GAN Training Outputs</div>
        <div class="alert-body">
          All GAN-generated images from training epochs are stored in Google Drive.
          Open the folder to compare real vs generated SAR imagery across epochs.
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button(
        "🔗 Open GAN Images on Google Drive",
        url=GAN_DRIVE_FOLDER_URL,
        use_container_width=True
    )