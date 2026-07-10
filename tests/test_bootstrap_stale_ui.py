"""Stale Streamlit module cache must not crash Home/Lab imports."""

from __future__ import annotations

import sys
from pathlib import Path
from types import ModuleType

import pytest

APP = Path(__file__).resolve().parents[1] / "app"
SRC = Path(__file__).resolve().parents[1] / "src"


@pytest.fixture(autouse=True)
def _path():
    for p in (str(APP), str(SRC)):
        if p in sys.path:
            sys.path.remove(p)
        sys.path.insert(0, p)
    # reset bootstrap flag between tests
    import components.bootstrap as boot

    boot._PATH_READY = False
    yield
    # leave clean ui for other tests
    for name in list(sys.modules):
        if name == "components.ui" or name.startswith("components.ui."):
            del sys.modules[name]
        if name == "components.hero" or name.startswith("components.hero."):
            del sys.modules[name]
    boot._PATH_READY = False


def test_ensure_stp_path_purges_stale_components_ui():
    from components import bootstrap as boot

    # Inject a fake pre-redesign ui module (missing new helpers)
    stale = ModuleType("components.ui")
    stale.__file__ = str(APP / "components" / "ui.py")
    stale.render_hero = lambda *a, **k: None  # type: ignore[attr-defined]
    sys.modules["components.ui"] = stale
    if "components" not in sys.modules:
        pkg = ModuleType("components")
        pkg.__path__ = [str(APP / "components")]  # type: ignore[attr-defined]
        sys.modules["components"] = pkg

    assert not hasattr(sys.modules["components.ui"], "link_action_card")

    boot.ensure_stp_path(APP / "Home.py")

    assert "components.ui" not in sys.modules or hasattr(
        sys.modules.get("components.ui"), "link_action_card"
    )
    # After purge, import_ui must load real symbols from disk
    (link_action_card,) = boot.import_ui("link_action_card")
    assert callable(link_action_card)
    (verdict_panel,) = boot.import_ui("verdict_panel")
    assert callable(verdict_panel)


def test_import_ui_recovers_from_stale_module():
    from components import bootstrap as boot

    boot.ensure_stp_path(APP / "Home.py")

    stale = ModuleType("components.ui")
    stale.__file__ = str(APP / "components" / "ui.py")
    sys.modules["components.ui"] = stale

    names = (
        "link_action_card",
        "verdict_panel",
        "render_hero",
        "page_header",
    )
    objs = boot.import_ui(*names)
    assert len(objs) == len(names)
    assert all(callable(o) for o in objs)
