"""Streamlit session helpers for local student accounts.

Global chrome: ``render_auth_topbar()`` is mounted from ``page_header`` /
``render_hero`` so login stays available on every page (top-right).
"""

from __future__ import annotations

from typing import Any

import streamlit as st

from stp.education.accounts import (
    StudentProgress,
    UserRecord,
    authenticate,
    create_account,
    load_progress,
    log_activity,
    save_progress,
)
from stp.i18n.core import get_lang, t

SESSION_USER = "stp_auth_user"
SESSION_PROGRESS = "stp_auth_progress"


def current_user() -> UserRecord | None:
    data = st.session_state.get(SESSION_USER)
    if not data or not isinstance(data, dict):
        return None
    try:
        return UserRecord(
            **{k: data[k] for k in UserRecord.__dataclass_fields__ if k in data}
        )
    except TypeError:
        return None


def is_logged_in() -> bool:
    return current_user() is not None


def set_session_user(user: UserRecord) -> None:
    # Never keep password material in session_state
    st.session_state[SESSION_USER] = user.public_dict()
    progress = load_progress(user.user_id)
    if progress is None:
        progress = StudentProgress(
            user_id=user.user_id,
            username=user.username,
            display_name=user.display_name,
        )
        save_progress(progress)
    st.session_state[SESSION_PROGRESS] = progress.to_dict()
    _apply_checklist_to_session(progress)


def clear_session_user() -> None:
    st.session_state.pop(SESSION_USER, None)
    st.session_state.pop(SESSION_PROGRESS, None)


def get_progress() -> StudentProgress | None:
    user = current_user()
    if not user:
        return None
    raw = st.session_state.get(SESSION_PROGRESS)
    if isinstance(raw, dict) and raw.get("user_id") == user.user_id:
        return StudentProgress.from_dict(raw)
    progress = load_progress(user.user_id)
    if progress:
        st.session_state[SESSION_PROGRESS] = progress.to_dict()
    return progress


def refresh_progress() -> StudentProgress | None:
    user = current_user()
    if not user:
        return None
    progress = load_progress(user.user_id)
    if progress:
        st.session_state[SESSION_PROGRESS] = progress.to_dict()
    return progress


def update_progress(progress: StudentProgress) -> None:
    st.session_state[SESSION_PROGRESS] = progress.to_dict()


def _apply_checklist_to_session(progress: StudentProgress) -> None:
    for key, done in progress.checklist.items():
        st.session_state[key] = bool(done)


def sync_checklist_from_session(progress: StudentProgress) -> StudentProgress:
    """Persist any ``lp_*`` checklist keys currently in session_state."""
    changed = False
    for k, v in list(st.session_state.items()):
        if not isinstance(k, str) or not k.startswith("lp_"):
            continue
        val = bool(v)
        if progress.checklist.get(k) != val:
            progress.checklist[k] = val
            changed = True
    if changed:
        log_activity(progress, "checklist_sync", {"n": len(progress.checklist)})
        save_progress(progress)
        update_progress(progress)
    return progress


def _logout() -> None:
    progress = get_progress()
    if progress:
        log_activity(progress, "logout", {})
        save_progress(progress)
    clear_session_user()
    st.rerun()


def _render_login_form(key_prefix: str) -> None:
    with st.form(f"{key_prefix}_login_form", clear_on_submit=False):
        username = st.text_input(t("auth.username"), max_chars=64, key=f"{key_prefix}_login_user")
        password = st.text_input(
            t("auth.password"),
            type="password",
            max_chars=128,
            key=f"{key_prefix}_login_pw",
        )
        submitted = st.form_submit_button(t("auth.btn_login"), type="primary", width="stretch")
    if submitted:
        u, err = authenticate(username, password)
        if err or not u:
            st.error(t(f"auth.err_{err or 'invalid_credentials'}"))
        else:
            set_session_user(u)
            st.success(t("auth.login_ok"))
            st.rerun()


