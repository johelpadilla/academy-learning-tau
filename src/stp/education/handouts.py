"""Downloadable educational handouts (Markdown packs)."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from stp.config.settings import CONTENT_DIR
from stp.i18n.content import localized_content_path
from stp.i18n.core import t

HANDOUTS_DIR = CONTENT_DIR / "handouts"


@dataclass(frozen=True)
class Handout:
    id: str
    title: str
    description: str
    filename: str  # download name
    path: Path | None  # None => generated
    audience: str
    tags: tuple[str, ...] = ()
    generator: str | None = None  # special: faq, glossary, pack_student, pack_teacher


# Static files under content/handouts/
_STATIC: list[tuple[str, str, str, str, str, tuple[str, ...]]] = [
    (
        "guia_rapida",
        "Guía rápida (1 página)",
        "Primera sesión en 15–20 min: 5 clics y primer experimento.",
        "01_guia_rapida.md",
        "stp_01_guia_rapida.md",
        ("inicio", "estudiante"),
    ),
    (
        "manual_usuario",
        "Manual de usuario",
        "Instalación, mapa de la app, Lab paso a paso, CLI y troubleshooting.",
        "02_manual_usuario.md",
        "stp_02_manual_usuario.md",
        ("operacion", "docente"),
    ),
    (
        "teoria",
        "Teoría — τ_s, RECD y lectura dual",
        "Marco conceptual para posgrado y docentes (imprimible).",
        "03_teoria_tau_recd.md",
        "stp_03_teoria_tau_recd.md",
        ("teoria", "estudiante"),
    ),
    (
        "matematica",
        "Matemática práctica",
        "Bandt–Pompe, notación, nulos y checklist numérico.",
        "04_matematica_practica.md",
        "stp_04_matematica_practica.md",
        ("teoria", "matematica"),
    ),
    (
        "cheatsheet",
        "Cheat-sheet del Laboratorio",
        "Presets, demos, lectura de salidas y frases permitidas/prohibidas.",
        "05_laboratorio_cheatsheet.md",
        "stp_05_laboratorio_cheatsheet.md",
        ("lab", "estudiante"),
    ),
    (
        "lectura_dual",
        "Guía de lectura dual",
        "Plantillas de concordancia/discordancia y párrafo de entrega.",
        "06_lectura_dual.md",
        "stp_06_lectura_dual.md",
        ("lab", "escritura"),
    ),
    (
        "checklist",
        "Checklist de análisis",
        "Lista imprimible para entrega de Lab / informe corto.",
        "07_checklist_analisis.md",
        "stp_07_checklist_analisis.md",
        ("evaluacion", "estudiante"),
    ),
    (
        "syllabus",
        "Syllabus 6 semanas (v1.1)",
        "Competencias C1–C7, programa semanal, rúbrica 12 pts, datasets, evaluación y notas docentes.",
        "08_syllabus_6_semanas.md",
        "stp_08_syllabus_6_semanas.md",
        ("docente", "curso"),
    ),
    (
        "etica",
        "Ética y alcance del núcleo",
        "Qué está listo, qué no, claims honestos y citación.",
        "09_etica_alcance.md",
        "stp_09_etica_alcance.md",
        ("etica", "docente"),
    ),
    (
        "extensiones",
        "Extensiones — Breathing y TDA/Betti",
        "Cómo activar y leer W adaptativa y curvas β₀/β₁ (operativo en el Lab).",
        "10_extensiones_tda_breathing.md",
        "stp_10_extensiones_tda_breathing.md",
        ("lab", "teoria", "extensiones"),
    ),
]


def _handout_meta(id_: str, fallback_title: str, fallback_desc: str) -> tuple[str, str]:
    title = t(f"handouts.{id_}.title")
    desc = t(f"handouts.{id_}.description")
    if title == f"handouts.{id_}.title":
        title = fallback_title
    if desc == f"handouts.{id_}.description":
        desc = fallback_desc
    return title, desc


def _handout_from_static(
    id_: str, title: str, desc: str, src: str, download: str, tags: tuple[str, ...]
) -> Handout:
    title, desc = _handout_meta(id_, title, desc)
    return Handout(
        id=id_,
        title=title,
        description=desc,
        filename=download,
        path=localized_content_path("handouts", src),
        audience=tags[0] if tags else "general",
        tags=tags,
        generator=None,
    )


def list_handouts() -> list[Handout]:
    items = [_handout_from_static(*row) for row in _STATIC]
    extras = [
        ("faq", "FAQ (respuestas profundas)", "Malentendidos de posgrado, datos, ética y dominios pedagógicos.",
         "stp_faq.md", localized_content_path("learning", "faq.md"), "todos", ("faq", "estudiante"), None),
        ("glosario", "Glosario", "Términos τ_s, RECD, excess3, EWS, surrogates… generado desde glossary.yaml.",
         "stp_glosario.md", None, "todos", ("glosario", "referencia"), "glossary"),
        ("pack_estudiante", "Pack estudiante (un solo MD)",
         "Guía rápida + teoría + math + cheatsheet + lectura dual + checklist + FAQ + ética.",
         "stp_pack_estudiante.md", None, "estudiante", ("pack", "estudiante"), "pack_student"),
        ("pack_docente", "Pack docente (un solo MD)",
         "Syllabus + ética + manual + packs de teoría/lab + FAQ + glosario.",
         "stp_pack_docente.md", None, "docente", ("pack", "docente"), "pack_teacher"),
        ("fundamentos_compilado", "Fundamentos compilados",
         "Concatena los módulos de content/fundamentos/ en un solo Markdown.",
         "stp_fundamentos_compilado.md", None, "teoria", ("teoria", "pack"), "fundamentos"),
    ]
    for id_, ft, fd, fn, path, aud, tags, gen in extras:
        title, desc = _handout_meta(id_, ft, fd)
        items.append(
            Handout(
                id=id_,
                title=title,
                description=desc,
                filename=fn,
                path=path,
                audience=aud,
                tags=tags,
                generator=gen,
            )
        )
    return items


def get_handout(handout_id: str) -> Handout:
    for h in list_handouts():
        if h.id == handout_id:
            return h
    raise KeyError(f"Unknown handout: {handout_id}")


def _load_glossary() -> list[dict[str, Any]]:
    path = localized_content_path("learning", "glossary.yaml")
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return list(data.get("terms") or [])


def glossary_to_markdown() -> str:
    terms = _load_glossary()
    title = t("handouts.glosario.title")
    lines = [
        f"# {title} — Systemic Tau Platform",
        "",
        "---",
        "",
    ]
    for item in sorted(terms, key=lambda x: (x.get("term") or "").lower()):
        term = item.get("term", item.get("id", "?"))
        short = (item.get("short") or "").strip()
        long = (item.get("long") or "").strip()
        level = item.get("level", "")
        lines.append(f"## {term}")
        if level:
            lines.append(f"*{level}*")
        lines.append("")
        if short:
            lines.append(f"**{short}**")
            lines.append("")
        if long:
            lines.append(long.strip())
            lines.append("")
        related = item.get("related") or []
        if related:
            lines.append(f"*→ {', '.join(str(r) for r in related)}*")
            lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


def _read_path(path: Path) -> str:
    if not path.exists():
        return f"_{t('common.file_missing', path=path)}_\n"
    return path.read_text(encoding="utf-8")


def _join_sections(title: str, subtitle: str, parts: list[tuple[str, str]]) -> str:
    """parts: list of (section_title, markdown_body)."""
    blocks = [
        f"# {title}",
        "",
        subtitle,
        "",
        f"*{t('common.generated_sections', n=len(parts))}*",
        "",
        "---",
        "",
    ]
    for i, (sec_title, body) in enumerate(parts, 1):
        blocks.append(f"# {t('common.part_n', i=i, title=sec_title)}")
        blocks.append("")
        # demote internal H1 to H2 to keep pack structure
        demoted = []
        for line in body.splitlines():
            if line.startswith("# ") and not line.startswith("# Parte") and not line.startswith("# Part"):
                demoted.append("#" + line)
            else:
                demoted.append(line)
        blocks.append("\n".join(demoted).strip())
        blocks.append("")
        blocks.append("---")
        blocks.append("")
    return "\n".join(blocks)


def _pack_student() -> str:
    ids = [
        "guia_rapida",
        "teoria",
        "matematica",
        "cheatsheet",
        "extensiones",
        "lectura_dual",
        "checklist",
        "faq",
        "etica",
    ]
    parts = []
    for hid in ids:
        h = get_handout(hid)
        body = render_handout(hid)
        parts.append((h.title, body))
    return _join_sections(
        t("handouts.pack_student_title"),
        t("handouts.pack_student_sub"),
        parts,
    )


def _pack_teacher() -> str:
    ids = [
        "syllabus",
        "etica",
        "manual_usuario",
        "guia_rapida",
        "teoria",
        "matematica",
        "cheatsheet",
        "extensiones",
        "lectura_dual",
        "checklist",
        "faq",
        "glosario",
    ]
    parts = []
    for hid in ids:
        h = get_handout(hid)
        body = render_handout(hid)
        parts.append((h.title, body))
    return _join_sections(
        t("handouts.pack_teacher_title"),
        t("handouts.pack_teacher_sub"),
        parts,
    )


def _fundamentos_compilado() -> str:
    # Inventory always from Spanish source; body from localized paths
    d = CONTENT_DIR / "fundamentos"
    files = sorted(d.glob("*.md")) if d.exists() else []
    parts = []
    for f in files:
        body = _read_path(localized_content_path("fundamentos", f.name))
        parts.append((f.stem.replace("_", " ").title(), body))
    title = t("handouts.fundamentos_compilado.title")
    return _join_sections(
        f"{title} — Systemic Tau Platform",
        t("handouts.fundamentos_compilado.description"),
        parts,
    )


def render_handout(handout_id: str) -> str:
    h = get_handout(handout_id)
    if h.generator == "glossary":
        return glossary_to_markdown()
    if h.generator == "pack_student":
        return _pack_student()
    if h.generator == "pack_teacher":
        return _pack_teacher()
    if h.generator == "fundamentos":
        return _fundamentos_compilado()
    if h.path is not None:
        return _read_path(h.path)
    raise ValueError(f"Handout {handout_id} has no path or generator")


def render_handout_bytes(handout_id: str) -> bytes:
    return render_handout(handout_id).encode("utf-8")


def markdown_to_pdf(md: str, *, title: str = "STP") -> bytes | None:
    """Convert Markdown to PDF via Pandoc + LaTeX when available.

    Prefers XeLaTeX for Unicode (τ, accents). Falls back to default engine.
    Returns PDF bytes, or ``None`` if Pandoc/LaTeX is missing or conversion fails.
    """
    import os
    import re
    import shutil
    import subprocess
    import tempfile

    pandoc = shutil.which("pandoc")
    if not pandoc:
        return None

    # Ensure common MacTeX path is visible to the subprocess
    env = os.environ.copy()
    texbin = "/Library/TeX/texbin"
    if Path(texbin).is_dir():
        env["PATH"] = texbin + os.pathsep + env.get("PATH", "")

    # Soften content that breaks old Pandoc/pdflatex (Latin-1 pedagogical PDF)
    replacements = {
        "τ_s": "tau_s",
        "τ": "tau",
        "Φ₁": "Phi1",
        "Φ₂": "Phi2",
        "Φ₃": "Phi3",
        "Φ": "Phi",
        "Δ": "Delta-",
        "δ": "delta-",
        "θ": "theta-",
        "β": "beta-",
        "α": "alpha-",
        "σ": "sigma-",
        "μ": "mu-",
        "π": "pi-",
        "★": "*",
        "☆": "o",
        "≥": ">=",
        "≤": "<=",
        "≈": "~",
        "≠": "!=",
        "→": "->",
        "↔": "<->",
        "·": "-",
        "×": "x",
        "–": "-",
        "—": "-",
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "«": '"',
        "»": '"',
        "…": "...",
        "✓": "[x]",
        "§": "sec.",
    }
    body = md
    for a, b in replacements.items():
        body = body.replace(a, b)
    # Horizontal rules produce broken \\linethickness on Pandoc 1.x
    body = re.sub(r"(?m)^\s*([-*_]){3,}\s*$", "", body)
    # Strip TeX math (greedy enough for table cells)
    body = re.sub(r"\$\$.*?\$\$", " ", body, flags=re.S)
    body = re.sub(r"\$[^$\n]+\$", " ", body)
    body = re.sub(r"\\\(.*?\\\)", " ", body, flags=re.S)
    body = re.sub(r"\\\[.*?\\\]", " ", body, flags=re.S)
    # Remaining backslash commands -> plain text
    body = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", body)
    body = re.sub(r"\\[a-zA-Z]+", " ", body)
    body = body.replace("\\", "")
    # Flatten wide markdown tables (old pandoc + long cells break LaTeX)
    flat_lines: list[str] = []
    for line in body.splitlines():
        if line.strip().startswith("|") and line.strip().endswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            # skip pure separator rows
            if all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells if c):
                continue
            flat_lines.append("- " + " | ".join(cells))
        else:
            flat_lines.append(line)
    body = "\n".join(flat_lines)
    # Keep Latin-1 (accents); drop Greek leftovers / emoji
    body = "".join(ch if ord(ch) < 256 else " " for ch in body)

    with tempfile.TemporaryDirectory(prefix="stp_pdf_") as td:
        td_path = Path(td)
        md_path = td_path / "doc.md"
        plain_path = td_path / "doc.txt"
        pdf_path = td_path / "doc.pdf"
        safe_title = re.sub(r"[^\w\s\-.,:;()/+]", "", title)[:80] or "STP"
        md_path.write_text(f"# {safe_title}\n\n{body}", encoding="utf-8")

        # Strategy 1: Markdown -> PDF (works for simpler handouts)
        # Strategy 2: Markdown -> plain -> PDF (more robust for long packs / nested lists)
        attempts: list[list[str]] = [
            [pandoc, str(md_path), "-o", str(pdf_path), "--standalone"],
            [
                pandoc,
                str(md_path),
                "-t",
                "plain",
                "-o",
                str(plain_path),
            ],
        ]
        for eng in ("xelatex", "pdflatex", "lualatex"):
            if shutil.which(eng, path=env.get("PATH")):
                attempts.insert(
                    1,
                    [
                        pandoc,
                        str(md_path),
                        "-o",
                        str(pdf_path),
                        "--standalone",
                        f"--pdf-engine={eng}",
                    ],
                )

        for cmd in attempts:
            try:
                proc = subprocess.run(
                    cmd,
                    capture_output=True,
                    timeout=180,
                    env=env,
                    check=False,
                )
            except (OSError, subprocess.TimeoutExpired):
                continue
            # Intermediate plain text step
            if cmd[-2:] == ["-o", str(plain_path)] and proc.returncode == 0 and plain_path.exists():
                plain = plain_path.read_text(encoding="utf-8", errors="replace")
                plain = "".join(ch if ord(ch) < 256 else " " for ch in plain)
                wrapped = f"# {safe_title}\n\n" + plain
                plain_md = td_path / "plain.md"
                plain_md.write_text(wrapped, encoding="utf-8")
                try:
                    proc2 = subprocess.run(
                        [pandoc, str(plain_md), "-o", str(pdf_path), "--standalone"],
                        capture_output=True,
                        timeout=180,
                        env=env,
                        check=False,
                    )
                except (OSError, subprocess.TimeoutExpired):
                    continue
                if proc2.returncode != 0:
                    continue
            if pdf_path.exists():
                data = pdf_path.read_bytes()
                if data.startswith(b"%PDF"):
                    return data
                try:
                    pdf_path.unlink()
                except OSError:
                    pass
        return None


def render_handout_pdf_bytes(handout_id: str) -> bytes | None:
    """Render a handout pack as PDF bytes (None if PDF pipeline unavailable)."""
    h = get_handout(handout_id)
    md = render_handout(handout_id)
    return markdown_to_pdf(md, title=h.title)


def pdf_available() -> bool:
    """True if Pandoc is on PATH (LaTeX still required for actual conversion)."""
    import shutil

    return shutil.which("pandoc") is not None
