         bool HasMQ = false;
         bool HasMD = false;
         bool HasResourceDir = false;
        // We need to find the last -o value.
        if (!Args.empty()) {
          std::size_t Idx = Args.size() - 1;
          for (auto It = Args.rbegin(); It != Args.rend(); ++It) {
            StringRef Arg = Args[Idx];
             if (LastO.empty()) {
              if (Arg == "-o" && It != Args.rbegin())
                LastO = Args[Idx + 1];
               else if (Arg.startswith("-o"))
                 LastO = Arg.drop_front(2).str();
             }
               HasMD = true;
             if (Arg == "-resource-dir")
               HasResourceDir = true;
            --Idx;
           }
         }
         // If there's no -MT/-MQ Driver would add -MT with the value of the last
         // -o option.
        tooling::CommandLineArguments AdjustedArgs = Args;
         AdjustedArgs.push_back("-o");
         AdjustedArgs.push_back("/dev/null");
         if (!HasMT && !HasMQ) {
             AdjustedArgs.push_back(std::string(ResourceDir));
           }
         }
         return AdjustedArgs;
       });
   AdjustingCompilations->appendArgumentsAdjuster(