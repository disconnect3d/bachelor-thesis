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
include CMakeFiles/compact_aos_vs_soa-O2.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/compact_aos_vs_soa-O2.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/compact_aos_vs_soa-O2.dir/flags.make

CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.o: CMakeFiles/compact_aos_vs_soa-O2.dir/flags.make
CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.o: /media/dc/B2B200EFB200B9BD/inz/benchmarks/src/compact_aos_vs_soa/compact_aos_vs_soa.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /media/dc/B2B200EFB200B9BD/inz/benchmarks/builds/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.o -c /media/dc/B2B200EFB200B9BD/inz/benchmarks/src/compact_aos_vs_soa/compact_aos_vs_soa.cpp

CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /media/dc/B2B200EFB200B9BD/inz/benchmarks/src/compact_aos_vs_soa/compact_aos_vs_soa.cpp > CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.i

CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /media/dc/B2B200EFB200B9BD/inz/benchmarks/src/compact_aos_vs_soa/compact_aos_vs_soa.cpp -o CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.s

CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.o.requires:
.PHONY : CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.o.requires

CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.o.provides: CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.o.requires
	$(MAKE) -f CMakeFiles/compact_aos_vs_soa-O2.dir/build.make CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.o.provides.build
.PHONY : CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.o.provides

CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.o.provides.build: CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.o

# Object files for target compact_aos_vs_soa-O2
compact_aos_vs_soa__O2_OBJECTS = \
"CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.o"

# External object files for target compact_aos_vs_soa-O2
compact_aos_vs_soa__O2_EXTERNAL_OBJECTS =

builds/compact_aos_vs_soa-O2: CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.o
builds/compact_aos_vs_soa-O2: CMakeFiles/compact_aos_vs_soa-O2.dir/build.make
builds/compact_aos_vs_soa-O2: CMakeFiles/compact_aos_vs_soa-O2.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable builds/compact_aos_vs_soa-O2"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/compact_aos_vs_soa-O2.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/compact_aos_vs_soa-O2.dir/build: builds/compact_aos_vs_soa-O2
.PHONY : CMakeFiles/compact_aos_vs_soa-O2.dir/build

CMakeFiles/compact_aos_vs_soa-O2.dir/requires: CMakeFiles/compact_aos_vs_soa-O2.dir/compact_aos_vs_soa/compact_aos_vs_soa.o.requires
.PHONY : CMakeFiles/compact_aos_vs_soa-O2.dir/requires

CMakeFiles/compact_aos_vs_soa-O2.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/compact_aos_vs_soa-O2.dir/cmake_clean.cmake
.PHONY : CMakeFiles/compact_aos_vs_soa-O2.dir/clean

CMakeFiles/compact_aos_vs_soa-O2.dir/depend:
	cd /media/dc/B2B200EFB200B9BD/inz/benchmarks/builds && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /media/dc/B2B200EFB200B9BD/inz/benchmarks/src /media/dc/B2B200EFB200B9BD/inz/benchmarks/src /media/dc/B2B200EFB200B9BD/inz/benchmarks/builds /media/dc/B2B200EFB200B9BD/inz/benchmarks/builds /media/dc/B2B200EFB200B9BD/inz/benchmarks/builds/CMakeFiles/compact_aos_vs_soa-O2.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/compact_aos_vs_soa-O2.dir/depend

