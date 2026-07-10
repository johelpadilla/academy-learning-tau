"""Biblioteca de investigación — corpus clasificado de Publicaciones."""

from __future__ import annotations

import sys
from pathlib import Path

_APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_APP))
from components.bootstrap import ensure_stp_path  # noqa: E402

ROOT = ensure_stp_path(__file__)

import streamlit as st

from components.ui import callout, footer, learning_goals, page_header, page_link, section_header
from stp.education.research_library import (
    collection_label,
    filter_library,
    group_by_collection,
    list_collections,
    list_library,
    library_stats,
    mime_for,
    publications_root,
    read_item_bytes,
)
from stp.i18n.core import get_lang, t

st.set_page_config(page_title=t("biblioteca.page_title"), page_icon="📚", layout="wide")

page_header(
    t("biblioteca.title"),
    subtitle=t("biblioteca.subtitle"),
    eyebrow=t("biblioteca.eyebrow"),
    icon="📚",
)

learning_goals(
    [t("biblioteca.goal_1"), t("biblioteca.goal_2"), t("biblioteca.goal_3")]
)

lang = get_lang()
root = publications_root()
stats = library_stats()

if root:
    callout(
        t(
            "biblioteca.root_ok",
            path=str(root),
            total=stats["total"],
            available=stats["available"],
        )
    )
else:
    st.error(t("biblioteca.root_missing"))
    st.markdown(t("biblioteca.root_help"))

# ── Metrics ────────────────────────────────────────────────────────
m1, m2, m3, m4 = st.columns(4)
m1.metric(t("biblioteca.metric_total"), stats["total"])
m2.metric(t("biblioteca.metric_available"), stats["available"])
m3.metric(t("biblioteca.metric_collections"), len(stats["by_collection"]))
m4.metric(t("biblioteca.metric_domains"), len(stats["by_domain"]))

# ── Featured ───────────────────────────────────────────────────────
section_header(t("biblioteca.featured_header"))
featured = filter_library(featured_only=True)
if not featured:
    st.caption(t("biblioteca.no_featured"))
else:
    cols = st.columns(min(3, len(featured)))
    for col, it in zip(cols, featured[:6]):
        with col:
            st.markdown(f"**{it.title}**")
            st.caption(
                f"{it.year or '—'} · {collection_label(it.collection, lang)} · {it.format.upper()}"
            )
            summary = it.display_summary(lang)
            if summary:
                st.markdown(summary[:280] + ("…" if len(summary) > 280 else ""))
            if it.available and it.path:
                try:
                    data = read_item_bytes(it.id)
                    if data:
                        st.download_button(
                            t("biblioteca.download"),
                            data=data,
                            file_name=it.path.name,
                            mime=mime_for(it),
                            key=f"feat_dl_{it.id}",
                            width="stretch",
                            type="primary",
                        )
                except ValueError as exc:
                    st.caption(str(exc))
            elif it.url:
                st.link_button(t("biblioteca.open_url"), it.url, width="stretch")
            else:
                st.caption(t("biblioteca.file_offline"))

# ── Filters ────────────────────────────────────────────────────────
section_header(t("biblioteca.catalog_header"))
all_items = list(list_library(include_orphans=True))
collections = list_collections(lang)
coll_ids = [c.id for c in collections]
domains = sorted({it.domain for it in all_items})
types = sorted({it.type for it in all_items})
years = sorted({it.year for it in all_items if it.year}, reverse=True)
statuses = sorted({it.status for it in all_items})

f1, f2, f3 = st.columns(3)
with f1:
    sel_coll = st.multiselect(
        t("biblioteca.filter_collection"),
        options=coll_ids,
        format_func=lambda cid: collection_label(cid, lang),
        default=[],
    )
    sel_domain = st.multiselect(t("biblioteca.filter_domain"), domains, default=[])
with f2:
    sel_type = st.multiselect(t("biblioteca.filter_type"), types, default=[])
    sel_status = st.multiselect(t("biblioteca.filter_status"), statuses, default=[])
with f3:
    sel_year = st.multiselect(t("biblioteca.filter_year"), years, default=[])
    available_only = st.checkbox(t("biblioteca.filter_available"), value=False)
    q = st.text_input(t("biblioteca.search"), "", placeholder=t("biblioteca.search_ph"))

# Apply filters (OR within multi, AND across dimensions)
filtered = all_items
if sel_coll:
    filtered = [it for it in filtered if it.collection in sel_coll]
