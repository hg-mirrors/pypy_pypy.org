from py.__.documentation.confrest import *

class PyPyPage(Page):
    def fill(self):
        super(PyPyPage, self).fill()
        self.menubar[:] = html.div(
            html.a("home", href="index.html", class_="menu"), " ",
            html.a("news", href="news.html", class_="menu"), " ",
            html.a("consortium", href="consortium.html", class_="menu"), " ",
            html.a("links", href="links.html", class_="menu"), " ",
            html.a("community/coding",
                   href="http://codespeak.net/pypy/dist/pypy/doc/index.html",
                   class_="menu"), " ",
            " ", id="menubar")

class Project(Project):
    title = "PyPy EU Project"
    stylesheet = 'http://codespeak.net/pypy/dist/pypy/doc/style.css'
    encoding = 'latin1'
    prefix_title = "EU/PyPy"
    logo = html.div(
        html.a(html.img(alt="PyPy", id="pyimg",
                        src="http://codespeak.net/pypy/img/py-web1.png",
                        height=110, width=149)),
        html.img(alt="EU Logo", id="extraimg",
                 src="ist.png",
                 height=105, width=213),
        )
    Page = PyPyPage


