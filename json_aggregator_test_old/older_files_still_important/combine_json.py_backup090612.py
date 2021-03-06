import json
import os

""" 
Purpose:

This module is designed to combine all the json files in a directory into one json file.
The decoder is specially defined for my craigslist motorcycle hourly databases. The json
decoder module will automatically convert them back to dictionaries.

"""


def import_file ( json_file_name ):

    """

    Pass this function a "xyz.json" filename to import it and return it as a variable 
    
    """

    json_file = open( json_file_name, 'r' )
    json_dict = json.load( json_file )
    json_file.close()

    return ( json_dict )


def get_file_names ( directory_explored ):

    """ 

    Get all xyz.json filenames in the prescribed directory. 
    
    This module assumes all json files in the prescribed directory are to be combined.

    This function will return a list of filenames 'xyz.json'  

    This module is currently configured to explore the directory this module is in.

    """

    # get a list of ALL files in the specified directory
    file_name_list = os.listdir( directory_explored )
    
    # declare the list which will contain only the name of all json files
    json_files_list = []

    # store all the files with .json at the end in json_files_list
    for each in file_name_list:
        if each[-5:] == ".json":
            json_files_list.append( each )
        else:
            pass

    # return just the files with .json at the end
    return ( json_files_list )


def process_the_directory ( directory_with_json_files ):
    """ Process all json files in directory_with_json_files  """

    # Get the list of json files in the directory specified.
    filename_list = get_file_names( directory_with_json_files )

    # Declare the list which will contain each json dictionary
    list_containing_json_dicts = []

    # All dict data from all json files goes into list_containing_json_dicts
    for each in filename_list:
        list_containing_json_dicts.append( import_file( each ) )

    ##  This is where the hardcore processing starts.  It isn't that hardcore
    ##  this segment of the module just takes all the values in the json dicts,
    ##  strips the keys which were an index, and then adds new keys for the compiled dict.

    combined_list_of_jsons = []  ## This is to store values and parse out duplicates

    for each_dict in list_containing_json_dicts:
        for each_key, each_value in each_dict.iteritems():
            if each_value not in combined_list_of_jsons:
                combined_list_of_jsons.append( each_value )
            else:
                pass
    
    md5_key_list = []
    # Generate a list of md5 keys from the data tuple, the md5s are the keys of the dict/json
    for each in combined_list_of_jsons:
        eachmd5 = md5.new()
        eachmd5.update( str(each) )
        md5_key_list.append( str( eachmd5.hexdigest() ) )

    # Zip a tuple and convert into a dictionary for JSON extraction
    extracted_data_dict = dict( zip( md5_key_list, extracted_data_tuple ) )
    
    #  Call the export function to dump the final json from the zipped dict
    export_dict_to_json( extracted_data_dict )
    
    return ( "Complete!" )
    
def export_dict_to_json ( dict_to_export ):
    
    """ Generic json dump function, needs expanded """

    path_and_filename = "./motorcycle_data_before_09.03.2012.json"

    json_file = open ( path_and_filename, "w" )
    json.dump( dict_to_export, json_file )
    json_file.close()

    return ()


# Run the module:
directory_to_use = "./"
process_the_directory( directory_to_use )
