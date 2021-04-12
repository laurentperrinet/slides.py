#/usr/bin/env python3
# -*- coding: utf-8 -*-
#import os
import markdown
import base64

class Slides:
    """
    TODO: make a class for one slide with labels etc - compile at the end
    TODO: a slide show is a (possibly nested) list of slides

    """
    def __init__(self, meta):
        self.meta = meta
        # Simply using https://docs.python.org/3.3/library/string.html#format-string-syntax to format strings...
        self.header ="""<!doctype html>
<html>
    <head>
        <meta charset="utf-8"/>

        <title>{short_title} - {conference}</title>

        <meta name="description" content="{title}">
        <meta name="author" content="{author}">

        <meta name="apple-mobile-web-app-capable" content="yes" >
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">

    	<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

        <!-- General and theme style sheets -->
        <link rel="stylesheet" href="{reveal_path}dist/reveal.css">
        <link rel="stylesheet" href="{reveal_path}dist/theme/{theme}.css" id="theme">

    	<!-- Theme used for syntax highlighting of code -->
        <link rel="stylesheet" href="{reveal_path}plugin/highlight/zenburn.css">

         <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
         <!--[if lt IE 9]>
         <script src="{reveal_path}lib/js/html5shiv.js"></script>
         <![endif]-->
    """.format(**meta)

        self.header += """
        <!-- Get Font-awesome from cdn -->
        <!-- <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.css"> -->
    </head>

<body>
    <div class="reveal">
        <div class="slides">
        """

        self.footer = """
        </div>
    </div>

    <script src="{reveal_path}dist/reveal.js"></script>
    <script src="{reveal_path}plugin/zoom/zoom.js"></script>
    <script src="{reveal_path}plugin/notes/notes.js"></script>
    <script src="{reveal_path}plugin/search/search.js"></script>
    <script src="{reveal_path}plugin/markdown/markdown.js"></script>
    <script src="{reveal_path}plugin/highlight/highlight.js"></script>

        """.format(**meta)
        self.footer +="""
	<script>

            // Full list of configuration options available at:
            // https://github.com/hakimel/reveal.js#configuration
            Reveal.initialize({
        """
        self.footer +="""
                // The "normal" size of the presentation, aspect ratio will be preserved
                // when the presentation is scaled to fit different resolutions. Can be
                // specified using percentage units.
                width: {width},
                height: {height},

                // Factor of the display size that should remain empty around the content
                margin: {margin},
        """.format(**meta)
        self.footer +="""
                // Display a presentation progress bar
                progress: true,
                slideNumber: 'c/t',

                // Push each slide change to the browser history
                //history: false,

                // Vertical centering of slides
                center: true,

                // Enables touch navigation on devices with touch input
                touch: true,

                // Bounds for smallest/largest possible scale to apply to content
                minScale: 0.2,
                maxScale: 2.5,

                // Display controls in the bottom right corner
                controls: false,

                // Enable keyboard shortcuts for navigation
                keyboard: true,

                // Enable the slide overview mode
                overview: true,

                // This slide transition gives best results:
                transition: 'fade', // default/cube/page/concave/zoom/linear/fade/none

                // Transition speed
                transitionSpeed: 'slow', // default/fast/slow

                // Transition style for full page backgrounds
                backgroundTransition: 'none', // default/linear/none

			    // Turns fragments on and off globally
                fragments: true,

                // Theme
                theme: '{theme}', // available themes are in /dist/theme

        """.format(**meta)
        if self.meta['draft']:
            self.footer +="""
                // Notes are only visible to the speaker inside of the speaker view. If you wish to share your notes with others you can initialize reveal.js with the showNotes config value set to true. Notes will appear near the presentations. https://revealjs.com/speaker-view/
                showNotes: true,
        """
        self.footer +="""

                // Learn about plugins: https://revealjs.com/plugins/
                plugins: [ RevealZoom, RevealNotes, RevealSearch, RevealMarkdown, RevealHighlight ]
            });
    </script>

    </body>
</html>
        """

        self.body = ''

    def open_section(self):
        self.body +=  "<section>"

    def hide_slide(self, **kwargs):
        """
        do nothing
        """
        pass

    def data_uri(self, fname):
        """
        reads an image and transforms it to a sequence of bytes
        """
        if str(fname)[:4] == 'http':
            from urllib.request import urlopen
            fread = urlopen(fname).read()
        else:
            fread = open(fname, 'rb').read()
        return base64.b64encode(fread).decode('utf-8').replace('\n', '')


    def embed(self, fname, ftype='image'):
        """

        Convert to bytes

        https://www.iandevlin.com/blog/2012/09/html5/html5-media-and-data-uri

        """
        data_uri = self.data_uri(fname)
        ext = str(fname)[-3:]
        data_str = f'data:{ftype}/{ext};base64,{data_uri}'
        return data_str

    def embed_image(self, image_fname):
        return self.embed(image_fname, ftype='image')

    def embed_video(self, video_fname):
        return self.embed(video_fname, ftype='video')

    def content_imagelet(self, fname, height_px, embed=None):
        if embed is None: embed = self.meta['embed']
        if embed:
            data_src = self.embed_image(fname)
            return f'<img class="plain" data-src="{data_src}"  height="{height_px}px" />'
        else:
            return f'<img class="plain" data-src="{fname}"  height="{height_px}px" />'

    def add_slide(self, hide=False, image_fname=None, video_fname=None, content='', notes='', md=False, embed=None):
        if hide: return 'Slide hidden'
        # https://developer.mozilla.org/fr/docs/Web/CSS/background-size
        if not image_fname is None:
            if (embed is None and self.meta['embed']) or ((not embed is None ) and embed):
                image_fname = self.embed_image(image_fname)
            slide = '<section data-background="{image_fname}" data-background-size="{height}px"> '.format(image_fname=image_fname, height = self.meta['height'])
        elif not video_fname is None:
            if (embed is None and self.meta['embed']) or ((not embed is None ) and embed):
                video_fname = self.embed_video(video_fname)
            slide = '<section data-background-video="{}">'.format(video_fname)
        elif md:
            slide = """
<section data-markdown>
<script type="text/template">
        """
        else:
            slide = "<section>"

        slide += content

        if md:
            slide += """
</script>
            """

        if not notes=='':
            slide +="""
                <aside class="notes">
                 {}
                </aside>
                """.format(markdown.markdown(notes))

        slide += """
</section>
        """
        self.body += slide

    def add_slide_outline(self, i=None, title='Outline', notes=''):
        content = self.content_title(title)  + '\n<ol>\n'
        for i_, section in enumerate(self.meta['sections']):
            section = markdown.markdown(section)[3:-4]
            if i_ is i:
                content += """
                    <h3>
                    <li>
                    <p class="fragment highlight-red">
                    {}
                    </p>
                    </li>
                    </h3>
                    """.format(section)
            else:
                content += """
                    <h3>
                    <li>
                    {}
                    </li>
                    </h3>
                    """.format(section)
        content += """
                     </ol>
                    """
        self.add_slide(content=content, notes=notes)

    def add_slide_summary(self, list_of_points, title='Interim summary', fragment_type=None, notes=''):
        """
        fragment_type to be chosen from:

        fade-in	Start visible, fade in
        fade-out	Start visible, fade out
        fade-up	Slide up while fading in
        fade-down	Slide down while fading in
        fade-left	Slide left while fading in
        fade-right	Slide right while fading in
        fade-in-then-out	Fades in, then out on the next step
        fade-in-then-semi-out	Fades in, then to 50% on the next step
        grow	Scale up
        shrink	Scale down
        strike	Strike through
        highlight-red	Turn text red
        highlight-green	Turn text green
        highlight-blue	Turn text blue
        highlight-current-red	Turn text red, then back to original on next step
        highlight-current-green	Turn text green, then back to original on next step
        highlight-current-blue	Turn text blue, then back to original on next step

        https://revealjs.com/fragments/
        """
        content = self.content_title(title) + """
            <ul>
            """
        if not fragment_type is None :
            fragment_begin = f'<p class="fragment {fragment_type}">'
        else:
            fragment_begin = '<p>'

        for point in list_of_points:
            content += f"""
{fragment_begin}
<h3>
<li>{markdown.markdown(point)[3:-4]}</li>
</h3>
</p>
"""
        content += "</ul>"
        self.add_slide(content=content, notes=notes)

    def content_title(self, title):
        if title is None:
            return ''
        else:
            return "<h3>{}</h3>".format(title)


    def content_figures(self, list_of_figures, transpose=False,
                        list_of_weights=None, title=None, height=None, width=None,
                        embed=None, fragment=False, url=None,
                        bgcolor="white", cell_bgcolor="white"):
        content =  self.content_title(title)

        if height is None:
            height = self.meta['height']
        content += """
            <div align="center">
            <table border=0px valign="top" bgcolor={bgcolor} height={height}>
            """.format(bgcolor=bgcolor, height=height)

        n_fig = len(list_of_figures)
        if list_of_weights is None:#str(int() ) +"%"
            sizes = [1./n_fig] * n_fig #+"%" for _ in list_of_figures]
        else:
            total_weight = sum(list_of_weights)
            sizes = [weight/total_weight for weight in list_of_weights]#1./n_fig*
            # print(sizes)
        if not transpose: # one line many columns
            content += """
            <tr padding=0px style="vertical-align:top" bgcolor={bgcolor}>
            """.format(bgcolor=bgcolor)

        for i_, (size, image_fname) in enumerate(zip(sizes, list_of_figures)):
            if width is None:
                width_str = " "
                width_ = int(size*self.meta['width'])#*height/self.meta['height']
                # print(width_)
            else:
                width_ = int(size*width)
                width_str = 'width="{width_}px"'.format(width_=width_)

            if (embed is None and self.meta['embed']) or ((not embed is None ) and embed):
                # data_uri = base64.b64encode(open(fname, 'rb').read()).decode('utf-8').replace('\n', '')
                # fname = 'data:image/{ext};base64,{data_uri}'.format(ext=fname[-3:], data_uri=data_uri)
                image_fname = self.embed_image(image_fname)

            if fragment and i_>0:
                fragment_begin = '<p class="fragment">'
            else:
                fragment_begin = '<p>'

            if not url is None:
                fragment_begin += '<a href="' + url[i_] + '">'
                fragment_end = '</a></p>'
            else:
                fragment_end = '</p>'

            if not transpose: # one line many columns
                content += """
                <td height={height} width="{width}" padding-top=0px padding-bottom=0px style="text-align:center; vertical-align:top" bgcolor="{cell_bgcolor}" >
                {fragment_begin}
                    <img class="plain" data-src="{fname}"  height="{height}px" {width_str} />
                {fragment_end}
                </td>
                """.format(cell_bgcolor=cell_bgcolor, height=int(height),
                           width=width_, width_str=width_str, fname=image_fname,
                           fragment_begin=fragment_begin, fragment_end=fragment_end)
            else:
                content += """
                <tr style="vertical-align:middle" bgcolor="{cell_bgcolor}"  height="{height_}px">
                    <td width="100%" style="text-align:top; vertical-align:top" bgcolor="{cell_bgcolor}" >
                    {fragment_begin}
                        <img class="plain" data-src="{fname}"  height="{height_}px"  />
                    {fragment_end}
                    </td>
                </tr>
                """.format(cell_bgcolor=cell_bgcolor, height_=int(size*height),
                        fname=image_fname,
                        fragment_begin=fragment_begin, fragment_end=fragment_end)

        # closing table
        if not transpose: # one line many columns
            content += """
            </tr>
            """
        content += """
        </table>
        </div>
        """
        return content

    def content_bib(self, author, year, journal, title='', url=None):
        if not url is None:
            journal = f'<a href="{url}">{journal}</a>'
        content = f'{author} ({year}) <small>{title}</small> <em>{journal}</em>'
        content = f'<div style="text-align:right;">{content}</div>'
        return content

    def close_section(self):
        self.body +=  "\n</section>\n"

    def compile(self, filename='index.html'):
        html = self.header + self.body + self.footer
        with open(filename, 'w') as f: f.write(html)
# s.body += """
# <script>
#       document.getElementById('theme').setAttribute('href','dist/theme/white.css'); return false;">
# </script>
