#! /bin/bash

if yamllint apps.yaml | grep "error" | grep -v "line too long"; then
	# found some lint errors
	exit 1
fi

if ! python validate.py; then
	exit 1
fi

exit 0
