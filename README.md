# Team Colors: Website
# AP CSP Period 3: Team Colors
## [Scrum Board](https://github.com/sarayu-pr11/flask_portfolio/projects/1)
## [Insights with Contributors and Commits](https://github.com/sarayu-pr11/flask_portfolio/graphs/contributors)
## Table of Contents
1. [Contributors]
2. [Pair Share Journals]
3. [Project Ideation]
4. [Sprint 0 - Introduction]
5. [Sprints 1,2 - Innovation]
6. [Sprints 3,4 - Prototyping]
## Contributors
| Name | GitHub ID and Profile | Tasks | Scrum Board | Commits |
|:-----|:----------------------|:-----:|:-----------:|:-------:|
| Sarayu Pochimireddy | [@sarayu-pr11](https://github.com/sarayu-pr11) | [Tasks](https://github.com/sarayu-pr11/flask_portfolio/issues/assigned/sarayu-pr11) |[Scrum Board](https://github.com/sarayu-pr11/flask_portfolio/projects/1?card_filter_query=assignee%3Asarayu-pr11) [Commits](https://github.com/sarayu-pr11/flask_portfolio/commits?author=sarayu-pr11)
| Saathvika Ajith | [@Saathvika-Ajith](https://github.com/Saathvika-Ajith) | [Tasks](https://github.com/sarayu-pr11/flask_portfolio/issues/assigned/Saathvika-Ajith) | [Scrum Board](https://github.com/sarayu-pr11/flask_portfolio/projects/1?card_filter_query=assignee%3Asaathvika-ajith) [Commits](https://github.com/sarayu-pr11/flask_portfolio/commits?author=Saathvika-Ajith)
| Pranavi Inukurti | [@PranaviInukurti](https://github.com/PranaviInukurti) | [Tasks](https://github.com/sarayu-pr11/flask_portfolio/issues/assigned/PranaviInukurti) |[Scrum Board](https://github.com/sarayu-pr11/flask_portfolio/projects/1?card_filter_query=assignee%3Apranaviinukurti) [Commits](https://github.com/sarayu-pr11/flask_portfolio/commits?author=PranaviInukurti)

## Checklist:
### Week 2:
- make an about page for each person
  - include greet project
  - https://github.com/sarayu-pr11/flask_portfolio/issues/4
### Week 3:
- make a dropdown menu
  - each menu needs a stub code page 
  - https://github.com/sarayu-pr11/flask_portfolio/issues/11
- brainstorm ideas for the website content
  - other than about me, that fulfils its purpose
  - https://github.com/sarayu-pr11/flask_portfolio/issues/9
- wireframe concepts for webpage design
  - three or more ideas needed
  - https://github.com/sarayu-pr11/flask_portfolio/issues/6
  
---

## Theme: Color Wheel

### Design Step 1: Ideation
- the theme is a colorwheel guide to del norte
- each slice of the color wheel would coordinate to a specific problem many incoming or resident students would have
- we could build on each problem with multiple layers to the colorwheel
- everything within would be color coded, background will have to be black so colors stand out
### Design Step 2: Specification
### Design Step 3: Prototyping/Developing
### Design Step 4: Testing/Feedback

---

# Previous: [Flask Portfolio Starter](https://nighthawkcodingsociety.com/projectsearch/details/Flask%20Portfolio%20Starter)

Runtime link: https://portfolio.nighthawkcodingsociety.com/

### Idea
Starter code should be fun and practical.

### Visual thoughts
 Organize with Bootstrap menu 
 Add some color and fun through VANTA Visuals (birds, halo, solar, net)
 Show some practical and fun links (hrefs) like Twitter, Git, YouTube
 Show project specific links (hrefs) per page

## Table of Contents
1. Greeting Project, Self Grade, and Justification
2. Daily Journal with Video Notes

### Implementation progress (August 13th, 2021)
 Project entry point is main.py, this enables Flask Web App and provides capability to renders templates (HTML files)
 The main.py is the  Web Server Gateway Interface, essentially it contains a HTTP route and HTML file relationship.  The Python code constructs WSGI relationships for index, kangaroos, walruses, and hawkers.
 The project structure contains many directories and files.  The template directory (containing html files) and static directory (containing js files) are common standards for HTML coding.  Static files can be pictures and videos, in this project they are mostly javascript backgrounds.
 WSGI templates: index.html, kangaroos.html, ... are aligned with routes in main.py.
 Other templates support WSGI templates.  The base.html template contains common Head, Style, Body, Script definitions.  WSGI templates often "include" or "extend" these templates.  This is a way to reuse code.
 The VANTA javascript statics (backgrounds) are shown and defaulted in base.html (birds), but are block replaced as needed in other templates (solar, net, ...)
 The Bootstrap Navbar code is in navbar.html. The base.html code includes navbar.html.  The WSGI html files extend base.html files.  This is a process of management and correlation to optimize code management.  For instance, if the menu changes discovery of navbar.html is easy, one change reflects on all WSGI html files. 
 Jinja2 variables usage is to isolate data and allow redefinitions of attributes in templates.  Observe "{% set variable = %}" syntax for definition and "{{ variable }}" for reference.
 The base.html uses combination of Bootstrap grid styling and custom CSS styling.  Grid styling in observe with the "<Col-3>" markers.  A Bootstrap Grid has a width of 12, thus four "Col-3" markers could fit on a Grid row.
 A key purpose of this project is to embed links to other content.  The "href=" definition embeds hyperlinks into the rendered HTML.  The base.html file shows usage of "href={{github}}", the "{{github}}" is a Jinja2 variable.  Jinja2 variables are pre-processed by Python, a variable swap with value, before being sent to the browser.

### IDE management (things that happened beyond plan)
 Recall on ".gitignore" solution to the pains of temporary files.  Start a ".gitignore" and avoid promoting temporary files to Git, for instance IDE xml files.
 A project needs to establish a "requirements.txt" to keep track of Python packages used by the project.  This help in other IDEs and Deployment.  IntelliJ has menu Tool -> Sync Python Requirements to start file. 
