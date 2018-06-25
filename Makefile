# Optional Environment Parameters:
#	CMD: Django command to run
#		Applies to `run`.
#	PORT: the port to run the development server on.
#		Default: 8000
#		Applies to `start`.
#   PACKAGE: desired python package to install
# 	    Applies to 'install_package'
# 		EXAMPLE: PACKAGE=flake8 make install_package

PORT         ?= 8000
SOURCE_DIRS  := project drest graphene models


# pretty print
define header
	@tput setaf 6
	@echo "* $1"
	@tput sgr0
endef

install:
	$(call header,"Installing")
	$(call header,"Updating dependencies")
	pipenv install

# Install specific package.
install_package:
	pipenv install $(PACKAGE)

# Start the development server
start:
	$(call header,"Starting development server")
	pipenv run python manage.py runserver $(PORT)

# Start the Django shell
shell:
	$(call header,"Starting shell")
	pipenv run python manage.py shell

# Run any Django command
run:
	$(call header,"Running command: $(CMD)")
	pipenv run python manage.py $(CMD)

# Migrate the test database
migrate:
	$(call header,"Running migrate")
	pipenv run python manage.py migrate

# Create new migrations
migrations:
	$(call header,"Running migrations")
	pipenv run python manage.py makemigrations

# Removes build files in working directory
clean_working_directory:
	$(call header,"Cleaning working directory")
	@rm -rf ./build ./dist ./project.egg-info
	@find . -type f -name '*.pyc' -exec rm -rf {} \;

# Lint the whole project
lint: clean_working_directory
	$(call header,"Linting code")
	pipenv run find $(SOURCE_DIRS) -type f -name '*.py' -not -path '*/migrations/*' | xargs flake8
