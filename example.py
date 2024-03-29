from slides import Slides
from slides import slugify
import sys
from pathlib import Path
import os
__author__ = "Laurent Perrinet INT - CNRS"
__licence__ = 'GPL licence'
DEBUG = True
DEBUG = False
"""

Documentation for slides.py - serves as a template for future presentations,
just fork :

https://github.com/laurentperrinet/slides.py

"""

fig_width = 12

# https://docs.python.org/3.8/library/pathlib.html
# import pathlib

home = Path(os.environ['HOME'])

# figpath_talk = Path.cwd().joinpath('figures')
figpath_talk = 'figures'
Path.cwd().joinpath(figpath_talk).mkdir(parents=True, exist_ok=True)

# print(figpath_talk)
# figpath_slides = os.path.join(home, 'quantic/libraries/slides.py/figures/')
figpath_slides = 'https://laurentperrinet.github.io/slides.py/figures/'
#
print(sys.argv)
tag = sys.argv[0].split('.')[0]
if len(sys.argv) > 1:
    slides_filename = sys.argv[1]
else:
    slides_filename = None

slugified = slugify(tag)

print('😎 Welcome to the script generating the slides for ', tag)
try:
    YYYY = int(tag[:4])
    MM = int(tag[5:7])
    DD = int(tag[8:10])
except:
    from datetime import datetime
    DD = datetime.now().day
    MM = datetime.now().month
    YYYY = datetime.now().year

# see https://github.com/laurentperrinet/slides.py

height_px = 80
height_ratio = .7

meta = dict(
 embed=False,
 draft=DEBUG,  # show notes etc
 width=1600,
 height=1000,
 margin=0.1618,
 reveal_path='https://laurentperrinet.github.io/2020-09-14_IWAI/reveal.js-master/',
 theme='simple',
 bgcolor="white",
 author='Perrinet, Laurent U',
 author_link=f'<a href="https://laurentperrinet.github.io/talk/{slugify(tag)}/">Laurent Perrinet</a>',
 title="""A simple way to make slideshows?""",
 short_title="What's slides.py?",
 conference="Example conference",
 conference_url='https://github.com/laurentperrinet/slides.py',
 short_conference=' (Ex conf)',
 location='INT, Marseille (France)',
 abstract="""This is a simple template for the slides package.""",
 YYYY=YYYY, MM=MM, DD=DD,
 tag=tag,
 projects='aprovis-3-d',
 time_start='15:45:00',
 time_end='16:30:00',
 # url=f'https://laurentperrinet.github.io/talk/{slugify(tag)}',
 url='https://laurentperrinet.github.io/slides.py',
 sections=['Intro', 'Methods', 'Results']
)

###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄            QR CODE                      🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################

# https://pythonhosted.org/PyQRCode/rendering.html
# pip3 install pyqrcode
# pip3 install pypng

# figname_qr = Path.cwd().joinpath(figpath_talk).joinpath('qr.png')
figname_qr = os.path.join(figpath_talk, 'qr.png')
if DEBUG or (not Path(figname_qr).is_file()):
    import pyqrcode as pq
    code = pq.create(meta['url'])
    code.png(figname_qr, scale=5)

print(meta['sections'])
s = Slides(meta)

