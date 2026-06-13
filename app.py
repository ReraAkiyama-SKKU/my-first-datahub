"""
Moments Archive - A Personal Space for Organizing Visual Memories
Built with Python and Streamlit
Author: Rera Akiyama
"""

import streamlit as st

# ─────────────────────────────────────────────
# PAGE CONFIGURATION
# Must be the very first Streamlit command
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Moments Archive",
    page_icon="📷",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# CUSTOM CSS — soft beige & dark gray palette
# ─────────────────────────────────────────────
st.markdown("""
<style>
    /* ── Google Font import ── */
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300&family=DM+Sans:wght@300;400;500&display=swap');

    /* ── Color tokens ── */
    :root {
        --beige-lightest: #F7F4EF;
        --beige-mid:      #EDE8DF;
        --beige-dark:     #C9BFB0;
        --charcoal:       #2B2B2B;
        --charcoal-soft:  #4A4A4A;
        --ink:            #1A1A1A;
        --accent:         #8C7B6B;
        --white:          #FFFFFF;
    }

    /* ── Base ── */
    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        background-color: var(--beige-lightest);
        color: var(--charcoal);
    }

    /* ── Remove default Streamlit padding ── */
    .main .block-container {
        padding-top: 0 !important;
        padding-bottom: 2rem;
        max-width: 1100px;
    }

    /* ── Hero / title section ── */
    .hero {
        background-color: var(--charcoal);
        color: var(--beige-lightest);
        padding: 4rem 3rem 3.5rem;
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
    }
    .hero::after {
        content: "";
        position: absolute;
        bottom: 0; left: 0; right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--accent), var(--beige-dark), var(--accent));
    }
    .hero-eyebrow {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.72rem;
        font-weight: 500;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        color: var(--beige-dark);
        margin-bottom: 0.8rem;
    }
    .hero-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 4.2rem;
        font-weight: 300;
        line-height: 1.05;
        letter-spacing: -0.01em;
        color: var(--beige-lightest);
        margin: 0 0 0.8rem;
    }
    .hero-subtitle {
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        font-size: 1.25rem;
        font-weight: 300;
        color: var(--beige-dark);
        margin: 0;
        letter-spacing: 0.01em;
    }

    /* ── Section labels ── */
    .section-label {
        font-size: 0.7rem;
        font-weight: 500;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: var(--accent);
        margin-bottom: 0.4rem;
    }
    .section-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2rem;
        font-weight: 400;
        color: var(--ink);
        margin-bottom: 1rem;
    }

    /* ── About card ── */
    .about-card {
        background: var(--beige-mid);
        border-left: 3px solid var(--accent);
        padding: 2rem 2.2rem;
        margin-bottom: 3rem;
        border-radius: 2px;
    }
    .about-card p {
        font-size: 1.05rem;
        line-height: 1.85;
        color: var(--charcoal-soft);
        margin: 0;
    }

    /* ── Filter pills ── */
    div[data-testid="stHorizontalBlock"] .stButton > button {
        border-radius: 20px !important;
        border: 1.5px solid var(--beige-dark) !important;
        background: transparent !important;
        color: var(--charcoal-soft) !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.82rem !important;
        font-weight: 400 !important;
        padding: 0.3rem 1.1rem !important;
        transition: all 0.2s ease !important;
    }
    div[data-testid="stHorizontalBlock"] .stButton > button:hover {
        background: var(--charcoal) !important;
        border-color: var(--charcoal) !important;
        color: var(--beige-lightest) !important;
    }

    /* ── Photo grid card ── */
    .photo-card {
        background: var(--white);
        border-radius: 4px;
        overflow: hidden;
        cursor: pointer;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        box-shadow: 0 1px 4px rgba(0,0,0,0.07);
        margin-bottom: 1rem;
    }
    .photo-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
    }
    .photo-meta {
        padding: 0.65rem 0.8rem 0.7rem;
    }
    .photo-caption {
        font-size: 0.82rem;
        font-weight: 500;
        color: var(--charcoal);
        margin: 0 0 0.2rem;
    }
    .photo-tag {
        font-size: 0.68rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: var(--accent);
    }

    /* ── Selected photo viewer ── */
    .viewer-caption {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.35rem;
        font-style: italic;
        color: var(--charcoal);
        margin-top: 0.8rem;
    }
    .viewer-tag {
        font-size: 0.72rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: var(--accent);
        margin-top: 0.3rem;
    }
    .viewer-desc {
        font-size: 0.95rem;
        color: var(--charcoal-soft);
        line-height: 1.7;
        margin-top: 0.6rem;
    }

    /* ── Divider ── */
    .thin-rule {
        border: none;
        border-top: 1px solid var(--beige-dark);
        margin: 2.5rem 0;
    }

    /* ── Footer ── */
    .footer {
        background-color: var(--charcoal);
        color: var(--beige-dark);
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
        font-size: 0.82rem;
        letter-spacing: 0.05em;
    }
    .footer a {
        color: var(--beige-dark);
        text-decoration: underline;
        text-underline-offset: 3px;
    }
    .footer a:hover { color: var(--beige-lightest); }

    /* ── Hide Streamlit chrome ── */
    #MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# PHOTO DATA
# Each photo uses a free Unsplash image.
# Fields: id, url, caption, category, description
# ─────────────────────────────────────────────
PHOTOS = [
    {
        "id": 1,
        "url": "Japan.JPG",
        "caption": "A Magical Day at Disneyland",
        "category": "Travel",
        "location": "Disneyland",
        "date": "2024-12-17",
        "description": "A joyful moment captured at Disneyland filled with excitement, laughter, and unforgettable memories.",
    },
    {
    "id": 2,
    "url": "Jeongseon1.JPG",
    "caption": "Morning in Jeongseon",
    "category": "Travel",
    "location": "Jeongseon Trip",
    "date": "2025-07-04",
    "description": "The peaceful scenery of Jeongseon welcomed us with fresh air and quiet beauty.",
    },
    {
    "id": 3,
    "url": "Jeongseon2.JPG",
    "caption": "A Taste of Jeongseon",
    "category": "Travel",
    "location": "Jeongseon Trip",
    "date": "2025-07-04",
    "description": "Trying Jeongseon's traditional dish, Kkotdeungchigi, became one of the most memorable parts of the trip.",
    },
    {
    "id": 4,
    "url": "Jeongseon3.jpeg",
    "caption": "A Curious Encounter",
    "category": "Nature",
    "location": "Jeongseon Trip",
    "date": "2025-07-04",
    "description": "A small encounter with a curious cat became one of the warmest memories from the trip.",
    },
    {
    "id": 5,
    "url": "Japan summer1.JPG",
    "caption": "Summer Day in Enoshima",
    "category": "Travel",
    "location": "Japan",
    "date": "2025-8-09",
    "description": "A bright summer seaside scene in Enoshima with blue ocean, sunlight, and a relaxed coastal atmosphere.",
    },
    {
    "id": 6,
    "url": "Japan summer2.JPG",
    "caption": "Summer Day in Enoshima",
    "category": "Travel",
    "location": "Japan",
    "date": "2025-8-09",
    "description": "A traditional restaurant in Enoshima surrounded by soft sunlight through trees, creating a calm summer atmosphere.",
    },
    {
    "id": 7,
    "url": "fall_skku.jpeg",
    "caption": "Golden Autumn at Sungkyunkwan",
    "category": "Nature",
    "location": "Sungkyunkwan University",
    "date": "2025-11-02",
    "description": "Golden ginkgo trees glowing in the autumn sunlight at Sungkyunkwan University, creating a peaceful and timeless atmosphere."
}
]
# All category options including "All"
ALL_CATEGORIES = ["All", "Daily Life", "Travel", "Nature", "Mood"]

# All event options including "All"
ALL_EVENTS = ["All"] + sorted(set(p["location"] for p in PHOTOS))


# ─────────────────────────────────────────────
# SESSION STATE
# Keeps track of which category is selected
# and which photo (if any) is being viewed
# ─────────────────────────────────────────────
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "All"

if "selected_photo_id" not in st.session_state:
    st.session_state.selected_photo_id = None

if "user_photos" not in st.session_state:
    st.session_state.user_photos = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []

# ─────────────────────────────────────────────
# HERO SECTION
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">📷 &nbsp; Personal Archive</div>
    <div class="hero-title">Moments Archive</div>
    <div class="hero-subtitle">A Personal Space for Organizing Visual Memories</div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# ABOUT SECTION
# ─────────────────────────────────────────────
st.markdown('<div class="section-label">About</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">What is Moments Archive?</div>', unsafe_allow_html=True)

st.markdown("""
<div class="about-card">
    <p>
        Moments Archive transforms everyday photographs into a meaningful personal archive.
        Rather than letting memories scatter across folders and devices, this space invites you
        to collect, organise, and revisit them — by mood, by place, by the ordinary rhythms of
        daily life. Each photograph holds something worth returning to. This is where you keep it.
    </p>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# PHOTO GALLERY SECTION
# ─────────────────────────────────────────────

# ── Upload a new memory ──
st.markdown('<div class="section-label">Upload</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Add a New Memory</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Choose a photo",
    type=["jpg", "jpeg", "png"]
)

caption_input = st.text_input("Caption")
category_input = st.selectbox("Category", ALL_CATEGORIES[1:])
Location_input = st.text_input("Location")

if st.button("Add Memory"):
    if uploaded_file:
        st.session_state.user_photos.append({
            "id": len(PHOTOS) + len(st.session_state.user_photos) + 1,
            "url": uploaded_file,
            "caption": caption_input,
            "category": category_input,
            "location": location_input,
            "date": "2026",
            "description": "Uploaded by the user.",
        })
        st.success("Memory added successfully!")
        
st.markdown('<div class="section-label">Gallery</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Your Collection</div>', unsafe_allow_html=True)

# ── Category filter pills ──
# We use one button per category and highlight the active one with different styling
st.markdown("**Filter by category:**")
selected_location = st.selectbox(
    "Filter by location:",
    ALL_EVENTS
)
cols_filter = st.columns(len(ALL_CATEGORIES))

for i, category in enumerate(ALL_CATEGORIES):
    with cols_filter[i]:
        if st.button(category, key=f"filter_{category}"):
            st.session_state.selected_category = category
            st.session_state.selected_photo_id = None  # reset viewer on filter change

# Show which filter is active
st.caption(f"Showing: **{st.session_state.selected_category}**")

show_favorites = st.checkbox("⭐ Show Favorites Only")

st.markdown('<hr class="thin-rule">', unsafe_allow_html=True)

# ── Filter photos by selected category ──

all_photos = PHOTOS + st.session_state.user_photos

filtered = all_photos

if st.session_state.selected_category != "All":
    filtered = [
        p for p in filtered
        if p["category"] == st.session_state.selected_category
    ]

if selected_location != "All":
    filtered = [
        p for p in filtered
        if p["location"] == selected_location
    ]

if show_favorites:
    filtered = [
        p for p in filtered
        if p["id"] in st.session_state.favorites
    ]

# ── Render 3-column photo grid ──
# We group photos into rows of 3
COLS_PER_ROW = 3

if not filtered:
    st.info("No photos in this category yet.")
else:
    # Walk through photos in chunks of COLS_PER_ROW
    for row_start in range(0, len(filtered), COLS_PER_ROW):
        row_photos = filtered[row_start : row_start + COLS_PER_ROW]
        grid_cols = st.columns(COLS_PER_ROW)

        for col, photo in zip(grid_cols, row_photos):
            with col:
                # Display the photo image
                st.image(photo["url"], use_container_width=True)

                # Caption and tag below the image
                st.markdown(
                    f'<div class="photo-meta">'
                    f'<div class="photo-caption">{photo["caption"]}</div>'
                    f'<div class="photo-tag">{photo["category"]}</div>'
                    f'</div>',
                    unsafe_allow_html=True,
                )

                # "View" button — clicking stores this photo's id in session state
                if st.button("View ↗", key=f"view_{photo['id']}"):
                    st.session_state.selected_photo_id = photo["id"]
                # Favorite button
                if photo["id"] in st.session_state.favorites:
                    if st.button("💔 Remove Favorite", key=f"fav_{photo['id']}"):
                       st.session_state.favorites.remove(photo["id"])
                       st.rerun()
                else:
                    if st.button("⭐ Favorite", key=f"fav_{photo['id']}"):
                        st.session_state.favorites.append(photo["id"])
                        st.rerun()


# ─────────────────────────────────────────────
# PHOTO VIEWER
# Shown only when a photo has been selected
# ─────────────────────────────────────────────
if st.session_state.selected_photo_id is not None:
    selected = next(
        (p for p in all_photos if p["id"] == st.session_state.selected_photo_id),
        None
    )

    if selected:
        st.markdown('<hr class="thin-rule">', unsafe_allow_html=True)
        st.markdown('<div class="section-label">Selected Moment</div>', unsafe_allow_html=True)

        left_col, right_col = st.columns([3, 2], gap="large")

        with left_col:
            st.image(selected["url"], use_container_width=True)

        with right_col:
            st.markdown(
                f'<div class="viewer-caption">{selected["caption"]}</div>'
                f'<div class="viewer-tag">{selected["category"]}</div>'
                f'<div class="viewer-desc">{selected["description"]}</div>',
                unsafe_allow_html=True,
            )

            if st.button("✕ Close", key="close_viewer"):
                st.session_state.selected_photo_id = None
                st.rerun()


# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div>Created by <strong>Rera Akiyama</strong></div>
    <div style="margin-top:0.4rem;">
        <a href="https://github.com/your-username" target="_blank">GitHub →</a>
    </div>
    <div style="margin-top:0.8rem; font-size:0.7rem; opacity:0.5; letter-spacing:0.1em;">
        MOMENTS ARCHIVE &nbsp;·&nbsp; BUILT WITH STREAMLIT
    </div>
</div>
""", unsafe_allow_html=True)
