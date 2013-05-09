#!/usr/bin/env python

from splparser.parsetree import *

from splparser.rules.common.byrules import *
from splparser.rules.common.fieldrules import *
from splparser.rules.common.fieldlistrules import *
from splparser.rules.common.valuerules import *

from splparser.lexers.rarelexer import tokens

start = 'cmdexpr'

def p_cmdexpr_rare(p):
    """cmdexpr : rarecmd"""
    p[0] = p[1]

def p_rare_fieldlist(p):
    """rarecmd : RARE fieldlist
               | SIRARE fieldlist"""
    p[0] = ParseTreeNode(p[1].upper())
    p[0].add_children(p[2].children)

def p_rare_fieldlist_by(p):
    """rarecmd : RARE fieldlist by fieldlist
               | SIRARE fieldlist by fieldlist"""
    by_node = ParseTreeNode('BY')
    by_node.add_children(p[4].children)
    p[0] = ParseTreeNode(p[1].upper())
    p[0].add_children(p[2].children)
    p[0].add_child(by_node)

def p_rare_rareopt_fieldlist(p):
    """rarecmd : RARE rareoptlist fieldlist
               | SIRARE rareoptlist fieldlist"""
    p[0] = ParseTreeNode(p[1].upper())
    p[0].add_children(p[2].children)
    p[0].add_children(p[3].children)

def p_rare_weird(p):
    """rarecmd : RARE INT fieldlist
               | SIRARE INT fieldlist"""
    p[0] = ParseTreeNode(p[1].upper())
    eq_node = ParseTreeNode('EQ')
    p[0].add_child(eq_node)
    p[0].add_children(p[3].children)
    limit_node = ParseTreeNode('LIMIT', option=True)
    int_node = ParseTreeNode('INT', raw=p[2], arg=True)
    eq_node.add_children([limit_node, int_node])
    limit_node.values.append(int_node)

def p_rare_rareopt_fieldlist_by(p):
    """rarecmd : RARE rareoptlist fieldlist by fieldlist
               | SIRARE rareoptlist fieldlist by fieldlist"""
    by_node = ParseTreeNode('BY')
    by_node.add_children(p[5].children)
    p[0] = ParseTreeNode(p[1].upper())
    p[0].add_children(p[2].children)
    p[0].add_children(p[3].children)
    p[0].add_child(by_node)

def p_rareoptlist(p):
    """rareoptlist : rareopt"""
    p[0] = ParseTreeNode('_TOP_OPT_LIST')
    p[0].add_child(p[1])

def p_rareoptlist_rareopt(p):
    """rareoptlist : rareopt rareoptlist"""
    p[0] = ParseTreeNode('_TOP_OPT_LIST')
    p[0].add_child(p[1])
    p[0].add_children(p[2].children) 

def p_rareopt(p):
    """rareopt : TOP_OPT EQ value"""
    p[0] = ParseTreeNode('EQ')
    opt_node = ParseTreeNode(p[1].upper())
    opt_node.values.append(p[3])
    p[0].add_child(opt_node)
    p[0].add_child(p[3])

def p_rareopt_commonopt(p):
    """rareopt : COMMON_OPT EQ value"""
    p[0] = ParseTreeNode('EQ')
    opt_node = ParseTreeNode(p[1].upper())
    opt_node.values.append(p[3])
    p[0].add_child(opt_node)
    p[0].add_child(p[3])

def p_error(p):
    raise SPLSyntaxError("Syntax error in rare parser input!") 
