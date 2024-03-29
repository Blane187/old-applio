from __future__ import annotations

from typing import Iterable
import gradio as gr

# gr.themes.builder()
from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes
import time


class Acayun(Base):
    def __init__(
        self,
        *,
        primary_hue: colors.Color | str = colors.green,
        secondary_hue: colors.Color | str = colors.emerald,
        neutral_hue: colors.Color | str = colors.neutral,
        spacing_size: sizes.Size | str = sizes.spacing_md,
        radius_size: sizes.Size | str = sizes.radius_md,
        text_size: sizes.Size | str = sizes.text_lg,
        font: fonts.Font | str | Iterable[fonts.Font | str] = (
            "Inter V",
            fonts.GoogleFont("Asap"),
            "ui-sans-serif",
            "sans-serif",
        ),
        font_mono: fonts.Font | str | Iterable[fonts.Font | str] = (
            "ui-monospace",
            fonts.GoogleFont("Fira Code"),
            "Consolas",
            "monospace",
        ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        self.name = ("Acayun",)
        self.secondary_100 = ("#e2effc",)
        self.secondary_200 = ("#bfa1ff",)
        self.secondary_300 = ("#9485d2",)
        self.secondary_400 = ("#8b37f9",)
        self.secondary_50 = ("#f1f8fe",)
        self.secondary_500 = ("#c5a1ff",)
        self.secondary_600 = ("#bfa1ff",)
        self.secondary_700 = ("#ae9df8",)
        self.secondary_800 = ("#9485d2",)
        self.secondary_900 = ("#9e5cf4",)
        self.secondary_950 = ("#7c48c1",)
        self.neutral_100 = ("#e2effc",)
        self.neutral_200 = ("#bfa1ff",)
        self.neutral_300 = ("#9485d2",)
        self.neutral_400 = ("#8b37f9",)
        self.neutral_50 = ("#f1f8fe",)
        self.neutral_500 = ("#c5a1ff",)
        self.neutral_600 = ("#bfa1ff",)
        self.neutral_700 = ("#ae9df8",)
        self.neutral_800 = ("#9485d2",)
        self.neutral_900 = ("#9e5cf4",)
        self.neutral_950 = ("#7c48c1",)
        self.primary_100 = ("#e2effc",)
        self.primary_200 = ("#bfa1ff",)
        self.primary_300 = ("#9485d2",)
        self.primary_400 = ("#8b37f9",)
        self.primary_50 = ("#f1f8fe",)
        self.primary_500 = ("#c5a1ff",)
        self.primary_600 = ("#bfa1ff",)
        self.primary_700 = ("#ae9df8",)
        self.primary_800 = ("#9485d2",)
        self.primary_900 = ("#9e5cf4",)
        self.primary_950 = ("#7c48c1",)
        super().set(
            # @iacat.
            background_fill_primary="#000000",
            background_fill_primary_dark="#000000",
            background_fill_secondary="#25212e",
            background_fill_secondary_dark="#25212e",
            block_background_fill="#15121a",
            block_background_fill_dark="#15121a",
            block_border_color="#2f2a3b",
            block_border_color_dark="#2f2a3b",
            block_border_width="1px",
            block_info_text_color="#c3b3f2",
            block_info_text_color_dark="#c3b3f2",
            block_info_text_size="*text_sm",
            block_info_text_weight="400",
            block_label_background_fill="#19191900",
            block_label_background_fill_dark="#19191900",
            block_label_border_color="#242424",
            block_label_border_color_dark="#242424",
            block_label_border_width="1px",
            block_label_margin="0",
            block_label_padding="*spacing_sm *spacing_lg",
            block_label_radius="calc(*radius_lg - 1px) 0 calc(*radius_lg - 1px) 0",
            block_label_right_radius="0 calc(*radius_lg - 1px) 0 calc(*radius_lg - 1px)",
            block_label_shadow="*block_shadow",
            block_label_text_color="#9e5cf4",
            block_label_text_color_dark="#9e5cf4",
            block_label_text_size="*text_sm",
            block_label_text_weight="400",
            block_padding="*spacing_xl calc(*spacing_xl + 2px)",
            block_radius="*radius_lg",
            block_shadow="#00000000",
            block_shadow_dark="#00000000",
            block_title_background_fill="#19191900",
            block_title_background_fill_dark="#19191900",
            block_title_border_color="#242424",
            block_title_border_color_dark="#242424",
            block_title_border_width="0px",
            block_title_padding="0",
            block_title_radius="none",
            block_title_text_color="#c5a1ff",
            block_title_text_color_dark="#c5a1ff",
            block_title_text_size="*text_md",
            block_title_text_weight="bold",
            body_background_fill="url('https://media.discordapp.net/attachments/1129587026598039632/1163639627475853312/okayu.png') #000000 no-repeat right bottom/auto 55svh padding-box fixed",
            body_background_fill_dark="url('https://media.discordapp.net/attachments/1129587026598039632/1163639627475853312/okayu.png') #000000 no-repeat right bottom/auto 55svh padding-box fixed",
            body_text_color="#dfccfc",
            body_text_color_dark="#dfccfc",
            body_text_color_subdued="#e9defa",
            body_text_color_subdued_dark="#e9defa",
            body_text_size="*text_md",
            body_text_weight="400",
            border_color_accent="#2f2a3b",
            border_color_accent_dark="#2f2a3b",
            border_color_primary="#2f2a3b",
            border_color_primary_dark="#2f2a3b",
            button_border_width="*input_border_width",
            button_border_width_dark="*input_border_width",
            button_cancel_background_fill="#242424",
            button_cancel_background_fill_dark="#242424",
            button_cancel_background_fill_hover="#202020",
            button_cancel_background_fill_hover_dark="#202020",
            button_cancel_border_color="#ECF2F7",
            button_cancel_border_color_dark="#ECF2F7",
            button_cancel_border_color_hover="#c5a1ff",
            button_cancel_border_color_hover_dark="#c5a1ff",
            button_cancel_text_color="#8b37f9",
            button_cancel_text_color_dark="#8b37f9",
            button_cancel_text_color_hover="#c5a1ff",
            button_cancel_text_color_hover_dark="#bfa1ff",
            button_large_padding="*spacing_lg calc(2 * *spacing_lg)",
            button_large_radius="*radius_lg",
            button_large_text_size="*text_lg",
            button_large_text_weight="600",
            button_primary_background_fill="#191919",
            button_primary_background_fill_dark="#191919",
            button_primary_background_fill_hover="#8b37f9",
            button_primary_background_fill_hover_dark="#8b37f9",
            button_primary_border_color="#8b37f9",
            button_primary_border_color_dark="#8b37f9",
            button_primary_border_color_hover="#c5a1ff",
            button_primary_border_color_hover_dark="#c5a1ff",
            button_primary_text_color="#c5a1ff",
            button_primary_text_color_dark="#c5a1ff",
            button_primary_text_color_hover="#ffffff",
            button_primary_text_color_hover_dark="#ffffff",
            button_secondary_background_fill="#242424",
            button_secondary_background_fill_dark="#242424",
            button_secondary_background_fill_hover="#8b37f9",
            button_secondary_background_fill_hover_dark="#8b37f9",
            button_secondary_border_color="#25212e",
            button_secondary_border_color_dark="#25212e",
            button_secondary_border_color_hover="#25212e",
            button_secondary_border_color_hover_dark="#25212e",
            button_secondary_text_color="#ae9dff",
            button_secondary_text_color_dark="#ae9dff",
            button_secondary_text_color_hover="#ffffff",
            button_secondary_text_color_hover_dark="#ffffff",
            button_shadow="none",
            button_shadow_active="none",
            button_shadow_hover="none",
            button_small_padding="*spacing_sm calc(2 * *spacing_sm)",
            button_small_radius="*radius_lg",
            button_small_text_size="*text_md",
            button_small_text_weight="400",
            button_transition="background-color 0.2s ease",
            checkbox_background_color="#25212e",
            checkbox_background_color_dark="#25212e",
            checkbox_background_color_focus="#25212e",
            checkbox_background_color_focus_dark="#25212e",
            checkbox_background_color_hover="#25212e",
            checkbox_background_color_hover_dark="#25212e",
            checkbox_background_color_selected="#8b37f9",
            checkbox_background_color_selected_dark="#8b37f9",
            checkbox_border_color="##ae9df8",
            checkbox_border_color_dark="#ae9df8",
            checkbox_border_color_focus="#8b37f9",
            checkbox_border_color_focus_dark="#8b37f9",
            checkbox_border_color_hover="#8b37f9",
            checkbox_border_color_hover_dark="#8b37f9",
            checkbox_border_color_selected="#8b37f9",
            checkbox_border_color_selected_dark="#8b37f9",
            checkbox_border_radius="*radius_sm",
            checkbox_border_width="1px",
            checkbox_border_width_dark="1px",
            checkbox_check="url(\"data:image/svg+xml,%3csvg viewBox='0 0 16 16' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M12.207 4.793a1 1 0 010 1.414l-5 5a1 1 0 01-1.414 0l-2-2a1 1 0 011.414-1.414L6.5 9.086l4.293-4.293a1 1 0 011.414 0z'/%3e%3c/svg%3e\")",
            checkbox_label_background_fill="#25212e",
            checkbox_label_background_fill_dark="#25212e",
            checkbox_label_background_fill_hover="#25212e",
            checkbox_label_background_fill_hover_dark="#25212e",
            checkbox_label_background_fill_selected="#25212e",
            checkbox_label_background_fill_selected_dark="#25212e",
            checkbox_label_border_color="#242424",
            checkbox_label_border_color_dark="#242424",
            checkbox_label_border_color_hover="#8b37f9",
            checkbox_label_border_color_hover_dark="#8b37f9",
            checkbox_label_border_width="1px",
            checkbox_label_border_width_dark="1px",
            checkbox_label_gap="*spacing_lg",
            checkbox_label_padding="*spacing_md calc(2 * *spacing_md)",
            checkbox_label_shadow="none",
            checkbox_label_text_color="#ECF2F7",
            checkbox_label_text_color_dark="#ECF2F7",
            checkbox_label_text_color_selected="#ffffff",
            checkbox_label_text_color_selected_dark="#ffffff",
            checkbox_label_text_size="*text_md",
            checkbox_label_text_weight="400",
            checkbox_shadow="*input_shadow",
            color_accent="*primary_500",
            color_accent_soft="#242424",
            color_accent_soft_dark="#242424",
            container_radius="*radius_lg",
            embed_radius="*radius_lg",
            error_background_fill="#242424",
            error_background_fill_dark="#242424",
            error_border_color="#ECF2F7",
            error_border_color_dark="#ECF2F7",
            error_border_width="1px",
            error_border_width_dark="1px",
            error_text_color="#ffffff",
            error_text_color_dark="#ffffff",
            form_gap_width="0px",
            input_background_fill="#242424",
            input_background_fill_dark="#242424",
            input_background_fill_focus="#242424",
            input_background_fill_focus_dark="#242424",
            input_background_fill_hover="#202020",
            input_background_fill_hover_dark="#202020",
            input_border_color="#ECF2F7",
            input_border_color_dark="#ECF2F7",
            input_border_color_focus="#ECF2F7",
            input_border_color_focus_dark="#ECF2F7",
            input_border_color_hover="#c5a1ff",
            input_border_color_hover_dark="#c5a1ff",
            input_border_width="0px",
            input_padding="*spacing_xl",
            input_placeholder_color="#ECF2F730",
            input_placeholder_color_dark="#ECF2F730",
            input_radius="*radius_lg",
            input_shadow="#ECF2F700",
            input_shadow_dark="#ECF2F700",
            input_shadow_focus="#ECF2F700",
            input_shadow_focus_dark="#ECF2F700",
            input_text_size="*text_md",
            input_text_weight="400",
            layout_gap="*spacing_xxl",
            link_text_color="#ffffff",
            link_text_color_active="#ffffff",
            link_text_color_active_dark="#ffffff",
            link_text_color_dark="#ffffff",
            link_text_color_hover="#ffffff",
            link_text_color_hover_dark="#ffffff",
            link_text_color_visited="#ffffff",
            link_text_color_visited_dark="#ffffff",
            loader_color="#8b37f9",
            loader_color_dark="#8b37f9",
            panel_background_fill="#191919",
            panel_background_fill_dark="#191919",
            panel_border_color="#8b37f9",
            panel_border_color_dark="#8b37f9",
            panel_border_width="0",
            prose_header_text_weight="600",
            prose_text_size="*text_md",
            prose_text_weight="400",
            radio_circle="url(\"data:image/svg+xml,%3csvg viewBox='0 0 16 16' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3ccircle cx='8' cy='8' r='3'/%3e%3c/svg%3e\")",
            section_header_text_size="*text_md",
            section_header_text_weight="400",
            shadow_drop="rgba(0,0,0,0.05) 0px 1px 2px 0px",
            shadow_drop_lg="0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)",
            shadow_inset="rgba(0,0,0,0.05) 0px 2px 4px 0px inset",
            shadow_spread="#000000",
            shadow_spread_dark="#000000",
            slider_color="#8b37f9",
            slider_color_dark="#8b37f9",
            stat_background_fill="#8b37f9",
            stat_background_fill_dark="#8b37f9",
            table_border_color="#ECF2F79",
            table_border_color_dark="#ECF2F7",
            table_even_background_fill="#191919",
            table_even_background_fill_dark="#191919",
            table_odd_background_fill="#242424",
            table_odd_background_fill_dark="#242424",
            table_radius="*radius_lg",
            table_row_focus="#ECF2F7",
            table_row_focus_dark="#ECF2F7",
        )
