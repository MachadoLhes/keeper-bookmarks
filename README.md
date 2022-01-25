# keeper-bookmark
Django app created for the Python engineer test for Keeper Solutions.

## Requirements

To run this project, you need the following:
```
- python 3.9
- django 4.0.1
```

### Database configuration
When running the project for the first time, please run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```
### Running server
```
python manage.py runserver
```

# API Details

## `/bookmarks/`
Endpoint for Bookmarks \
__*GET*__
```json
Response at "/"
{
	"count": 1,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"title": "World Leading Remote Software Development - Keeper Solutions",
			"private": false,
			"url": "https://keepersolutions.com/",
			"created_at": "2022-01-25T22:39:18.102069Z",
			"updated_at": "2022-01-25T22:40:26.879435Z"
		}
	]
}

Response at "/{id}"
{
	"id": 1,
	"title": "World Leading Remote Software Development - Keeper Solutions",
	"private": false,
	"url": "https://keepersolutions.com/",
	"created_at": "2022-01-25T22:39:18.102069Z",
	"updated_at": "2022-01-25T22:40:26.879435Z"
}
```

__*PUT*__
```json
Request
{
    title: String,
    url: String,
    private: Boolean
}
```
__*POST*__
```json
Request
{
    title: String,
    url: String,
    private: Boolean
}
```
__*DELETE*__
```json
Response
204
```
---
## `/tag/`
Endpoint for Bookmarks \
__*GET*__
```json
Response at "/"
{
	"count": 2,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"tag": "Work"
		},
		{
			"id": 2,
			"tag": "Fun"
		}
	]
}

Response at "/{id}"
{
	"id": 1,
	"tag": "Work"
}
```

__*PUT*__
```json
Request
{
    tag: String,
}
```
__*POST*__
```json
Request
{
    tag: String,
}
```
__*DELETE*__
```json
Response
204
```
---