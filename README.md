
# Django Signals Example

This project demonstrates the usage of Django signals with three examples:
1. **Synchronous Signal Execution** - Demonstrates that Django signals are executed synchronously by default.
2. **Signal Execution in the Same Thread** - Shows that Django signals run in the same thread as the caller.
3. **Signals Running in the Same Database Transaction** - Proves that Django signals are executed within the same transaction as the caller.

## Setup

1. Ensure you have a Django project with an app created (e.g., `myapp`).
2. Copy the code from `django_signals_example.py` into your app directory.
3. Run database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Run the examples using the Django shell:

```bash
python manage.py shell < myapp/django_signals_example.py
```

## Examples

1. **Synchronous Signal Execution**: Executes after the object is saved.
2. **Signal Execution in the Same Thread**: Demonstrates that signals run on the same thread.
3. **Signals Running in the Same Database Transaction**: Confirms that signals are executed in the same transaction as the caller.
# AccuknoxTest
