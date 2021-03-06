# API Documents (v1.0)

*Tips*: user '/restful-api/v2.0' for v2.0 restful api

## `GET` /api/v1.0/token

### Implementation Notes

get token

### Response Class (Status 200)

OK

Model | Model schema

    {
        "expiration": 3600,
        "token":eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ2OTg3MjY1NywiaWF0IjoxNDY5ODY5MDU3fQ.eyJpZCI6MX0.qDMfoALz│42SVVCulUyedjf2pR1KEgM8i7DZ-QrZqefl3M",
        "user_id": 1,
    }

Response Content Type: application/json

### Parameters

Parameter      | Desciption        | Parameter Type | Data Type
:--------------|:------------------|:---------------|:--------------
param.email    | The email of user | header         | string
param.password | The password      | header         | string

## `GET` /api/v1.0/users/{int:user_id}

### Implementation Notes

Get information about user

### Response Class (Status 200)

OK

Model | Model schema

    {
        "todo_lists": "http://127.0.0.1:5000/api/v1.0/todo_lists/",
        "url": "http://127.0.0.1:5000/api/v1.0/users/1",
        'username": "user1",
    }

Response Content Type: application/json

### Parameters

Parameter            | Desciption                            | Parameter Type | Data Type
:--------------------|:--------------------------------------|:---------------|:--------------
param.email_or_token | The email or token of user            | header         | string
param.password       | The password or None if token is used | header         | string

## `GET` /api/v1.0/todo_lists/

### Implementation Notes

Get a list of todo_lists of current user

### Response Class (Status 200)

OK

Model | Model schema

    {
        "count": 2,
        "next": null,
        "prev": null,
        "todo_lists": [
            {
                "events": "http://127.0.0.1:5000/api/v1.0/todo_lists/1/events/",
                "master": "http://127.0.0.1:5000/api/v1.0/users/1",
                "tasks": "http://127.0.0.1:5000/api/v1.0/todo_lists/1/tasks/",
                "timestamp": "Fri, 29 Jul 2016 08:03:23 GMT",
                "title": "First list by api",
                "url": "http://127.0.0.1:5000/api/v1.0/todo_lists/1"
            },
            {
                "events": "http://127.0.0.1:5000/api/v1.0/todo_lists/3/events/",
                "master": "http://127.0.0.1:5000/api/v1.0/users/1",
                "tasks": "http://127.0.0.1:5000/api/v1.0/todo_lists/3/tasks/",
                "timestamp": "Fri, 29 Jul 2016 08:03:23 GMT",
                "title": "First list by api",
                "url": "http://127.0.0.1:5000/api/v1.0/todo_lists/3"
            },
        ]
    }

Response Content Type: application/json

### Parameters

Parameter            | Desciption                            | Parameter Type | Data Type
:--------------------|:--------------------------------------|:---------------|:--------------
param.email_or_token | The email or token of user            | header         | string
param.password       | The password or None if token is used | header         | string

## `POST` /api/v1.0/todo_lists/

### Implementation Notes

Create a new todo list

### Response Class (Status 201)

OK

Model | Model schema

    {
        "events": "http://127.0.0.1:5000/api/v1.0/todo_lists/4/events/",
        "master": "http://127.0.0.1:5000/api/v1.0/users/1",
        "tasks": "http://127.0.0.1:5000/api/v1.0/todo_lists/4/tasks/",
        "timestamp": "Sun, 31 Jul 2016 06:17:54 GMT",
        "title": "new list",
        "url": "http://127.0.0.1:5000/api/v1.0/todo_lists/4"
    }

Response Content Type: application/json

### Parameters

Parameter            | Value      | Desciption                            | Parameter Type | Data Type
:--------------------|:-----------|:--------------------------------------|:---------------|:--------------
param.email_or_token |            | The email or token of user            | header         | string
param.password       |            | The password or None if token is used | header         | string
param.title          | 'new list' | The title of new list                 | query          | string

## `GET` /api/v1.0/todo_lists/{int:list_id}

