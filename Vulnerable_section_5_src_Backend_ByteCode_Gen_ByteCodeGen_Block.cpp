                     SWAG_ASSERT(symbol);
                     for (const auto overload : symbol->overloads)
                     {
                        if (overload->hasFlag(OVERLOAD_VAR_INLINE))
                         {
                             RegisterList rl;
                             SWAG_CHECK(emitDefaultParamValue(context, defaultParam, rl));