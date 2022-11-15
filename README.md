# desafio-tech

-Desenvolvimento do Front-End:

![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

-Desenvolvimento do Back-End:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)

-Desenvolvimento em:

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

## <a id="instalacao"> 🔴 PASSO A PASSO DE COMO EXECUTAR A APLICAÇÃO </a>

<b>-Clone o repositório com o comando:</b> `https://github.com/laishelen/desafio-tech` <br>
<b>-Criando virtual environment:</b> `python -m venv venv`<br>
<b>-Ativando o virtual environment: </b>`. venv\Scripts\Activate`<br>
<b>-Execução do código </b>`pip install django`<br>

*Alterar as configurações do DataBase no arquivo <b>`settings.py`</b> <br>

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "desafiopython",
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '',
        'PORT': '3306',
        'OPTIONS': {
        'sql_mode': 'traditional',
        }
}

-Migre o banco de dados com: `python manage.py migrate` <br>
-Execute o servidor: `python manage.py runserver` <br>
