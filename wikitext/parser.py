# coding=utf-8
import logging
import pprint
import traceback

__author__ = 'alistra'

import ply.yacc as yacc
# noinspection PyUnresolvedReferences
from wikitext.lexer import tokens


def func_name():
    return traceback.extract_stack(None, 2)[0][2]


def p_empty(p):
    'empty :'
    print "Parsed %s" % func_name()
    return None


def p_article_empty(p):
    'article : empty'
    p[0] = []
    print "Parsed %s" % func_name()


def p_article_name(p):
    'article : article object'
    print "Parsed %s" % func_name()
    p[0] = p[1] + [p[2]]


def p_object_name(p):
    'object : NAME'
    print "Parsed %s" % func_name()
    p[0] = p[1]


def p_object_number(p):
    'object : NUMBER'
    print "Parsed %s" % func_name()
    p[0] = p[1]


def p_object_coma(p):
    'object : COMMA'
    print "Parsed %s" % func_name()
    p[0] = p[1]


def p_object_square2(p):
    'object : LSQUARE2 insidesquare2 RSQUARE2'
    print "Parsed %s" % func_name()
    p[0] = {'type': "internal_link", 'value': p[2]}


def p_insidesquare2_name(p):
    'insidesquare2 : NAME'
    print "Parsed %s" % func_name()


def p_insidesquare2_name_with_colon(p):
    'insidesquare2 : NAME COLON NAME'
    print "Parsed %s" % func_name()


def p_insidesquare2_name_with_pipe(p):
    'insidesquare2 : NAME COLON NAME PIPE pipelist'
    pass


def p_pipelist_recursive(p):
    'pipelist : pipelist PIPE object'
    pass


def p_pipelist_base(p):
    'pipelist : article'
    pass


#
# def p_expression_plus(p):
#     'expression : expression PLUS term'
#     p[0] = p[1] + p[3]
#
#
# def p_expression_minus(p):
#     'expression : expression MINUS term'
#     p[0] = p[1] - p[3]
#
#
# def p_expression_term(p):
#     'expression : term'
#     p[0] = p[1]
#
#
# def p_term_times(p):
#     'term : term TIMES factor'
#     p[0] = p[1] * p[3]
#
#
# def p_term_div(p):
#     'term : term DIVIDE factor'
#     p[0] = p[1] / p[3]
#
#
# def p_term_factor(p):
#     'term : factor'
#     p[0] = p[1]
#
#
# def p_factor_num(p):
#     'factor : NUMBER'
#     p[0] = p[1]
#
#
# def p_factor_expr(p):
#     'factor : LPAREN expression RPAREN'
#     p[0] = p[2]
#


# Error rule for syntax errors
def p_error(p):
    pprint.pprint(p)
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc(start='article')


def parse(text):
    return parser.parse(text, debug=logging.getLogger())