
## Задание выполнено в рамках курсовой работы 7 - DRF

### 1. Для запуска необходим файл `.env` со следующими переменными:
```
SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_NAME=habits
DB_HOST=127.0.0.1
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=postgres

TG_BOT_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

REDIS_HOST=redis://127.0.0.1:6379
```

### Результат проверки flake8:

```
(venv) fedor@fedor-Z68P-DS3:~/CODE/SkyPro/course_work07$ flake8 .
(venv) fedor@fedor-Z68P-DS3:~/CODE/SkyPro/course_work07$
```

### Результат запуска тестов:

```
(venv) fedor@fedor-Z68P-DS3:~/CODE/SkyPro/course_work07$ coverage run --source='.' manage.py test && coverage report
Found 4 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....
----------------------------------------------------------------------
Ran 4 tests in 2.050s

OK
Destroying test database for alias 'default'...
Name                                                                       Stmts   Miss  Cover
----------------------------------------------------------------------------------------------
config/__init__.py                                                             2      0   100%
config/asgi.py                                                                 4      4     0%
config/celery.py                                                               6      0   100%
config/settings.py                                                            35      0   100%
config/urls.py                                                                 7      0   100%
config/wsgi.py                                                                 4      4     0%
habits/__init__.py                                                             0      0   100%
habits/admin.py                                                                0      0   100%
habits/apps.py                                                                 4      0   100%
habits/migrations/0001_initial.py                                              7      0   100%
habits/migrations/0002_alter_habit_period_alter_habit_place_and_more.py        4      0   100%
habits/migrations/__init__.py                                                  0      0   100%
habits/models.py                                                              18      1    94%
habits/paginators.py                                                           5      0   100%
habits/permissions.py                                                          4      0   100%
habits/serializers.py                                                          8      0   100%
habits/tasks.py                                                               15      9    40%
habits/telegram.py                                                            26     19    27%
habits/tests.py                                                               37      0   100%
habits/urls.py                                                                 5      0   100%
habits/validators.py                                                          32      5    84%
habits/views.py                                                               35      1    97%
manage.py                                                                     12      2    83%
users/__init__.py                                                              0      0   100%
users/admin.py                                                                 5      0   100%
users/apps.py                                                                  4      0   100%
users/migrations/0001_initial.py                                               7      0   100%
users/migrations/0002_user_chat_id_user_update_id_alter_user_telegram.py       4      0   100%
users/migrations/0003_alter_user_chat_id_alter_user_update_id.py               4      0   100%
users/migrations/__init__.py                                                   0      0   100%
users/models.py                                                                9      0   100%
users/permissions.py                                                          16     12    25%
users/serializers.py                                                          12      0   100%
users/tests.py                                                                 0      0   100%
users/urls.py                                                                  9      0   100%
users/views.py                                                                24     10    58%
----------------------------------------------------------------------------------------------
TOTAL                                                                        364     67    82%
(venv) fedor@fedor-Z68P-DS3:~/CODE/SkyPro/course_work07$
```

```