### Implementation Notes

Get infomations about the todo list

### Response Class (Status 200)

OK

Model | Model schema

    {
        "events": "http://127.0.0.1:5000/api/v1.0/todo_lists/5/events/",
        "master": "http://127.0.0.1:5000/api/v1.0/users/1",
        "tasks": "http://127.0.0.1:5000/api/v1.0/todo_lists/5/tasks/",
        "timestamp": "Sun, 31 Jul 2016 06:29:19 GMT",
        "title": "new task",
        "url": "http://127.0.0.1:5000/api/v1.0/todo_lists/5"
    }


Response Content Type: application/json

### Parameters

Parameter            | Value      | Desciption                            | Parameter Type | Data Type
:--------------------|:-----------|:--------------------------------------|:---------------|:--------------
param.email_or_token |            | The email or token of user            | header         | string
param.password       |            | The password or None if token is used | header         | string

## `DELETE` /api/v1.0/todo_lists/{int:list_id}

### Implementation Notes

Delete a todo list

### Response Class (Status 303)

OK

Model | Model schema

null

Response Content Type: application/json

Response Location: Location": "http://127.0.0.1:5000/api/v1.0/todo_lists/
### Parameters

Parameter            | Value      | Desciption                            | Parameter Type | Data Type
:--------------------|:-----------|:--------------------------------------|:---------------|:--------------
param.email_or_token |            | The email or token of user            | header         | string
param.password       |            | The password or None if token is used | header         | string


## `POST` /api/v1.0/todo_lists/5/tasks/

### Implementation Notes

Add new task into the todo list

### Response Class (Status 201)

OK

Model | Model schema

    {
        "body": "first task",
        "state": "todo",
        "timestamp": "Sun, 31 Jul 2016 10:52:41 GMT",
        "todo_list": "http://127.0.0.1:5000/api/v1.0/todo_lists/5",
        "url": "http://127.0.0.1:5000/api/v1.0/tasks/2"
    }


Response Content Type: application/json

Response Location: http://127.0.0.1:5000/api/v1.0/todo_lists/5/tasks/

### Parameters

Parameter            | Value      | Desciption                            | Parameter Type | Data Type
:--------------------|:-----------|:--------------------------------------|:---------------|:--------------
param.email_or_token |            | The email or token of user            | header         | string
param.password       |            | The password or None if token is used | header         | string
param.body           | 'new task' | The body of new task                  | query          | string

## `GET` /api/v1.0/todo_lists/5/tasks/

### Implementation Notes

Show all tasks in the list

### Response Class (Status 200)

OK

Model | Model schema

    {
        "doing_tasks": [],
        "done_tasks": [],
        "todo_tasks": [
            {
                "body": "first task",
                "state": "todo",
                "timestamp": "Sun, 31 Jul 2016 10:52:41 GMT",
                "todo_list": "http://127.0.0.1:5000/api/v1.0/todo_lists/5",
                "url": "http://127.0.0.1:5000/api/v1.0/tasks/2"
            },
            {
                "body": "second task",
                "state": "todo",
                "timestamp": "Sun, 31 Jul 2016 11:04:56 GMT",
                "todo_list": "http://127.0.0.1:5000/api/v1.0/todo_lists/5",
                "url": "http://127.0.0.1:5000/api/v1.0/tasks/3"
            }
        ]
    }

Response Content Type: application/json

### Parameters

Parameter            | Desciption                            | Parameter Type | Data Type
:--------------------|:--------------------------------------|:---------------|:--------------
param.email_or_token | The email or token of user            | header         | string
param.password       | The password or None if token is used | header         | string

## `GET` /api/v1.0/tasks/{int:task_id}

### Implementation Notes

Get details of the task

### Response Class (Status 200)

OK

Model | Model schema

    {
        "body": "first task",
        "state": "todo",
        "timestamp": "Sun, 31 Jul 2016 10:52:41 GMT",
        "todo_list": "http://127.0.0.1:5000/api/v1.0/todo_lists/5",
        "url": "http://127.0.0.1:5000/api/v1.0/tasks/2"
    }

