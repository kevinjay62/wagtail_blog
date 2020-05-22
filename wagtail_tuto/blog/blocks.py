#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-12-23 michael_yin
#
from wagtailcodeblock.blocks import CodeBlock
from wagtail.core import blocks
from wagtail.core.blocks.stream_block import StreamBlock
from wagtail.images.blocks import ImageChooserBlock


class ColumnBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(classname="full title")
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        template = 'blog/blocks/column.html'


class TwoColumnBlock(blocks.StructBlock):

    left_column = ColumnBlock(icon='arrow-right', label='Left column content')
    right_column = ColumnBlock(
        icon='arrow-right',
        label='Right column content'
    )

    class Meta:
        template = 'blog/blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'


class TextBlock(blocks.StreamBlock):
    """Text Block"""

    text = blocks.RichTextBlock()
    excerpt = blocks.RichTextBlock()

    class Meta:
        template = "blog/blocks/text_blocks.html"
        icon = 'grip'
        label = 'Text'


class ContentStreamBlock(StreamBlock):
    """ Used by WagtailCodeBlock"""

    heading = TextBlock()
    paragraph = TextBlock()
    code = CodeBlock(label='Code')
