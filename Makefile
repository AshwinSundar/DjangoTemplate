run: 
	make db-migrate
	python3 manage.py runserver 

db-make-migrations:
	python3 manage.py makemigrations

db-migrate:
	python3 manage.py migrate

format:
	ruff format .

run-detached:
	tmux kill-session -t dev 2>/dev/null; tmux new-session -d -s dev 'make run'

run-de:
	make run-detached

run-reattach:
	tmux attach -t dev

run-re:
	make run-reattach
