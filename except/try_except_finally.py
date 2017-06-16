import logging
def divide(dividee, divider):
    try :
        r = int(dividee)/int(divider)
        print 'reult:', r
    except ValueError, e:
        print 'ValueError', e
    except ZeroDivisionError, e:
        print 'ZeroDivisionError:', e
    finally:
        print 'finally'
    print 'END'

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        print 'Error!'
        logging.exception(e)
    finally:
        print 'finally...'

if __name__ == '__main__':
    # divide(10, 0)
    #
    # divide(10, 'a')
    #
    # divide('10','2')

    main()



