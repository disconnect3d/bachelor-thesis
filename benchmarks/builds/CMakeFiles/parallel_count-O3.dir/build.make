# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.2

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /media/dc/B2B200EFB200B9BD/inz/benchmarks/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /media/dc/B2B200EFB200B9BD/inz/benchmarks/builds

# Include any dependencies generated for this target.
include CMakeFiles/parallel_count-O3.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/parallel_count-O3.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/parallel_count-O3.dir/flags.make

CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.o: CMakeFiles/parallel_count-O3.dir/flags.make
CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.o: /media/dc/B2B200EFB200B9BD/inz/benchmarks/src/parallel_count/parallel_count.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /media/dc/B2B200EFB200B9BD/inz/benchmarks/builds/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.o -c /media/dc/B2B200EFB200B9BD/inz/benchmarks/src/parallel_count/parallel_count.cpp

CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /media/dc/B2B200EFB200B9BD/inz/benchmarks/src/parallel_count/parallel_count.cpp > CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.i

CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /media/dc/B2B200EFB200B9BD/inz/benchmarks/src/parallel_count/parallel_count.cpp -o CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.s

CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.o.requires:
.PHONY : CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.o.requires

CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.o.provides: CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.o.requires
	$(MAKE) -f CMakeFiles/parallel_count-O3.dir/build.make CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.o.provides.build
.PHONY : CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.o.provides

CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.o.provides.build: CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.o

# Object files for target parallel_count-O3
parallel_count__O3_OBJECTS = \
"CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.o"

# External object files for target parallel_count-O3
parallel_count__O3_EXTERNAL_OBJECTS =

builds/parallel_count-O3: CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.o
builds/parallel_count-O3: CMakeFiles/parallel_count-O3.dir/build.make
builds/parallel_count-O3: CMakeFiles/parallel_count-O3.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable builds/parallel_count-O3"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/parallel_count-O3.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/parallel_count-O3.dir/build: builds/parallel_count-O3
.PHONY : CMakeFiles/parallel_count-O3.dir/build

CMakeFiles/parallel_count-O3.dir/requires: CMakeFiles/parallel_count-O3.dir/parallel_count/parallel_count.o.requires
.PHONY : CMakeFiles/parallel_count-O3.dir/requires

CMakeFiles/parallel_count-O3.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/parallel_count-O3.dir/cmake_clean.cmake
.PHONY : CMakeFiles/parallel_count-O3.dir/clean

CMakeFiles/parallel_count-O3.dir/depend:
	cd /media/dc/B2B200EFB200B9BD/inz/benchmarks/builds && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /media/dc/B2B200EFB200B9BD/inz/benchmarks/src /media/dc/B2B200EFB200B9BD/inz/benchmarks/src /media/dc/B2B200EFB200B9BD/inz/benchmarks/builds /media/dc/B2B200EFB200B9BD/inz/benchmarks/builds /media/dc/B2B200EFB200B9BD/inz/benchmarks/builds/CMakeFiles/parallel_count-O3.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/parallel_count-O3.dir/depend

