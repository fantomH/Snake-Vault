# :----------------------------------------------------------------------- INFO
# :[snake_vault/flask_utils/paginate.py]
# /author        : fantomH
# /created       : 2023-09-11 11:42:51 UTC
# /updated       : 2024-05-26 13:16:31 UTC
# /description   : Pagination module for Flask.

from math import ceil

from flask import render_template
from flask import request

class Paginate():
    '''
    Simple module to paginate in Flask.

    Uses Bootstrap 5, so make sure you have the following CSS in the <head>:
    <!-------------------- [ Bootstrap 5 CSS ] -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    And the JavaScript at the end of the <body>:
    <!-------------------- [ Bootstrap javascript ] -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    Might eventually add more CSS toolkit in the future, but don't hold your
    breath.

    ARGUMENTS:

    - entries: This takes all kind of list and divides it into x items per pages.
    - per_page: Set by default to 10 items per page.

    EXAMPLE:

    from flask import Flask, render_template
    from snake_vault.falsk_utils.paginate import Paginate

    @app.route('/')
    def home():
        entries = [x for x in range(100)]
        paginate = Paginate(entries=entries, per_page=20)
        
        return render_template('index.html', 
                                items=paginate.current_entries,
                                paginate=paginate)

    In your HTML:
    
    {% extends "base.html" %}
        {% block content %}
            {% for item in items %}
                <p>{{ item }}</p>
            {% endfor %}

            {{ paginate.load() | safe }}
        {% endblock content %}
    '''

    def __init__(self, entries, per_page=10):
        self.entries = entries
        self.per_page = per_page
        self.total_pages = ceil(len(self.entries) / self.per_page)
        self.url = request.base_url
        self.arguments = request.args.to_dict()
        self.page = request.args.get('page', 1, type=int)

    def __str__(self):
        return f"{self.url}"

    @property
    def current_entries(self):
        start = self.per_page * self.page - self.per_page
        end = self.per_page * self.page
        return self.entries[start:end]

    @property
    def arguments_as_string(self):
        arguments_to_list = []
        for k, v in self.arguments.items():
            if k == "page":
                pass
            else:
                arguments_to_list.append(f"{k}={v}")

        arguments_to_string = '&'.join(arguments_to_list) + "&"
        return arguments_to_string

    @property
    def base_url(self):
        return f"{self.url}?{self.arguments_as_string}"

    @property
    def links(self):
        links_construct = []
        for c in range(self.total_pages):
            c = c + 1
            if c == self.page:
                link = f'<li class="page-item active"><a class="page-link" href="{self.base_url}page={c}">{c}</a></li>'
                links_construct.append(link)
            else:
                link = f'<li class="page-item"><a class="page-link" href="{self.base_url}page={c}">{c}</a></li>'
                links_construct.append(link)
        return "\n".join(links_construct)

    @property
    def has_previous(self):
        if self.page < 2:
            return "disabled"
        else:
            return ""

    @property
    def previous_link(self):
        return f'<a class="page-link" href="{self.base_url}page={self.page - 1}">Previous</a>'

    @property
    def has_next(self):
        if self.total_pages - self.page == 0:
            return "disabled"
        else:
            return ""

    @property
    def next_link(self):
        return f'<a class="page-link" href="{self.base_url}page={self.page + 1}">Next</a>'

    def load(self):
        navigation = f"""
            <nav aria-label="Page navigation example">
                <ul class="pagination justify-content-end">
                    <li class="page-item {self.has_previous}">
                        {self.previous_link}
                    </li>
                    {self.links}
                    <li class="page-item {self.has_next}">
                        {self.next_link}
                    </li>
                </ul>
            </nav>
            """

        return navigation