Response Content Type: application/json

### Parameters

Parameter            | Desciption                            | Parameter Type | Data Type
:--------------------|:--------------------------------------|:---------------|:--------------
param.email_or_token | The email or token of user            | header         | string
param.password       | The password or None if token is used | header         | string

## `PUT` /api/v1.0/tasks/{int:task_id}

### Implementation Notes

Change state of the task

### Response Class (Status 202)

OK

Model | Model schema

    {
        "body": "first new test task after fix bug",
        "state": "doing",
        "timestamp": "Sun, 31 Jul 2016 12:48:31 GMT",
        "todo_list": "http://127.0.0.1:5000/api/v1.0/todo_lists/7",
        "url": "http://127.0.0.1:5000/api/v1.0/tasks/5"
    }

Response Content Type: application/json

### Parameters

Parameter            | Value  | Desciption                            | Parameter Type | Data Type
:--------------------|:-------|:--------------------------------------|:---------------|:--------------
param.email_or_token |        | The email or token of user            | header         | string
param.password       |        | The password or None if token is used | header         | string
param.state          | 'done' | The new state of the task             | query          | string

## `DELETE` /api/v1.0/tasks/{int:task_id}

### Implementation Notes

delete the task

### Response Class (Status 303)

OK

Model | Model schema

null

Response Content Type: application/json

### Parameters

Parameter            | Desciption                            | Parameter Type | Data Type
:--------------------|:--------------------------------------|:---------------|:--------------
param.email_or_token | The email or token of user            | header         | string
param.password       | The password or None if token is used | header         | string

## `GET` /api/v1.0/todo_lists/5/events/

### Implementation Notes

Show all events in the list

### Response Class (Status 200)

OK

Model | Model schema

    {
        "count": 7,
        "next": null,
        "prev": null,
        "todo_lists": [
            {
                "event": "List \"new test list after fix bug\" was created.",
                "timestamp": "Sun, 31 Jul 2016 12:42:17 GMT",
                "todo_list": "http://127.0.0.1:5000/api/v1.0/todo_lists/7",
                "url": "http://127.0.0.1:5000/api/v1.0/events/20"
            },
            {
                "event": "Task \"first new test task after fix bug\" was created.",
                "timestamp": "Sun, 31 Jul 2016 12:45:26 GMT",
                "todo_list": "http://127.0.0.1:5000/api/v1.0/todo_lists/7",
                "url": "http://127.0.0.1:5000/api/v1.0/events/21"
            },
            {
                "event": "Task \"first new test task after fix bug\" was changed from \"todo\" to \"doing\".",
                "timestamp": "Sun, 31 Jul 2016 12:48:31 GMT",
                "todo_list": "http://127.0.0.1:5000/api/v1.0/todo_lists/7",
                "url": "http://127.0.0.1:5000/api/v1.0/events/22"
            },
        ]
    }

Response Content Type: application/json

### Parameters

Parameter            | Desciption                            | Parameter Type | Data Type
:--------------------|:--------------------------------------|:---------------|:--------------
param.email_or_token | The email or token of user            | header         | string
param.password       | The password or None if token is used | header         | string

## `GET` /api/v1.0/events/26

### Implementation Notes

Show details of the event

### Response Class (Status 200)

OK

Model | Model schema

    {
        "event": "Task \"first new test task after fix bug\" was deleted.",
        "timestamp": "Sun, 31 Jul 2016 13:04:47 GMT",
        "todo_list": "http://127.0.0.1:5000/api/v1.0/todo_lists/7",
        "url": "http://127.0.0.1:5000/api/v1.0/events/26"
    }

Response Content Type: application/json

### Parameters

Parameter            | Desciption                            | Parameter Type | Data Type
:--------------------|:--------------------------------------|:---------------|:--------------
param.email_or_token | The email or token of user            | header         | string
param.password       | The password or None if token is used | header         | string
