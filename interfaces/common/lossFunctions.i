////////////////////////////////////////////////////////////////////////////////////////////////////
//
//  Project:  Embedded Machine Learning Library (EMLL)
//  File:     lossFunctions.i (interfaces)
//  Authors:  Chuck Jacobs
//
//  [copyright]
//
////////////////////////////////////////////////////////////////////////////////////////////////////

%module lossFunctions

%{
#define SWIG_FILE_WITH_INIT
#include "HingeLoss.h"
#include "LogLoss.h"
#include "SquaredLoss.h"
%}

%include "HingeLoss.h"
%include "LogLoss.h"
%include "SquaredLoss.h"
