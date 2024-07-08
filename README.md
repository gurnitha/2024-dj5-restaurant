# 2024-dj5-restaurant
Membuat aplikasi restauran menggunakan Django versi 5


## 1. SETUP


#### 1. Membuat venv

        λ python --version
        Python 3.12.1
        λ pip --version
        pip 24.1.1 
        λ python -m venv venv312506 --promp dj5-resta
        λ ls
        README.md  venv312506/


#### 2. Menginstal django versi 5.0.6

        λ venv312506\Scripts\activate.bat

        (dj5-resta) λ pip install django==5.0.6
        Collecting django==5.0.6
        ...
        Successfully installed asgiref-3.8.1 django-5.0.6 sqlparse-0.5.0 tzdata-2024.1

        [notice] A new release of pip is available: 23.2.1 -> 24.1.2
        [notice] To update, run: python.exe -m pip install --upgrade pip

        (dj5-resta) λ django-admin --version
        5.0.6

        (dj5-resta) λ pip list
        Package  Version
        -------- -------
        asgiref  3.8.1
        Django   5.0.6
        pip      23.2.1
        sqlparse 0.5.0
        tzdata   2024.1


#### 3. Meng-upgrade pip

        (dj5-resta) λ python.exe -m pip install --upgrade pip
        ...
        Successfully installed pip-24.1.2



## 2. PROYEK DAN APLIKASI


#### 1. Membuat proyek dengan nama 'config'

        (dj5-resta) λ django-admin startproject config .

        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 2. Membuat aplikasi restauran

        (dj5-resta) λ mkdir app\restauran
        (dj5-resta) λ django-admin startapp restauran app\restauran

        modified:   README.md
        new file:   app/restauran/__init__.py
        new file:   app/restauran/admin.py
        new file:   app/restauran/apps.py
        new file:   app/restauran/migrations/__init__.py
        new file:   app/restauran/models.py
        new file:   app/restauran/tests.py
        new file:   app/restauran/views.py


#### 3. Membuat aplikasi blog

        (dj5-resta) λ mkdir app\blog
        (dj5-resta) λ django-admin startapp blog app\blog

        modified:   README.md
        new file:   app/blog/__init__.py
        new file:   app/blog/admin.py
        new file:   app/blog/apps.py
        new file:   app/blog/migrations/__init__.py
        new file:   app/blog/models.py
        new file:   app/blog/tests.py
        new file:   app/blog/views.py


#### 4. Membuat aplikasi user

        (dj5-resta) λ mkdir app\user
        (dj5-resta) λ django-admin startapp user app\user

        modified:   README.md
        new file:   app/user/__init__.py
        new file:   app/user/admin.py
        new file:   app/user/apps.py
        new file:   app/user/migrations/__init__.py
        new file:   app/user/models.py
        new file:   app/user/tests.py
        new file:   app/user/views.py



## 3. PAGES: URLS, VIEWS, TEMPLATES


#### 1. Membuat laman home

        modified:   README.md
        new file:   app/restauran/urls.py
        modified:   app/restauran/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/restauran/index.html


#### 2. Mengisi HTML template untuk laman home

        modified:   README.md
        modified:   templates/restauran/index.html


#### 3. Membuat laman about

        modified:   README.md
        modified:   app/restauran/urls.py
        modified:   app/restauran/views.py
        new file:   templates/restauran/about.html


#### 4. Mengisi HTML template untuk laman about

        modified:   README.md
        modified:   templates/restauran/about.html


#### 5. Mengisi HTML template untuk laman menu

        modified:   app/restauran/urls.py
        modified:   app/restauran/views.py
        new file:   templates/restauran/menu.html


#### 6. Mengisi HTML template untuk laman menu

        modified:   README.md
        modified:   templates/restauran/menu.html