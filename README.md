![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=24&height=200&section=header&text=QA%20GURU&fontAlignY=35&fontSize=60&desc=PROJECT%20REST%20API%20AUTO&descAlignY=60&descSize=50&animation=twinkling&fontColor=E9E9E9F3&descAlign=60&fontAlign=25
)

# <p  align="center"> Этот проект является дипломной работой по курсу QA.GURU в части построения фреймворка по автоматизации тестирования REST API на примере https://api.sampleapis.com (fake bank)

# <p  align="center"> В реализации использованы инструменты и библиотеки:

<p  align="center">
  <code><img width="6%" title="Python" src=".github/github_readme/images/logo/python.png" alt="python"></code>
  <code><img width="6%" title="Pycharm" src=".github/github_readme/images/logo/pycharm.png" alt="pycharm"></code>
  <code><img width="6%" title="Pytest" src=".github/github_readme/images/logo/pytest.png" alt="pytest"></code>
  <code><img width="6%" title="Requests" src=".github/github_readme/images/logo/requests.png" alt="requests"></code>
  <code><img width="6%" title="Pydantic" src=".github/github_readme/images/logo/pydantic.png" alt="pydantic"></code>
  <code><img width="6%" title="GitHub" src=".github/github_readme/images/logo/github.png" alt="github"></code>
  <code><img width="6%" title="Jenkins" src=".github/github_readme/images/logo/jenkins.png" alt="jenkins"></code>
  <code><img width="6%" title="Allure Report" src=".github/github_readme/images/logo/allure_report.png" alt="allure"></code>
  <code><img width="6%" title="Allure TestOps" src=".github/github_readme/images/logo/allure_testops.png" alt="allure_testops"></code>
  <code><img width="6%" title="Telegram" src=".github/github_readme/images/logo/tg.png" alt="telegram"></code>
  <code><img width="6%" title="Jira" src=".github/github_readme/images/logo/jira-original.svg" alt="jira"></code>
</p>

## <img width="3%" title="pycharm" src=".github/github_readme/images/logo/pycharm.png"> Для локального запуска тестов:

1) Клонировать репозиторий: git clone git@github.com:falinpavel/qa_guru_graduation_project_rest_api.git
2) Установить зависимости (в проекте используется poetry): poetry init -> poetry install -> poetry env activate
3) Запуск всех тестов с генерацией отчетов Allure использовать команду: pytest (все параметры запуска зашиты в pyproject.toml)
4) Просмотр отчета Allure (если установлен Allure CLI): allure serve reports/allure-results

## <img width="3%" title="jenkins" src=".github/github_readme/images/logo/jenkins.png"> Для запуска тестов в Jenkins:

1) Авторизоваться в Jenkins
2) Перейти в одноименную с репозиторием джобу
3) Для запуска тестов в Jenkins нажать "Build with parameters"
4) Нажать "Build"

<p><img title="jenkins_build" src=".github/github_readme/images/screenshot/jenkins_build_1.png"></p>
<p><img title="jenkins_build" src=".github/github_readme/images/screenshot/jenkins_build_2.png"></p>

## <img width="3%" title="allure" src=".github/github_readme/images/logo/allure_report.png"> Визуализация результатов (Allure Reports и Allure TestOps)

## Если тесты запускались локально, то сгенерированный Allure отчет можно посмотрь выполнив команду в терминале: 

```bash
allure serve reports/allure-results
```
## Если тесты запускались в Jenkins, то результаты можно посмотреть кликнув по иконке Allure Report в Jenkins в завершенной сборке:

<p><img title="allure" src=".github/github_readme/images/screenshot/allure_report_in_jenkins_1.png"></p>
<p><img title="allure" src=".github/github_readme/images/screenshot/allure_report_in_jenkins_2.png"></p>
<p><img title="allure" src=".github/github_readme/images/screenshot/allure_report_in_jenkins_3.png"></p>

## <img width="3%" title="allure" src=".github/github_readme/images/logo/github.png"> Allure отчет так же можно посмотреть на GitHub в разделе Deployments (https://github.com/falinpavel/qa_guru_graduation_project_rest_api/deployments) данного репозитория (Тестовый прогон выполняется после каждого push в ветку main и публикуется на github-pages, см. подробнее в test.yaml)

<p><img title="github_pages" src=".github/github_readme/images/screenshot/github_pages_1.png"></p>

## <img width="3%" title="allure" src=".github/github_readme/images/logo/allure_testops.png"> Для просмотра результатов тестового прогона в Allure TestOps кликнув на соответствующую ему иконку в джобе Jenkins:

<p><img title="allure_testops" src=".github/github_readme/images/screenshot/allure_testops_in_jenkins_1.png"></p>
<p><img title="allure_testops" src=".github/github_readme/images/screenshot/allure_testops_in_jenkins_2.png"></p>
<p><img title="allure_testops" src=".github/github_readme/images/screenshot/allure_testops_in_jenkins_3.png"></p>

## <img width="3%" title="tg" src=".github/github_readme/images/logo/tg.png"> Интеграция с Telegram в Jenkins для автоматической отправки результатов тестового прогона через бота

<p><img title="telegram" src=".github/github_readme/images/screenshot/telegram_1.png"></p>