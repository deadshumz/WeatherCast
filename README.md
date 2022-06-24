# WeatherCast
Weather app on django framework that shows weather forecast

Application capabilities:
* User registration and authorization
* Location Search
  * Current temperature
  * Icon for weather conditions
  * 12 hour weather forecast starting from the current local time
* Favorite places
  * Add or remove space from favorites
  * 6 hour weather forecast for selected place with weather conditions icons

| User status / Functions        | Authorized           | Non-authorized  |
| ------------- |:-------------:|:----:|
| Location Search      | ✓ | ✓ |
| Favorite places      | ✓ | ✕ |

## Requirements

Modules needed to run the application

```
pip install -r requirements.txt
```

### Running

Standard run django Web Application

```
python manage.py runserver
```


## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Python](https://www.python.org/) - Language used
* [SASS](https://sass-lang.com/) - CSS Preprocessor

## Authors

* **Deadshumz** - *Initial work* - [github](https://github.com/deadshumz)

See also the list of [contributors](https://github.com/deadshumz/WeatherCast/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
