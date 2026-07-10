"""Research library catalog and filters."""

from __future__ import annotations

from pathlib import Path

import pytest

from stp.education.research_library import (
    catalog_path,
    clear_library_cache,
    filter_library,
    get_item,
    group_by_collection,
    list_collections,
    list_library,
    library_stats,
    publications_root,
)
from stp.i18n.core import SUPPORTED_LANGS, clear_catalog_cache, set_lang, t


@pytest.fixture(autouse=True)
def _reset():
    clear_library_cache()
    clear_catalog_cache()
    set_lang("es")
    yield
    clear_library_cache()
    set_lang("es")


def test_catalog_yaml_exists():
    assert catalog_path().is_file()


def test_list_library_covers_corpus():
    items = list_library(include_orphans=True)
    assert len(items) >= 30
    ids = {it.id for it in items}
    assert "cctp_sddb_manuscript" in ids
    assert "systemic_tau_foundations" in ids
    assert "pp_202509_1428" in ids
    assert "n06_dengue_early_warning" in ids


def test_collections_defined():
    colls = list_collections("es")
    ids = {c.id for c in colls}
    assert "empirical_anchor" in ids
    assert "preprints_2025" in ids
    assert "numbered_corpus" in ids


def test_filter_by_domain_and_query():
    cardio = filter_library(domain="cardiology")
    assert any(it.id == "cctp_sddb_manuscript" for it in cardio)
    dengue = filter_library(query="dengue")
    assert len(dengue) >= 2
    assert all(
        "dengue" in (it.title + it.summary + it.summary_es + " ".join(it.topics)).lower()
        or it.domain == "epidemiology"
        for it in dengue
    )


def test_featured_and_group():
    featured = filter_library(featured_only=True)
    assert len(featured) >= 3
    groups = group_by_collection(list_library(include_orphans=False), lang="es")
    assert groups
    # No raw machine keys in labels
    for meta, items in groups:
        if meta:
            assert "domain_voice" not in meta.label("es")
            assert items


def test_local_files_when_root_present():
    root = publications_root()
    if root is None:
        pytest.skip("Publications directory not on this machine")
    stats = library_stats()
    assert stats["available"] >= 20
    cctp = get_item("cctp_sddb_manuscript")
    assert cctp is not None
    assert cctp.available
    assert cctp.path and cctp.path.is_file()


def test_no_duplicate_orphans_for_curated():
    items = list_library(include_orphans=True)
    files = [it.file for it in items if it.file]
    # basename uniqueness among curated+orphan after unicode normalize
    import unicodedata

    norms = [unicodedata.normalize("NFC", Path(f).name) for f in files]
    assert len(norms) == len(set(norms)), "duplicate basenames in library"


def test_ui_keys_all_langs():
    for lang in SUPPORTED_LANGS:
        set_lang(lang)
        for key in (
            "biblioteca.title",
            "biblioteca.subtitle",
            "biblioteca.featured_header",
            "biblioteca.download",
            "nav.biblioteca",
            "evidencia.pubs_library_link",
        ):
            val = t(key)
            assert val != key, f"{lang}: unresolved {key}"