if sel_domain:
    filtered = [it for it in filtered if it.domain in sel_domain]
if sel_type:
    filtered = [it for it in filtered if it.type in sel_type]
if sel_status:
    filtered = [it for it in filtered if it.status in sel_status]
if sel_year:
    filtered = [it for it in filtered if it.year in sel_year]
if available_only:
    filtered = [it for it in filtered if it.available]
if q.strip():
    filtered = filter_library(filtered, query=q)

st.caption(t("biblioteca.showing", n=len(filtered), total=len(all_items)))

# ── Grouped catalog ────────────────────────────────────────────────
view = st.radio(
    t("biblioteca.view_mode"),
    options=["grouped", "flat"],
    format_func=lambda v: t(f"biblioteca.view_{v}"),
    horizontal=True,
    key="lib_view_mode",
)


def _render_item(it) -> None:
    pills = (
        f'<span class="stp-pill">{it.type}</span> '
        f'<span class="stp-pill high">{it.domain}</span> '
        f'<span class="stp-pill purple">{it.status}</span>'
    )
    doi_html = f' · DOI <code>{it.doi}</code>' if it.doi else ""
    avail = (
        f'<span class="stp-pill high">{t("biblioteca.online")}</span>'
        if it.available
        else f'<span class="stp-pill">{t("biblioteca.offline")}</span>'
    )
    st.markdown(
        f"""
        <div class="stp-pub">
          <h3 style="margin-bottom:0.25rem">{it.title}</h3>
          <div class="meta">
            {it.authors} · {it.year or "—"} · {it.format.upper()} · {it.size_label()}
            {doi_html} · {avail}
          </div>
          <div style="margin:0.4rem 0">{pills}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    summary = it.display_summary(lang)
    if summary:
        st.markdown(summary)
    if it.topics:
        st.caption(" · ".join(it.topics))
    if it.file:
        st.caption(f"`{it.file}`")

    b1, b2, b3 = st.columns([1, 1, 2])
    with b1:
        if it.available and it.path:
            try:
                data = read_item_bytes(it.id)
                if data is not None:
                    st.download_button(
                        t("biblioteca.download"),
                        data=data,
                        file_name=it.path.name,
                        mime=mime_for(it),
                        key=f"dl_{it.id}",
                        width="stretch",
                    )
            except ValueError as exc:
                st.warning(str(exc))
        else:
            st.caption(t("biblioteca.file_offline"))
    with b2:
        if it.url:
            st.link_button(t("biblioteca.open_url"), it.url, width="stretch")
        elif it.doi and it.doi.startswith("10."):
            st.link_button(
                t("biblioteca.open_doi"),
                f"https://doi.org/{it.doi}",
                width="stretch",
            )
    with b3:
        if it.related:
            st.caption(
                t("biblioteca.related") + ": " + ", ".join(f"`{r}`" for r in it.related[:4])
            )


if not filtered:
    st.info(t("biblioteca.no_match"))
elif view == "flat":
    for it in filtered:
        _render_item(it)
        st.divider()
else:
    for meta, items in group_by_collection(filtered, lang=lang):
        label = meta.label(lang) if meta else collection_label(items[0].collection, lang)
        desc = ""
        if meta:
            if lang.startswith("es"):
                desc = meta.description_es
            elif lang.startswith("fr"):
                desc = meta.description_fr or meta.description_en
            else:
                desc = meta.description_en or meta.description_es
        with st.expander(f"{label} ({len(items)})", expanded=True):
            if desc:
                st.caption(desc)
            for it in items:
                _render_item(it)
                st.divider()

# ── Stats sidebar tables ───────────────────────────────────────────
section_header(t("biblioteca.stats_header"))
c1, c2 = st.columns(2)
with c1:
    st.markdown(f"**{t('biblioteca.by_collection')}**")
    st.dataframe(
        [{"colección": k, "n": v} for k, v in stats["by_collection"].items()],
        hide_index=True,
        width="stretch",
    )
with c2:
    st.markdown(f"**{t('biblioteca.by_domain')}**")
    st.dataframe(
        [{"dominio": k, "n": v} for k, v in stats["by_domain"].items()],
        hide_index=True,
        width="stretch",
    )

page_link("pages/6_Evidencia.py", label=t("biblioteca.to_evidence"), icon="📑")
page_link("pages/8_Materiales.py", label=t("biblioteca.to_materials"), icon="📦")
page_link("pages/4_Laboratorio.py", label=t("nav.lab"), icon="🔬")

footer()