def _render_register_form(key_prefix: str) -> None:
    st.caption(t("auth.register_hint"))
    with st.form(f"{key_prefix}_register_form", clear_on_submit=False):
        username = st.text_input(
            t("auth.username"), max_chars=64, key=f"{key_prefix}_reg_user"
        )
        display_name = st.text_input(
            t("auth.display_name"), max_chars=80, key=f"{key_prefix}_reg_name"
        )
        password = st.text_input(
            t("auth.password"),
            type="password",
            max_chars=128,
            key=f"{key_prefix}_reg_pw",
        )
        password2 = st.text_input(
            t("auth.password_confirm"),
            type="password",
            max_chars=128,
            key=f"{key_prefix}_reg_pw2",
        )
        submitted = st.form_submit_button(
            t("auth.btn_register"), type="primary", width="stretch"
        )
    if submitted:
        if password != password2:
            st.error(t("auth.err_password_mismatch"))
        else:
            u, err = create_account(
                username,
                password,
                display_name=display_name,
                lang_pref=get_lang(),
            )
            if err or not u:
                st.error(t(f"auth.err_{err or 'invalid_username'}"))
            else:
                set_session_user(u)
                st.success(t("auth.register_ok"))
                st.rerun()


def render_login_register_forms(*, key_prefix: str = "main", compact: bool = False) -> bool:
    """Full login/register UI. Returns True if user is logged in."""
    user = current_user()
    if user:
        st.success(t("auth.welcome_back", name=user.display_name))
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"**{t('auth.username')}:** `{user.username}`")
            st.markdown(f"**{t('auth.member_since')}:** {user.created_at[:10]}")
        with c2:
            if st.button(t("auth.logout"), key=f"{key_prefix}_logout_main", width="stretch"):
                _logout()
        return True

    if compact:
        st.caption(t("auth.topbar_hint"))
    tab_login, tab_reg = st.tabs([t("auth.tab_login"), t("auth.tab_register")])
    with tab_login:
        _render_login_form(f"{key_prefix}_in")
    with tab_reg:
        _render_register_form(f"{key_prefix}_up")
    return is_logged_in()


def render_auth_topbar() -> None:
    """Persistent top-right account control (every page via page chrome)."""
    st.markdown(
        '<div class="stp-auth-topbar-anchor" aria-hidden="true"></div>',
        unsafe_allow_html=True,
    )

    user = current_user()
    # Push controls to the upper-right of the main pane
    _spacer, right = st.columns([3.2, 1.15], gap="small")
    with right:
        st.markdown('<div class="stp-auth-topbar-inner">', unsafe_allow_html=True)
        if user:
            short = (user.display_name or user.username)[:22]
            label = f"👤 {short}"
            with st.popover(label, use_container_width=True):
                st.markdown(f"**{user.display_name}**")
                st.caption(f"@{user.username}")
                st.caption(t("auth.session_persistent"))
                try:
                    st.page_link(
                        "pages/9_Evaluaciones.py",
                        label=t("nav.evaluaciones"),
                        icon="✅",
                    )
                except (KeyError, Exception):
                    st.caption(f"✅ {t('nav.evaluaciones')}")
                if st.button(
                    t("auth.logout"),
                    key="stp_topbar_logout",
                    type="secondary",
                    width="stretch",
                ):
                    _logout()
        else:
            label = f"🔑 {t('auth.topbar_guest')}"
            with st.popover(label, use_container_width=True):
                render_login_register_forms(key_prefix="topbar", compact=True)
        st.markdown("</div>", unsafe_allow_html=True)


def render_auth_sidebar() -> None:
    """Account block in the sidebar (mirrors top bar; full forms when guest)."""
    user = current_user()
    st.sidebar.markdown(
        f'<div class="stp-sidebar-section">{t("auth.section")}</div>',
        unsafe_allow_html=True,
    )
    if user:
        st.sidebar.caption(t("auth.logged_as", name=user.display_name))
        st.sidebar.caption(f"@{user.username}")
        if st.sidebar.button(t("auth.logout"), key="stp_logout_btn", width="stretch"):
            _logout()
        try:
            st.sidebar.page_link(
                "pages/9_Evaluaciones.py",
                label=t("nav.evaluaciones"),
                icon="✅",
            )
        except (KeyError, Exception):
            st.sidebar.caption(f"✅ {t('nav.evaluaciones')}")
    else:
        st.sidebar.caption(t("auth.guest_hint"))
        with st.sidebar.expander(t("auth.login_or_register"), expanded=False):
            render_login_register_forms(key_prefix="side", compact=True)


def activity_label(action: str) -> str:
    key = f"auth.act_{action}"
    label = t(key)
    return label if label != key else action


def public_user_dict() -> dict[str, Any] | None:
    u = current_user()
    return u.public_dict() if u else None
