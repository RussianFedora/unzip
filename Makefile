# Makefile for source rpm: unzip
# $Id$
NAME := unzip
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
