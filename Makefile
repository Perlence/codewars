.PHONY: watch
watch:
	reflex -d none -g '*.py' -- py.test {} &
	reflex -d none -g '*.js' -- sh -c 'tape {} | tap-dot'