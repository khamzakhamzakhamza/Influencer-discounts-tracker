run tests: $env:PYTHONPATH = (Get-Location).Path; pytest tests/
freeze requirements: pip freeze > requirements.txt
