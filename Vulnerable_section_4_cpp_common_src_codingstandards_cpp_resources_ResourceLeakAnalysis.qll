 import cpp
 import semmle.code.cpp.dataflow.DataFlow
import semmle.code.cpp.valuenumbering.GlobalValueNumbering
 import semmle.code.cpp.controlflow.Dominance
 import codeql.util.Boolean
 
 
   predicate isFree(ControlFlowNode node, DataFlow::Node resource);
 
   default DataFlow::Node getAnAlias(DataFlow::Node node) {
     DataFlow::localFlow(node, result)
     or
     exists(Expr current, Expr after |
       current in [node.asExpr(), node.asDefiningArgument()] and
       after in [result.asExpr(), result.asDefiningArgument()] and
      globalValueNumber(current) = globalValueNumber(after) and
       strictlyDominates(current, after)
     )
   }
       Config::isAllocate(cfgNode, resource)
     }
 
  /**
   * Get an alias of a resource, and aliases of nodes that are aliased by a resource.
   */
  private DataFlow::Node getAnAliasRecursive(DataFlow::Node node) {
    result = Config::getAnAlias(node) and
    Config::isAllocate(_, node)
    or
    exists(DataFlow::Node parent |
      node = getAnAliasRecursive(parent) and
      result = Config::getAnAlias(parent)
    )
  }

   private predicate isLeakedAtControlPoint(TResource resource, ControlFlowNode cfgNode) {
     // Holds if this control point is where the resource was allocated (and therefore not freed).
     resource = TJustResource(_, cfgNode)
     isLeakedAtControlPoint(resource, cfgNode.getAPredecessor()) and
     not exists(DataFlow::Node freed, DataFlow::Node resourceNode |
       Config::isFree(cfgNode, freed) and
      freed = getAnAliasRecursive(resourceNode) and
       resource = TJustResource(resourceNode, _)
     )
   }