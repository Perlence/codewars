.PHONY: test
test:
	py.test *.py
	ava *.js
	raco test *.rkt

.PHONY: watch
watch:
	reflex -d none -g '*.py' -- py.test {} &
	ava -w *.js &
	reflex -d none -g '*.rkt' -- raco test {}
