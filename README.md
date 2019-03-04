Fancier Outlines for Python-Markdown
=====================================

This is a fork of [mdx_outline](https://github.com/aleray/mdx_outline) that adds the option of inserting a "Jump to Top" link at the end of sections. See that project for general usage. This extension currently works with the default settings for mdx\_outline, but it will probably break (for now) if you use non-default settings. 

### Installation

Run the following command:

`$ pip install git+git://github.com/BaeoMaltinsky/fancy_outline.git`

### Usage

To use this extension, place the following marker somewhere in the markdown:

```
[JTT]
```

which inserts the following at the end of `<section class="section1">` elements:

```
<a class="jump-to-top" href="#">Jump to Top</a>
```

This can be anywhere in the text so long as it's somewhere inside of a paragraph. If you're using this with the Pelican plugin [extract_toc](https://github.com/getpelican/pelican-plugins/tree/master/extract_toc), you should place it after `[TOC]`.

You can change the section level the link appears at and the link text with the following syntax:

```
[JTT] {"level": 3, "link_text": "Help! There are too many words here!"}
```

*Because everything is better with JSON!*

This inserts the following at the end of `<section class="section3">` elements:

```
<a class="jump-to-top" href="#">Help! There are too many words here!</a>
```

If you want to include multiple conflicting configurations in the same file, the setting will be based on the first instance in the markdown.
