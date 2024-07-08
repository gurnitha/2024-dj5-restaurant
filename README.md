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