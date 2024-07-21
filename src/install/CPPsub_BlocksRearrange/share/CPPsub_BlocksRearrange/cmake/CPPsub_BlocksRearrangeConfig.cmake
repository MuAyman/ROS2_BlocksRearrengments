# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_CPPsub_BlocksRearrange_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED CPPsub_BlocksRearrange_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(CPPsub_BlocksRearrange_FOUND FALSE)
  elseif(NOT CPPsub_BlocksRearrange_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(CPPsub_BlocksRearrange_FOUND FALSE)
  endif()
  return()
endif()
set(_CPPsub_BlocksRearrange_CONFIG_INCLUDED TRUE)

# output package information
if(NOT CPPsub_BlocksRearrange_FIND_QUIETLY)
  message(STATUS "Found CPPsub_BlocksRearrange: 0.0.0 (${CPPsub_BlocksRearrange_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'CPPsub_BlocksRearrange' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${CPPsub_BlocksRearrange_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(CPPsub_BlocksRearrange_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${CPPsub_BlocksRearrange_DIR}/${_extra}")
endforeach()
