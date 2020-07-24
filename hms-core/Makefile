# Makefile for the HMS Core (hms-core) project
TMPDIR=/tmp/build/hms_core_build

local: setup
	# Doesn't (yet) do anything other than running the test and 
	# setup targets

setup:
	# Calls the main setup.py to build a source-distribution
	~/py_envs/hms/core/bin/python setup.py sdist

unit_test:
	# Executes the unit-tests for the package, allowing the build-
	# process to die and stop the build if a test fails
	~/py_envs/hms/core/bin/python setup.py test

build_dir:
	# Creates a temporary build-directory, copies the project-files 
	# to it.
	# Creating "$(TMPDIR)"
	mkdir -p $(TMPDIR)
	# Copying project-files to $(TMPDIR)
	cp -R bin $(TMPDIR)
	cp -R etc $(TMPDIR)
	cp -R src $(TMPDIR)
	cp -R var $(TMPDIR)
	cp setup.py $(TMPDIR)

dev_prep:
	# Renames any dev-specific files so that they will be the "real" 
	# files included in the build.
	# At this point, there are none, so we'll just exit

dev: unit_test build_dir dev_prep
	# A make-target that generates a build intended to be deployed 
	# to a shared development environment.
	cd $(TMPDIR);~/py_envs/hms/core/bin/python setup.py sdist

