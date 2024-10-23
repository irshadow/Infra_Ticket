def custome_template_maker(input_dict):
    lstField=[]
    dictInputTags = {'pageTitle': input_dict['title']}
   
   
    for item in input_dict['fields']:
        field = ' '
        counter = 1
        for attribute,value in item.items():
            field += attribute + " = " + value + ""
            if counter!=len(item):
                counter += 1
                field += " "
        field += ' '
        lstField.append(field)
    dictInputTags.update({'inputFields':lstField})
    
    
    act = ' '
    counter=1
    for attribute, value in input_dict['action'].items():
        if attribute.lower() == 'url':
            attribute = 'formaction'
        if attribute.lower() == 'method':
            attribute = 'formmethod'
        if attribute.lower() == 'text':
            attribute = 'value'
        act += attribute + " = " + value + ""
        if counter != len(input_dict['action']):
            counter += 1
            act += " "
    act += ' '

    print("\n\n\n\n\n")
    
    dictInputTags.update({'action':[act]})
    print(dictInputTags)
    return dictInputTags