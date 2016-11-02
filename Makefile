.PHONY: test
test:
	py.test *.py
	ava *.js

.PHONY: watch
watch:
	reflex -d none -g '*.py' -- py.test {} &
	ava -w *.js
