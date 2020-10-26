

Zavrsni rad preddiplomskog studija Informatike 2019/2020

Za prikazivanj evizualizacije podataka u praksi odabran je projekt koji uključuje izradu mrežne aplikacije s vizualizacijom podataka o Korona virusu. Tri glavne tehnologije korištene za implementaciju ove ideje su Django, Dash i Plotly. Django i Dash su Python okviri za izradu mrežnih aplikacija, a Plotly je Python biblioteka za vizualizaciju podataka koja omogućava izradu interaktivnih vizualizacija u mrežnom okruženju.

Skupove podataka odabrane za realizaciju ovog projekta može se pronaći na poveznicama:

• https://www.trackcorona.live/api/countries

• https://www.trackcorona.live/api/travel

• https://api.covid19api.com/summary

• https://opendata.ecdc.europa.eu/covid19/casedistribution/csv

• https://docs.google.com/spreadsheets/d/e/2PACX-1vTxATUFm0tR6Vqq-UAOuqQ-BoQDvYYEe-BmJ20s50yBKDHEifGofP2P1LJ4jWFIu0Pb_4kRhQeyhHmn/pub?gid=0&single=true&output=csv.

U samom početku potrebno je osigurati okruženje koje će omogućiti korištenje do sada navedenih biblioteka i paketa za rad s podacima. U ovom projektu korištena je Conda, sustav za upravljanje paketima i sustav upravljanja okruženjima koji radi na Windowsima, MacOS-u i Linuxu. Conda brzo instalira, pokreće i ažurira pakete. Prvo je u Anaconda Prompt naredbenoj ljusci (eng. Command Shell) naredbom conda create env dash_plotly stvoreno novo okruženje u koje su instalirani potrebni paketi korišteni u aplikaciji i to naredbama: pip install django, pip install django_plotly_dash, pip install plotly. Potom je stvoren novi Django projekt naredbom django-admin startproject django_dash_plotly unutar kojeg su stvorene nove aplikacije naredbama: python manage.py startapp corona i python manage.py startapp users. Ovim je postupkom stvoren Django projekt naziva django_dash_plotly koji sadrži aplikacije corona i users, a njegovim pokretanjem u novostvorenom okruženju dash_plotly, moguće je unutar projekta koristiti instalirane pakete django, django-plotly-dash i plotly (koji sadrži i dash).

Aplikacija se pokreće u Anaconda Prompt-u naredbom python manage.py runserver, uz uvjet da je naredbom conda activate dash_plotly pokrenuto dash_plotly okruženje te je trenutna pozicija naredbenog retka u direktoriju django_dash_plotly aplikacije. Ovime se pokreće Django razvojni poslužitelj (eng. development server) koji omogućuje lokalno pokretanje aplikacije tako da se u web preglednik upiše http://127.0.0.1:8000.
