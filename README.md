# psyturk

Mturk hit maker for embedding user website in xframe of mturk site.

### Setup

- sudo pip install virtualenv
- virtualenv venv
- . venv/bin/activate
- python setup.py install

### Configuring with MTurk

- [Follow these instructions](https://requester.mturk.com/developer)
- When you rearch Step 5, read below

### How to use

- Modify settings.py and add AWS key, secret, and your url
- For specifics modify "hit.py"
- Run "python hit.py"

### How to test

- Login as a worker in the sandbox [here](https://workersandbox.mturk.com/mturk/welcome)
- Login as a requester in the sandbox [here](https://requestersandbox.mturk.com/)
- As a worker, search for your registration name. You should see your task.
- As a requester, go to Manage > Manage HITs Individually. You should see your task.

