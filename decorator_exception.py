def log_on_exception(function):
    def wrapper_accepting_arguments(tag1,tag2):
        print (tag1)
        function(tag1,tag2)
    return wrapper_accepting_arguments

    
@log_on_exception
def log(tag1,tag2):
    #raise Exception('Exception happened')
    print (tag1)
log('tag1','tag2')

