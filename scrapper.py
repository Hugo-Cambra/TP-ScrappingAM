from scrapperFunctions import *

arguments = get_inputs_arguments()
input_arg = arguments[0]
output_arg = arguments[1]

with open(input_arg,'r') as file:
    id_url_list=json.load(file)

res_output = []

for url_id in id_url_list["videos_id"]:
    result = get_info(url_id)
    res_output.append(result)

generate_output(res_output,output_arg)