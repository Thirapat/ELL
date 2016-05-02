////////////////////////////////////////////////////////////////////////////////////////////////////
//
//  Project:  Embedded Machine Learning Library (EMLL)
//  File:     IntegerStack.cpp (utilities)
//  Authors:  Ofer Dekel
//
//  [copyright]
//
////////////////////////////////////////////////////////////////////////////////////////////////////

#include "IntegerStack.h"

// stl
#include <cassert>

namespace utilities
{
    uint64_t IntegerStack::Pop()
    {
        uint64_t top;

        if(_stack.empty())
        {
            top = _smallestUnpopped;
            _smallestUnpopped++;
        }
        else
        {
            top = _stack.top();
            _stack.pop();
        }

        return top;
    }
    uint64_t IntegerStack::Top() const
    {
        if(_stack.empty())
        {
            return _smallestUnpopped;
        }
        else
        {
            return _stack.top();
        }
    }
    void IntegerStack::Push(uint64_t value)
    {
        _stack.push(value);

        assert(value < _smallestUnpopped);
    }

    bool IntegerStack::IsTopNovel() const
    {
        return _stack.empty();
    }
}
