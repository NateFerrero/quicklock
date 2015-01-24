.PHONY: env __env req test

env:
	@if [ "`pwd`/env/bin/python" = "`which python`" ]; then echo '>>> Already in virtualenv'; else make __env; fi

__env:
	@which pip &> /dev/null || sudo easy_install pip
	@which virtualenv &> /dev/null || sudo pip install virtualenv
	@ls ./env &> /dev/null || mkdir ./env
	@ls ./env/bin &> /dev/null || virtualenv ./env
	@echo 'export DIR="`pwd`"; \
	ls ~/.zshrc &> /dev/null && source ~/.zshrc; \
	cd $${DIR}; \
	echo ">>> Now entering Python virtualenv"; \
	source ./env/bin/activate; \
	echo -en ">>> python is now "; \
	which python' > ./env/bin/.zshrc
	@if which zsh &> /dev/null; then ZDOTDIR=./env/bin zsh; \
		echo ">>> Now exiting Python virtualenv"; \
	else bash --rcfile ./env/bin/.zshrc; fi

req:
	@if [ "`pwd`/env/bin/python" != "`which python`" ]; then echo 'Not in virtualenv'; \
	else pip install -r requirements.txt; fi


test:
	@if [ "`pwd`/env/bin/python" != "`which python`" ]; then echo 'Not in virtualenv'; \
	else nosetests --nocapture --exe; fi
