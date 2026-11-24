# Copyright Modal Labs 2026
import sys

from modal.output import OutputManager

GREEN = "#7FEE64"

ASCII_LOGO = r"""
    ALINGO FILM MAKER
    تخیل توں حقیقت تک
"""

UNICODE_LOGO_LARGE = ASCII_LOGO

UNICODE_LOGO_SMALL = ASCII_LOGO



def get_logo():
    if sys.stdout.encoding and sys.stdout.encoding.lower().startswith("utf"):
        return UNICODE_LOGO_SMALL
    else:
        return ASCII_LOGO


def print_logo():
    if sys.stdout.isatty():
        OutputManager.get().print(get_logo(), highlight=False, style=GREEN)
