## Frontend 

The project frontend and all its instructions can be found at here [Atlas Frontend](https://github.com/gpmc-lab-ufrgs/atlas)

## How to run atlas-backend

This project was developed using Python and Django. To set the environment and run in your machine, please follow the instructions bellow:

<!-- PARA DOCKER(AINDA NÃO ESTÁ PRONTO) -->
<!-- ### Setting the environment and Running the project
```
docker-compose up
```  -->

<!-- versão temporaria sem docker -->
### Setting the environment

#### 1 - Execute docker-compose and start docker container with postgis image

```
docker-compose up -d
sudo docker start <Container_ID>
```

#### 1 - Installing all the requirements

```
pip install -r requirements.txt
```

#### 2 - Set migrations

```
python manage.py makemigrations
```
#### 3 - Apply all the migrations

```
python manage.py migrate
```
#### 4 - Populate database with states data

```
python manage.py load_state 
```
#### 5 - Populate database with districts data

```
python manage.py load_dist
```
### Running the project

#### 1 - Activate Virtual Python Environment

```
source env/bin/activate 
```
#### 2 - Config this python env

```
python3 -m venv env                                
```

#### 3 - Running the project

```
python manage.py runserver
```

#### 4 - Accessing the platform

```
open http://localhost:8000/admin/
```

## How to Contribute to this project?
See our [Contribution Guide](CONTRIBUTION.md)  

## Contributors 

<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://www.github.com/andredemori/"><img src="https://github.com/andredemori.png" width="100px;" alt=""/><br /><sub><b>André M. Demori</b></sub></a><br /><a href="https://github.com/gpmc-lab-ufrgs/atlas/commits?author=andredemori" title="Code"></a> <a href="#ideas-andredemori" title="Ideas, Planning, & Feedback"></a> <a href="https://github.com/gpmc-lab-ufrgs/atlas/commits?author=andredemori" title="Documentation"></a> <a href="https://github.com/gpmc-lab-ufrgs/atlas/pulls/assigned/andredemori" title="Reviewed Pull Requests"></a></td>
      <td align="center"><a href="https://www.linkedin.com/in/leosilvagomes/"><img src="https://avatars.githubusercontent.com/u/61520601?v=4" width="100px;" alt=""/><br /><sub><b>Leanordo Gomes</b></sub></a><br /><a href="https://github.com/gpmc-lab-ufrgs/atlas-backend/commits?author=LeoSilvaGomes" title="Code"></a> <a href="#ideas-LeoSilvaGomes" title="Ideas, Planning, & Feedback"></a> <a href="https://github.com/gpmc-lab-ufrgs/atlas-backend/commits?author=LeoSilvaGomes" title="Documentation"></a> <a href="https://github.com/gpmc-lab-ufrgs/atlas-backend/pulls?q=is%3Apr+assignee%3ALeoSilvaGomes+is%3Aclosed" title="Reviewed Pull Requests"></a></td>
      <td align="center"><a href="https://www.linkedin.com/in/ana-beatriz-pontes/"><img src="https://avatars.githubusercontent.com/u/47431053?v=4" width="100px;" alt=""/><br /><sub><b>Ana Beatriz Pontes</b></sub></a><br /><a href="https://github.com/gpmc-lab-ufrgs/atlas-backend/commits?author=AnaBeatrizPontes" title="Code"></a> <a href="#ideas-AnaBeatrizPontes" title="Ideas, Planning, & Feedback"></a> <a href="https://github.com/gpmc-lab-ufrgs/atlas-backend/commits?author=AnaBeatrizPontes" title="Documentation"></a> <a href="https://github.com/gpmc-lab-ufrgs/atlas-backend/pulls?q=is%3Apr+is%3Aclosed+assignee%3AAnaBeatrizPontes" title="Reviewed Pull Requests"></a></td>
    </tr>
  </tbody>
</table>

