# Import xlsx to django model

Simple import an Excel data to implementation in django model.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.
I asume that we have already install django and make project from it

```bash
pip install django_import_export
```

## Usage

In admin.py from app directory, add this :
```python
# import your model first
from import_export.admin import ImportExportModelAdmin

@admin.register(YourModel)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id',) #to blacklist id collumn because it auto generate
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. I like to sharing and learning to and from other.