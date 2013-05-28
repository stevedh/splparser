#!/usr/bin/env python

from splparser.parsetree import *
from splparser.exceptions import SPLSyntaxError

from splparser.rules.common.evalfnexprrules import *
from splparser.rules.common.simplefieldrules import *
from splparser.rules.common.simplevaluerules import *

from splparser.lexers.headlexer import precedence, tokens

start = 'cmdexpr'

def p_cmdexpr_head(p):
    """cmdexpr : headcmd"""
    p[0] = p[1]

def p_headcmd_head(p):
    """headcmd : HEAD"""
    p[0] = ParseTreeNode('HEAD')

def p_headcmd_head_int(p):
    """headcmd : HEAD int"""
    p[0] = ParseTreeNode('HEAD')
    p[0].add_child(p[2])
    p[2].field = False
    p[2].value = False
    p[2].option = True

def p_headcmd_head_eval(p):
    """headcmd : HEAD evalfnexpr"""
    p[0] = ParseTreeNode('HEAD')
    p[0].add_child(p[2])

def p_headcmd_head_headopt(p):
    """headcmd : HEAD headoptlist"""
    p[0] = ParseTreeNode('HEAD') 
    p[0].add_children(p[2].children)

def p_headcmd_head_int_headopt(p):
    """headcmd : HEAD int headoptlist"""
    p[0] = ParseTreeNode('HEAD')
    p[0].add_child(p[2])
    p[0].add_children(p[3].children)
    p[2].field = False
    p[2].value = False
    p[2].option = True

def p_headcmd_head_eval_headopt(p):
    """headcmd : HEAD evalfnexpr headoptlist"""
    p[0] = ParseTreeNode('HEAD')
    p[0].add_child(p[2])
    p[0].add_children(p[3].children)

def p_headoptlist(p):
    """headoptlist : headopt"""
    p[0] = ParseTreeNode('_HEAD_OPT_LIST')
    p[0].add_child(p[1])

def p_headoptlist_headopt(p):
    """headoptlist : headopt headoptlist"""
    p[0] = ParseTreeNode('_HEAD_OPT_LIST')
    p[0].add_child(p[1])
    p[0].add_children(p[2].children) 

def p_headopt(p):
    """headopt : HEAD_OPT EQ simplevalue"""
    p[0] = ParseTreeNode(p[1].upper(), option=True)
    p[0].values.append(p[3])
    p[0].add_child(p[3])

def p_headopt_commonopt(p):
    """headopt : COMMON_OPT EQ simplevalue"""
    p[0] = ParseTreeNode(p[1].upper(), option=True)
    p[0].values.append(p[3])
    p[0].add_child(p[3])

def p_error(p):
    raise SPLSyntaxError("Syntax error in head parser input!") 
