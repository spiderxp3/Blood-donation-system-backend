# Blood-donation-system-backend
Blood donation is one of the major issue in today's system that need effective management system and constant encourgaement to give an effective pipeline in modern world. So to solve this problem, here we introduce backend for management system for this problem using Django frameowork Lib.
* According to reports, In India every year overall 6M blood units are required but only 4M fulfilled. Currently, many blood donation apps and services are there in market. But with time, everyone lose their interest in fulfilling the requirement and it become source of income for them resulting in scram. To face this issue, we can only encourage donors by giving recognization.

-----
Workflow
-----
* Development of flutter Blood donation app.
* We'll using django to integrate app for the backend.
* Databases: SQl/MongoDB
* Database handling and quick responsing.
-----
## Future Goals
* To develop a quick response donation management system.
* Add portfolio generation to encourage youngsters to donate blood by giving them proper recognization.
* Develop Ios and Android applications with Sql for daatabases and launch app on playstore.
* Get certified from government to make this app official for the use.
----
## 🛠 &nbsp;<span style="color: #f2cf4a; font-family: Babas; font-size: 1.4em;">Tech Stack
</span>


![Django](https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white)&nbsp;
![Python](https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white)&nbsp;
![Flutter](https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=Flutter&logoColor=white)
![Dart](https://img.shields.io/badge/dart-%230175C2.svg?style=for-the-badge&logo=dart&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
----
## 💼 &nbsp; <span style="color: #f2cf4a; font-family: Babas; font-size: 1.2em;">Testing
</span>



>To clone the repository:

```sh
$ git clone https://github.com/spiderxp3/blood-donation-system-backend.git
```


- Create a virtual environment to install dependencies in and activate it:
  ```sh
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```

- Install the django using
    ```sh
    $ pip3 install django
    ```

- Install all the dependencies using
    ```sh
    $ pip3 install -r requirements.txt
    ```
-  Run the migrations using the following commands         
    ```sh
    $ python3 manage.py makemigrations
    ```
    ```sh
    $ python3 manage.py migrate
    ```
- Run the Django server by
    ```sh
    $ python3 manage.py runserver
    ```

*Note :*  In case you encounter errors during migrations, make sure that you have access rights to *db.sqlite3* file. You can use the following command to rectify permission denied error
```sh
$ chown *username* db.sqlite3
```

<span style="font-family: times, serif; font-size:14pt; font-style:italic">Run the migrations again to continue. </span>

----
<!-- CONTRIBUTING -->

## 🤝🏻 &nbsp;<span style="color: #f2cf4a; font-family: Babas; font-size: 1.2em;">Contributing
</span>

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch `git checkout -b feature/AmazingFeature`
3. Commit your Changes `git commit -m 'Add some AmazingFeature`
4. Push to the Branch `git push origin feature/AmazingFeature`
5. Open a Pull Request
----
<!-- LICENSE -->
## [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  

Distributed under the MIT License. See `LICENSE` for more information.