###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄                INTRO                    🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
# path_people = os.path.join(home, 'ownCNRS/2019-01_LACONEU/people')
path_people = home.joinpath('quantic/blog/hugo_academic/content/authors')
# path_people = 'https://laurentperrinet.github.io/authors/'
# ls ~/github/hugo_academic/content/authors/**/avat*
People = ''
People += s.content_imagelet(path_people.joinpath('chloe-pasturel/avatar.png'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('emmanuel-dauce/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('etienne-rey/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('hugo-ladret/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('james-a-bednar/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('jens-kremkow/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('karl-friston/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('kiana-mansour-pour/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('laurent-u-perrinet/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('manuel-samuelides/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('maria-jose-escobar/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('mina-a-khoei/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('nicole-voges/avatar.gif'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('paula-s-leon/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('simon-j-thorpe/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('victor-boutin/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('wahiba-taouali/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('yves-fregnac/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('rick-a-adams/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('anna-montagnini/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('laurent-madelain/avatar.png'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('jean-bernard-damasse/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('stephane-viollet/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('alberto-vergani/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('angelo-franciosini/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('frederic-y-chavane/avatar.png'), height_px, embed=True)
People += s.content_imagelet('https://www.python.org/static/community_logos/python-powered-h-140x182.png', height_px, embed=False)
s.meta['Acknowledgements'] = f"""
<small>
<h5>Acknowledgements:</h5>
<ul><li> Hakim El Hattab for <a href="https://revealjs.com/">reveal-js</a>
<li>Some people...</li>
<li>Lots more people...</li>
</ul>
<BR>
{People}</a>
<BR>
    This work was supported by ....
</small>

"""
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 Should I stay or should I go? 🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
i_section = 0
s.open_section()
###############################################################################
intro = """
<h2 class="title">{title}</h2>
<h3>{author_link}</h3>
""".format(**meta)
# intro += s.content_imagelet('figures/ins-logo.png',
#                             s.meta['height']*.24,
#                             embed=False)
intro += s.content_imagelet('https://laurentperrinet.github.io/slides.py/figures/troislogos.png',
                            s.meta['height']*.32,
                            embed=False)  # bgcolor="black",
intro += """
<h4><a href="{conference_url}">{conference} {short_conference}</a>, {DD}/{MM}/{YYYY} </h4>

{Acknowledgements}
""".format(**meta)
###############################################################################
# s.add_slide(content=intro)
#
# s.add_slide(content=s.content_figures(
#     #[os.path.join(figpath_talk, 'qr.png')], bgcolor="black",
#     [os.path.join(figpath_slides, 'mire.png')], bgcolor=meta['bgcolor'],
#     height=s.meta['height']*1.),
#     #image_fname=os.path.join(figpath_aSPEM, 'mire.png'),
#     notes="""
# Check-list:
# -----------
#
# * (before) bring VGA adaptors, AC plug, remote, pointer
# * (avoid distractions) turn off airport, screen-saver, mobile, sound, ... other running applications...
# * (VP) open monitor preferences / calibrate / title page
# * (timer) start up timer
# * (look) @ audience
#
# http://pne.people.si.umich.edu/PDF/howtotalk.pdf
#
#  """)
#
# s.add_slide(content=s.content_figures([figname_qr], cell_bgcolor=meta['bgcolor'], height=s.meta['height']*height_ratio) + '<BR><a href="{url}"> {url} </a>'.format(url=meta['url']),
#             notes="All the material is available online - please flash this QRcode this leads to a page with links to further references and code ")

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

s.add_slide(content=intro,
            notes="""
* (AUTHOR) Hello, I am Laurent Perrinet from the Institute of Neurosciences of
la Timone in Marseille, a joint unit from the CNRS and the AMU
* (OBJECTIVE) in this short talk, I will demonstrate how to use slides.py to generate
simple slides...
* (ACKNO) and focus on content rather than on form
""")
s.close_section()
###############################################################################
# Methods - 15''
###############################################################################
###############################################################################
s.open_section()
s.add_slide_outline(i_section)
i_section += 1
s.add_slide_summary(
    ['Go fullscreen using the ``f`` key',
     'You can have an overlook using the ``o`` key',
     'Navigate using the arrow keys',
     'see notes using the ``n`` key',
     'getting help using the ``?`` key'],
    title='Useful shortcuts', fragment_type='grow',
    notes="""
* and write notes using markdown

""")
s.close_section()
###############################################################################
# Results - 15''
###############################################################################
###############################################################################
s.open_section()
s.add_slide_outline(i_section)
i_section += 1
s.add_slide(content=s.content_figures(
    [os.path.join(figpath_slides, "troislogos.png")], bgcolor="black",
    height=s.meta['height']*.3, width=s.meta['height']*1.2),
            notes="""
You can embed images.
""")

s.add_slide(content="""
    <video controls autoplay loop width=60%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format(s.embed_video(os.path.join(figpath_talk, 'video.mp4'))),
            notes="""
You can also embed videos.
""")

myurl = 'https://docs.python.org/3/_static/py.png'
myurl = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Gruenebaumpython4cele4.jpg/1200px-Gruenebaumpython4cele4.jpg"
s.add_slide(content=s.content_figures(
                    [myurl], bgcolor="black",
                    height=s.meta['height']*.3),  # width=s.meta['height']*1.2),
            notes="""
You can embed images from an URL.
""")

s.close_section()
###############################################################################
# Conclusion - 15''
###############################################################################
###############################################################################
s.open_section()
s.add_slide_outline()
s.add_slide_summary(title='Conclusion',
                    list_of_points=['install using instructions on <a href=https://github.com/laurentperrinet/slides.py>https://github.com/laurentperrinet/slides.py</a>',
                                    'suggest <a href="https://github.com/laurentperrinet/slides.py/issues">improvments or issues</a>, ',
                                    'fork!'],
                    notes="""
* and write notes using markdown

""")
s.add_slide(content=intro,
            notes="""


* Thanks for your attention!
""")

print(figname_qr)
s.add_slide(content=s.content_figures([figname_qr], cell_bgcolor=meta['bgcolor'], height=s.meta['height']*height_ratio) + '<BR><a href="{url}"> {url} </a>'.format(url=meta['url']),
            notes="All the material is available online - please flash this code this leads to a page with links to further references and code ")

s.close_section()

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################


if slides_filename is None:
    with open("README.md", "w") as text_file:
        text_file.write("""\
# {title}

* What:: talk @ [{conference}{short_conference}]({conference_url})
* Who:: {author}
* Where: {location}, see {url}
* When: {DD:02d}/{MM:02d}/{YYYY}, time: {time_start}-{time_end}

* What:
  * Slides @ https://laurentperrinet.github.io/{tag}
  * Code for slides @ https://github.com/laurentperrinet/{tag}/
  * Abstract: {abstract}

""".format(**meta))

    with open("/tmp/talk.bib", "w") as text_file:
        text_file.write("""\
@inproceedings{{{tag},
    Author = "{author}",
    Booktitle = "{conference}",
    Title = "{title}",
    Abstract = "{abstract}",
    Url = "{url}",
    Year = "{YYYY}",
    Date = "{YYYY}-{MM:02d}-{DD:02d}",
    location = "{location}",
    projects = "{projects}",
    time_start = "{YYYY}-{MM:02d}-{DD:02d}T{time_start}",
    time_start = "{YYYY}-{MM:02d}-{DD:02d}T{time_end}",
    url = "{url}",
    url_slides = "https://laurentperrinet.github.io/{tag}",
    url_code = "https://github.com/laurentperrinet/{tag}/",
}}

""".format(**meta))

else:
    s.compile(filename=slides_filename)

# Check-list:
# -----------
#
# * (before) bring miniDVI adaptors, AC plug, remote, pointer
# * (avoid distractions) turn off airport, screen-saver, mobile, sound, ... other running applications...
# * (VP) open monitor preferences / calibrate / title page
# * (timer) start up timer
# * (look) @ audience
#
# Preparing Effective Presentations
# ---------------------------------
#
# Clear Purpose - An effective image should have a main point and not be just a collection of available data. If the central theme of the image isn't identified readily, improve the paper by revising or deleting the image.
#
# Readily Understood - The main point should catch the attention of the audience immediately. When trying to figure out the image, audience members aren't fully paying attention to the speaker - try to minimize this.
#
# Simple Format - With a simple, uncluttered format, the image is easy to design and directs audience attention to the main point.
#
# Free of Nonessential Information - If information doesn't directly support the main point of the image, reserve this content for questions.
#
# Digestible - Excess information can confuse the audience. With an average of seven images in a 10-minute paper, roughly one minute is available per image. Restrict information to what is extemporaneously explainable to the uninitiated in the allowed length of time - reading prepared text quickly is a poor substitute for editing.
#
# Unified - An image is most effective when information is organized around a single central theme and tells a unified story.
#
# Graphic Format - In graphs, qualitative relationships are emphasized at the expense of precise numerical values, while in tables, the reverse is true. If a qualitative statement, such as "Flow rate increased markedly immediately after stimulation," is the main point of the image, the purpose is better served with a graphic format. A good place for detailed, tabular data is in an image or two held in reserve in case of questions.
#
# Designed for the Current Oral Paper - Avoid complex data tables irrelevant to the current paper. The audience cares about evidence and conclusions directly related to the subject of the paper - not how much work was done.
#
# Experimental - There is no time in a 10-minute paper to teach standard technology. Unless the paper directly examines this technology, only mention what is necessary to develop the theme.
#
# Visual Contrast - Contrasts in brightness and tone between illustrations and backgrounds improves legibility. The best color combinations include white letters on medium blue, or black on yellow. Never use black letters on a dark background. Many people are red/green color blind - avoid using red and green next to each other.
#
# Integrated with Verbal Text - Images should support the verbal text and not merely display numbers. Conversely, verbal text should lay a proper foundation for each image. As each image is shown, give the audience a brief opportunity to become oriented before proceeding. If you will refer to the same image several times during your presentation, duplicate images.
#
# Clear Train of Thought - Ideas developed in the paper and supported by the images should flow smoothly in a logical sequence, without wandering to irrelevant asides or bogging down in detail. Everything presented verbally or visually should have a clear role supporting the paper's central thesis.
#
# Rights to Use Material - Before using any text, image, or other material, make sure that you have the rights to use it. Complex laws and social rules govern how much of someone's work you can reproduce in a presentation. Ignorance is no defense. Check that you are not infringing on copyright or other laws or on the customs of academic discourse when using material.
#
# http://pne.people.si.umich.edu/PDF/howtotalk.pdf
#
