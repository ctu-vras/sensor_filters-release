// SPDX-License-Identifier: BSD-3-Clause
// SPDX-FileCopyrightText: Czech Technical University in Prague

#include <sensor_msgs/Range.h>

#include <sensor_filters/FilterChainNode.h>

int main(int argc, char** argv)
{
  sensor_filters::spinFilterChain<sensor_msgs::Range>("range_filter_chain", argc, argv);
}
