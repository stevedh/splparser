
from splparser.parsetree import *

def p_value_hostname(p):
    """value : hostname"""
    p[0] = p[1]

def p_hostname(p):
    """hostname : wordid PERIOD wordid"""
    r = ".".join([p[1].raw, p[3].raw])
    p[0] = ParseTreeNode('HOSTNAME', raw=r)

def p_hostname_wordid(p):
    """hostname : hostname PERIOD wordid"""
    r = ".".join([p[1].raw, p[3].raw])
    p[0] = ParseTreeNode('HOSTNAME', raw=r)

